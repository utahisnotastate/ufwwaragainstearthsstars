"""Find single transits and test whether transits are fading.

For young readers
-----------------
When a planet passes in front of its star, the star looks a tiny bit dimmer
for a few hours. That is called a transit. Some planets take so long to go
around their star that a telescope sees only one transit. Others slowly tip
their orbits so each transit gets shallower until it disappears. This file
helps find both.

For experts
-----------
* :func:`detrend_running_median` — robust, transit-preserving detrending
  when the window is >~3x the longest transit duration searched.
* :func:`single_event_search` — matched box filter over a grid of durations,
  O(N) per duration via cumulative sums; SNR uses a robust (MAD) noise
  estimate. Red noise is not modelled: treat SNR as optimistic and inspect
  candidates (momentum dumps, scattered light, eclipsing binaries).
* :func:`depth_trend_test` — weighted linear regression of per-transit depth
  versus time (e.g. for grazing, precessing planets such as TOI-2535 b).
* :func:`min_period_from_duration` — lower bound on the orbital period of a
  single-transit planet from its duration and stellar density (circular
  orbit; b = 0 gives the bound).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.stats import norm

from .constants import DAY_S, GM_SUN_KM3_S2, R_SUN_AU, AU_KM

FloatArray = NDArray[np.float64]

__all__ = ["robust_std", "detrend_running_median", "TransitEvent", "single_event_search",
           "inject_box_transit", "depth_trend_test", "transit_duration_hours",
           "min_period_from_duration", "load_tess_lightcurve"]


def robust_std(x: ArrayLike) -> float:
    """1.4826 x median absolute deviation (equals sigma for Gaussian noise)."""
    a = np.asarray(x, dtype=np.float64)
    a = a[np.isfinite(a)]
    return float(1.4826 * np.median(np.abs(a - np.median(a))))


def detrend_running_median(time: ArrayLike, flux: ArrayLike, window_days: float = 1.0) -> FloatArray:
    """Divide the flux by a running median computed in a time window."""
    t = np.asarray(time, dtype=np.float64)
    f = np.asarray(flux, dtype=np.float64)
    order = np.argsort(t)
    ts, fs = t[order], f[order]
    half = 0.5 * window_days
    lo = np.searchsorted(ts, ts - half, side="left")
    hi = np.searchsorted(ts, ts + half, side="right")
    trend = np.array([np.nanmedian(fs[a:b]) for a, b in zip(lo, hi)])
    out = np.empty_like(f)
    out[order] = fs / trend
    return out


@dataclass(frozen=True)
class TransitEvent:
    t_mid: float
    duration_days: float
    depth: float
    depth_err: float
    snr: float
    n_points: int


def single_event_search(
    time: ArrayLike,
    flux: ArrayLike,
    *,
    durations_hours: ArrayLike = (1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0),
    snr_threshold: float = 7.0,
    min_points: int = 3,
) -> list[TransitEvent]:
    """Matched-box search for individual transit-like dips in normalized flux (~1).

    Overlapping detections are merged, keeping the highest SNR.
    """
    t = np.asarray(time, dtype=np.float64)
    f = np.asarray(flux, dtype=np.float64)
    good = np.isfinite(t) & np.isfinite(f)
    t, f = t[good], f[good]
    order = np.argsort(t)
    t, f = t[order], f[order]
    dip = 1.0 - f
    sigma = robust_std(dip)
    if sigma <= 0:
        return []
    csum = np.concatenate([[0.0], np.cumsum(dip)])

    found: list[TransitEvent] = []
    for dur_h in np.atleast_1d(np.asarray(durations_hours, dtype=np.float64)):
        dur = dur_h / 24.0
        lo = np.searchsorted(t, t - 0.5 * dur, side="left")
        hi = np.searchsorted(t, t + 0.5 * dur, side="right")
        npts = hi - lo
        ok = npts >= min_points
        depth = np.zeros_like(t)
        depth[ok] = (csum[hi[ok]] - csum[lo[ok]]) / npts[ok]
        err = np.full_like(t, np.inf)
        err[ok] = sigma / np.sqrt(npts[ok])
        snr = depth / err
        idx = np.flatnonzero(snr >= snr_threshold)
        for k in idx:
            found.append(TransitEvent(float(t[k]), float(dur), float(depth[k]), float(err[k]),
                                      float(snr[k]), int(npts[k])))

    found.sort(key=lambda e: -e.snr)
    kept: list[TransitEvent] = []
    for ev in found:
        if all(abs(ev.t_mid - k.t_mid) > 0.5 * (ev.duration_days + k.duration_days) for k in kept):
            kept.append(ev)
    return sorted(kept, key=lambda e: e.t_mid)


def inject_box_transit(time: ArrayLike, flux: ArrayLike, t_mid: float, duration_days: float, depth: float) -> FloatArray:
    """Return a copy of ``flux`` with a box-shaped transit injected (for tests and teaching)."""
    t = np.asarray(time, dtype=np.float64)
    out = np.array(flux, dtype=np.float64, copy=True)
    out[np.abs(t - t_mid) <= 0.5 * duration_days] -= depth
    return out


def depth_trend_test(epochs: ArrayLike, depths: ArrayLike, depth_errs: ArrayLike) -> dict:
    """Is transit depth changing linearly with time?

    Returns the weighted slope (depth per unit time), its error, the
    two-sided p-value of "no trend", and the chi-square of a constant-depth model.
    """
    x = np.asarray(epochs, dtype=np.float64)
    y = np.asarray(depths, dtype=np.float64)
    s = np.asarray(depth_errs, dtype=np.float64)
    if x.size < 3:
        raise ValueError("need at least 3 transits")
    w = 1.0 / s**2
    xm = np.sum(w * x) / np.sum(w)
    sxx = np.sum(w * (x - xm) ** 2)
    slope = float(np.sum(w * (x - xm) * y) / sxx)
    intercept = float(np.sum(w * y) / np.sum(w) - slope * xm)
    slope_err = float(1.0 / math.sqrt(sxx))
    z = slope / slope_err
    mean_const = float(np.sum(w * y) / np.sum(w))
    chi2_const = float(np.sum(w * (y - mean_const) ** 2))
    chi2_lin = float(np.sum(w * (y - (intercept + slope * x)) ** 2))
    return {
        "slope": slope,
        "slope_err": slope_err,
        "z": float(z),
        "p_value_no_trend": float(2.0 * norm.sf(abs(z))),
        "chi2_constant": chi2_const,
        "chi2_linear": chi2_lin,
        "dof_constant": int(x.size - 1),
        "fading": bool(z < -3.0),
    }


def _a_au(period_days: float, mstar_msun: float) -> float:
    p_s = period_days * DAY_S
    a_km = (GM_SUN_KM3_S2 * mstar_msun * p_s**2 / (4.0 * math.pi**2)) ** (1.0 / 3.0)
    return a_km / AU_KM


def transit_duration_hours(period_days: float, rstar_rsun: float = 1.0, mstar_msun: float = 1.0,
                           b: float = 0.0, rp_over_rs: float = 0.0) -> float:
    """Total transit duration T14 (hours) for a circular orbit (Seager & Mallen-Ornelas 2003)."""
    a_over_r = _a_au(period_days, mstar_msun) / (rstar_rsun * R_SUN_AU)
    inc = math.acos(b / a_over_r)
    chord = math.sqrt(max(0.0, (1.0 + rp_over_rs) ** 2 - b * b))
    arg = min(1.0, chord / (a_over_r * math.sin(inc)))
    return period_days / math.pi * math.asin(arg) * 24.0


def min_period_from_duration(duration_hours: float, rstar_rsun: float = 1.0, mstar_msun: float = 1.0) -> float:
    """Minimum period (days) consistent with a single transit's duration.

    For a circular orbit with impact parameter b, T ~ (P / pi)(R*/a) sqrt(1 - b^2),
    so P = pi G M T^3 / (4 R*^3 (1 - b^2)^(3/2)) >= the b = 0 value returned here.
    (Eccentric orbits can break this bound.)
    """
    t_s = duration_hours * 3600.0
    r_km = rstar_rsun * R_SUN_AU * AU_KM
    p_s = math.pi * GM_SUN_KM3_S2 * mstar_msun * t_s**3 / (4.0 * r_km**3)
    return p_s / DAY_S


def load_tess_lightcurve(target: str, *, author: str = "SPOC", sector: int | None = None):
    """Download and stitch a TESS light curve with :mod:`lightkurve` (optional extra).

    Returns (time_btjd, normalized_flux, flux_err). Requires network access.
    """
    try:
        import lightkurve as lk
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise ImportError("install the optional extra: pip install 'fdastro[archives]'") from exc
    search = lk.search_lightcurve(target, mission="TESS", author=author, sector=sector)
    if len(search) == 0:
        raise LookupError(f"no {author} light curves found for {target!r}")
    lc = search.download_all().stitch().remove_nans().normalize()
    return (np.asarray(lc.time.value, dtype=np.float64), np.asarray(lc.flux.value, dtype=np.float64),
            np.asarray(lc.flux_err.value, dtype=np.float64))
