# Tutorial 8 — The exomoon timing test

> **In one sentence:** Check whether a planet's transit times and transit lengths wobble together in the special "90 degrees apart" pattern that a moon would cause.

## For young readers

Walk around a big circle while holding hands with a friend who spins around you. When your friend is in front, they pull you ahead — you arrive early. When they are behind, you arrive late. When they swing to the side, you speed up or slow down. Early-or-late and fast-or-slow take turns, a quarter of a spin apart. A moon does this to its planet. We can look for this pattern in when a planet crosses its star, and how long the crossing takes.

## The big idea

- **TTV** (transit timing variation): the transit comes a bit early or late.
- **TDV** (transit duration variation): the transit lasts a bit longer or shorter.

For a moon, TTV follows the planet's *position* around the planet–moon balance point, while TDV follows its *speed*. Position and speed are a quarter-cycle (90°) apart (Kipping 2009). Many other causes make TTVs, but they do not usually make this exact 90° pattern.

## Step 1 — How big is the effect?

```python
from fdastro.exomoon import ttv_amplitude_seconds

# Our own Earth and Moon, seen transiting the Sun from far away.
print(f"Earth–Moon timing wobble: about {ttv_amplitude_seconds(384_400, 0.0123, 29.78):.0f} seconds")
```

About 2.6 minutes. Small, but measurable for bright stars with many transits.

## Step 2 — Make practice data with a moon

```python
import numpy as np
from fdastro.exomoon import ttv_tdv_phase_test

rng = np.random.default_rng(3)
n = np.arange(40, dtype=float)                       # 40 transits
phase = 2 * np.pi * 0.21 * n                         # the moon's (aliased) rhythm
ttv = 3.0 * np.sin(phase) + rng.normal(0, 0.6, n.size)              # minutes
tdv = 2.0 * np.sin(phase + np.pi / 2) + rng.normal(0, 0.4, n.size)  # minutes, 90° later

result = ttv_tdv_phase_test(n, ttv, 0.6, tdv, 0.4, n_permutations=200, n_bootstrap=200)
print(f"rhythm: every {result.period_epochs:.2f} transits")
print(f"phase offset: {result.phase_offset_deg:.0f}° ± {result.phase_offset_err_deg:.0f}°")
print(f"false-alarm probability: {result.false_alarm_probability:.3f}")
print(result.verdict)
```

## Step 3 — A look-alike that is NOT a moon

```python
tdv_in_phase = 2.0 * np.sin(phase) + rng.normal(0, 0.4, n.size)   # same rhythm, no 90° offset
print(ttv_tdv_phase_test(n, ttv, 0.6, tdv_in_phase, 0.4, n_permutations=200, n_bootstrap=200).verdict)
```

## Why the rhythm looks strange

A moon goes around its planet many times between two transits. We only "take a photo" once per transit, so the fast rhythm shows up as a slower, fake rhythm — like a car wheel in a movie that seems to spin slowly or backwards. This is called **aliasing**. The test searches rhythms between 0 and 0.5 cycles per transit for that reason.

## Real data

Published transit-time catalogs (for example the Kepler TTV catalog of Holczer et al. 2016) list mid-times and durations for thousands of planets. Read the TTV and TDV columns with their errors and pass them to `ttv_tdv_phase_test`.

## How we could be wrong

- Two planets near a resonance can also make TTVs **and** TDVs.
- Star spots can shift measured transit times.
- Changes in the impact parameter (orbit tilt) add a different TDV component.
- Detrending can distort durations.

Two famous exomoon candidates, Kepler-1625 b-i and Kepler-1708 b-i, are still debated. See [D12](../disclosures/d12-exomoons-timing-duration.md).

## For experts

- Joint periodogram: weighted sin + cos + constant fits at each trial frequency for both series; power = summed χ² reduction. Phase offset = φ_TDV − φ_TTV with parametric-bootstrap error.
- False-alarm probability: permutation test over (TTV, TDV) pairs, which includes the look-elsewhere effect over the frequency grid; resolution is limited to 1/(n_permutations + 1).
- Quadrature criterion: |offset| within max(2σ, 5°) of 90° and within 30°. This is a screening rule; a claim requires photodynamical modelling and model comparison.

## Next

[Tutorial 9 — Tilted orbits and hidden companions](t09-tilted-orbits-and-hidden-companions.md)
