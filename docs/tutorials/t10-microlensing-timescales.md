# Tutorial 10 — Microlensing timescales

> **In one sentence:** Learn why a lonely Earth-size planet drifting between the stars makes a brightening that lasts only hours, while a star makes one that lasts weeks.

## For young readers

Gravity can bend light. When something heavy passes exactly in front of a faraway star, it acts like a magnifying glass, and the star looks brighter for a while. Heavy things make long, slow brightenings. Light things, like a planet floating alone in space, make short ones — just a few hours. Some planets have no star at all. This is one of the only ways to find them.

## Step 1 — The size of the "magnifying glass"

The **Einstein radius** is the angle of the ring of light a perfect lens would make.

```python
from fdastro.microlensing import einstein_radius_mas, einstein_time_days
from fdastro.constants import M_EARTH_MSUN, M_JUPITER_MSUN

for name, m in [("Sun-like star", 1.0), ("Jupiter-mass planet", M_JUPITER_MSUN), ("Earth-mass planet", M_EARTH_MSUN)]:
    theta = einstein_radius_mas(m, d_lens_kpc=4.0, d_source_kpc=8.0)
    t_e = einstein_time_days(m, 4.0, 8.0, mu_rel_mas_yr=5.0)
    print(f"{name:20s} θE = {theta:8.4f} mas   event lasts ~ {t_e:7.2f} days ({t_e * 24:7.1f} hours)")
```

(1 mas, a milliarcsecond, is the width of a coin seen from about 5,000 km away.)

## Step 2 — Draw a light curve

```python
import numpy as np
from fdastro.microlensing import paczynski_magnification

hours = np.linspace(-6, 6, 13)
mag = paczynski_magnification(hours / 24.0, t0=0.0, t_e=einstein_time_days(M_EARTH_MSUN, 4.0, 8.0, 5.0), u0=0.1)
for h, a in zip(hours, mag):
    print(f"{h:+5.1f} h  {'#' * int(a * 5):<60} x{a:.2f}")
```

## Step 3 — Is it really lensing? Check the color

Gravity bends all colors the same way, so a real lensing event should not change the star's color (unless light from a nearby star is blended in). Flares and many variable stars do change color.

```python
from fdastro.microlensing import achromaticity_test

t = np.linspace(-0.3, 0.3, 30)
red = 18.0 - 2.5 * np.log10(paczynski_magnification(t, 0.0, 0.15, 0.2))
blue = red + 0.8                         # same shape, constant color
err = np.full(t.size, 0.01)
print("lensing-like:", achromaticity_test(blue, err, red, err)["achromatic"])
print("flare-like  :", achromaticity_test(red * 0.95 + 0.9, err, red, err)["achromatic"])
```

## Real surveys

OGLE, MOA and KMTNet watch hundreds of millions of stars toward the center of our galaxy. They have found short events that point to free-floating planets, including Earth-mass candidates (for example Mróz et al. 2020). NASA's Nancy Grace Roman Space Telescope is expected to find many more. See [D07](../disclosures/d07-short-microlensing-free-floating-planets.md).

## For experts

- Point-source point-lens magnification A(u) = (u² + 2)/(u √(u² + 4)).
- θ_E = √(κ M π_rel), κ = 8.144 mas M☉⁻¹; t_E = θ_E / μ_rel. A single t_E is degenerate in M, π_rel and μ_rel; masses need θ_E (finite-source effects) and π_E (microlens parallax).
- For Earth-mass lenses, ρ = θ*/θ_E is often ≳ 1 for bulge giants, so finite-source effects dominate the light-curve shape.

## Done!

You have finished the tutorials. Read [how to report a discovery](../about/how-to-report-a-discovery.md) before sharing any result, and see the [disclosures](../disclosures/README.md) for open questions you can help with.
