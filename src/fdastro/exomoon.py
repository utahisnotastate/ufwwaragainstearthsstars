"""Look for the timing-and-duration pattern a moon would give its planet.

For young readers
-----------------
Imagine walking around a big circle while holding hands with a friend who
spins around you. Sometimes your friend pulls you ahead, so you arrive early.
Sometimes they pull you back, so you arrive late. You also speed up and slow
down. A moon does the same thing to a planet. We can look for this pattern
in the times when a planet passes in front of its star.

For experts
-----------
For a planet with a moon, transit timing variations (TTV) follow the
planet's barycentric *position* while velocity-induced transit duration
variations (TDV-V) follow its barycentric *velocity*, so the two signals
share a frequency and are offset by pi/2 (Kipping 2009a, MNRAS 392, 181;
2009b, MNRAS 396, 1797). Sampled once per transit, the moon's frequency is
aliased into (0, 0.5] cycles per epoch.

:func:`ttv_tdv_phase_test` fits sinusoids at a common trial frequency to both
series, picks the frequency with the largest joint chi-square reduction, and
reports the phase offset with a bootstrap error. A permutation test (shuffling
the (TTV, TDV) pairs across epochs) gives a false-alarm probability that
includes the look-elsewhere effect over the frequency grid.

A ~90 deg offset is *consistent with* a moon; it is not a confirmation.
Planet–planet perturbations, stellar activity and the TIP (impact-parameter)
TDV component can mimic or mask the signal. Model comparison with full
photodynamical fits is required before any claim.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray

FloatArray = NDArray[np.float64]

__all__ = ["ExomoonTestResult", "ttv_tdv_phase_test", "ttv_amplitude_seconds", "tdv_amplitude_seconds"]


def _fit_sinusoid(n: FloatArray, y: FloatArray, w: FloatArray, freq: float):
    phase = 2.0 * math.pi * freq * n
    design = np.stack([np.sin(phase), np.cos(phase), np.ones_like(n)], axis=1)
    sw = np.sqrt(w)
    coef, *_ = np.linalg.lstsq(design * sw[:, None], y * sw, rcond=None)
    model = design @ coef
    chi2 = float(np.sum(w * (y - model) ** 2))
    return coef, chi2


def _chi2_reduction(design: FloatArray, y: FloatArray, w: FloatArray) -> FloatArray:
    """Chi-square drop from a constant model to sin+cos+constant, for every frequency at once."""
    normal = np.einsum("fni,n,fnj->fij", design, w, design)
    rhs = np.einsum("fni,n,n->fi", design, w, y)
    coef = np.linalg.solve(normal, rhs[..., None])[..., 0]
    explained = np.einsum("fi,fi->f", coef, rhs)
    return explained - (np.sum(w * y) ** 2) / np.sum(w)


def _joint_power(n, ttv, w1, tdv, w2, freqs):
    phase = 2.0 * math.pi * freqs[:, None] * n[None, :]
    design = np.stack([np.sin(phase), np.cos(phase), np.ones_like(phase)], axis=2)
    return _chi2_reduction(design, ttv, w1) + _chi2_reduction(design, tdv, w2)


def _phase_deg(coef: FloatArray) -> float:
    # y = A sin(x) + B cos(x) = R sin(x + phi), phi = atan2(B, A)
    return math.degrees(math.atan2(coef[1], coef[0]))


def _wrap180(x: float) -> float:
    return (x + 180.0) % 360.0 - 180.0


@dataclass(frozen=True)
class ExomoonTestResult:
    frequency_cycles_per_epoch: float
    period_epochs: float
    ttv_amplitude: float
    tdv_amplitude: float
    phase_offset_deg: float          # TDV phase minus TTV phase, in (-180, 180]
    phase_offset_err_deg: float
    false_alarm_probability: float
    quadrature: bool                 # |offset| within 2 sigma (and 30 deg) of 90 deg
    verdict: str


def ttv_tdv_phase_test(
    epochs: ArrayLike,
    ttv: ArrayLike,
    ttv_err: ArrayLike,
    tdv: ArrayLike,
    tdv_err: ArrayLike,
    *,
    freqs: ArrayLike | None = None,
    n_permutations: int = 300,
    n_bootstrap: int = 300,
    rng: np.random.Generator | int | None = 0,
) -> ExomoonTestResult:
    """Test whether TTV and TDV share a periodic signal offset by ~90 degrees."""
    n = np.asarray(epochs, dtype=np.float64)
    y1 = np.asarray(ttv, dtype=np.float64)
    y2 = np.asarray(tdv, dtype=np.float64)
    w1 = 1.0 / np.asarray(ttv_err, dtype=np.float64) ** 2 * np.ones_like(n)
    w2 = 1.0 / np.asarray(tdv_err, dtype=np.float64) ** 2 * np.ones_like(n)
    if n.size < 8:
        raise ValueError("need at least 8 transits for a meaningful test")
    span = float(n.max() - n.min())
    if freqs is None:
        fmin = 1.0 / max(span, 1.0)
        freqs = np.linspace(fmin, 0.5, int(max(200, 8 * span)))
    freqs = np.asarray(freqs, dtype=np.float64)

    power = _joint_power(n, y1, w1, y2, w2, freqs)
    k = int(np.argmax(power))
    f_best = float(freqs[k])
    c1, _ = _fit_sinusoid(n, y1, w1, f_best)
    c2, _ = _fit_sinusoid(n, y2, w2, f_best)
    offset = _wrap180(_phase_deg(c2) - _phase_deg(c1))

    gen = np.random.default_rng(rng)
    s1 = 1.0 / np.sqrt(w1)
    s2 = 1.0 / np.sqrt(w2)
    m1 = c1[0] * np.sin(2 * math.pi * f_best * n) + c1[1] * np.cos(2 * math.pi * f_best * n) + c1[2]
    m2 = c2[0] * np.sin(2 * math.pi * f_best * n) + c2[1] * np.cos(2 * math.pi * f_best * n) + c2[2]
    boots = []
    for _ in range(n_bootstrap):
        b1, _ = _fit_sinusoid(n, m1 + gen.normal(0, s1), w1, f_best)
        b2, _ = _fit_sinusoid(n, m2 + gen.normal(0, s2), w2, f_best)
        boots.append(_wrap180(_phase_deg(b2) - _phase_deg(b1) - offset))
    offset_err = float(np.std(boots))

    exceed = 0
    for _ in range(n_permutations):
        perm = gen.permutation(n.size)
        p = _joint_power(n, y1[perm], w1[perm], y2[perm], w2[perm], freqs)
        if p.max() >= power[k]:
            exceed += 1
    fap = (exceed + 1) / (n_permutations + 1)

    dist90 = abs(abs(offset) - 90.0)
    quadrature = dist90 <= max(2.0 * offset_err, 5.0) and dist90 <= 30.0
    if fap < 0.01 and quadrature:
        verdict = "periodic TTV/TDV signal in quadrature: consistent with an exomoon (needs photodynamical modelling)"
    elif fap < 0.01:
        verdict = "periodic TTV/TDV signal NOT in quadrature: more like a perturbing planet or activity"
    else:
        verdict = "no significant shared periodic signal"
    return ExomoonTestResult(
        frequency_cycles_per_epoch=f_best, period_epochs=1.0 / f_best,
        ttv_amplitude=float(math.hypot(c1[0], c1[1])), tdv_amplitude=float(math.hypot(c2[0], c2[1])),
        phase_offset_deg=offset, phase_offset_err_deg=offset_err,
        false_alarm_probability=float(fap), quadrature=bool(quadrature), verdict=verdict,
    )


def ttv_amplitude_seconds(moon_semimajor_km: float, moon_to_planet_mass: float, planet_orbital_speed_kms: float) -> float:
    """Maximum moon-induced timing shift: a_bary / v_orb, with a_bary = a_s M_s / (M_p + M_s)."""
    a_bary = moon_semimajor_km * moon_to_planet_mass / (1.0 + moon_to_planet_mass)
    return a_bary / planet_orbital_speed_kms


def tdv_amplitude_seconds(transit_duration_s: float, moon_semimajor_km: float, moon_to_planet_mass: float,
                          moon_period_days: float, planet_orbital_speed_kms: float) -> float:
    """Maximum velocity-induced duration change: tau * v_bary / v_orb (circular, coplanar moon)."""
    a_bary = moon_semimajor_km * moon_to_planet_mass / (1.0 + moon_to_planet_mass)
    v_bary = 2.0 * math.pi * a_bary / (moon_period_days * 86400.0)
    return transit_duration_s * v_bary / planet_orbital_speed_kms
