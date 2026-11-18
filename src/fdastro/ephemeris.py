"""Where is the Earth? A small, dependency-free ephemeris and observer positions.

For young readers
-----------------
To know where something is in space, we first need to know where *we* are.
The Earth moves around the Sun, so this file works out the Earth's position on
any date.

For experts
-----------
:func:`earth_heliocentric` uses the low-precision solar coordinates of the
*Astronomical Almanac* (section C, accurate to about 0.01 deg in longitude for
1950-2050), rotated from the mean equinox of date to J2000 by subtracting
general precession in longitude. Expected position error is ~1e-4 au. That is
enough for teaching, simulations and first-pass screening.

For real astrometric work, pass your own observer positions computed with a
JPL DE ephemeris (for example ``astropy`` with ``solar_system_ephemeris`` set
to ``"de440"``, or JPL Horizons) — see :func:`earth_heliocentric_astropy`.

Times are MJD. The low-precision model does not distinguish TT/TDB from UTC
(the ~69 s offset moves the Earth ~2,000 km, well below this model's error).
"""

from __future__ import annotations

import math

import numpy as np
from numpy.typing import ArrayLike, NDArray

from .constants import AU_KM, EARTH_RADIUS_KM, MJD_J2000, OBLIQUITY_J2000_DEG

FloatArray = NDArray[np.float64]

__all__ = [
    "earth_heliocentric",
    "earth_heliocentric_velocity",
    "earth_heliocentric_astropy",
    "gmst_deg",
    "observer_geocentric_offset",
    "parse_obscodes",
]

_PRECESSION_DEG_PER_CENTURY = 5028.796195 / 3600.0  # general precession in longitude


def earth_heliocentric(mjd: ArrayLike) -> FloatArray:
    """Heliocentric position of the Earth, J2000 equatorial frame, au. Shape (N, 3)."""
    t = np.atleast_1d(np.asarray(mjd, dtype=np.float64))
    n = t - MJD_J2000
    big_l = np.deg2rad((280.460 + 0.9856474 * n) % 360.0)
    g = np.deg2rad((357.528 + 0.9856003 * n) % 360.0)
    lam_date = big_l + np.deg2rad(1.915) * np.sin(g) + np.deg2rad(0.020) * np.sin(2.0 * g)
    lam_j2000 = lam_date - np.deg2rad(_PRECESSION_DEG_PER_CENTURY) * (n / 36525.0)
    radius = 1.00014 - 0.01671 * np.cos(g) - 0.00014 * np.cos(2.0 * g)
    eps = math.radians(OBLIQUITY_J2000_DEG)
    # Geocentric Sun, then flip the sign to get the heliocentric Earth.
    x = radius * np.cos(lam_j2000)
    y = radius * np.sin(lam_j2000) * math.cos(eps)
    z = radius * np.sin(lam_j2000) * math.sin(eps)
    return -np.stack([x, y, z], axis=1)


def earth_heliocentric_velocity(mjd: ArrayLike, step_days: float = 0.05) -> FloatArray:
    """Heliocentric velocity of the Earth (au/day) by central differences."""
    t = np.atleast_1d(np.asarray(mjd, dtype=np.float64))
    return (earth_heliocentric(t + step_days) - earth_heliocentric(t - step_days)) / (2.0 * step_days)


def earth_heliocentric_astropy(mjd_tdb: ArrayLike, ephemeris: str = "builtin") -> FloatArray:
    """Heliocentric Earth position (au, ICRF axes) from :mod:`astropy`.

    Requires the optional ``archives`` extra. Use ``ephemeris="de440"`` for
    full JPL accuracy (downloads the kernel on first use).
    """
    try:
        import astropy.units as u
        from astropy.coordinates import get_body_barycentric, solar_system_ephemeris
        from astropy.time import Time
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise ImportError("install the optional extra: pip install 'fdastro[archives]'") from exc

    t = Time(np.atleast_1d(np.asarray(mjd_tdb, dtype=np.float64)), format="mjd", scale="tdb")
    with solar_system_ephemeris.set(ephemeris):
        earth = get_body_barycentric("earth", t)
        sun = get_body_barycentric("sun", t)
    d = earth - sun
    return np.stack([d.x.to_value(u.au), d.y.to_value(u.au), d.z.to_value(u.au)], axis=1)


def gmst_deg(mjd_ut1: ArrayLike) -> FloatArray:
    """Greenwich mean sidereal time in degrees (IAU 1982 expression)."""
    t = np.atleast_1d(np.asarray(mjd_ut1, dtype=np.float64))
    d = t - MJD_J2000
    tc = d / 36525.0
    gmst = 280.46061837 + 360.98564736629 * d + 0.000387933 * tc**2 - tc**3 / 38_710_000.0
    return np.mod(gmst, 360.0)


def observer_geocentric_offset(
    mjd_utc: ArrayLike, lon_deg: float, rho_cos_phi: float, rho_sin_phi: float
) -> FloatArray:
    """Geocentric position of a ground observatory in au (equatorial, of-date axes).

    ``lon_deg``, ``rho_cos_phi`` and ``rho_sin_phi`` are the parallax constants
    published for each observatory code by the Minor Planet Center
    (ObsCodes list). Precession of the station vector is neglected (tens of
    km over decades), which is far below typical astrometric errors.
    """
    theta = np.deg2rad(gmst_deg(mjd_utc) + lon_deg)
    scale = EARTH_RADIUS_KM / AU_KM
    return scale * np.stack(
        [rho_cos_phi * np.cos(theta), rho_cos_phi * np.sin(theta),
         np.full_like(theta, rho_sin_phi)], axis=1)


def parse_obscodes(text: str) -> dict[str, tuple[float, float, float, str]]:
    """Parse the MPC observatory code list into ``{code: (lon, rho_cos, rho_sin, name)}``.

    Lines without parallax constants (space-based or roving observers) are
    skipped because they need per-observation positions instead.
    """
    out: dict[str, tuple[float, float, float, str]] = {}
    for line in text.splitlines():
        if len(line) < 4 or line.startswith("Code"):
            continue
        code = line[:3]
        parts = line[3:].split()
        if len(parts) < 3:
            continue
        try:
            lon, rc, rs = float(parts[0]), float(parts[1]), float(parts[2])
        except ValueError:
            continue
        out[code] = (lon, rc, rs, " ".join(parts[3:]))
    return out
