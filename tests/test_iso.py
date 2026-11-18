import numpy as np
import pytest

from fdastro.catalogs import INTERSTELLAR_OBJECTS
from fdastro.iso import (
    bound_orbit_test,
    fit_orbit,
    make_observations,
    range_scan,
    screen_object,
    screen_tracklet_pairs,
    simulate_observations,
)
from fdastro.kepler import ecliptic_to_equatorial, elements_to_state


def _eq_state(q, e, i, node, peri, nu):
    s = elements_to_state(q, e, i, node, peri, nu)
    return np.concatenate([ecliptic_to_equatorial(s[:3]), ecliptic_to_equatorial(s[3:])])


def _nights(epoch, offsets, per_night=3):
    return np.concatenate([epoch + o + np.arange(per_night) * 0.02 for o in offsets])


EPOCH = 60850.0


@pytest.fixture(scope="module")
def hyperbolic_case():
    o = INTERSTELLAR_OBJECTS[2]
    state = _eq_state(o["q_au"], o["e"], o["i_deg"], o["node_deg"], o["peri_deg"], -80.0)
    mjd = _nights(EPOCH, [0.0, 2.0, 5.0, 9.0, 14.0, 20.0])
    obs = simulate_observations(state, EPOCH, mjd, sigma_arcsec=0.3, rng=7)
    scan = range_scan(obs)
    fit = fit_orbit(obs, scan=scan)
    test = bound_orbit_test(obs, fit, scan=scan)
    return o, state, obs, fit, test


def test_hyperbolic_orbit_recovered(hyperbolic_case):
    o, _state, _obs, fit, _test = hyperbolic_case
    assert fit.success
    assert fit.reduced_chi2 < 2.0
    assert fit.rms_arcsec < 0.6
    assert fit.elements.e > 2.0
    assert fit.elements.i_deg == pytest.approx(o["i_deg"], abs=3.0)


def test_bound_orbit_rejected_for_interstellar(hyperbolic_case):
    *_, test = hyperbolic_case
    assert test.sigma >= 5.0
    assert "hyperbolic candidate" in test.verdict
    assert test.delta_chi2 > 25


def test_main_belt_asteroid_is_consistent_with_bound():
    state = _eq_state(2.7 * 0.85, 0.15, 10.0, 80.0, 30.0, 20.0)
    mjd = _nights(EPOCH, [0.0, 3.0, 7.0, 12.0])
    obs = simulate_observations(state, EPOCH, mjd, sigma_arcsec=0.3, rng=3)
    scan = range_scan(obs)
    fit = fit_orbit(obs, scan=scan)
    test = bound_orbit_test(obs, fit, scan=scan)
    assert fit.reduced_chi2 < 2.0
    assert test.sigma < 3.0
    assert test.verdict == "consistent with a bound orbit"


def test_screen_object_summary_is_honest(hyperbolic_case):
    _o, _state, obs, _fit, _test = hyperbolic_case
    summary = screen_object(obs, name="synthetic")
    assert "CONFIRMED" not in summary["verdict"].upper()
    assert summary["radiant_ra_dec_deg"] is not None
    assert summary["v_infinity_kms"] is not None and summary["v_infinity_kms"] > 20


def test_short_arc_warning():
    o = INTERSTELLAR_OBJECTS[1]
    state = _eq_state(o["q_au"], o["e"], o["i_deg"], o["node_deg"], o["peri_deg"], -70.0)
    mjd = EPOCH + np.array([0.0, 0.02, 0.04, 1.0, 1.02, 1.04])
    obs = simulate_observations(state, EPOCH, mjd, sigma_arcsec=0.3, rng=11)
    summary = screen_object(obs)
    assert "warning" in summary


def test_tracklet_pairing_finds_hyperbolic_join():
    o = INTERSTELLAR_OBJECTS[2]
    state = _eq_state(o["q_au"], o["e"], o["i_deg"], o["node_deg"], o["peri_deg"], -80.0)
    t1 = simulate_observations(state, EPOCH, EPOCH + np.array([0.0, 0.02, 0.04, 1.0, 1.02]),
                               sigma_arcsec=0.2, rng=1)
    t2 = simulate_observations(state, EPOCH, EPOCH + np.array([9.0, 9.02, 9.04, 10.0, 10.02]),
                               sigma_arcsec=0.2, rng=2)
    decoy_state = _eq_state(2.4, 0.1, 5.0, 100.0, 10.0, 0.0)
    t3 = simulate_observations(decoy_state, EPOCH, EPOCH + np.array([5.0, 5.02, 5.04]),
                               sigma_arcsec=0.2, rng=3)
    hits = screen_tracklet_pairs({"A": t1, "B": t2, "C": t3}, max_rate_deg_per_day=20.0)
    assert hits and hits[0]["name"] == "A+B"


def test_make_observations_validates_input():
    with pytest.raises(ValueError):
        make_observations([1.0, 2.0], [10.0], [5.0, 6.0])
    with pytest.raises(ValueError):
        make_observations([1.0], [10.0], [5.0], sigma_arcsec=0.0)
