"""Tilted orbits as signposts to unseen outer planets.

For young readers
-----------------
A spinning top that leans over without falling is being pushed by
something. Some planets orbit at a big tilt compared with how their star
spins. One possible reason is a heavy, unseen planet farther out that keeps
"pushing" the tilt in step. This file works out how heavy and how far away
such a hidden planet would need to be.

For experts
-----------
Two sources make an inner planet's orbit node precess:

* the star's rotational oblateness: ``g_* = (3/2) J2 (R*/a1)^2 n1 cos(psi)``
* an outer companion (Laplace–Lagrange):
  ``g_12 = (1/4) n1 (m2/M*) alpha^2 b_{3/2}^{(1)}(alpha)``, ``alpha = a1/a2``

A secular resonance g_* ~ g_12 can excite or maintain obliquity (e.g. the
"disk-driven resonance" scenario of Petrovich et al. 2020, AJ 160, 275).
Setting the two equal gives a locus in (a2, m2) that tells observers where
to look with radial velocities or Gaia astrometry. In the hierarchical limit
(b ~ 3 alpha) this is ``(m2/M*)(a1/a2)^3 ~ 2 J2 (R*/a1)^2 cos(psi)``.

This is a simplified, two-frequency condition. It ignores planet–planet
coupling beyond lowest order, general relativity, disk dispersal, and the
inner planet's back-reaction on the star; treat results as targeting
guidance, not predictions.
"""

from __future__ import annotations

import math

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.integrate import quad

from .constants import DAY_S, GM_SUN_KM3_S2, M_JUPITER_MSUN, R_SUN_AU, AU_KM

FloatArray = NDArray[np.float64]

__all__ = ["laplace_coefficient", "mean_motion_rad_per_day", "stellar_quadrupole_nodal_rate",
           "companion_nodal_rate", "j2_from_rotation", "resonant_companion_mass_mjup"]


def laplace_coefficient(s: float, j: int, alpha: float) -> float:
    """b_s^(j)(alpha) = (1/pi) * integral_0^{2pi} cos(j psi) / (1 - 2 alpha cos psi + alpha^2)^s d psi."""
    if not (0.0 <= alpha < 1.0):
        raise ValueError("alpha must be in [0, 1)")

    def integrand(psi: float) -> float:
        return math.cos(j * psi) / (1.0 - 2.0 * alpha * math.cos(psi) + alpha * alpha) ** s

    val, _ = quad(integrand, 0.0, 2.0 * math.pi, limit=200, epsabs=1e-13, epsrel=1e-11)
    return val / math.pi


def mean_motion_rad_per_day(a_au: float, mstar_msun: float = 1.0) -> float:
    """Keplerian mean motion n = sqrt(G M / a^3) in rad/day."""
    a_km = a_au * AU_KM
    return math.sqrt(GM_SUN_KM3_S2 * mstar_msun / a_km**3) * DAY_S


def stellar_quadrupole_nodal_rate(j2: float, rstar_rsun: float, a1_au: float, psi_deg: float,
                                  mstar_msun: float = 1.0) -> float:
    """|dOmega/dt| from stellar oblateness, rad/day (precession is retrograde)."""
    n1 = mean_motion_rad_per_day(a1_au, mstar_msun)
    return 1.5 * j2 * (rstar_rsun * R_SUN_AU / a1_au) ** 2 * n1 * math.cos(math.radians(psi_deg))


def companion_nodal_rate(m2_msun: float, a1_au: float, a2_au: float, mstar_msun: float = 1.0) -> float:
    """|dOmega/dt| of an inner orbit induced by an outer companion, rad/day (lowest order)."""
    if not a1_au < a2_au:
        raise ValueError("companion must be exterior: a1 < a2")
    alpha = a1_au / a2_au
    n1 = mean_motion_rad_per_day(a1_au, mstar_msun)
    return 0.25 * n1 * (m2_msun / mstar_msun) * alpha**2 * laplace_coefficient(1.5, 1, alpha)


def j2_from_rotation(prot_days: float, rstar_rsun: float = 1.0, mstar_msun: float = 1.0, k2: float = 0.03) -> float:
    """Order-of-magnitude J2 = (k2/3) Omega^2 R^3 / (G M) for a rotating star.

    k2 (the apsidal-motion constant / Love number) is ~0.01-0.03 for Sun-like stars.
    The Sun (P ~ 25 d) gives ~2e-7, close to the measured 2.2e-7.
    """
    omega = 2.0 * math.pi / (prot_days * DAY_S)
    r_km = rstar_rsun * R_SUN_AU * AU_KM
    return k2 / 3.0 * omega**2 * r_km**3 / (GM_SUN_KM3_S2 * mstar_msun)


def resonant_companion_mass_mjup(
    a2_au: ArrayLike,
    *,
    j2: float,
    rstar_rsun: float,
    a1_au: float,
    psi_deg: float,
    mstar_msun: float = 1.0,
) -> FloatArray:
    """Companion mass (Jupiter masses) at each ``a2`` for which g_12 = g_* (secular resonance)."""
    a2 = np.atleast_1d(np.asarray(a2_au, dtype=np.float64))
    g_star = stellar_quadrupole_nodal_rate(j2, rstar_rsun, a1_au, psi_deg, mstar_msun)
    out = np.empty_like(a2)
    for k, a in enumerate(a2):
        per_unit_mass = companion_nodal_rate(1.0, a1_au, float(a), mstar_msun)  # rate for m2 = 1 Msun
        out[k] = (g_star / per_unit_mass) / M_JUPITER_MSUN
    return out
