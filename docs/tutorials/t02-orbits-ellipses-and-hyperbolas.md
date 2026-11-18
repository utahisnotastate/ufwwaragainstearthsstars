# Tutorial 2 — Ellipses and hyperbolas

> **In one sentence:** Learn why objects that belong to the Sun travel on closed loops, while visitors from other stars travel on open, V-shaped paths.

## For young readers

Throw a ball up gently, and it comes back down. Throw it hard enough, and (if you were on a tiny moon) it could fly away forever. The Sun's gravity works the same way. Slow objects stay and loop around the Sun. Fast objects escape. Their paths open up like a wide letter V. That shape is called a **hyperbola**.

## The big idea

Every object moving under the Sun's gravity alone follows a **conic section**: a circle, an ellipse, a parabola or a hyperbola. Which one depends on a single number, the **specific orbital energy**:

- energy below zero → bound (ellipse, eccentricity `e < 1`)
- energy exactly zero → parabola (`e = 1`)
- energy above zero → unbound (hyperbola, `e > 1`)

## Step 1 — Build a state from orbital elements

A **state vector** is a position (x, y, z) and a velocity (vx, vy, vz). The function `elements_to_state` makes one from orbital elements.

```python
import numpy as np
from fdastro.kepler import elements_to_state, state_to_elements, specific_energy, escape_speed
from fdastro.constants import KMS_PER_AU_DAY

# A main-belt asteroid and a 3I/ATLAS-like visitor, both roughly 3 au from the Sun.
asteroid = elements_to_state(q=2.2, e=0.2, i_deg=8, node_deg=0, peri_deg=0, true_anomaly_deg=100)
visitor = elements_to_state(q=1.35, e=6.12, i_deg=175, node_deg=323, peri_deg=129, true_anomaly_deg=-70)

for name, s in [("asteroid", asteroid), ("visitor", visitor)]:
    r, v = s[:3], s[3:]
    dist = np.linalg.norm(r)
    speed = np.linalg.norm(v) * KMS_PER_AU_DAY
    v_esc = escape_speed(dist) * KMS_PER_AU_DAY
    energy = specific_energy(r, v)
    print(f"{name:9s} r = {dist:4.2f} au  speed = {speed:5.1f} km/s  escape = {v_esc:5.1f} km/s  energy {'>' if energy > 0 else '<'} 0")
```

The visitor moves much faster than the local escape speed. The Sun cannot hold it.

## Step 2 — Follow the paths through time

`propagate` moves a state forward or backward in time using exact two-body motion. It works for ellipses and hyperbolas alike (it uses the "universal variable" method).

```python
from fdastro.kepler import propagate

days = np.linspace(-400, 400, 9)
r_ast, _ = propagate(asteroid, days)
r_vis, _ = propagate(visitor, days)
for d, ra, rv in zip(days, np.linalg.norm(r_ast, axis=1), np.linalg.norm(r_vis, axis=1)):
    print(f"day {d:+6.0f}: asteroid {ra:5.2f} au   visitor {rv:6.2f} au")
```

The asteroid's distance goes up and down as it loops. The visitor swoops in once and then leaves for good.

## Step 3 — Turn a state back into elements

```python
el = state_to_elements(visitor[:3], visitor[3:])
print(f"e = {el.e:.3f}, q = {el.q:.3f} au, a = {el.a:.3f} au (negative for a hyperbola)")
print(f"v_infinity = {el.v_infinity_kms:.1f} km/s")
```

## Step 4 — Where did the visitor come from?

A hyperbola has two straight "arms" far from the Sun. The incoming arm points back toward the visitor's **radiant**: the part of the sky it came from.

```python
from fdastro.catalogs import INTERSTELLAR_OBJECTS
from fdastro.kepler import incoming_radiant, ecliptic_to_equatorial, unit_vector_to_radec

oumuamua = INTERSTELLAR_OBJECTS[0]
s = elements_to_state(oumuamua["q_au"], oumuamua["e"], oumuamua["i_deg"],
                      oumuamua["node_deg"], oumuamua["peri_deg"], 0.0)
ra, dec = unit_vector_to_radec(ecliptic_to_equatorial(incoming_radiant(s[:3], s[3:])))
print(f"ʻOumuamua came from RA {ra:.1f}°, Dec {dec:+.1f}° — near the bright star Vega in Lyra")
```

## Check your understanding

1. What sign does the energy have for a bound orbit? *(Negative.)*
2. Why is the semi-major axis `a` negative for a hyperbola? *(Because `a = -GM / (2 × energy)` and the energy is positive.)*
3. Why does the radiant not point exactly at the star the object came from? *(The object has traveled for millions of years and stars move; the radiant points to the direction, not to a specific star.)*

## For experts

- Propagation: universal-variable Kepler equation solved with the Laguerre–Conway iteration; Stumpff functions use series near zero and are clipped for very large hyperbolic arguments. Verified against DOP853 integration to < 1e-8 au over ±200 days in the test suite.
- Radiant: `-(1/e) P̂ - sqrt(1 - 1/e²) Q̂` in the perifocal basis. For ʻOumuamua this reproduces the published radiant (RA ≈ 279.8°, Dec ≈ +34°) to better than 1°.
- Elements are frame-dependent. Rotate equatorial states with `equatorial_to_ecliptic` before comparing with catalog elements.

## Next

[Tutorial 3 — Fit an orbit and test if it is bound](t03-fit-an-orbit-and-test-if-bound.md)
