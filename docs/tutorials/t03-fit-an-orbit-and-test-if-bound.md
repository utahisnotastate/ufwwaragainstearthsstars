# Tutorial 3 — Fit an orbit and test if it is bound

> **In one sentence:** Starting only from sky positions, find the best orbit and ask whether a closed (bound) orbit could still explain the data.

## For young readers

A telescope tells us *where* a moving dot is in the sky, but not *how far away* it is. So the computer plays a guessing game. It tries many distances and speeds, keeps the guess that matches the dots best, and then asks: "Could this be an ordinary space rock that loops around the Sun?" If the answer is "no way", we may have found a visitor from another star. Then real astronomers must check!

## The big idea

1. **Range scan.** Try many distances (`rho`) and line-of-sight speeds (`rho_dot`). Score each guess.
2. **Orbit fit.** Start from the best guesses and adjust all six numbers of the orbit until the predicted positions match the observed ones as closely as possible (least squares).
3. **Bound-orbit test.** Fit again, but force the speed to stay below the Sun's escape speed. If the best "forced-bound" orbit fits much worse, a bound orbit is unlikely.

## Step 1 — Make practice observations

We simulate a 3I/ATLAS-like object observed on six nights over 20 days. These are **synthetic** data: we know the right answer, so we can check the method.

```python
import numpy as np
from fdastro.catalogs import INTERSTELLAR_OBJECTS
from fdastro.kepler import elements_to_state, ecliptic_to_equatorial
from fdastro.iso import simulate_observations

o = INTERSTELLAR_OBJECTS[2]
s_ecl = elements_to_state(o["q_au"], o["e"], o["i_deg"], o["node_deg"], o["peri_deg"], -80.0)
true_state = np.concatenate([ecliptic_to_equatorial(s_ecl[:3]), ecliptic_to_equatorial(s_ecl[3:])])

epoch = 60850.0
nights = epoch + np.array([0, 2, 5, 9, 14, 20])
mjd = np.concatenate([n + np.array([0.0, 0.02, 0.04]) for n in nights])  # 3 images per night
obs = simulate_observations(true_state, epoch, mjd, sigma_arcsec=0.3, rng=7)
print(f"{obs.n} observations over {obs.arc_days:.1f} days")
```

## Step 2 — Scan distances and fit the orbit

```python
from fdastro.iso import range_scan, fit_orbit

scan = range_scan(obs)
fit = fit_orbit(obs, scan=scan)
el = fit.elements
print(f"rms = {fit.rms_arcsec:.2f} arcsec, reduced chi2 = {fit.reduced_chi2:.2f}")
print(f"e = {el.e:.2f} ± {fit.e_sigma:.2f} (true {o['e']:.2f}),  i = {el.i_deg:.1f}° (true {o['i_deg']:.1f}°)")
```

A reduced chi-square near 1 means the fit matches the data about as well as the noise allows.

## Step 3 — Run the bound-orbit test

```python
from fdastro.iso import bound_orbit_test

test = bound_orbit_test(obs, fit, scan=scan)
print(f"best bound orbit is worse by Δχ² = {test.delta_chi2:.0f}")
print(f"significance = {test.sigma:.1f} sigma")
print(test.verdict)
```

## Step 4 — Compare with an ordinary asteroid

```python
asteroid = elements_to_state(2.3, 0.15, 10.0, 80.0, 30.0, 20.0)
ast_state = np.concatenate([ecliptic_to_equatorial(asteroid[:3]), ecliptic_to_equatorial(asteroid[3:])])
ast_obs = simulate_observations(ast_state, epoch, mjd, sigma_arcsec=0.3, rng=3)
ast_scan = range_scan(ast_obs)
ast_fit = fit_orbit(ast_obs, scan=ast_scan)
print(bound_orbit_test(ast_obs, ast_fit, scan=ast_scan).verdict)
```

## Step 5 — One-line summary

`screen_object` does all three steps and returns a short, honest summary.

```python
import json
from fdastro.iso import screen_object

print(json.dumps(screen_object(obs, name="practice-object"), indent=2))
```

Notice the wording: "hyperbolic **candidate** … needs independent follow-up". The tool never says "confirmed". Only new observations by other teams can confirm a discovery.

## Things that can fool you

| Problem | What happens | What to do |
|---|---|---|
| Arc too short (one night) | Almost any orbit fits; `e` is meaningless | Wait for more nights; the tool warns if the arc is under 3 days |
| Wrong uncertainties | Too-small `sigma_arcsec` makes everything look significant | Use realistic errors (often 0.1"–1" for surveys) |
| Wrong linkage | Two different objects joined into one "orbit" | Look at residuals; a bad link gives large, patterned residuals |
| Topocentric parallax ignored | Nearby objects look like they have odd orbits | Pass observatory positions (see [Tutorial 4](t04-reading-mpc-observations.md)) |
| Comet outgassing | Small extra push changes the orbit | Try `fit_orbit(obs, fit_a1=True)` |
| Timing errors | Positions shifted along the track | Check observatory time stamps |

## Check your understanding

1. Why do we try many distances first? *(A single image gives direction, not distance; the scan finds good starting guesses.)*
2. What does a large Δχ² mean? *(Forcing a bound orbit makes the fit much worse.)*
3. Why is "candidate" the right word? *(Independent confirmation is still needed.)*

## For experts

- **Parametrization:** Cartesian state at the mean epoch; optional radial non-gravitational term `A1 (1 au/r)²` (au/day²) integrated with DOP853.
- **Light time:** two-iteration correction; aberration is absorbed because simulated and real astrometric positions are compared consistently (for real data, use astrometric RA/Dec as the MPC provides).
- **Initial orbit determination:** attributable `(α, δ, α̇, δ̇)` from a low-order polynomial plus a `(ρ, ρ̇)` grid (48 × 41 by default, 0.01–60 au, ±0.06 au/day ≈ ±104 km/s), in the spirit of statistical ranging (Virtanen et al. 2001) and admissible regions (Milani et al. 2004).
- **Bound test:** velocity reparametrized as `v = v_esc(r) w / sqrt(1 + |w|²)`; the likelihood-ratio statistic Δχ² follows ½χ²₀ + ½χ²₁ at the boundary (Chernoff 1954), so the one-sided Gaussian-equivalent significance is `sqrt(Δχ²)`.
- **Linearized `σ_e`** comes from the normal-matrix covariance and is optimistic for short arcs; the Δχ² test is the more robust statement.
- **Scale:** `screen_tracklet_pairs` is an O(n²) pilot tool for hundreds of tracklets. Survey-scale linking needs dedicated software such as HelioLinC3D (Rubin) or THOR.

## Next

[Tutorial 4 — Reading Minor Planet Center observations](t04-reading-mpc-observations.md)
