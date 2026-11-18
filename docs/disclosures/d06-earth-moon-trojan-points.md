# D06 — Dust clouds and possible mini-moons at the Earth–Moon balance points

> **In one sentence:** Two "balance points" in the Moon's orbit may hold faint clouds of dust, and astronomers are still checking whether anything solid could be hiding there too.
>
> **Evidence level:** 🟠 **Level 4 — Long shot** (solid bodies at the Earth–Moon L4/L5 points). The dust clouds themselves are 🔵 **Level 2 — Strong evidence, still debated**.
>
> *Last reviewed: November 2026.*

## For young readers

Picture a big merry-go-round in a park. There are two special spots on the floor where things tend to stay put as it spins. If you drop a leaf there, it rides along instead of flying off.

The Earth and Moon have spots like this too. They are called **L4** and **L5**. One is 60 degrees ahead of the Moon in its orbit, and one is 60 degrees behind. In 1961, a Polish astronomer named Kazimierz Kordylewski said he saw very faint dust clouds there. For years, many people doubted it. In 2018, Hungarian scientists used polarized light (light whose waves line up) and reported seeing the dust. Could there also be small rocks or "mini-moons" there? Searches have not found any so far. The Sun's pull keeps stirring these spots, so it is hard for things to stay a long time.

## The big idea

In a system of two large bodies, such as the Earth and the Moon, there are five special points where a small object can move along with the pair. These are the **Lagrange points**. Two of them, L4 and L5, form equilateral triangles with the Earth and Moon. In an idealized system of just two big bodies, small objects near L4 and L5 can stay for a very long time.

But the Earth–Moon system is not alone. The Sun pulls strongly on both, and on anything at L4 or L5. That extra pull makes long-term stability much weaker than in the ideal case. Dust may pass through and collect temporarily, but long-lived rocks are much less likely.

Kordylewski's clouds are extremely faint — much fainter than the zodiacal light and the glow of the night sky. That is why they were disputed for decades. The 2018–2019 polarization measurements used the fact that sunlight scattered by small dust grains is polarized in a predictable way.

Two other kinds of "extra moons" are real, and are worth knowing about because they are often confused with L4/L5 objects:

- **Quasi-satellites** such as **469219 Kamoʻoalewa** orbit the Sun, not the Earth, but stay near Earth for many years. Kamoʻoalewa was discovered in 2016, may be a piece of the Moon, and is the target of China's Tianwen-2 sample-return mission, launched in 2025.
- **Temporary mini-moons** such as **2024 PT5** are captured loosely by Earth for a short time. 2024 PT5 stayed from 29 September to 25 November 2024.

## What we already know

- 🔵 **Level 2 — Strong evidence, still debated.** Imaging polarimetry reported a dust cloud at the Earth–Moon L5 point consistent with Kordylewski's description (Slíz-Balogh, Barta & Horváth 2018, 2019). Follow-up polarimetric observations have been published since, but independent confirmation by other groups and methods is still limited.
- 🟢 **Level 1 — Confirmed.** Photographic searches of the Earth–Moon libration points found no discrete natural or artificial objects down to about 14th magnitude (Freitas & Valdes 1980; Valdes & Freitas 1983).
- 🟢 **Level 1 — Confirmed.** Solar and planetary perturbations destabilize the Earth–Moon triangular Lagrange points over long times (Lissauer & Chambers 2008).
- 🟢 **Level 1 — Confirmed.** Kamoʻoalewa is an Earth quasi-satellite with a reflectance spectrum similar to lunar material (Sharkey et al. 2021).
- 🟢 **Level 1 — Confirmed.** 2024 PT5 was a short-lived mini-moon from 29 September to 25 November 2024 (de la Fuente Marcos & de la Fuente Marcos 2024).

## What is still open

**Are there any solid bodies — not just dust — near the Earth–Moon L4 and L5 points today?**

A body would need to be either very small, very recently captured, or very dark and in a region not yet searched to the right depth. Modern wide-field cameras and synthetic tracking (shifting and stacking many short images to follow a moving object) are far more sensitive than the photographic plates of the 1980s.

## How you could test it

1. **Compute the positions** of L4 and L5 on the sky for each night. They are 60° ahead of and behind the Moon along its orbit.
2. **Pick dark nights** when L4 or L5 is high in the sky and far from the Moon's glare.
3. **Take many short images** with a wide-field camera.
4. **Shift and stack** the images at the expected rate of motion of an object riding along with the Moon (about half a degree per hour relative to the stars).
5. **Look for point sources** that appear only at that rate.
6. **Add polarization** (optional): image through a polarizer at several angles to study the dust, following the published method.
7. **Report** any moving object to the Minor Planet Center with exact times and positions.

## How we could be wrong

- **Satellites.** Many artificial satellites cross these regions. Check every candidate against satellite catalogs (for example, CelesTrak).
- **Airglow and zodiacal light.** These background glows are much brighter than the dust clouds and change with time.
- **Instrument polarization and stray light.** These can mimic faint polarized patches.
- **A clear "no" result.** A deep synthetic-tracking survey at both points that finds no moving sources sets an upper limit on the size of any solid body.

## For experts

**Brightness of a hypothetical body.** For a body of diameter *D* (km) and geometric albedo *p*,

$$ H = 5\log_{10}\!\left(\frac{1329}{D\sqrt{p}}\right), \qquad V \approx H + 5\log_{10}(r\,\Delta) + \text{phase term}, $$

with *r* ≈ 1 au and Δ ≈ 0.00257 au (the Moon's distance). For *D* = 0.1 km and *p* = 0.05, *H* ≈ 23.9 and *V* ≈ 10.9 near opposition. Even for *D* = 0.03 km, *V* ≈ 13.5. So any dark body tens of meters across at L4/L5 would be relatively bright near opposition, not magnitude 22–24 as stated in the original notes; that error has been corrected here. This is why older searches to magnitude ~14 already constrain bodies larger than a few tens of meters in the regions they covered.

**Motion.** Objects co-moving with the Moon drift relative to the stars at roughly the Moon's sidereal rate, about 0.5″ s⁻¹ (about 0.55° per hour), plus libration around the triangular point.

**Polarization.** Small dust grains at large phase angles give positive linear polarization. Rough, dark regolith surfaces show a **negative polarization branch** at small phase angles (minimum polarization of order −1% to −2% near 7°–10° for dark asteroids). Measuring the polarization–phase curve could in principle distinguish dust from a solid surface, but only if a source is first detected.

**Dynamics.** In the circular restricted three-body problem, L4/L5 are linearly stable for mass ratios μ < 0.0385; the Earth–Moon μ ≈ 0.0122 satisfies this. Solar forcing near the 1:1 resonance between the synodic month and libration frequencies destroys long-term stability for most initial conditions (Lissauer & Chambers 2008).

## Try it

- Lesson: [Balance points in space](../lessons/l05-balance-points-in-space.md)
- Lesson: [Light has a direction](../lessons/l07-light-has-a-direction.md)
- Code module: `fdastro.kepler` (orbit basics)
- Related: [D11 — Trojan and co-orbital asteroids near Venus, Earth and Mars](d11-inner-solar-system-trojans.md)
- Reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- de la Fuente Marcos, C. & de la Fuente Marcos, R. (2024). A two-month mini-moon: 2024 PT5 captured by Earth from September to November. *Research Notes of the AAS* 8, 224. doi:10.3847/2515-5172/ad781f
- Freitas, R. A. & Valdes, F. (1980). A search for natural or artificial objects located at the Earth–Moon libration points. *Icarus* 42, 442.
- Kordylewski, K. (1961). [Photographic study of the L5 libration point of the Earth–Moon system; in German.] *Acta Astronomica* 11, 165.
- Lissauer, J. J. & Chambers, J. E. (2008). Solar and planetary destabilization of the Earth–Moon triangular Lagrangian points. *Icarus* 195, 16.
- Sharkey, B. N. L. et al. (2021). Lunar-like silicate material forms the Earth quasi-satellite (469219) 2016 HO3 Kamoʻoalewa. *Communications Earth & Environment* 2, 231.
- Slíz-Balogh, J., Barta, A. & Horváth, G. (2018). Celestial mechanics and polarization optics of the Kordylewski dust cloud in the Earth–Moon Lagrange point L5 – I. *Monthly Notices of the Royal Astronomical Society* 480, 5550. arXiv:1910.07466
- Slíz-Balogh, J., Barta, A. & Horváth, G. (2019). Celestial mechanics and polarization optics of the Kordylewski dust cloud in the Earth–Moon Lagrange point L5 – II. Imaging polarimetric observation. *Monthly Notices of the Royal Astronomical Society* 482, 762. arXiv:1910.07471
- Valdes, F. & Freitas, R. A. (1983). A search for objects near the Earth–Moon Lagrangian points. *Icarus* 53, 453.
