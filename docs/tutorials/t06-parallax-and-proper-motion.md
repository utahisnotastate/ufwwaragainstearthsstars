# Tutorial 6 — Parallax and proper motion

> **In one sentence:** Measure how far away a nearby cold object is by watching it wiggle back and forth as the Earth goes around the Sun.

## For young readers

Hold your thumb out at arm's length. Close your left eye, then your right eye. Your thumb jumps against the background! That jump is called **parallax**. Now bring your thumb closer to your face and try again. It jumps more. Close things jump more than far things. Astronomers use the Earth's trip around the Sun the same way, to measure how far away nearby stars and cold "failed stars" are.

## The big idea

A nearby object's sky position changes for two reasons:

1. **Proper motion** — it really moves through space, so it drifts in a straight line.
2. **Parallax** — the Earth moves around the Sun, so the object seems to trace a small yearly loop.

The size of the loop is the **parallax angle** ϖ (in arcseconds). Distance in parsecs is 1/ϖ. One parsec is about 3.26 light-years.

## Step 1 — Simulate ten years of infrared sky survey visits

NASA's WISE spacecraft (later NEOWISE) scanned the whole sky about twice a year, always looking roughly 90° away from the Sun. That viewing angle is the best possible for measuring parallax.

```python
import numpy as np
from fdastro.astrometry import simulate_five_parameter, fit_five_parameter, tangential_velocity_kms

# Two visits, 2 days apart, every ~half year, timed for 90° from the Sun.
mjd = np.sort(np.concatenate([np.arange(56791, 60300, 182.6), np.arange(56793, 60300, 182.6)]))
# A made-up cold brown dwarf 2.3 parsecs away, moving fast across the sky.
ra, dec = simulate_five_parameter(mjd, 133.8, -7.2, pmra_arcsec_yr=-8.1, pmdec_arcsec_yr=0.7,
                                  parallax_arcsec=0.439, sigma_arcsec=0.05, rng=5)
print(f"{mjd.size} detections over {(mjd[-1] - mjd[0]) / 365.25:.1f} years")
```

## Step 2 — Fit the five astrometric parameters

```python
fit = fit_five_parameter(mjd, ra, dec, sigma_arcsec=0.05)
print(f"parallax   = {fit.parallax_arcsec:.3f} ± {fit.sigmas['parallax_arcsec']:.3f} arcsec")
print(f"distance   = {fit.distance_pc:.2f} parsec = {fit.distance_pc * 3.2616:.1f} light-years")
print(f"motion     = {fit.proper_motion_arcsec_yr:.2f} arcsec per year")
print(f"speed      = {tangential_velocity_kms(fit.proper_motion_arcsec_yr, fit.parallax_arcsec):.0f} km/s across our line of sight")
```

## Step 3 — See why viewing angle matters

```python
for label, start in [("near opposition", 56700), ("at 90° from the Sun", 56791)]:
    t = np.sort(np.concatenate([np.arange(start, 60300, 182.6), np.arange(start + 2, 60300, 182.6)]))
    r, d = simulate_five_parameter(t, 133.8, -7.2, pmra_arcsec_yr=-8.1, pmdec_arcsec_yr=0.7,
                                   parallax_arcsec=0.439, sigma_arcsec=0.05, rng=5)
    f = fit_five_parameter(t, r, d, 0.05)
    print(f"{label:22s} parallax error = {f.sigmas['parallax_arcsec']:.3f} arcsec")
```

Looking straight away from the Sun, the Earth's motion is along our line of sight, so the yearly wiggle almost disappears in one direction. Looking at 90°, the wiggle is biggest.

## Why fast movers can be missed

Catalogs often match detections from different dates by looking for a source within a few arcseconds. A very nearby object can move many arcseconds between visits, so its detections may not be matched to each other. Projects like **Backyard Worlds: Planet 9** asked volunteers to spot fast movers by eye in WISE images — and found many new cold brown dwarfs that way. See [D04](../disclosures/d04-nearby-cold-worlds-wise.md).

## Real data

```py
# Requires: pip install "fdastro[archives]" and internet access.
from astroquery.ipac.irsa import Irsa
# Query the NEOWISE single-exposure source table near a position, then pass
# the detections' MJD, RA, Dec and uncertainties to fit_five_parameter.
```

Check IRSA's documentation for current table names; they change between data releases.

## For experts

- Model: gnomonic tangent plane about (α₀, δ₀); parallax factors `f_α* = X sin α − Y cos α`, `f_δ = (X cos α + Y sin α) sin δ − Z cos δ`.
- This module uses the heliocentric Earth (≈1% scale error relative to barycentric) unless you pass `observer_au`. For WISE/NEOWISE, the spacecraft's own position matters at the ~1e-4 au level; for precise work use the spacecraft ephemeris.
- `distance_pc` is reported only for parallax S/N ≥ 5, because 1/ϖ is a biased estimator at low S/N (Bailer-Jones 2015).
- Cold-object color: late-T and Y dwarfs are very red in W1 − W2 (roughly ≥ 2 mag for late-T; Kirkpatrick et al. 2011). Use color to prioritize, not to classify alone.

## Next

[Tutorial 7 — Single and fading transits](t07-single-and-fading-transits.md)
