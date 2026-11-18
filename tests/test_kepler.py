import math

import numpy as np
import pytest

from fdastro.catalogs import INTERSTELLAR_OBJECTS
from fdastro.constants import GM_SUN
from fdastro.kepler import (
    ecliptic_to_equatorial,
    elements_to_state,
    equatorial_to_ecliptic,
    incoming_radiant,
    propagate,
    propagate_universal,
    specific_energy,
    state_to_elements,
    unit_vector_to_radec,
    v_infinity_from_q_e_kms,
)


@pytest.mark.parametrize(
    "q,e,inc,node,peri,nu",
    [
        (1.0, 0.0167, 0.001, 0.0, 102.9, 30.0),  # Earth-like ellipse
        (2.3, 0.15, 10.0, 80.0, 70.0, -120.0),  # main belt
        (0.6, 0.999, 50.0, 10.0, 20.0, 5.0),  # near-parabolic comet
        (0.2559, 1.2011, 122.74, 24.6, 241.8, -60.0),  # 1I-like hyperbola
        (1.352, 6.123, 175.24, 323.0, 128.8, -80.0),  # 3I-like hyperbola
    ],
)
def test_elements_round_trip(q, e, inc, node, peri, nu):
    s = elements_to_state(q, e, inc, node, peri, nu)
    el = state_to_elements(s[:3], s[3:])
    assert el.q == pytest.approx(q, rel=1e-10)
    assert el.e == pytest.approx(e, rel=1e-10)
    assert el.i_deg == pytest.approx(inc, abs=1e-8)
    if inc > 1e-2:
        assert el.node_deg == pytest.approx(node % 360, abs=1e-7)
        assert el.peri_deg == pytest.approx(peri % 360, abs=1e-6)
    assert el.true_anomaly_deg == pytest.approx(nu, abs=1e-6)


@pytest.mark.parametrize("e", [0.3, 0.9, 1.0 + 1e-9, 1.5, 6.1])
def test_universal_matches_numerical_integration(e):
    s = elements_to_state(1.2, e, 30.0, 40.0, 50.0, -40.0)
    dt = np.array([-120.0, -30.0, -1.0, 0.0, 0.5, 10.0, 200.0])
    r_u, v_u = propagate_universal(s[:3], s[3:], dt)
    # a1 = 1e-30 forces the numerical (DOP853) branch with negligible extra force.
    r_n, v_n = propagate(s, dt, a1=1e-30)
    assert np.max(np.abs(r_u - r_n)) < 1e-8
    assert np.max(np.abs(v_u - v_n)) < 1e-10


def test_energy_and_angular_momentum_conserved():
    s = elements_to_state(0.9, 3.0, 20.0, 0.0, 0.0, -90.0)
    r, v = propagate_universal(s[:3], s[3:], np.linspace(-300, 300, 25))
    e0 = specific_energy(s[:3], s[3:])
    h0 = np.cross(s[:3], s[3:])
    for ri, vi in zip(r, v):
        assert specific_energy(ri, vi) == pytest.approx(e0, rel=1e-10)
        assert np.allclose(np.cross(ri, vi), h0, rtol=1e-10, atol=1e-14)


def test_full_period_returns_to_start():
    a = 2.0
    s = elements_to_state(a * (1 - 0.3), 0.3, 5.0, 0.0, 0.0, 10.0)
    period = 2 * math.pi * math.sqrt(a**3 / GM_SUN)
    r, v = propagate_universal(s[:3], s[3:], period)
    assert np.allclose(r[0], s[:3], atol=1e-9)


@pytest.mark.parametrize(
    "obj,expected",
    [(INTERSTELLAR_OBJECTS[0], 26.3), (INTERSTELLAR_OBJECTS[1], 32.3), (INTERSTELLAR_OBJECTS[2], 58.0)],
)
def test_interstellar_v_infinity(obj, expected):
    assert v_infinity_from_q_e_kms(obj["q_au"], obj["e"]) == pytest.approx(expected, abs=0.6)


def test_v_infinity_requires_hyperbola():
    with pytest.raises(ValueError):
        v_infinity_from_q_e_kms(1.0, 0.5)


def test_oumuamua_radiant_near_vega():
    o = INTERSTELLAR_OBJECTS[0]
    s_ecl = elements_to_state(o["q_au"], o["e"], o["i_deg"], o["node_deg"], o["peri_deg"], 0.0)
    rad_ecl = incoming_radiant(s_ecl[:3], s_ecl[3:])
    ra, dec = unit_vector_to_radec(ecliptic_to_equatorial(rad_ecl))
    # Published radiant: RA ~ 279.8 deg, Dec ~ +34.0 deg (near Vega).
    assert ra == pytest.approx(279.8, abs=1.0)
    assert dec == pytest.approx(34.0, abs=1.0)


def test_frame_rotation_inverse():
    v = np.array([0.3, -1.2, 0.7])
    assert np.allclose(ecliptic_to_equatorial(equatorial_to_ecliptic(v)), v)


def test_radiant_rejects_bound_orbit():
    s = elements_to_state(1.0, 0.5, 10, 0, 0, 0)
    with pytest.raises(ValueError):
        incoming_radiant(s[:3], s[3:])
