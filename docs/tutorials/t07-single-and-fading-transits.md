# Tutorial 7 — Single and fading transits

> **In one sentence:** Search a star's brightness record for a single planet "shadow", and test whether a planet's shadows are getting shallower over the years.

## For young readers

When a planet passes in front of its star, the star dims a tiny bit. This is called a **transit**. Some planets are so far from their star that a telescope sees just one transit while it is watching. Other planets slowly tip their orbits, so each transit is a little smaller until it disappears — like a moth flying past a lighthouse, a little higher each night until its shadow misses you.

## Part A — Find a single transit

### Step 1 — Make a practice light curve

A **light curve** is a list of brightness measurements over time. We make 27 days of fake data (like one TESS sector), add slow star variations and noise, and hide one 6-hour transit.

```python
import numpy as np
from fdastro.transits import inject_box_transit, detrend_running_median, single_event_search

rng = np.random.default_rng(42)
t = np.arange(0.0, 27.0, 2.0 / 1440.0)                   # every 2 minutes
flux = 1.0 + 0.001 * np.sin(2 * np.pi * t / 8.0) + rng.normal(0, 400e-6, t.size)
flux = inject_box_transit(t, flux, t_mid=13.37, duration_days=0.25, depth=1500e-6)
```

### Step 2 — Remove the slow wiggles and search

```python
clean = detrend_running_median(t, flux, window_days=1.5)  # window > 3x the longest transit
events = single_event_search(t, clean, snr_threshold=7.0)
for e in events:
    print(f"dip at day {e.t_mid:.2f}: depth {e.depth * 1e6:.0f} ppm, {e.duration_days * 24:.0f} h, SNR {e.snr:.0f}")
```

### Step 3 — How long is the orbit, at least?

One transit does not give the period directly. But the transit's length and the star's size and mass give a **minimum** period.

```python
from fdastro.transits import min_period_from_duration, transit_duration_hours

print(f"Earth seen from afar: transit lasts {transit_duration_hours(365.25):.1f} h")
print(f"A 6-hour transit of a Sun-like star means P ≥ {min_period_from_duration(6.0):.0f} days")
```

## Part B — Is a transit fading?

TOI-2535 b's transits grew shallower and shorter, then stopped in March 2026 (Yee et al. 2026). The likely cause: a hidden neighbor planet is tilting its orbit. Here is how to test for a trend in measured transit depths.

```python
from fdastro.transits import depth_trend_test

years = np.array([2019.3, 2020.4, 2021.5, 2022.4, 2023.5, 2024.4, 2025.5])
depths_ppm = np.array([5200, 4900, 4300, 3600, 2700, 1500, 600])   # illustrative numbers
errors_ppm = np.full(depths_ppm.size, 150)
result = depth_trend_test(years, depths_ppm, errors_ppm)
print(f"slope = {result['slope']:.0f} ± {result['slope_err']:.0f} ppm per year, z = {result['z']:.1f}")
print("fading!" if result["fading"] else "no clear trend")
```

## Real data

```py
# Requires: pip install "fdastro[archives]" and internet access.
from fdastro.transits import load_tess_lightcurve, detrend_running_median, single_event_search
t, f, ferr = load_tess_lightcurve("TOI-2535")
events = single_event_search(t, detrend_running_median(t, f, 1.5))
```

## Things that can fool you

- **Spacecraft events:** TESS fires thrusters ("momentum dumps") and sees scattered light. These can make fake dips. Check the quality flags.
- **Eclipsing binary stars** make deep or V-shaped dips, sometimes with a second, shallower dip.
- **Nearby stars** can blend into the same pixels. The dip might belong to a neighbor.
- **Red noise:** our SNR assumes white noise, so it is optimistic. Inspect every candidate by eye.

Community projects such as **Planet Hunters TESS** look for exactly these single events, and their volunteers have found real planets. See [D03](../disclosures/d03-single-transit-planets.md).

## For experts

- Box matched filter with cumulative sums: O(N) per trial duration; noise from 1.4826 × MAD.
- `min_period_from_duration`: P = π G M T³ / (4 R³ (1 − b²)^{3/2}); b = 0 gives the lower bound for circular orbits. Eccentric orbits can violate it (transit near periastron is shorter).
- For grazing, precessing systems, model the impact parameter `b(t)` directly (depth and duration are both functions of b), rather than fitting a linear depth trend.

## Next

[Tutorial 8 — The exomoon timing test](t08-exomoon-timing-test.md)
