"""Parallax and proper motion: how nearby objects wiggle and drift across the sky.

For young readers
-----------------
Hold up your thumb and close one eye, then the other. Your thumb seems to
jump. That jump is called parallax. As the Earth goes around the Sun, nearby
stars and cold "failed stars" seem to jump back and forth a little each year.
Close objects jump more. They also drift in a straight line as they travel
through space. This file measures both.

For experts
-----------
Standard five-parameter astrometric model in the gnomonic tangent plane about
a reference point (alpha_0, delta_0):

    xi(t)  = xi_0  + mu_alpha* (t - t_0) + varpi * f_alpha(t)
    eta(t) = eta_0 + mu_delta  (t - t_0) + varpi * f_delta(t)

with parallax factors f_alpha = X sin a - Y cos a and
f_delta = (X cos a + Y sin a) sin d - Z cos d, where (X, Y, Z) is the
observer's barycentric position in au. This module uses the heliocentric
Earth from :mod:`fdastro.ephemeris` (differs from barycentric by ~0.01 au,
i.e. ~1% in the parallax factor) unless you pass your own positions.
Solved by weighted linear least squares.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray

from .constants import ARCSEC_PER_RAD, JULIAN_YEAR_DAYS, KMS_PER_AU_PER_YEAR
from .ephemeris import earth_heliocentric

FloatArray = NDArray[np.float64]

__all__ = ["parallax_factors", "gnomonic", "inverse_gnomonic", "FiveParameterFit",
           "fit_five_parameter", "simulate_five_parameter", "tangential_velocity_kms"]


def parallax_factors(mjd: ArrayLike, ra_deg: float, dec_deg: float,
                     observer_au: ArrayLike | None = None) -> tuple[FloatArray, FloatArray]:
    """Parallax factors (f_alpha*, f_delta), in au, for a source at (ra, dec)."""
    t = np.atleast_1d(np.asarray(mjd, dtype=np.float64))
    pos = earth_heliocentric(t) if observer_au is None else np.asarray(observer_au, dtype=np.float64)
    x, y, z = pos[:, 0], pos[:, 1], pos[:, 2]
    a, d = math.radians(ra_deg), math.radians(dec_deg)
    f_a = x * math.sin(a) - y * math.cos(a)
    f_d = (x * math.cos(a) + y * math.sin(a)) * math.sin(d) - z * math.cos(d)
    return f_a, f_d


def gnomonic(ra_deg: ArrayLike, dec_deg: ArrayLike, ra0_deg: float, dec0_deg: float) -> tuple[FloatArray, FloatArray]:
    """Tangent-plane coordinates (xi, eta) in arcsec about (ra0, dec0)."""
    a = np.deg2rad(np.asarray(ra_deg, dtype=np.float64))
    d = np.deg2rad(np.asarray(dec_deg, dtype=np.float64))
    a0, d0 = math.radians(ra0_deg), math.radians(dec0_deg)
    cosc = np.sin(d) * math.sin(d0) + np.cos(d) * math.cos(d0) * np.cos(a - a0)
    xi = np.cos(d) * np.sin(a - a0) / cosc
    eta = (np.sin(d) * math.cos(d0) - np.cos(d) * math.sin(d0) * np.cos(a - a0)) / cosc
    return xi * ARCSEC_PER_RAD, eta * ARCSEC_PER_RAD


def inverse_gnomonic(xi_arcsec: ArrayLike, eta_arcsec: ArrayLike, ra0_deg: float, dec0_deg: float) -> tuple[FloatArray, FloatArray]:
    """Inverse of :func:`gnomonic`; returns (ra_deg, dec_deg)."""
    xi = np.asarray(xi_arcsec, dtype=np.float64) / ARCSEC_PER_RAD
    eta = np.asarray(eta_arcsec, dtype=np.float64) / ARCSEC_PER_RAD
    a0, d0 = math.radians(ra0_deg), math.radians(dec0_deg)
    denom = math.cos(d0) - eta * math.sin(d0)
    a = a0 + np.arctan2(xi, denom)
    d = np.arctan2(math.sin(d0) + eta * math.cos(d0), np.hypot(xi, denom))
    return np.rad2deg(a) % 360.0, np.rad2deg(d)


@dataclass(frozen=True)
class FiveParameterFit:
    ra0_deg: float
    dec0_deg: float
    ref_mjd: float
    xi0_arcsec: float
    eta0_arcsec: float
    pmra_arcsec_yr: float      # mu_alpha* (includes cos dec)
    pmdec_arcsec_yr: float
    parallax_arcsec: float
    sigmas: dict
    chi2: float
    dof: int
    rms_arcsec: float

    @property
    def proper_motion_arcsec_yr(self) -> float:
        return math.hypot(self.pmra_arcsec_yr, self.pmdec_arcsec_yr)

    @property
    def parallax_snr(self) -> float:
        s = self.sigmas["parallax_arcsec"]
        return self.parallax_arcsec / s if s > 0 else math.inf

    @property
    def distance_pc(self) -> float | None:
        """1/parallax, only when parallax is detected at > 5 sigma (naive inversion)."""
        if self.parallax_arcsec <= 0 or self.parallax_snr < 5.0:
            return None
        return 1.0 / self.parallax_arcsec


def fit_five_parameter(
    mjd: ArrayLike,
    ra_deg: ArrayLike,
    dec_deg: ArrayLike,
    sigma_arcsec: ArrayLike = 0.1,
    *,
    ra0_deg: float | None = None,
    dec0_deg: float | None = None,
    ref_mjd: float | None = None,
    observer_au: ArrayLike | None = None,
) -> FiveParameterFit:
    """Weighted least-squares fit of position, proper motion and parallax."""
    t = np.atleast_1d(np.asarray(mjd, dtype=np.float64))
    ra = np.atleast_1d(np.asarray(ra_deg, dtype=np.float64))
    dec = np.atleast_1d(np.asarray(dec_deg, dtype=np.float64))
    n = t.size
    if n < 3:
        raise ValueError("need at least 3 epochs (5 parameters from 2 coordinates each)")
    sig = np.broadcast_to(np.asarray(sigma_arcsec, dtype=np.float64), t.shape)
    if ra0_deg is None or dec0_deg is None:
        u = np.stack([np.cos(np.deg2rad(dec)) * np.cos(np.deg2rad(ra)),
                      np.cos(np.deg2rad(dec)) * np.sin(np.deg2rad(ra)),
                      np.sin(np.deg2rad(dec))], axis=1).mean(axis=0)
        ra0_deg = math.degrees(math.atan2(u[1], u[0])) % 360.0
        dec0_deg = math.degrees(math.asin(u[2] / np.linalg.norm(u)))
    t0 = float(np.mean(t)) if ref_mjd is None else float(ref_mjd)
    dt_yr = (t - t0) / JULIAN_YEAR_DAYS
    xi, eta = gnomonic(ra, dec, ra0_deg, dec0_deg)
    f_a, f_d = parallax_factors(t, ra0_deg, dec0_deg, observer_au)

    design = np.zeros((2 * n, 5))
    design[:n, 0] = 1.0
    design[:n, 2] = dt_yr
    design[:n, 4] = f_a
    design[n:, 1] = 1.0
    design[n:, 3] = dt_yr
    design[n:, 4] = f_d
    obs = np.concatenate([xi, eta])
    w = 1.0 / np.concatenate([sig, sig])
    aw = design * w[:, None]
    bw = obs * w
    params, *_ = np.linalg.lstsq(aw, bw, rcond=None)
    cov = np.linalg.pinv(aw.T @ aw)
    resid = obs - design @ params
    chi2 = float(np.sum((resid * w) ** 2))
    errs = np.sqrt(np.clip(np.diag(cov), 0.0, None))
    names = ["xi0_arcsec", "eta0_arcsec", "pmra_arcsec_yr", "pmdec_arcsec_yr", "parallax_arcsec"]
    return FiveParameterFit(
        ra0_deg=float(ra0_deg), dec0_deg=float(dec0_deg), ref_mjd=t0,
        xi0_arcsec=float(params[0]), eta0_arcsec=float(params[1]),
        pmra_arcsec_yr=float(params[2]), pmdec_arcsec_yr=float(params[3]),
        parallax_arcsec=float(params[4]),
        sigmas={k: float(v) for k, v in zip(names, errs)},
        chi2=chi2, dof=2 * n - 5, rms_arcsec=float(np.sqrt(np.mean(resid**2))),
    )


def simulate_five_parameter(
    mjd: ArrayLike, ra0_deg: float, dec0_deg: float, *, pmra_arcsec_yr: float,
    pmdec_arcsec_yr: float, parallax_arcsec: float, ref_mjd: float | None = None,
    sigma_arcsec: float = 0.0, rng: np.random.Generator | int | None = None,
) -> tuple[FloatArray, FloatArray]:
    """Synthetic (ra, dec) track for given astrometric parameters."""
    t = np.atleast_1d(np.asarray(mjd, dtype=np.float64))
    t0 = float(np.mean(t)) if ref_mjd is None else float(ref_mjd)
    dt_yr = (t - t0) / JULIAN_YEAR_DAYS
    f_a, f_d = parallax_factors(t, ra0_deg, dec0_deg)
    xi = pmra_arcsec_yr * dt_yr + parallax_arcsec * f_a
    eta = pmdec_arcsec_yr * dt_yr + parallax_arcsec * f_d
    if sigma_arcsec > 0:
        gen = np.random.default_rng(rng)
        xi = xi + gen.normal(0.0, sigma_arcsec, t.size)
        eta = eta + gen.normal(0.0, sigma_arcsec, t.size)
    return inverse_gnomonic(xi, eta, ra0_deg, dec0_deg)


def tangential_velocity_kms(proper_motion_arcsec_yr: float, parallax_arcsec: float) -> float:
    """v_tan = 4.74 * mu / parallax (km/s), with mu and parallax in arcsec(/yr)."""
    if parallax_arcsec <= 0:
        raise ValueError("parallax must be positive")
    return KMS_PER_AU_PER_YEAR * proper_motion_arcsec_yr / parallax_arcsec
