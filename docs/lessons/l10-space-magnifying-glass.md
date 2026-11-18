# Lesson 10 — The Space Magnifying Glass

| | |
|---|---|
| **Ages** | 11–15 |
| **Time** | 45 minutes |
| **Group size** | Pairs |
| **Connects to** | [D07 — Free-floating planets in brief lensing flashes](../disclosures/d07-short-microlensing-free-floating-planets.md) |

## Big question

**How can a dark planet floating alone in space make a faraway star look brighter?**

## For young readers

Gravity can bend light. Not much — but a little. When a heavy object passes exactly in front of a faraway star, its gravity bends the star's light like a magnifying glass. For a short time, the star looks **brighter**. Then it fades back to normal. This is called **microlensing**.

The heavier the object, the longer the brightening lasts. A star passing in front of another star can cause a brightening that lasts weeks. A planet-sized object causes a flash that lasts only hours or days.

Some planets do not orbit any star. They float alone through the galaxy. We call them **free-floating** or **rogue** planets. They are dark, but microlensing can reveal them!

## Learning goals

Learners will be able to:

1. Show how a curved glass can bend and focus light.
2. Explain that gravity can bend light from distant stars.
3. Explain that lighter lenses make shorter brightenings.

## NGSS alignment

- **MS-PS4-2** — light is bent (transmitted) by materials.
- **HS-ESS1-4** — math models of motion (extension).

## Materials

- The base of a clear wine glass (plastic stemware works for younger groups; real glass works best — adult handles it)
- Graph paper or a printed grid of dots
- A small flashlight or a phone flashlight, or a candle-free LED "tea light"
- A dark corner of the room
- Paper and pencil for graphing

## Safety

- Real glass can break: an adult should hold it, or use plastic.
- Do not shine bright lights into anyone's eyes.

## Steps

1. **Look through the "lens."** Hold the glass base flat over the graph paper and look down through it. The grid lines look bent and stretched. Mass bends light in a similar way (but for a different reason).
2. **Make a ring.** In a dark corner, put the small light about 1–2 m away. Look at the light through the bottom of the glass. Slowly move the glass sideways. When the light is exactly behind the center, you may see a **ring** of light. Astronomers call this an **Einstein ring**.
3. **Make a light curve.** Have a partner hold a light-meter app (optional) or simply judge brightness on a scale of 1–5. Slide the glass slowly across the line between your eye and the light. Record brightness every second.
4. **Graph it.** Time across, brightness up. You should get a smooth hump: rise, peak, fall. This is the shape astronomers look for.
5. **Lighter lens, shorter flash.** Repeat with a smaller curved lens (for example, a small round clear bead or the base of a smaller glass), moving at the same speed. In the real Universe, a lighter lensing object makes a brief flash. This is how astronomers find planet-mass lenses.
6. **Discuss.** If a free-floating planet lenses a star for only a few hours, what kind of telescope would you need to catch it? (One that looks at the same stars very often, day and night, or from space.)

**Accessible version:** Use a light-sensor app with sound output to "hear" the brightening as the lens passes in front of the light.

## Discussion questions

1. Why does the star get brighter instead of being blocked?
2. Why do lighter objects make shorter brightenings?
3. Why do astronomers watch crowded star fields near the center of our galaxy for this?
4. Could a star flare look similar? How could you tell the difference? (Lensing brightens all colors equally; flares are usually much bluer.)

## Check for understanding (answers for the teacher)

| Question | Expected answer |
|---|---|
| What is microlensing? | When a foreground object's gravity bends and brightens the light of a background star for a short time. |
| What does the brightening's length tell us? | Mostly the lens's mass (heavier → longer), along with distance and speed. |
| What is a free-floating planet? | A planet not orbiting any star. |
| How can you tell lensing from a flare? | Lensing is achromatic (same in all colors) and has a smooth, symmetric shape. |

## Extension

- Older learners: the duration (the "Einstein time") grows with the **square root** of the mass. If a Sun-mass lens gives about 25 days, roughly how long does a Jupiter-mass lens (about 1/1000 of the Sun) give? (About 25 ÷ √1000 ≈ 0.8 days.) An Earth-mass lens (about 1/333,000 of the Sun)? (About 25 ÷ 577 ≈ 0.04 days ≈ 1 hour.)
- See [Tutorial 10](../tutorials/t10-microlensing-timescales.md) to compute these with code.

## For the teacher: the science behind it

**Model limits.** A wine-glass base is a refracting lens; gravitational lensing is not refraction. The glass base is a good analogy because its shape (thick center, thin edges, with a central "foot") produces a ring and arcs similar to a point-mass gravitational lens, but the exact mapping differs.

**Point-lens microlensing (🟢 Level 1).** The angular Einstein radius is θ_E = √[(4*GM*/*c*²) · *D*ₗₛ/(*D*ₗ *D*ₛ)]. The Einstein timescale is *t*_E = θ_E/μ_rel, where μ_rel is the lens–source relative proper motion. With impact parameter *u*(*t*) = √(*u*₀² + [(*t* − *t*₀)/*t*_E]²), the magnification is *A*(*u*) = (*u*² + 2)/(*u*√(*u*² + 4)) (Paczyński 1986). Because *t*_E ∝ √*M*, typical Galactic-bulge events last about a month for stellar lenses, about a day for Jupiter-mass lenses and about an hour for Earth-mass lenses (exact values depend on distances and velocities).

**Free-floating planets (🔵 Level 2).** Surveys including OGLE, MOA and KMTNet have found very short events consistent with free-floating planetary-mass lenses. OGLE-2016-BLG-1928 has *t*_E ≈ 42 minutes and is a candidate terrestrial-mass rogue planet (Mróz et al. 2020). Sumi et al. (2023) estimated from MOA data that free-floating planets may be more numerous than stars, with large uncertainties. NASA's Nancy Grace Roman Space Telescope, launched in 2026, includes a Galactic Bulge microlensing survey expected to measure this population much better. See [D07](../disclosures/d07-short-microlensing-free-floating-planets.md).

**False positives:** stellar flares (chromatic), cataclysmic variables, asteroid passages through the photometric aperture, and detector artifacts. Two-band photometry checks achromaticity.

### References

- Paczyński, B. (1986). Gravitational microlensing by the galactic halo. *The Astrophysical Journal*, 304, 1–5. doi:10.1086/164140
- Mróz, P., et al. (2020). A terrestrial-mass rogue planet candidate detected in the shortest-timescale microlensing event. *The Astrophysical Journal Letters*, 903, L11.
- Sumi, T., et al. (2023). Free-floating planet mass function from MOA-II 9-year survey toward the Galactic bulge. *The Astronomical Journal*, 166, 108.

## Connects to

- Disclosure: [D07 — Free-floating planets in brief lensing flashes](../disclosures/d07-short-microlensing-free-floating-planets.md)
- Tutorial: [Tutorial 10 — Microlensing timescales](../tutorials/t10-microlensing-timescales.md)
- Next lesson: [Lesson 11 — Moons that make planets wobble](l11-moons-that-make-planets-wobble.md)
