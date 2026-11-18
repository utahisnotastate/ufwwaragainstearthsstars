import math

import numpy as np
import pytest

from fdastro.astrometry import (
    fit_five_parameter,
    gnomonic,
    inverse_gnomonic,
    parallax_factors,
    simulate_five_parameter,
    tangential_velocity_kms,
)
from fdastro.catalogs import HIGH_INCLINATION_EXAMPLES
from fdastro.constants import A_JUPITER_AU, M_EARTH_MSUN
from fdastro.exomoon import tdv_amplitude_seconds, ttv_amplitude_seconds, ttv_tdv_phase_test
from fdastro.microlensing import (
    achromaticity_test,
    einstein_radius_mas,
    einstein_time_days,
    lens_mass_msun,
    paczynski_magnification,
)
from fdastro.obliquity import (
    companion_nodal_rate,
    j2_from_rotation,
    laplace_coefficient,
    resonant_companion_mass_mjup,
    stellar_quadrupole_nodal_rate,
)
from fdastro.stats import (
    fit_gumbel_moments,
    gumbel_return_period,
    p_to_sigma,
    sigma_to_p,
    trials_corrected_p,
)
from fdastro.tisserand import capture_candidate_screen, jupiter_class, tisserand_parameter
from fdastro.transits import (
    depth_trend_test,
    detrend_running_median,
    inject_box_transit,
    min_period_from_duration,
    single_event_search,
    transit_duration_hours,
)

# ----------------------------------------------------------------- Tisserand


def test_tisserand_of_jupiter_itself_is_three():
    assert tisserand_parameter(A_JUPITER_AU, 0.0, 0.0) == pytest.approx(3.0)


def test_tisserand_2015_bz509():
    bz = HIGH_INCLINATION_EXAMPLES[0]
    assert tisserand_parameter(bz["a"], bz["e"], bz["i"]) == pytest.approx(-0.75, abs=0.01)


def test_tisserand_rejects_unbound():
    with pytest.raises(ValueError):
        tisserand_parameter(-1.0, 1.5, 10.0)


def test_capture_screen_flags_only_odd_orbits():
    hits = capture_candidate_screen(HIGH_INCLINATION_EXAMPLES)
    names = [h.name for h in hits]
    assert any("2015 BZ509" in n for n in names)
    assert all("main-belt" not in n for n in names)
    assert hits == sorted(hits, key=lambda h: h.tj)
    assert jupiter_class(3.5).startswith("asteroid")
    assert jupiter_class(-0.7).startswith("retrograde")

# ----------------------------------------------------------------- astrometry


def test_parallax_ellipse_is_circle_at_ecliptic_pole():
    f_a, f_d = parallax_factors(np.arange(60000, 60365, 5.0), 270.0, 66.560708)
    amp = np.hypot(f_a, f_d)
    assert np.all(np.abs(amp - amp.mean()) < 0.02)
    assert amp.mean() == pytest.approx(1.0, abs=0.02)


def test_gnomonic_round_trip():
    ra, dec = np.array([10.0, 10.01, 9.99]), np.array([-30.0, -30.02, -29.97])
    xi, eta = gnomonic(ra, dec, 10.0, -30.0)
    ra2, dec2 = inverse_gnomonic(xi, eta, 10.0, -30.0)
    assert np.allclose(ra2, ra, atol=1e-12)
    assert np.allclose(dec2, dec, atol=1e-12)


def test_five_parameter_recovery_of_nearby_brown_dwarf():
    # WISE/NEOWISE scan at ~90 deg solar elongation, which maximizes the parallax
    # factor. For RA 133.8 deg that happens around early May and early November.
    mjd = np.sort(np.concatenate([np.arange(56791, 60300, 182.6), np.arange(56793, 60300, 182.6)]))
    ra, dec = simulate_five_parameter(mjd, 133.8, -7.2, pmra_arcsec_yr=-8.1, pmdec_arcsec_yr=0.7,
                                      parallax_arcsec=0.439, sigma_arcsec=0.05, rng=5)
    fit = fit_five_parameter(mjd, ra, dec, 0.05)
    assert fit.parallax_arcsec == pytest.approx(0.439, abs=0.01)
    assert fit.pmra_arcsec_yr == pytest.approx(-8.1, abs=0.01)
    assert fit.pmdec_arcsec_yr == pytest.approx(0.7, abs=0.01)
    assert fit.distance_pc == pytest.approx(1 / 0.439, rel=0.03)
    assert fit.chi2 / fit.dof < 2.0


def test_tangential_velocity():
    assert tangential_velocity_kms(1.0, 1.0) == pytest.approx(4.7405, abs=1e-3)

# ----------------------------------------------------------------- transits


def test_single_transit_found_in_noise():
    rng = np.random.default_rng(42)
    t = np.arange(0.0, 27.0, 2.0 / 1440.0)
    flux = 1.0 + 0.001 * np.sin(2 * np.pi * t / 8.0) + rng.normal(0, 400e-6, t.size)
    flux = inject_box_transit(t, flux, 13.37, 6.0 / 24.0, 1500e-6)
    clean = detrend_running_median(t, flux, window_days=1.5)
    events = single_event_search(t, clean)
    assert len(events) >= 1
    best = max(events, key=lambda e: e.snr)
    assert best.t_mid == pytest.approx(13.37, abs=0.1)
    assert best.depth == pytest.approx(1500e-6, rel=0.3)


def test_no_false_alarm_in_pure_noise():
    rng = np.random.default_rng(1)
    t = np.arange(0.0, 27.0, 2.0 / 1440.0)
    flux = 1.0 + rng.normal(0, 400e-6, t.size)
    assert single_event_search(t, flux, snr_threshold=7.0) == []


def test_depth_trend_detects_fading():
    epochs = np.arange(10, dtype=float)
    depths = 0.010 - 0.0008 * epochs
    res = depth_trend_test(epochs, depths + np.random.default_rng(0).normal(0, 1e-4, 10), np.full(10, 1e-4))
    assert res["fading"] and res["z"] < -10
    flat = depth_trend_test(epochs, np.full(10, 0.01), np.full(10, 1e-4))
    assert not flat["fading"]


def test_earth_transit_duration_and_period_bound():
    dur = transit_duration_hours(365.25, 1.0, 1.0)
    assert dur == pytest.approx(13.0, abs=0.2)
    assert min_period_from_duration(dur, 1.0, 1.0) == pytest.approx(365.25, rel=0.01)

# ----------------------------------------------------------------- exomoon


def test_earth_moon_ttv_amplitude():
    ttv = ttv_amplitude_seconds(384_400.0, 0.0123, 29.78)
    assert ttv == pytest.approx(157.0, abs=2.0)
    assert tdv_amplitude_seconds(13 * 3600, 384_400.0, 0.0123, 27.32, 29.78) > 0


def _moon_series(offset_deg, seed):
    rng = np.random.default_rng(seed)
    n = np.arange(40, dtype=float)
    ph = 2 * np.pi * 0.21 * n
    ttv = 3.0 * np.sin(ph) + rng.normal(0, 0.6, n.size)
    tdv = 2.0 * np.sin(ph + np.radians(offset_deg)) + rng.normal(0, 0.4, n.size)
    return n, ttv, tdv


def test_exomoon_quadrature_detected():
    n, ttv, tdv = _moon_series(90.0, 3)
    res = ttv_tdv_phase_test(n, ttv, 0.6, tdv, 0.4, n_permutations=200, n_bootstrap=200)
    assert res.false_alarm_probability < 0.01
    assert res.frequency_cycles_per_epoch == pytest.approx(0.21, abs=0.01)
    assert abs(abs(res.phase_offset_deg) - 90.0) < 15.0
    assert res.quadrature and "exomoon" in res.verdict


def test_in_phase_signal_is_not_called_a_moon():
    n, ttv, tdv = _moon_series(0.0, 4)
    res = ttv_tdv_phase_test(n, ttv, 0.6, tdv, 0.4, n_permutations=200, n_bootstrap=200)
    assert res.false_alarm_probability < 0.01
    assert not res.quadrature


def test_noise_only_is_not_significant():
    rng = np.random.default_rng(9)
    n = np.arange(40, dtype=float)
    res = ttv_tdv_phase_test(n, rng.normal(0, 1, 40), 1.0, rng.normal(0, 1, 40), 1.0,
                             n_permutations=200, n_bootstrap=100)
    assert res.false_alarm_probability > 0.01

# ----------------------------------------------------------------- obliquity


def test_laplace_coefficient_small_alpha():
    a = 0.01
    assert laplace_coefficient(1.5, 1, a) == pytest.approx(3 * a * (1 + 15 / 8 * a * a), rel=1e-6)


def test_solar_j2_order_of_magnitude():
    assert 1e-7 < j2_from_rotation(25.4, 1.0, 1.0, k2=0.03) < 4e-7


def test_resonant_mass_satisfies_condition():
    kw = dict(j2=1e-5, rstar_rsun=1.0, a1_au=0.05, psi_deg=60.0)
    m = resonant_companion_mass_mjup([1.0, 3.0], **kw)
    assert np.all(m > 0) and m[1] > m[0]
    g_star = stellar_quadrupole_nodal_rate(1e-5, 1.0, 0.05, 60.0)
    from fdastro.constants import M_JUPITER_MSUN
    g_comp = companion_nodal_rate(m[0] * M_JUPITER_MSUN, 0.05, 1.0)
    assert g_comp == pytest.approx(g_star, rel=1e-9)

# ----------------------------------------------------------------- microlensing


def test_paczynski_at_u_equals_one():
    assert paczynski_magnification(0.0, 0.0, 1.0, 1.0) == pytest.approx(3 / math.sqrt(5))


def test_einstein_scales():
    assert einstein_radius_mas(1.0, 4.0, 8.0) == pytest.approx(1.009, abs=0.005)
    te_earth = einstein_time_days(M_EARTH_MSUN, 4.0, 8.0, 5.0)
    assert 0.05 < te_earth < 0.3  # a few hours
    assert lens_mass_msun(te_earth, 4.0, 8.0, 5.0) == pytest.approx(M_EARTH_MSUN, rel=1e-9)


def test_achromaticity():
    mags = 18 - 2.5 * np.log10(paczynski_magnification(np.linspace(-1, 1, 30), 0, 0.3, 0.2))
    err = np.full(30, 0.01)
    assert achromaticity_test(mags, err, mags - 0.8, err)["achromatic"]
    assert not achromaticity_test(mags, err, mags * 0.9, err)["achromatic"]

# ----------------------------------------------------------------- stats


def test_sigma_p_round_trip():
    assert p_to_sigma(sigma_to_p(5.0)) == pytest.approx(5.0)
    assert sigma_to_p(1.96, two_sided=True) == pytest.approx(0.05, abs=1e-3)


def test_trials_correction():
    assert trials_corrected_p(1e-6, 1e6) == pytest.approx(1 - math.exp(-1), rel=1e-5)
    assert trials_corrected_p(0.0, 10) == 0.0


def test_gumbel_return_period():
    mu, beta = fit_gumbel_moments(np.random.default_rng(0).gumbel(10.0, 2.0, 5000))
    assert mu == pytest.approx(10.0, abs=0.15) and beta == pytest.approx(2.0, abs=0.1)
    assert gumbel_return_period(mu, mu, beta) == pytest.approx(1 / (1 - math.exp(-1)))
