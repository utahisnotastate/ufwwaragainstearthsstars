import gzip
import math

import numpy as np
import pytest

from fdastro.constants import AU_KM, EARTH_RADIUS_KM
from fdastro.ephemeris import (
    earth_heliocentric,
    earth_heliocentric_velocity,
    gmst_deg,
    observer_geocentric_offset,
    parse_obscodes,
)
from fdastro.kepler import equatorial_to_ecliptic
from fdastro.mpc import group_by_designation, load_mpc80, parse_mpc80, parse_mpc80_line


def test_earth_distance_range_over_a_year():
    r = np.linalg.norm(earth_heliocentric(np.arange(60000, 60366)), axis=1)
    assert 0.982 < r.min() < 0.985
    assert 1.015 < r.max() < 1.018


def test_earth_longitude_at_j2000():
    # At 2000-01-01 12:00 the Sun's geocentric ecliptic longitude is ~280.4 deg,
    # so the Earth's heliocentric longitude is ~100.4 deg.
    ecl = equatorial_to_ecliptic(earth_heliocentric(51544.5)[0])
    lon = math.degrees(math.atan2(ecl[1], ecl[0])) % 360
    assert lon == pytest.approx(100.4, abs=0.05)
    assert abs(ecl[2]) < 1e-6


def test_earth_speed_about_30_kms():
    v = np.linalg.norm(earth_heliocentric_velocity(np.array([60000.0, 60180.0])), axis=1)
    assert np.all(np.abs(v * AU_KM / 86400 - 29.8) < 0.6)


def test_gmst_at_j2000():
    assert gmst_deg(51544.5)[0] == pytest.approx(280.46061837, abs=1e-6)


def test_observer_offset_magnitude():
    off = observer_geocentric_offset(np.array([60000.1]), 203.744, 0.936241, 0.351543)
    rho = np.linalg.norm(off[0]) * AU_KM / EARTH_RADIUS_KM
    assert rho == pytest.approx(math.hypot(0.936241, 0.351543), rel=1e-12)


def test_parse_obscodes_skips_space_based():
    text = (
        "Code  Long.   cos      sin    Name\n"
        "000   0.0000 0.62411 +0.77873 Greenwich\n"
        "500                           Geocentric\n"
        "F51 203.74409 0.936241 +0.351543 Pan-STARRS 1, Haleakala\n"
    )
    codes = parse_obscodes(text)
    assert set(codes) == {"000", "F51"}
    assert codes["F51"][0] == pytest.approx(203.74409)
    assert codes["F51"][3].startswith("Pan-STARRS")


def _line(desig="     K25N01A", note2="C", date="2025 07 01.12345 ", ra="18 06 12.345",
          dec="-18 34 56.78", mag="18.1 r", code="W68"):
    line = f"{desig[:12]:<12}  {note2}{date:<17}{ra:<12}{dec:<12}         {mag:<6}      {code:>3}"
    assert len(line) == 80, len(line)
    return line


def test_parse_single_line():
    o = parse_mpc80_line(_line())
    assert o is not None
    assert o.designation == "K25N01A"
    assert o.obscode == "W68"
    assert o.mjd_utc == pytest.approx(60857.12345, abs=1e-9)
    assert o.ra_deg == pytest.approx((18 + 6 / 60 + 12.345 / 3600) * 15)
    assert o.dec_deg == pytest.approx(-(18 + 34 / 60 + 56.78 / 3600))
    assert o.mag == pytest.approx(18.1)
    assert o.band == "r"


def test_negative_zero_declination():
    o = parse_mpc80_line(_line(dec="-00 30 00.00"))
    assert o.dec_deg == pytest.approx(-0.5)


def test_second_lines_skipped_and_grouping(tmp_path):
    lines = [
        _line(desig="     AAA0001", date="2025 07 01.10000 "),
        _line(desig="     AAA0001", date="2025 07 01.12000 "),
        _line(desig="     AAA0001", note2="s", date="2025 07 01.12000 "),
        _line(desig="     BBB0002", date="2025 07 02.10000 "),
        "garbage line",
    ]
    obs = parse_mpc80(lines)
    assert len(obs) == 3
    groups = group_by_designation(obs, min_obs=2)
    assert list(groups) == ["AAA0001"]
    path = tmp_path / "itf_sample.txt.gz"
    with gzip.open(path, "wt", encoding="ascii") as fh:
        fh.write("\n".join(lines[:2]) + "\n")
    assert len(load_mpc80(path)) == 2
