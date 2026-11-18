"""Gravitational microlensing: when a dark object briefly magnifies a background star.

For young readers
-----------------
Gravity can bend light, a bit like the bottom of a glass bends what you see
through it. When a dark planet floats in front of a faraway star, the star
can look brighter for a short time. Small planets make short flashes, only
hours long. Big objects make longer ones.

For experts
-----------
Point-source point-lens (Paczynski 1986) magnification
A(u) = (u^2 + 2) / (u sqrt(u^2 + 4)), u(t)^2 = u0^2 + ((t - t0)/tE)^2.
Einstein radius theta_E = sqrt(kappa M pi_rel), kappa = 4G/(c^2 au) = 8.144 mas/Msun,
pi_rel = au (1/D_L - 1/D_S). Timescale t_E = theta_E / mu_rel. Since
t_E ~ sqrt(M), Earth-mass lenses give hours-long events (cf. Mróz et al.
2020, ApJL 903, L11). Finite-source effects (rho = theta_*/theta_E) are
important for such short events and are not modelled here.

Lensing is achromatic: the source colour should not change during the event
(blending aside). :func:`achromaticity_test` checks that.
"""

from __future__ import annotations

import math

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.stats import chi2 as chi2_dist

from .constants import JULIAN_YEAR_DAYS, MICROLENS_KAPPA_MAS_PER_MSUN

FloatArray = NDArray[np.float64]

__all__ = ["relative_parallax_mas", "einstein_radius_mas", "einstein_time_days",
           "lens_mass_msun", "paczynski_magnification", "achromaticity_test"]


def relative_parallax_mas(d_lens_kpc: float, d_source_kpc: float) -> float:
    if not 0 < d_lens_kpc < d_source_kpc:
        raise ValueError("need 0 < D_L < D_S")
    return 1.0 / d_lens_kpc - 1.0 / d_source_kpc


def einstein_radius_mas(mass_msun: float, d_lens_kpc: float, d_source_kpc: float) -> float:
    return math.sqrt(MICROLENS_KAPPA_MAS_PER_MSUN * mass_msun * relative_parallax_mas(d_lens_kpc, d_source_kpc))


def einstein_time_days(mass_msun: float, d_lens_kpc: float, d_source_kpc: float, mu_rel_mas_yr: float) -> float:
    return einstein_radius_mas(mass_msun, d_lens_kpc, d_source_kpc) / mu_rel_mas_yr * JULIAN_YEAR_DAYS


def lens_mass_msun(t_e_days: float, d_lens_kpc: float, d_source_kpc: float, mu_rel_mas_yr: float) -> float:
    """Invert t_E for the lens mass, given assumed distances and relative proper motion."""
    theta_e = t_e_days / JULIAN_YEAR_DAYS * mu_rel_mas_yr
    return theta_e**2 / (MICROLENS_KAPPA_MAS_PER_MSUN * relative_parallax_mas(d_lens_kpc, d_source_kpc))


def paczynski_magnification(t: ArrayLike, t0: float, t_e: float, u0: float) -> FloatArray:
    tt = np.asarray(t, dtype=np.float64)
    u = np.sqrt(u0 * u0 + ((tt - t0) / t_e) ** 2)
    return (u * u + 2.0) / (u * np.sqrt(u * u + 4.0))


def achromaticity_test(mag_a: ArrayLike, err_a: ArrayLike, mag_b: ArrayLike, err_b: ArrayLike) -> dict:
    """Chi-square test that the colour (a - b) stays constant through an event.

    Use simultaneous (or interpolated) magnitudes in two bands. Blending with
    a differently coloured neighbour can produce colour changes even for real
    lensing, so a failure is a flag, not a verdict.
    """
    a = np.asarray(mag_a, dtype=np.float64)
    b = np.asarray(mag_b, dtype=np.float64)
    color = a - b
    err = np.sqrt(np.asarray(err_a, dtype=np.float64) ** 2 + np.asarray(err_b, dtype=np.float64) ** 2)
    w = 1.0 / err**2
    mean = float(np.sum(w * color) / np.sum(w))
    chi2 = float(np.sum(w * (color - mean) ** 2))
    dof = int(color.size - 1)
    p = float(chi2_dist.sf(chi2, dof)) if dof > 0 else 1.0
    return {"mean_color": mean, "chi2": chi2, "dof": dof, "p_value": p, "achromatic": bool(p > 0.01)}
