"""Two-body (Keplerian) orbits for every conic: ellipses, parabolas and hyperbolas.

For young readers
-----------------
A planet or comet that stays with the Sun moves on a closed oval (an ellipse).
A visitor from another star moves fast enough to escape. Its path opens up
like a wide "V" (a hyperbola). The code in this file can follow both kinds of path.

For experts
-----------
Propagation uses the universal-variable formulation (Battin 1987; Vallado 2013,
Algorithm 8) solved with the Laguerre–Conway iteration, which converges for
all conics. Optionally, a radial non-gravitational acceleration
``A1 * (1 au / r)^2`` (Marsden et al. 1973 style, with g(r) = r^-2) can be
added; in that case the equations of motion are integrated numerically with
DOP853.

All vectors are heliocentric, in au and au/day. The frame is whatever frame the
input state uses (usually ICRF/equatorial). Use
:func:`equatorial_to_ecliptic` before computing elements that should be
compared with catalog values, which are referred to the J2000 ecliptic.
"""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.integrate import solve_ivp

from .constants import GM_SUN, KMS_PER_AU_DAY, OBLIQUITY_J2000_DEG

FloatArray = NDArray[np.float64]

__all__ = [
    "OrbitalElements",
    "stumpff_c2c3",
    "propagate",
    "propagate_universal",
    "state_to_elements",
    "elements_to_state",
    "specific_energy",
    "escape_speed",
    "hyperbolic_excess_speed_kms",
    "v_infinity_from_q_e_kms",
    "incoming_radiant",
    "equatorial_to_ecliptic",
    "ecliptic_to_equatorial",
    "unit_vector_to_radec",
]


# ---------------------------------------------------------------------------
# Frame helpers
# ---------------------------------------------------------------------------

def _rot_x(angle_rad: float) -> FloatArray:
    c, s = math.cos(angle_rad), math.sin(angle_rad)
    return np.array([[1.0, 0.0, 0.0], [0.0, c, -s], [0.0, s, c]])


def _rot_z(angle_rad: float) -> FloatArray:
    c, s = math.cos(angle_rad), math.sin(angle_rad)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


_EQ_TO_ECL = _rot_x(-math.radians(OBLIQUITY_J2000_DEG))
_ECL_TO_EQ = _rot_x(math.radians(OBLIQUITY_J2000_DEG))


def equatorial_to_ecliptic(vec: ArrayLike) -> FloatArray:
    """Rotate vector(s) from the J2000 equatorial frame to the J2000 ecliptic frame."""
    v = np.asarray(vec, dtype=np.float64)
    return v @ _EQ_TO_ECL.T


def ecliptic_to_equatorial(vec: ArrayLike) -> FloatArray:
    """Rotate vector(s) from the J2000 ecliptic frame to the J2000 equatorial frame."""
    v = np.asarray(vec, dtype=np.float64)
    return v @ _ECL_TO_EQ.T


def unit_vector_to_radec(u: ArrayLike) -> tuple[float, float]:
    """Return (RA, Dec) in degrees for a (not necessarily unit) equatorial vector."""
    x, y, z = (float(c) for c in np.asarray(u, dtype=np.float64))
    norm = math.sqrt(x * x + y * y + z * z)
    if norm == 0.0:
        raise ValueError("zero-length vector has no direction")
    ra = math.degrees(math.atan2(y, x)) % 360.0
    dec = math.degrees(math.asin(max(-1.0, min(1.0, z / norm))))
    return ra, dec


# ---------------------------------------------------------------------------
# Universal-variable propagation
# ---------------------------------------------------------------------------

def stumpff_c2c3(psi: ArrayLike) -> tuple[FloatArray, FloatArray]:
    """Stumpff functions c2(psi) and c3(psi), stable for every sign of psi.

    Uses a series near zero to avoid cancellation, and clips very negative
    arguments to avoid overflow in ``cosh``/``sinh``.
    """
    psi = np.atleast_1d(np.asarray(psi, dtype=np.float64))
    c2 = np.empty_like(psi)
    c3 = np.empty_like(psi)

    small = np.abs(psi) < 1e-3
    pos = (psi >= 1e-3)
    neg = (psi <= -1e-3)

    p = psi[small]
    c2[small] = 0.5 - p / 24.0 + p * p / 720.0 - p**3 / 40320.0
    c3[small] = 1.0 / 6.0 - p / 120.0 + p * p / 5040.0 - p**3 / 362880.0

    sp = np.sqrt(psi[pos])
    c2[pos] = (1.0 - np.cos(sp)) / psi[pos]
    c3[pos] = (sp - np.sin(sp)) / sp**3

    sn = np.sqrt(np.minimum(-psi[neg], 700.0**2))
    c2[neg] = (np.cosh(sn) - 1.0) / (sn * sn)
    c3[neg] = (np.sinh(sn) - sn) / sn**3
    return c2, c3


def propagate_universal(
    r0: ArrayLike,
    v0: ArrayLike,
    dt: ArrayLike,
    mu: float = GM_SUN,
    *,
    tol: float = 1e-13,
    max_iter: int = 60,
) -> tuple[FloatArray, FloatArray]:
    """Propagate a two-body state by time offsets ``dt`` (days, scalar or array).

    Parameters
    ----------
    r0, v0 : array_like, shape (3,)
        Position (au) and velocity (au/day) at the reference epoch.
    dt : array_like
        Time offsets from the reference epoch, in days. May be negative.
    mu : float
        Gravitational parameter in au^3/day^2.

    Returns
    -------
    r, v : ndarray, shape (N, 3)
        Positions and velocities at each requested offset.
    """
    r0 = np.asarray(r0, dtype=np.float64).reshape(3)
    v0 = np.asarray(v0, dtype=np.float64).reshape(3)
    dt = np.atleast_1d(np.asarray(dt, dtype=np.float64))

    r0n = float(np.linalg.norm(r0))
    if r0n <= 0.0:
        raise ValueError("initial position must be non-zero")
    v0sq = float(v0 @ v0)
    sqmu = math.sqrt(mu)
    rdotv = float(r0 @ v0)
    sigma0 = rdotv / sqmu
    alpha = 2.0 / r0n - v0sq / mu  # 1/a ; negative for hyperbolas
    one_minus_ar0 = 1.0 - alpha * r0n

    # Initial guess: valid for small |dt|; refine with the hyperbolic guess
    # of Vallado (2013) where it is defined.
    chi = sqmu * dt / r0n
    if alpha > 1e-12:
        chi = sqmu * dt * alpha
    elif alpha < -1e-12:
        a = 1.0 / alpha
        sgn = np.sign(dt)
        denom = rdotv + sgn * np.sqrt(-mu * a) * one_minus_ar0
        with np.errstate(divide="ignore", invalid="ignore"):
            arg = (-2.0 * mu * alpha * dt) / denom
            guess = sgn * np.sqrt(-a) * np.log(arg)
        ok = np.isfinite(guess) & (arg > 0)
        chi = np.where(ok, guess, chi)

    n_lag = 5.0
    converged = np.zeros(dt.shape, dtype=bool)
    for _ in range(max_iter):
        z = alpha * chi * chi
        c2, c3 = stumpff_c2c3(z)
        chi2 = chi * chi
        f = sigma0 * chi2 * c2 + one_minus_ar0 * chi2 * chi * c3 + r0n * chi - sqmu * dt
        fp = sigma0 * chi * (1.0 - z * c3) + one_minus_ar0 * chi2 * c2 + r0n
        fpp = sigma0 * (1.0 - z * c2) + one_minus_ar0 * chi * (1.0 - z * c3)
        disc = np.sqrt(np.abs((n_lag - 1.0) ** 2 * fp * fp - n_lag * (n_lag - 1.0) * f * fpp))
        denom = fp + np.sign(fp) * disc
        denom = np.where(denom == 0.0, fp, denom)
        delta = n_lag * f / denom
        chi = np.where(converged, chi, chi - delta)
        converged |= np.abs(delta) <= tol * np.maximum(1.0, np.abs(chi))
        if converged.all():
            break
    else:
        if not converged.all():
            raise RuntimeError("universal Kepler equation did not converge")

    z = alpha * chi * chi
    c2, c3 = stumpff_c2c3(z)
    chi2 = chi * chi
    f = 1.0 - chi2 * c2 / r0n
    g = dt - chi2 * chi * c3 / sqmu
    r = f[:, None] * r0[None, :] + g[:, None] * v0[None, :]
    rn = np.linalg.norm(r, axis=1)
    fdot = sqmu / (rn * r0n) * chi * (z * c3 - 1.0)
    gdot = 1.0 - chi2 * c2 / rn
    v = fdot[:, None] * r0[None, :] + gdot[:, None] * v0[None, :]
    return r, v


def _nongrav_rhs(mu: float, a1: float):
    def rhs(_t: float, y: FloatArray) -> FloatArray:
        r = y[:3]
        rn = math.sqrt(r @ r)
        acc = (-mu / rn**3 + a1 / rn**3) * r  # A1 * (1 au/r)^2 * r_hat
        return np.concatenate([y[3:], acc])

    return rhs


def propagate(
    state0: ArrayLike,
    dt: ArrayLike,
    *,
    mu: float = GM_SUN,
    a1: float = 0.0,
    rtol: float = 1e-12,
    atol: float = 1e-14,
) -> tuple[FloatArray, FloatArray]:
    """Propagate a 6-element state by ``dt`` days.

    With ``a1 == 0`` this is exact two-body motion (:func:`propagate_universal`).
    With ``a1 != 0`` a radial acceleration ``a1 * (1 au / r)^2`` (au/day^2) is
    added and the motion is integrated numerically. Positive ``a1`` pushes
    away from the Sun, as outgassing usually does.
    """
    s = np.asarray(state0, dtype=np.float64).reshape(6)
    dt = np.atleast_1d(np.asarray(dt, dtype=np.float64))
    if a1 == 0.0:
        return propagate_universal(s[:3], s[3:], dt, mu)

    out_r = np.empty((dt.size, 3))
    out_v = np.empty((dt.size, 3))
    rhs = _nongrav_rhs(mu, a1)
    for sign in (1.0, -1.0):
        mask = (dt > 0) if sign > 0 else (dt <= 0)
        if not mask.any():
            continue
        tgt = dt[mask]
        t_end = float(tgt.max()) if sign > 0 else float(tgt.min())
        if t_end == 0.0:
            out_r[mask] = s[:3]
            out_v[mask] = s[3:]
            continue
        sol = solve_ivp(rhs, (0.0, t_end), s, method="DOP853", rtol=rtol, atol=atol,
                        dense_output=True)
        if not sol.success:
            raise RuntimeError(f"non-gravitational integration failed: {sol.message}")
        y = sol.sol(tgt)
        out_r[mask] = y[:3].T
        out_v[mask] = y[3:].T
    return out_r, out_v


# ---------------------------------------------------------------------------
# Elements
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class OrbitalElements:
    """Osculating heliocentric elements (angles in degrees, lengths in au).

    ``a`` is negative for hyperbolic orbits and infinite for parabolic ones.
    ``q`` (perihelion distance) is always finite and positive.
    """

    a: float
    e: float
    q: float
    i_deg: float
    node_deg: float
    peri_deg: float
    true_anomaly_deg: float
    specific_energy: float  # au^2/day^2
    v_infinity_kms: float | None

    @property
    def is_bound(self) -> bool:
        return self.e < 1.0

    def as_dict(self) -> dict:
        return asdict(self)


def specific_energy(r: ArrayLike, v: ArrayLike, mu: float = GM_SUN) -> float:
    """Specific orbital energy v^2/2 - mu/r (au^2/day^2). Positive means unbound."""
    r = np.asarray(r, dtype=np.float64)
    v = np.asarray(v, dtype=np.float64)
    return float(0.5 * (v @ v) - mu / np.linalg.norm(r))


def escape_speed(r_au: ArrayLike, mu: float = GM_SUN) -> FloatArray:
    """Local escape speed sqrt(2 mu / r) in au/day."""
    return np.sqrt(2.0 * mu / np.asarray(r_au, dtype=np.float64))


def hyperbolic_excess_speed_kms(r: ArrayLike, v: ArrayLike, mu: float = GM_SUN) -> float | None:
    """Hyperbolic excess speed v_inf in km/s, or ``None`` if the orbit is bound."""
    energy = specific_energy(r, v, mu)
    if energy <= 0.0:
        return None
    return math.sqrt(2.0 * energy) * KMS_PER_AU_DAY


def v_infinity_from_q_e_kms(q_au: float, e: float, mu: float = GM_SUN) -> float:
    """v_inf = sqrt(mu (e - 1) / q) in km/s, for e > 1."""
    if e <= 1.0:
        raise ValueError("v_infinity is only defined for hyperbolic orbits (e > 1)")
    return math.sqrt(mu * (e - 1.0) / q_au) * KMS_PER_AU_DAY


def state_to_elements(r: ArrayLike, v: ArrayLike, mu: float = GM_SUN) -> OrbitalElements:
    """Convert a heliocentric state vector to osculating elements.

    Angles are measured in whatever frame (r, v) are expressed in. Pass
    ecliptic vectors to compare with catalog elements.
    """
    r = np.asarray(r, dtype=np.float64).reshape(3)
    v = np.asarray(v, dtype=np.float64).reshape(3)
    rn = float(np.linalg.norm(r))
    h = np.cross(r, v)
    hn = float(np.linalg.norm(h))
    if hn == 0.0:
        raise ValueError("rectilinear orbit (zero angular momentum) has undefined elements")
    e_vec = ((v @ v - mu / rn) * r - (r @ v) * v) / mu
    e = float(np.linalg.norm(e_vec))
    energy = 0.5 * float(v @ v) - mu / rn
    a = -mu / (2.0 * energy) if energy != 0.0 else math.inf
    q = hn * hn / (mu * (1.0 + e))

    inc = math.degrees(math.acos(max(-1.0, min(1.0, h[2] / hn))))
    node_vec = np.array([-h[1], h[0], 0.0])
    nn = float(np.linalg.norm(node_vec))
    if nn > 1e-15 * hn:
        node = math.degrees(math.atan2(node_vec[1], node_vec[0])) % 360.0
    else:  # equatorial orbit: node undefined, use x axis
        node_vec = np.array([1.0, 0.0, 0.0])
        nn = 1.0
        node = 0.0

    h_hat = h / hn
    if e > 1e-12:
        cos_w = float(node_vec @ e_vec) / (nn * e)
        sin_w = float(np.cross(node_vec, e_vec) @ h_hat) / (nn * e)
        peri = math.degrees(math.atan2(sin_w, cos_w)) % 360.0
        cos_nu = float(e_vec @ r) / (e * rn)
        sin_nu = float(np.cross(e_vec, r) @ h_hat) / (e * rn)
        nu = math.degrees(math.atan2(sin_nu, cos_nu))
    else:  # circular: argument of latitude stands in for true anomaly
        peri = 0.0
        cos_u = float(node_vec @ r) / (nn * rn)
        sin_u = float(np.cross(node_vec, r) @ h_hat) / (nn * rn)
        nu = math.degrees(math.atan2(sin_u, cos_u))

    v_inf = math.sqrt(2.0 * energy) * KMS_PER_AU_DAY if energy > 0 else None
    return OrbitalElements(a=a, e=e, q=q, i_deg=inc, node_deg=node, peri_deg=peri,
                           true_anomaly_deg=nu, specific_energy=energy, v_infinity_kms=v_inf)


def _perifocal_basis(i_deg: float, node_deg: float, peri_deg: float) -> tuple[FloatArray, FloatArray, FloatArray]:
    rot = _rot_z(math.radians(node_deg)) @ _rot_x(math.radians(i_deg)) @ _rot_z(math.radians(peri_deg))
    return rot[:, 0], rot[:, 1], rot[:, 2]


def elements_to_state(
    q: float,
    e: float,
    i_deg: float,
    node_deg: float,
    peri_deg: float,
    true_anomaly_deg: float,
    mu: float = GM_SUN,
) -> FloatArray:
    """Convert (q, e, i, node, argument of perihelion, true anomaly) to a state vector.

    Works for every conic because it is written in terms of the perihelion
    distance ``q``. For hyperbolas the true anomaly must satisfy
    ``|nu| < arccos(-1/e)``.
    """
    if q <= 0:
        raise ValueError("perihelion distance must be positive")
    nu = math.radians(true_anomaly_deg)
    if e > 1.0 and abs(nu) >= math.acos(-1.0 / e):
        raise ValueError("true anomaly is beyond the hyperbolic asymptote")
    p = q * (1.0 + e)
    r = p / (1.0 + e * math.cos(nu))
    pv, qv, _ = _perifocal_basis(i_deg, node_deg, peri_deg)
    pos = r * (math.cos(nu) * pv + math.sin(nu) * qv)
    vel = math.sqrt(mu / p) * (-math.sin(nu) * pv + (e + math.cos(nu)) * qv)
    return np.concatenate([pos, vel])


def incoming_radiant(r: ArrayLike, v: ArrayLike, mu: float = GM_SUN) -> FloatArray:
    """Unit vector pointing to where a hyperbolic object came from (its radiant).

    This is the direction of the incoming asymptote as seen from the Sun,
    ``-(1/e) P - sqrt(1 - 1/e^2) Q`` in the perifocal basis. It is expressed in
    the same frame as the input vectors. Convert to RA/Dec with
    :func:`unit_vector_to_radec` when the inputs are equatorial.
    """
    r = np.asarray(r, dtype=np.float64).reshape(3)
    v = np.asarray(v, dtype=np.float64).reshape(3)
    rn = float(np.linalg.norm(r))
    h = np.cross(r, v)
    e_vec = ((v @ v - mu / rn) * r - (r @ v) * v) / mu
    e = float(np.linalg.norm(e_vec))
    if e <= 1.0:
        raise ValueError("a radiant (incoming asymptote) exists only for hyperbolic orbits")
    p_hat = e_vec / e
    q_hat = np.cross(h / np.linalg.norm(h), p_hat)
    return -(1.0 / e) * p_hat - math.sqrt(1.0 - 1.0 / (e * e)) * q_hat
