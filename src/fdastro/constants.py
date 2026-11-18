"""Physical and astronomical constants used across :mod:`fdastro`.

Units follow the usual small-body conventions: astronomical units (au) for
length, days for time, and degrees for angles at the public API boundary.
"""

from __future__ import annotations

import math

#: Gaussian gravitational constant k (au^(3/2) / day / Msun^(1/2)).
GAUSS_K: float = 0.01720209895

#: Heliocentric gravitational parameter GM_sun in au^3 / day^2 (k^2).
GM_SUN: float = GAUSS_K**2

#: GM_sun in km^3 / s^2 (IAU 2015 nominal).
GM_SUN_KM3_S2: float = 1.3271244e11

#: Astronomical unit in km (IAU 2012, exact).
AU_KM: float = 149_597_870.7

#: Seconds per day.
DAY_S: float = 86_400.0

#: Conversion factor from au/day to km/s.
KMS_PER_AU_DAY: float = AU_KM / DAY_S

#: Speed of light in km/s (exact).
C_KMS: float = 299_792.458

#: Speed of light in au/day.
C_AU_PER_DAY: float = C_KMS * DAY_S / AU_KM

#: Arcseconds per radian.
ARCSEC_PER_RAD: float = 180.0 * 3600.0 / math.pi

#: Milliarcseconds per radian.
MAS_PER_RAD: float = ARCSEC_PER_RAD * 1000.0

#: Mean obliquity of the ecliptic at J2000.0, in degrees (IAU 2006).
OBLIQUITY_J2000_DEG: float = 23.4392911

#: Modified Julian Date of the J2000.0 epoch (2000-01-01 12:00 TT).
MJD_J2000: float = 51_544.5

#: Days per Julian year.
JULIAN_YEAR_DAYS: float = 365.25

#: Equatorial radius of the Earth in km (WGS-84 / IERS).
EARTH_RADIUS_KM: float = 6378.137

#: Mean semi-major axis of Jupiter in au (as used for Tisserand parameters,
#: Murray & Dermott 1999). JPL's osculating value differs at the 1e-3 level.
A_JUPITER_AU: float = 5.2026

#: Mean semi-major axis of Neptune in au.
A_NEPTUNE_AU: float = 30.07

#: Solar radius in au (IAU 2015 nominal 695,700 km).
R_SUN_AU: float = 695_700.0 / AU_KM

#: Jupiter mass in solar masses (IAU 2015 nominal ratio).
M_JUPITER_MSUN: float = 1.0 / 1047.348644

#: Earth mass in solar masses.
M_EARTH_MSUN: float = 1.0 / 332_946.0487

#: Proper-motion to tangential-velocity factor: v_t [km/s] = 4.740470 * mu["/yr] / parallax["].
KMS_PER_AU_PER_YEAR: float = AU_KM / (JULIAN_YEAR_DAYS * DAY_S)

#: Microlensing constant kappa = 4 G / (c^2 au) in mas / Msun.
MICROLENS_KAPPA_MAS_PER_MSUN: float = 8.144
