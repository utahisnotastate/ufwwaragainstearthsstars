"""Fit orbits to sky positions and test whether an object could be bound to the Sun.

For young readers
-----------------
A telescope only tells us *where in the sky* something is, not how far away it
is. This file tries many possible distances and speeds, finds the path that
best matches the sky positions, and then asks one careful question:
"Could this object still be on a closed loop around the Sun, or must it be
a visitor that is just passing through?"

For experts
-----------
1. A coarse **range scan** over topocentric distance ``rho`` and range-rate
   ``rho_dot`` at a reference epoch (attributable + range parametrization,
   in the spirit of statistical ranging; Virtanen et al. 2001, Milani et al.
   2004) provides starting points.
2. **Least-squares orbit determination** of the 6-element Cartesian state
   (optionally plus a radial non-gravitational parameter ``A1``) with exact
   two-body propagation and light-time correction.
3. A **bound-orbit likelihood-ratio test**: the fit is repeated with the
   velocity constrained inside the local escape speed,
   ``v = v_esc(r) * w / sqrt(1 + |w|^2)``. The statistic
   ``Delta chi^2 = chi^2_bound - chi^2_free`` is referred to the boundary
   (Chernoff 1954) mixture ``0.5 chi^2_0 + 0.5 chi^2_1``.

The test is only as good as the astrometric uncertainties you supply, and
short arcs can be dominated by systematic errors (timing, catalog zero
points, mis-linkage). A high significance is a reason for follow-up, never a
confirmation by itself.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.optimize import least_squares
from scipy.stats import norm

from .constants import ARCSEC_PER_RAD, C_AU_PER_DAY, GM_SUN
from .ephemeris import earth_heliocentric, earth_heliocentric_velocity
from .kepler import (
    OrbitalElements,
    equatorial_to_ecliptic,
    escape_speed,
    incoming_radiant,
    propagate,
    state_to_elements,
    unit_vector_to_radec,
)

FloatArray = NDArray[np.float64]

__all__ = [
    "Observations",
    "OrbitFit",
    "BoundTest",
    "make_observations",
    "simulate_observations",
    "predict_radec",
    "range_scan",
    "fit_orbit",
    "bound_orbit_test",
    "screen_object",
    "screen_tracklet_pairs",
]


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Observations:
    """Astrometric observations of one object (or one candidate linkage)."""

    mjd: FloatArray            # (N,) observation times (TT/TDB recommended)
    ra_deg: FloatArray         # (N,) right ascension, degrees (ICRF)
    dec_deg: FloatArray        # (N,) declination, degrees (ICRF)
    sigma_arcsec: FloatArray   # (N,) 1-sigma uncertainty per coordinate
    observer_au: FloatArray    # (N, 3) heliocentric observer positions, au

    @property
    def n(self) -> int:
        return int(self.mjd.size)

    @property
    def arc_days(self) -> float:
        return float(self.mjd.max() - self.mjd.min()) if self.n else 0.0

    def subset(self, mask: ArrayLike) -> "Observations":
        m = np.asarray(mask)
        return Observations(self.mjd[m], self.ra_deg[m], self.dec_deg[m],
                            self.sigma_arcsec[m], self.observer_au[m])

    def concat(self, other: "Observations") -> "Observations":
        order = np.argsort(np.concatenate([self.mjd, other.mjd]), kind="stable")
        return Observations(
            np.concatenate([self.mjd, other.mjd])[order],
            np.concatenate([self.ra_deg, other.ra_deg])[order],
            np.concatenate([self.dec_deg, other.dec_deg])[order],
            np.concatenate([self.sigma_arcsec, other.sigma_arcsec])[order],
            np.concatenate([self.observer_au, other.observer_au])[order],
        )


def make_observations(
    mjd: ArrayLike,
    ra_deg: ArrayLike,
    dec_deg: ArrayLike,
    sigma_arcsec: ArrayLike = 0.5,
    *,
    observer_au: ArrayLike | None = None,
    observer_offset_au: ArrayLike | None = None,
) -> Observations:
    """Build an :class:`Observations` object, sorted by time.

    If ``observer_au`` is not given, the geocenter from
    :func:`fdastro.ephemeris.earth_heliocentric` is used, plus an optional
    geocentric ``observer_offset_au`` (for example from
    :func:`fdastro.ephemeris.observer_geocentric_offset`). Topocentric
    parallax matters: at 0.1 au an Earth radius shifts positions by ~90".
    """
    t = np.atleast_1d(np.asarray(mjd, dtype=np.float64))
    ra = np.atleast_1d(np.asarray(ra_deg, dtype=np.float64))
    dec = np.atleast_1d(np.asarray(dec_deg, dtype=np.float64))
    if not (t.shape == ra.shape == dec.shape):
        raise ValueError("mjd, ra_deg and dec_deg must have the same shape")
    sig = np.broadcast_to(np.asarray(sigma_arcsec, dtype=np.float64), t.shape).copy()
    if np.any(sig <= 0):
        raise ValueError("sigma_arcsec must be positive")
    if observer_au is None:
        obs = earth_heliocentric(t)
        if observer_offset_au is not None:
            obs = obs + np.asarray(observer_offset_au, dtype=np.float64).reshape(-1, 3)
    else:
        obs = np.asarray(observer_au, dtype=np.float64).reshape(-1, 3)
    if obs.shape[0] != t.size:
        raise ValueError("observer positions must have one row per observation")
    order = np.argsort(t, kind="stable")
    return Observations(t[order], ra[order], dec[order], sig[order], obs[order])


# ---------------------------------------------------------------------------
# Forward model
# ---------------------------------------------------------------------------

def predict_radec(
    state: ArrayLike,
    epoch_mjd: float,
    mjd: ArrayLike,
    observer_au: ArrayLike,
    *,
    a1: float = 0.0,
    light_time: bool = True,
) -> tuple[FloatArray, FloatArray]:
    """Predict astrometric RA/Dec (radians) seen from ``observer_au`` at ``mjd``."""
    t = np.atleast_1d(np.asarray(mjd, dtype=np.float64))
    observer = np.asarray(observer_au, dtype=np.float64).reshape(-1, 3)
    dt = t - epoch_mjd
    r, _ = propagate(state, dt, a1=a1)
    if light_time:
        for _ in range(2):
            rho = np.linalg.norm(r - observer, axis=1)
            r, _ = propagate(state, dt - rho / C_AU_PER_DAY, a1=a1)
    d = r - observer
    dn = np.linalg.norm(d, axis=1)
    ra = np.arctan2(d[:, 1], d[:, 0])
    dec = np.arcsin(np.clip(d[:, 2] / dn, -1.0, 1.0))
    return ra, dec


def _normalized_residuals(ra_pred: FloatArray, dec_pred: FloatArray, obs: Observations) -> FloatArray:
    ra_o = np.deg2rad(obs.ra_deg)
    dec_o = np.deg2rad(obs.dec_deg)
    dra = (ra_o - ra_pred + np.pi) % (2.0 * np.pi) - np.pi
    res_ra = dra * np.cos(dec_o) * ARCSEC_PER_RAD / obs.sigma_arcsec
    res_dec = (dec_o - dec_pred) * ARCSEC_PER_RAD / obs.sigma_arcsec
    return np.concatenate([res_ra, res_dec])


def simulate_observations(
    state: ArrayLike,
    epoch_mjd: float,
    mjd: ArrayLike,
    *,
    sigma_arcsec: float = 0.2,
    observer_au: ArrayLike | None = None,
    a1: float = 0.0,
    rng: np.random.Generator | int | None = None,
) -> Observations:
    """Make synthetic astrometry for a known orbit, with Gaussian noise."""
    t = np.atleast_1d(np.asarray(mjd, dtype=np.float64))
    observer = earth_heliocentric(t) if observer_au is None else np.asarray(observer_au, dtype=np.float64)
    ra, dec = predict_radec(state, epoch_mjd, t, observer, a1=a1)
    gen = np.random.default_rng(rng)
    noise = gen.normal(0.0, sigma_arcsec, size=(2, t.size)) / ARCSEC_PER_RAD
    dec_n = dec + noise[1]
    ra_n = ra + noise[0] / np.cos(dec_n)
    return make_observations(t, np.rad2deg(ra_n) % 360.0, np.rad2deg(dec_n), sigma_arcsec,
                             observer_au=observer)


# ---------------------------------------------------------------------------
# Initial orbit determination by range scanning
# ---------------------------------------------------------------------------

def _attributable(obs: Observations) -> tuple[float, float, float, float, float]:
    """(t0, ra, dec, ra_dot, dec_dot) at the mean epoch from a low-order polynomial fit."""
    t0 = float(np.mean(obs.mjd))
    tt = obs.mjd - t0
    ra = np.unwrap(np.deg2rad(obs.ra_deg))
    dec = np.deg2rad(obs.dec_deg)
    n_times = np.unique(np.round(obs.mjd, 4)).size
    deg = int(min(2, max(1, n_times - 1)))
    if obs.arc_days < 1.0:
        deg = 1
    p_ra = np.polyfit(tt, ra, deg)
    p_dec = np.polyfit(tt, dec, deg)
    return (t0, float(np.polyval(p_ra, 0.0)), float(np.polyval(p_dec, 0.0)),
            float(np.polyval(np.polyder(p_ra), 0.0)), float(np.polyval(np.polyder(p_dec), 0.0)))


def _state_from_range(att, rho: float, rho_dot: float, obs_pos: FloatArray, obs_vel: FloatArray) -> FloatArray:
    _, ra, dec, ra_dot, dec_dot = att
    cd, sd, ca, sa = math.cos(dec), math.sin(dec), math.cos(ra), math.sin(ra)
    u = np.array([cd * ca, cd * sa, sd])
    du_da = np.array([-cd * sa, cd * ca, 0.0])
    du_dd = np.array([-sd * ca, -sd * sa, cd])
    r = obs_pos + rho * u
    v = obs_vel + rho_dot * u + rho * (ra_dot * du_da + dec_dot * du_dd)
    return np.concatenate([r, v])


@dataclass(frozen=True)
class RangeScan:
    """Chi-square over a (rho, rho_dot) grid at ``epoch_mjd``."""

    epoch_mjd: float
    rho: FloatArray
    rho_dot: FloatArray
    chi2: FloatArray          # shape (len(rho), len(rho_dot))
    eccentricity: FloatArray  # same shape
    states: FloatArray        # shape (len(rho), len(rho_dot), 6)


def range_scan(
    obs: Observations,
    *,
    rho_grid: ArrayLike | None = None,
    rho_dot_grid: ArrayLike | None = None,
) -> RangeScan:
    """Evaluate chi-square for trial distances and radial speeds (no light time)."""
    if obs.n < 3:
        raise ValueError("need at least 3 observations")
    rho = np.geomspace(0.01, 60.0, 48) if rho_grid is None else np.asarray(rho_grid, dtype=np.float64)
    rdot = np.linspace(-0.06, 0.06, 41) if rho_dot_grid is None else np.asarray(rho_dot_grid, dtype=np.float64)
    att = _attributable(obs)
    t0 = att[0]
    obs_pos = earth_heliocentric(t0)[0]
    obs_vel = earth_heliocentric_velocity(t0)[0]
    chi = np.full((rho.size, rdot.size), np.inf)
    ecc = np.full((rho.size, rdot.size), np.nan)
    states = np.zeros((rho.size, rdot.size, 6))
    for i, rh in enumerate(rho):
        for j, rd in enumerate(rdot):
            s = _state_from_range(att, float(rh), float(rd), obs_pos, obs_vel)
            states[i, j] = s
            try:
                ra_p, dec_p = predict_radec(s, t0, obs.mjd, obs.observer_au, light_time=False)
            except (RuntimeError, ValueError, FloatingPointError):
                continue
            res = _normalized_residuals(ra_p, dec_p, obs)
            chi[i, j] = float(res @ res)
            r, v = s[:3], s[3:]
            rn = np.linalg.norm(r)
            e_vec = ((v @ v - GM_SUN / rn) * r - (r @ v) * v) / GM_SUN
            ecc[i, j] = float(np.linalg.norm(e_vec))
    return RangeScan(t0, rho, rdot, chi, ecc, states)


# ---------------------------------------------------------------------------
# Least-squares orbit determination
# ---------------------------------------------------------------------------

@dataclass
class OrbitFit:
    """Result of :func:`fit_orbit`. States are J2000 equatorial; elements are J2000 ecliptic."""

    epoch_mjd: float
    state: FloatArray
    a1: float
    chi2: float
    dof: int
    rms_arcsec: float
    covariance: FloatArray
    elements: OrbitalElements
    e_sigma: float
    arc_days: float
    n_obs: int
    success: bool
    residuals_arcsec: FloatArray = field(repr=False)

    @property
    def reduced_chi2(self) -> float:
        return self.chi2 / max(1, self.dof)


def _ecc_of_state(state: FloatArray) -> float:
    r, v = state[:3], state[3:6]
    rn = np.linalg.norm(r)
    e_vec = ((v @ v - GM_SUN / rn) * r - (r @ v) * v) / GM_SUN
    return float(np.linalg.norm(e_vec))


def _fit_from(obs: Observations, x0: FloatArray, epoch: float, fit_a1: bool, light_time: bool):
    def fun(x: FloatArray) -> FloatArray:
        a1 = float(x[6]) if fit_a1 else 0.0
        try:
            ra_p, dec_p = predict_radec(x[:6], epoch, obs.mjd, obs.observer_au, a1=a1,
                                        light_time=light_time)
        except (RuntimeError, ValueError, FloatingPointError):
            return np.full(2 * obs.n, 1e6)
        return _normalized_residuals(ra_p, dec_p, obs)

    method = "lm" if 2 * obs.n >= x0.size else "trf"
    return least_squares(fun, x0, method=method, x_scale="jac", xtol=1e-12, ftol=1e-12,
                         gtol=1e-12, max_nfev=4000)


def fit_orbit(
    obs: Observations,
    *,
    fit_a1: bool = False,
    n_starts: int = 6,
    light_time: bool = True,
    scan: RangeScan | None = None,
) -> OrbitFit:
    """Least-squares orbit fit, started from the best points of a range scan.

    Parameters
    ----------
    obs : Observations
        At least 3 observations (4+ with ``fit_a1``); 2 or more nights strongly recommended.
    fit_a1 : bool
        Also fit a radial non-gravitational acceleration A1 (au/day^2 at 1 au).
    n_starts : int
        Number of distinct range-scan minima used as starting points.
    """
    n_par = 7 if fit_a1 else 6
    if 2 * obs.n < n_par:
        raise ValueError(f"need at least {math.ceil(n_par / 2)} observations")
    scan = scan or range_scan(obs)
    epoch = scan.epoch_mjd
    flat = np.argsort(scan.chi2, axis=None)
    starts: list[FloatArray] = []
    used: list[tuple[int, int]] = []
    for idx in flat:
        i, j = np.unravel_index(idx, scan.chi2.shape)
        if not np.isfinite(scan.chi2[i, j]):
            break
        if any(abs(i - a) <= 2 and abs(j - b) <= 2 for a, b in used):
            continue
        used.append((i, j))
        starts.append(scan.states[i, j])
        if len(starts) >= n_starts:
            break

    best = None
    for s0 in starts:
        x0 = np.concatenate([s0, [0.0]]) if fit_a1 else s0.copy()
        res = _fit_from(obs, x0, epoch, fit_a1, light_time)
        if best is None or res.cost < best.cost:
            best = res
    if best is None:
        raise RuntimeError("range scan produced no usable starting points")

    x = best.x
    resid = best.fun
    chi2_val = float(resid @ resid)
    jac = best.jac
    try:
        cov = np.linalg.pinv(jac.T @ jac)
    except np.linalg.LinAlgError:
        cov = np.full((x.size, x.size), np.nan)

    state = x[:6].copy()
    # Numerical gradient of e with respect to the state, for a linearized sigma_e.
    grad = np.zeros(x.size)
    for k in range(6):
        h = 1e-7 * max(1.0, abs(state[k])) if k < 3 else 1e-9 * max(1e-2, abs(state[k]))
        sp, sm = state.copy(), state.copy()
        sp[k] += h
        sm[k] -= h
        grad[k] = (_ecc_of_state(sp) - _ecc_of_state(sm)) / (2 * h)
    var_e = float(grad @ cov @ grad)
    e_sigma = math.sqrt(var_e) if var_e >= 0 and np.isfinite(var_e) else math.nan

    elements = state_to_elements(equatorial_to_ecliptic(state[:3]), equatorial_to_ecliptic(state[3:6]))
    n = obs.n
    res_arcsec = resid.copy()
    res_arcsec[:n] *= obs.sigma_arcsec
    res_arcsec[n:] *= obs.sigma_arcsec
    rms = float(np.sqrt(np.mean(res_arcsec**2)))
    return OrbitFit(
        epoch_mjd=epoch, state=state, a1=float(x[6]) if fit_a1 else 0.0, chi2=chi2_val,
        dof=2 * n - x.size, rms_arcsec=rms, covariance=cov, elements=elements,
        e_sigma=e_sigma, arc_days=obs.arc_days, n_obs=n, success=bool(best.success),
        residuals_arcsec=res_arcsec,
    )


# ---------------------------------------------------------------------------
# Bound-orbit likelihood-ratio test
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class BoundTest:
    """Outcome of :func:`bound_orbit_test`."""

    chi2_free: float
    chi2_bound: float
    delta_chi2: float
    p_value: float
    sigma: float
    bound_state: FloatArray
    verdict: str


def _w_from_velocity(r: FloatArray, v: FloatArray, shrink: float = 0.98) -> FloatArray:
    s = v / escape_speed(np.linalg.norm(r))
    sn = np.linalg.norm(s)
    if sn >= shrink:
        s = s * (shrink / sn)
        sn = shrink
    return s / math.sqrt(1.0 - sn * sn)


def _velocity_from_w(r: FloatArray, w: FloatArray) -> FloatArray:
    return escape_speed(np.linalg.norm(r)) * w / math.sqrt(1.0 + float(w @ w))


def bound_orbit_test(
    obs: Observations,
    fit: OrbitFit,
    *,
    scan: RangeScan | None = None,
    n_starts: int = 6,
    light_time: bool = True,
) -> BoundTest:
    """Is a bound (e < 1) orbit significantly worse than the best unconstrained orbit?

    Returns the likelihood-ratio statistic and a one-sided Gaussian-equivalent
    significance. ``sigma >= 5`` earns the label "hyperbolic candidate".
    """
    epoch = fit.epoch_mjd
    a1 = fit.a1

    def fun(x: FloatArray) -> FloatArray:
        r = x[:3]
        v = _velocity_from_w(r, x[3:6])
        try:
            ra_p, dec_p = predict_radec(np.concatenate([r, v]), epoch, obs.mjd, obs.observer_au,
                                        a1=a1, light_time=light_time)
        except (RuntimeError, ValueError, FloatingPointError):
            return np.full(2 * obs.n, 1e6)
        return _normalized_residuals(ra_p, dec_p, obs)

    starts = [np.concatenate([fit.state[:3], _w_from_velocity(fit.state[:3], fit.state[3:6])])]
    scan = scan or range_scan(obs)
    bound_mask = np.isfinite(scan.chi2) & (scan.eccentricity < 1.0)
    if bound_mask.any():
        order = np.argsort(np.where(bound_mask, scan.chi2, np.inf), axis=None)
        for idx in order[: n_starts - 1]:
            i, j = np.unravel_index(idx, scan.chi2.shape)
            if not bound_mask[i, j]:
                break
            s = scan.states[i, j]
            starts.append(np.concatenate([s[:3], _w_from_velocity(s[:3], s[3:])]))

    best = None
    method = "lm" if 2 * obs.n >= 6 else "trf"
    for x0 in starts:
        res = least_squares(fun, x0, method=method, x_scale="jac", xtol=1e-12, ftol=1e-12,
                            gtol=1e-12, max_nfev=4000)
        if best is None or res.cost < best.cost:
            best = res
    assert best is not None
    chi2_bound = float(best.fun @ best.fun)
    delta = max(0.0, chi2_bound - fit.chi2)
    # Under the boundary mixture 0.5 chi2_0 + 0.5 chi2_1, P = 0.5 P(chi2_1 > delta)
    # = P(Z > sqrt(delta)), so the one-sided Gaussian-equivalent significance is
    # exactly sqrt(delta). This avoids underflow for very large delta.
    sigma = math.sqrt(delta)
    p = float(norm.sf(sigma)) if delta > 0 else 1.0
    if sigma >= 5.0:
        verdict = "hyperbolic candidate: bound orbits rejected at >= 5 sigma (needs independent follow-up)"
    elif sigma >= 3.0:
        verdict = "possibly hyperbolic: bound orbits disfavoured at >= 3 sigma (extend the arc)"
    else:
        verdict = "consistent with a bound orbit"
    r = best.x[:3]
    bound_state = np.concatenate([r, _velocity_from_w(r, best.x[3:6])])
    return BoundTest(fit.chi2, chi2_bound, delta, p, sigma, bound_state, verdict)


def screen_object(obs: Observations, *, name: str = "candidate", fit_a1: bool = False) -> dict:
    """Fit, test and summarize one object as a JSON-friendly dictionary."""
    scan = range_scan(obs)
    fit = fit_orbit(obs, fit_a1=fit_a1, scan=scan)
    test = bound_orbit_test(obs, fit, scan=scan)
    el = fit.elements
    summary = {
        "name": name,
        "verdict": test.verdict,
        "bound_rejection_sigma": round(test.sigma, 2),
        "delta_chi2": round(test.delta_chi2, 3),
        "eccentricity": round(el.e, 4),
        "eccentricity_sigma_linear": None if math.isnan(fit.e_sigma) else round(fit.e_sigma, 4),
        "perihelion_au": round(el.q, 4),
        "inclination_deg": round(el.i_deg, 3),
        "v_infinity_kms": None if el.v_infinity_kms is None else round(el.v_infinity_kms, 2),
        "heliocentric_distance_au": round(float(np.linalg.norm(fit.state[:3])), 4),
        "rms_arcsec": round(fit.rms_arcsec, 4),
        "reduced_chi2": round(fit.reduced_chi2, 3),
        "arc_days": round(fit.arc_days, 3),
        "n_obs": fit.n_obs,
        "a1_au_per_day2": fit.a1 if fit_a1 else None,
        "radiant_ra_dec_deg": None,
    }
    if el.e > 1.0:
        ra, dec = unit_vector_to_radec(incoming_radiant(fit.state[:3], fit.state[3:6]))
        summary["radiant_ra_dec_deg"] = [round(ra, 2), round(dec, 2)]
    if fit.arc_days < 3.0:
        summary["warning"] = "arc shorter than 3 days: eccentricity is poorly constrained"
    return summary


# ---------------------------------------------------------------------------
# Small-scale tracklet pairing (teaching / pilot scale, not survey scale)
# ---------------------------------------------------------------------------

def _angular_sep_deg(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    r1, d1, r2, d2 = map(math.radians, (ra1, dec1, ra2, dec2))
    c = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(r1 - r2)
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def screen_tracklet_pairs(
    tracklets: dict[str, Observations],
    *,
    max_gap_days: float = 15.0,
    max_rate_deg_per_day: float = 10.0,
    max_rms_arcsec: float = 1.0,
    min_sigma: float = 5.0,
) -> list[dict]:
    """Try to join pairs of short tracklets and keep joins that look hyperbolic.

    This is an O(n^2) pilot tool for small samples (hundreds of tracklets).
    Survey-scale linking needs dedicated software (for example HelioLinC3D or
    THOR). A pair is attempted only if the implied angular rate between the
    two tracklets is below ``max_rate_deg_per_day``.
    """
    names = sorted(tracklets, key=lambda k: float(np.mean(tracklets[k].mjd)))
    out: list[dict] = []
    for a_idx, a in enumerate(names):
        ta = tracklets[a]
        for b in names[a_idx + 1:]:
            tb = tracklets[b]
            gap = float(np.mean(tb.mjd) - np.mean(ta.mjd))
            if gap <= 0.5 or gap > max_gap_days:
                continue
            sep = _angular_sep_deg(float(np.mean(ta.ra_deg)), float(np.mean(ta.dec_deg)),
                                   float(np.mean(tb.ra_deg)), float(np.mean(tb.dec_deg)))
            if sep / gap > max_rate_deg_per_day:
                continue
            joined = ta.concat(tb)
            try:
                summary = screen_object(joined, name=f"{a}+{b}")
            except (RuntimeError, ValueError):
                continue
            if summary["rms_arcsec"] <= max_rms_arcsec and summary["bound_rejection_sigma"] >= min_sigma:
                out.append(summary)
    return sorted(out, key=lambda d: -d["bound_rejection_sigma"])
