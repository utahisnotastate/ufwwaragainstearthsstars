# D12 — Exomoons from timing and duration wobbles

> **In one sentence:** A moon makes its planet wobble, so the planet crosses its star a little early or late and a little faster or slower — and for a moon, those two wobbles follow a special pattern that astronomers can test.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (finding exomoons with this timing pattern in archival data). No exomoon has yet been confirmed; the two best-known candidates are 🔵 **Level 2 — Strong evidence, disputed**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine a runner going around a track at night, carrying a lantern. Now imagine the runner is holding hands with a child, and they spin around each other while they run. Sometimes the child swings ahead and pulls the runner across the finish line a little early. Sometimes the child swings behind and the runner is a little late. And when the child swings to the side, the runner moves a bit faster or slower as they cross the line.

A planet with a big moon does the same thing. The planet and moon spin around each other while they orbit the star. So the planet's **transit** (its little shadow crossing the star) can come early or late, and can last a bit longer or shorter. For a moon, the "early-or-late" wobble and the "faster-or-slower" wobble are a quarter-turn out of step. If you draw one wobble against the other, you get a loop! That loop is a clue that a moon might be there.

## The big idea

Exoplanets are planets around other stars. **Exomoons** would be moons around those planets. None has been confirmed yet, but our own Solar System has hundreds of moons, so astronomers expect them to be common.

A moon is usually too small to see directly in a transit light curve. But the planet and moon orbit their shared center of mass (the barycenter). This moves the planet back and forth along its path and changes its speed:

- **Transit Timing Variations (TTVs):** the transit happens early or late because the planet is ahead of or behind the barycenter.
- **Transit Duration Variations (TDVs):** the transit lasts longer or shorter because the planet moves slower or faster as it crosses the star.

Kipping (2009) showed that for a moon, the TTV depends on the planet's *position* around the barycenter and the main TDV part depends on its *velocity*. Position and velocity in a circular orbit are 90° out of phase. So TTV and TDV should be 90° out of phase, too. Other causes of TTVs, such as another planet, usually do not produce this exact relationship.

For a sense of scale: if aliens watched Earth transit the Sun, our Moon would shift Earth's transit times by up to about 2.6 minutes.

## What we already know

- 🟢 **Level 1 — Confirmed.** A moon induces TTVs in its host planet (Sartoretti & Schneider 1999), and the velocity-induced TDV is 90° out of phase with the TTV (Kipping 2009a, 2009b).
- 🟢 **Level 1 — Confirmed.** Catalogs of Kepler transit times and durations exist for thousands of planets (Holczer et al. 2016).
- 🔵 **Level 2 — Strong evidence, disputed.** Kepler-1625 b-i was proposed as a large exomoon using Kepler and Hubble data (Teachey & Kipping 2018). Kepler-1708 b-i was proposed from a survey of 70 cool giant planets (Kipping et al. 2022).
- 🔵 **Level 2 — Strong evidence, disputed.** A reanalysis using a full photodynamical model concluded that large exomoons are unlikely around both planets, suggesting the signals may come from modeling choices and stellar activity (Heller & Hippke 2024). The debate shows how hard exomoon detection is.

## What is still open

**Do any known transiting planets show TTV and TDV signals with the same frequency and a 90° phase difference, at a significance that survives a careful false-alarm analysis?**

## How you could test it

1. **Start with planets that have many transits** and good timing, for example from the Holczer et al. (2016) Kepler catalog or from TESS.
2. **Measure each transit's time and duration** with uncertainties.
3. **Search for a common frequency.** Because a moon orbits faster than once per planet orbit, its signal is sampled only once per transit and appears at an "alias" frequency. Search a grid of trial frequencies.
4. **Fit sine waves** to TTVs and TDVs at that frequency and measure the phase difference.
5. **Estimate the false-alarm probability** by shuffling the data or simulating noise many times, and correct for the number of planets and frequencies tried.
6. **Check against other explanations**, such as additional planets, starspots and stellar activity.
7. **Follow up** strong candidates with full photodynamical models.

## How we could be wrong

- **TDVs are noisy.** Durations are much harder to measure than times. Small errors can create fake phase relationships.
- **Starspots.** A planet crossing a spot changes the transit shape, which shifts measured times and durations.
- **Other planets.** Planet–planet interactions produce TTVs and can produce TDVs, sometimes with phase offsets.
- **An extra moon term.** If the moon's orbit is tilted, a second TDV component appears that is in phase with the TTV (Kipping 2009b), changing the expected phase.
- **A clear "no" result.** If no significant common-frequency signal appears, or the phase is far from 90° with small uncertainty, a single moon is ruled out as the cause.

## For experts

**Barycentric displacement.** For a planet of mass *M*<sub>p</sub> and moon of mass *M*<sub>s</sub> at separation *a*<sub>s</sub>, the planet's distance from the planet–moon barycenter is

$$ a_{p,\rm bary} = a_s\,\frac{M_s}{M_p+M_s}. $$

The maximum timing shift is about *a*<sub>p,bary</sub>/*v*<sub>p</sub>, where *v*<sub>p</sub> = 2π*a*<sub>p</sub>/*P*<sub>p</sub>. For the Earth–Moon system, *a*<sub>p,bary</sub> ≈ 4,670 km and *v*<sub>p</sub> ≈ 29.8 km s⁻¹, giving ≈ 157 s.

**Phase relation (circular, coplanar moon orbit).**

$$ \mathrm{TTV}_k \propto \sin(\omega_s t_k + \phi_0), \qquad \mathrm{TDV\text{-}V}_k \propto \cos(\omega_s t_k + \phi_0), $$

so the two series trace an ellipse in the (TTV, TDV) plane. Sampling at transit epochs *t*<sub>k</sub> = *t*₀ + *k P*<sub>p</sub> aliases ω<sub>s</sub> to a frequency in [0, π/*P*<sub>p</sub>]. Aliasing applies equally to both series, so the 90° offset is preserved, although its sign depends on the alias branch.

**Recommended test.** For each trial alias frequency ν, fit TTV<sub>k</sub> = *A* sin(2πν*k*) + *B* cos(2πν*k*) and the same for TDV with weights 1/σ². Compute the phase difference and its uncertainty from the covariance, and the joint power. Calibrate the false-alarm probability by permuting epochs or by bootstrap resampling of residuals, then apply a trials correction over ν and the number of targets.

**Hill stability.** Prograde moons are stable only within roughly half the planet's Hill radius, which bounds *a*<sub>s</sub> and the moon's orbital frequency.

The project's code module `fdastro.exomoon` provides a common-frequency TTV–TDV phase test; see the tutorial for current functions and how false alarms are estimated.

## Try it

- Tutorial: [Exomoon timing test](../tutorials/t08-exomoon-timing-test.md)
- Lesson: [Moons that make planets wobble](../lessons/l11-moons-that-make-planets-wobble.md)
- Code module: `fdastro.exomoon`
- Reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Heller, R. & Hippke, M. (2024). Large exomoons unlikely around Kepler-1625 b and Kepler-1708 b. *Nature Astronomy* 8, 193.
- Holczer, T. et al. (2016). Transit timing observations from Kepler. IX. Catalog of the full long-cadence data set. *The Astrophysical Journal Supplement Series* 225, 9.
- Kipping, D. M. (2009a). Transit timing effects due to an exomoon. *Monthly Notices of the Royal Astronomical Society* 392, 181.
- Kipping, D. M. (2009b). Transit timing effects due to an exomoon – II. *Monthly Notices of the Royal Astronomical Society* 396, 1797.
- Kipping, D. et al. (2022). An exomoon survey of 70 cool giant exoplanets and the new candidate Kepler-1708 b-i. *Nature Astronomy* 6, 367.
- Sartoretti, P. & Schneider, J. (1999). On the detection of satellites of extrasolar planets with the method of transits. *Astronomy & Astrophysics Supplement Series* 134, 553.
- Teachey, A. & Kipping, D. M. (2018). Evidence for a large exomoon orbiting Kepler-1625b. *Science Advances* 4, eaav1784.
