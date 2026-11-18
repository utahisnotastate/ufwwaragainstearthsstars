# D07 — Free-floating planets in brief lensing flashes

> **In one sentence:** When a lone planet drifts in front of a distant star, its gravity acts like a tiny magnifying glass and makes the star brighten for a few hours — so very short brightening events reveal planets that have no star at all.
>
> **Evidence level:** 🔵 **Level 2 — Strong evidence** (how common Earth-mass free-floating planets are). The detection method is 🟢 **Level 1 — Confirmed**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine a dark backyard with a porch light far away. A clear glass marble rolls across in front of the light. For a moment, the marble bends the light and makes it look brighter. Then it rolls on and the light looks normal again.

In space, gravity can bend light, a bit like that marble. If a planet passes exactly in front of a faraway star, the star looks brighter for a short time. This is called **gravitational microlensing**. Heavy stars make the star brighten for weeks. Small planets make it brighten for just hours. Some planets do not orbit any star — they float alone through the galaxy. Astronomers call them **free-floating** or **rogue planets**. Microlensing is one of the only ways to find them, because they give off almost no light of their own.

## The big idea

Einstein's theory of gravity says mass bends the path of light. A star or planet passing almost exactly between us and a background star focuses that star's light and makes it brighter. The brightening rises and falls in a smooth, symmetric curve. Its length depends mostly on the lens mass: bigger masses make longer events.

Survey telescopes such as OGLE (Poland/Chile), MOA (Japan/New Zealand) and KMTNet (Korea, with telescopes in Chile, South Africa and Australia) watch hundreds of millions of stars toward the center of the Milky Way, where the chance of an alignment is highest. They now take images every few minutes to every quarter-hour, which is fast enough to catch events lasting less than a day.

The shortest events, lasting hours, point to Earth-mass or smaller lenses with no star nearby. Because the planet makes no light, these events are a direct census of the dark, wandering planets of the galaxy. NASA's Nancy Grace Roman Space Telescope (launch targeted for 30 August 2026; see NASA for current mission status) is designed to find many more from space.

## What we already know

- 🟢 **Level 1 — Confirmed.** Microlensing by stars and planets is well established (Paczyński 1986 introduced the modern method for the Milky Way).
- 🟢 **Level 1 — Confirmed.** OGLE-2016-BLG-1928 had an Einstein timescale of about 41.5 minutes, the shortest known. It is one of the best candidates for a terrestrial-mass rogue planet (Mróz et al. 2020).
- 🔵 **Level 2 — Strong evidence.** An earlier claim that Jupiter-mass free-floating planets are about twice as common as stars (Sumi et al. 2011) was not supported by a larger OGLE sample (Mróz et al. 2017), a good example of science correcting itself.
- 🔵 **Level 2 — Strong evidence.** Analysis of nine years of MOA-II data suggests roughly 21 (+23/−13) free-floating or very wide-orbit planets per star in the mass range from about one-third of Earth's mass up to many Jupiter masses, with most of them small (Sumi et al. 2023). The uncertainty is large.
- 🔵 **Level 2 — Strong evidence.** Simulations predict Roman will detect hundreds of free-floating planets, down to roughly Mars mass (Johnson et al. 2020).

## What is still open

**How common are Earth-mass and smaller planets drifting between the stars, and how many short events already in survey archives have not yet been fully analyzed?**

Short events have few data points, so they are easy to confuse with stellar flares, variable stars, moving asteroids, or instrument problems. Careful, consistent reanalysis of archival short events — especially using multiple colors of light — is a testable way to refine the numbers.

## How you could test it

1. **Get the data.** OGLE, MOA and KMTNet publish event lists and light curves (see [data sources](../about/data-sources.md)).
2. **Fit a standard microlensing curve** (the Paczyński curve) to each short event to measure the Einstein timescale *t*<sub>E</sub>.
3. **Check color.** Lensing affects all colors of light the same way. Compare brightening in two filters; a real lensing event should show the same magnification in both.
4. **Check symmetry and shape.** Flares rise fast and fade slowly. Lensing is symmetric (unless the source star's size matters, which leaves a recognizable flattened peak).
5. **Rule out asteroids.** Check whether a known asteroid passed through that position at that time.
6. **Compare with published catalogs** to see whether the event is already known.

## How we could be wrong

- **Stellar flares** from faint M dwarfs are short and bright, but they are blue and asymmetric.
- **Asteroids** in the ecliptic can cross survey fields and mimic short brightening of a blended star.
- **Cosmic rays and detector artifacts** usually affect only one image.
- **Wide-orbit planets.** A planet far from its star (say, more than 10 au) can look free-floating if the star's own lensing effect is too weak to see. Later high-resolution imaging can find the host star.
- **A clear "no" result.** If the two-color magnifications disagree, or the curve is clearly asymmetric, the event is not lensing.

## For experts

**Einstein radius and timescale.**

$$ \theta_E = \sqrt{\kappa\,M\,\pi_{\rm rel}}, \quad \kappa = \frac{4G}{c^2\,\mathrm{au}} \approx 8.144\ \mathrm{mas}\,M_\odot^{-1}, \quad \pi_{\rm rel} = \mathrm{au}\left(\frac{1}{D_L}-\frac{1}{D_S}\right), $$

$$ t_E = \frac{\theta_E}{\mu_{\rm rel}}. $$

For *M* = 1 M⊕ (3.0 × 10⁻⁶ M⊙), *D*<sub>L</sub> = 4 kpc, *D*<sub>S</sub> = 8 kpc (π<sub>rel</sub> = 0.125 mas) and μ<sub>rel</sub> = 5 mas yr⁻¹: θ<sub>E</sub> ≈ 1.7 μas and *t*<sub>E</sub> ≈ 3 hours. A Jupiter mass gives about 2 days; a 0.3 M⊙ star about 40 days. *t*<sub>E</sub> ∝ √*M*.

**Point-source, point-lens magnification (Paczyński curve).**

$$ A(u) = \frac{u^2+2}{u\sqrt{u^2+4}}, \qquad u(t) = \sqrt{u_0^2 + \left(\frac{t-t_0}{t_E}\right)^2}. $$

**Finite-source effects.** For small θ<sub>E</sub>, the source angular radius θ<sub>⋆</sub> can exceed θ<sub>E</sub>, flattening the peak. Measuring ρ = θ<sub>⋆</sub>/θ<sub>E</sub> gives θ<sub>E</sub> directly (with θ<sub>⋆</sub> from the source color and brightness), which breaks part of the mass–distance degeneracy.

**Achromaticity.** Point-lens magnification is wavelength-independent; with finite-source effects, limb darkening introduces weak chromaticity at the peak. Blending with unrelated stars changes the *observed* amplitude per band, so fit source and blend fluxes separately in each band before comparing.

The project's code module `fdastro.microlensing` provides the Einstein radius, timescale and magnification curve.

## Try it

- Tutorial: [Microlensing timescales](../tutorials/t10-microlensing-timescales.md)
- Lesson: [A space magnifying glass](../lessons/l10-space-magnifying-glass.md)
- Code module: `fdastro.microlensing`
- Reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Johnson, S. A. et al. (2020). Predictions of the Nancy Grace Roman Space Telescope Galactic Exoplanet Survey. II. Free-floating planet detection rates. *The Astronomical Journal* 160, 123.
- Mróz, P. et al. (2017). No large population of unbound or wide-orbit Jupiter-mass planets. *Nature* 548, 183.
- Mróz, P. et al. (2020). A terrestrial-mass rogue planet candidate detected in the shortest-timescale microlensing event. *The Astrophysical Journal Letters* 903, L11. doi:10.3847/2041-8213/abbfad
- Paczyński, B. (1986). Gravitational microlensing by the galactic halo. *The Astrophysical Journal* 304, 1.
- Sumi, T. et al. (2011). Unbound or distant planetary mass population detected by gravitational microlensing. *Nature* 473, 349.
- Sumi, T. et al. (2023). Free-floating planet mass function from MOA-II 9-year survey toward the Galactic bulge. *The Astronomical Journal* 166, 108. doi:10.3847/1538-3881/ace688
