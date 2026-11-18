# Tutorial 9 — Tilted orbits and hidden companions

> **In one sentence:** Use a tilted planet's orbit to draw a "treasure map" of where an unseen outer planet could be.

## For young readers

A spinning top leans and slowly turns. If it keeps leaning without falling, something is helping it. Some planets orbit their star at a big tilt compared with the way the star spins. One idea is that a heavy, unseen planet farther out is gently pushing on it in rhythm, like pushing a swing at the right moment. We can work out how heavy and how far away that hidden planet would need to be.

## The big idea

Two things make the tilted orbit slowly swivel (precess):

1. **The star's bulge.** Spinning stars are slightly flattened. That bulge pulls on the planet.
2. **An outer planet.** Its gravity also makes the inner orbit swivel.

If the two swivel rates match, they can work together — a **secular resonance** — and keep the tilt large. Setting the two rates equal gives a curve of possible (distance, mass) pairs for the hidden planet.

## Step 1 — How flattened is the star?

```python
from fdastro.obliquity import j2_from_rotation

print(f"Sun (25.4-day spin): J2 ≈ {j2_from_rotation(25.4):.1e}")      # measured value ≈ 2.2e-7
print(f"Young star (3-day spin): J2 ≈ {j2_from_rotation(3.0):.1e}")
```

## Step 2 — Draw the treasure map

Example: a warm Neptune at 0.05 au with a 60° tilt, around a Sun-like star with J2 = 1e-5 (a young, faster-spinning star).

```python
import numpy as np
from fdastro.obliquity import resonant_companion_mass_mjup

a2 = np.array([0.5, 1.0, 2.0, 3.0, 5.0])
masses = resonant_companion_mass_mjup(a2, j2=1e-5, rstar_rsun=1.0, a1_au=0.05, psi_deg=60.0)
for a, m in zip(a2, masses):
    print(f"outer planet at {a:3.1f} au would need about {m:8.2f} Jupiter masses")
```

Close companions can be light; distant ones must be heavy. Observers can compare this curve with radial-velocity limits or Gaia astrometry to decide where to look.

## Step 3 — Check the two rates directly

```python
from fdastro.obliquity import stellar_quadrupole_nodal_rate, companion_nodal_rate
from fdastro.constants import M_JUPITER_MSUN

g_star = stellar_quadrupole_nodal_rate(1e-5, 1.0, 0.05, 60.0)
g_comp = companion_nodal_rate(masses[1] * M_JUPITER_MSUN, 0.05, 1.0)
print(f"star bulge: one swivel every {2 * np.pi / g_star / 365.25:,.0f} years")
print(f"companion : one swivel every {2 * np.pi / g_comp / 365.25:,.0f} years")
```

## How we could be wrong

- Tilted orbits can also come from past events: planet–planet scattering, the star's birth environment, or a tilted disk.
- The star's J2 is uncertain by a factor of a few.
- Real systems have more than two planets. The full secular problem must be solved.

Known examples of tilted inner planets with outer companions include HAT-P-11 (with HAT-P-11 c) and π Mensae. See [D13](../disclosures/d13-tilted-orbits-hidden-companions.md).

## For experts

- g_* = (3/2) J₂ (R*/a₁)² n₁ cos ψ; g₁₂ = (1/4) n₁ (m₂/M*) α² b⁽¹⁾₃/₂(α), α = a₁/a₂, with Laplace coefficients by quadrature.
- In the hierarchical limit b⁽¹⁾₃/₂ ≈ 3α, so (m₂/M*)(a₁/a₂)³ ≈ 2 J₂ (R*/a₁)² cos ψ.
- This is a two-frequency, lowest-order condition (cf. Petrovich et al. 2020 for a dynamical scenario producing misaligned close-in Neptunes). Use it for target prioritization, not as a prediction.

## Next

[Tutorial 10 — Microlensing timescales](t10-microlensing-timescales.md)
