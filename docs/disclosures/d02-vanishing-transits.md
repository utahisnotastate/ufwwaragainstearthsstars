# D02 — Planets whose transits fade away

> **In one sentence:** When a hidden neighbor planet slowly tilts another planet's orbit, that planet's shadow on its star can shrink and then disappear — and the way it fades tells us about the hidden neighbor.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (how many more such systems are in the archives). The effect itself is 🟢 **Level 1 — Confirmed**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine a lighthouse far away at night. Every night at the same time, a moth flies in front of the light. You see a tiny shadow. Then, one year, the shadow starts to get smaller. Soon it is gone!

Did the moth fly away? Maybe not. Maybe a bigger bug you cannot see is flying next to it. The big bug's pull makes the moth's path tilt, like a wobbling hula hoop. Now the moth passes a little above the light, so its shadow misses you.

Planets do this too. A planet that passes in front of its star makes a tiny dip in the star's light. This is called a **transit**. If a hidden planet tilts its orbit, the dips get shallower and shorter, and then they stop. In November 2026, astronomers reported exactly this for a planet called **TOI-2535 b**.

## The big idea

Space telescopes such as Kepler and TESS (the Transiting Exoplanet Survey Satellite) watch hundreds of thousands of stars. When a planet crosses in front of its star, the star's brightness dips by a small, regular amount. Most search software looks for dips that repeat with the same depth and the same length.

But orbits are not frozen. If two planets in a system orbit in different planes, they pull on each other, and the orbits slowly turn, or **precess**, like a spinning top. Seen from Earth, the planet's path across the star moves up or down. The transit becomes shorter as the path moves toward the edge of the star. Near the edge, the planet only "grazes" the star, so the dip also becomes shallower. Eventually the planet misses the star entirely — and later, perhaps decades later, it may come back.

This is useful. How fast the transit changes depends on how massive the hidden neighbor is, how far away it is, and how tilted its orbit is. So a fading transit is a clue to a planet we cannot see directly.

## What we already know

- 🟢 **Level 1 — Confirmed.** **TOI-2535 b**, a hot Jupiter (a giant planet very close to its star) about 1,000 light-years away, was watched by TESS from April 2019 to March 2026. Its transits grew shorter and shallower and were absent by March 2026. The authors attribute this to precession driven by an unseen neighbor that is likely at least Saturn-sized, and they estimate transits may return in roughly 30–50 years (Yee et al. 2026).
- 🟢 **Level 1 — Confirmed.** **Kepler-13Ab** shows a slowly changing transit shape and duration because its orbit is tilted relative to its rapidly spinning, flattened star and precesses over time (Szabó et al. 2014; Masuda 2015; Herman et al. 2018). Combined Kepler and TESS data show the change continuing (Szabó et al. 2020).
- 🟢 **Level 1 — Confirmed.** **Kepler-108** has two Saturn-mass planets whose transit durations and depths change. Mills & Fabrycky (2017) used this to measure a mutual inclination of about 24° (+11°/−8°) between the two orbits.
- 🔵 **Level 2 — Strong evidence.** Catalogs of Kepler transit timing also report changes in duration for some planets (Holczer et al. 2016). Not all of these have been explained.

## What is still open

**How many more planets in Kepler and TESS data have transits that are slowly shrinking because of a hidden, tilted neighbor?**

Most automatic pipelines assume a fixed transit shape. A planet whose depth changes over several years is still found if it transits enough times, but the change itself is not always flagged or studied. A systematic search for monotonic (steadily changing) depth and duration could find new systems with hidden companions.

## How you could test it

1. **Choose targets.** Start with known planets that have long time coverage, such as Kepler planets that TESS later observed again.
2. **Fit each transit separately.** Measure the depth, duration and mid-time of every individual transit, not just the average.
3. **Look for a steady trend.** Fit a straight line (or a physically motivated curve) to depth and duration over time. Check whether the slope is significantly different from zero.
4. **Check that both change together.** A real orbital tilt changes depth and duration in a linked way. Instrument problems usually do not.
5. **Model the neighbor.** If a trend is real, estimate what companion mass and orbit could produce that precession rate.
6. **Ask for follow-up.** Radial-velocity measurements or Gaia astrometry can test whether the predicted companion is there.

Public data: Kepler and TESS light curves from MAST (the Mikulski Archive for Space Telescopes). See [data sources](../about/data-sources.md).

## How we could be wrong

- **Different telescopes, different "dilution".** TESS uses large pixels, so light from nearby stars can blend in. If the blending changes between observing sectors, the transit can look shallower even when nothing changed. Always compare the contamination correction for each sector.
- **Kepler versus TESS differences.** The two telescopes see different colors of light. Stars look darker at their edges (limb darkening) by different amounts in different colors, which changes transit shape slightly.
- **Starspots.** Dark spots on the star can make transits look deeper or shallower.
- **Low signal-to-noise.** Single-transit depths from TESS for small planets are often too noisy to show a trend.
- **A clear "no" result.** If careful per-sector modeling shows constant depth and duration within errors, the precession explanation is ruled out for that target.

## For experts

**Impact parameter.** For a planet with semi-major axis *a*, orbital inclination *i*, eccentricity *e* and argument of periastron ω,

$$ b = \frac{a\cos i}{R_\star}\,\frac{1-e^2}{1+e\sin\omega}. $$

**Transit duration** (circular orbit, total duration):

$$ T_{14} \approx \frac{P}{\pi}\,\frac{R_\star}{a}\,\sqrt{(1+k)^2-b^2}, \qquad k = R_p/R_\star . $$

As *b* → 1 + *k*, *T*₁₄ → 0. For *b* > 1 − *k* the transit is grazing, and the depth falls below *k*² as less of the planet's disk overlaps the star.

**Precession.** Nodal precession of the inner orbit about the system's total angular momentum vector changes *i* (as seen from Earth) over time, so

$$ \frac{db}{dt} = -\frac{a\sin i}{R_\star}\,\frac{di}{dt}. $$

For an outer companion of mass *m*₂ at *a*₂ ≫ *a*₁, the nodal precession rate is approximately

$$ \dot\Omega \approx -\frac{3}{4}\, n_1\,\frac{m_2}{M_\star}\left(\frac{a_1}{a_2}\right)^3 \cos I, $$

where *I* is the mutual inclination and *n*₁ the inner mean motion. For a rapidly rotating star, the stellar quadrupole (*J*₂) term must be added; this dominates for Kepler-13Ab.

**Trend test.** With per-transit depths δ<sub>k</sub> ± σ<sub>k</sub> at times *t*<sub>k</sub>, fit δ = α + β *t* by weighted least squares and report β/σ<sub>β</sub>. Include a jitter term for stellar variability. Repeat for duration. Joint significance should account for the number of targets searched (look-elsewhere effect).

The project's code module `fdastro.transits` provides tools for testing trends in per-transit measurements; see the tutorial for current functions.

## Try it

- Tutorial: [Single and fading transits](../tutorials/t07-single-and-fading-transits.md)
- Lesson: [Shadows on a star](../lessons/l02-shadows-on-a-star.md)
- Code module: `fdastro.transits`
- Related: [D03 — Planets seen only once](d03-single-transit-planets.md), [D13 — Tilted orbits that point to unseen planets](d13-tilted-orbits-hidden-companions.md)
- Found a candidate? [How to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Herman, M. K. et al. (2018). Spin–orbit misalignment and precession in the Kepler-13Ab planetary system. *The Astronomical Journal* 155, 13. doi:10.3847/1538-3881/aa991f
- Holczer, T. et al. (2016). Transit timing observations from Kepler. IX. Catalog of the full long-cadence data set. *The Astrophysical Journal Supplement Series* 225, 9.
- Mills, S. M. & Fabrycky, D. C. (2017). Kepler-108: a mutually inclined giant planet system. *The Astronomical Journal* 153, 45. arXiv:1606.04485
- Masuda, K. (2015). Spin–orbit angles of Kepler-13Ab and HAT-P-7b from gravity-darkened transit light curves. *The Astrophysical Journal* 805, 28.
- Szabó, Gy. M. et al. (2014). Mapping a star with transits: orbit precession effects in the Kepler-13 system. arXiv:1309.2899
- Szabó, Gy. M. et al. (2020). The clockwork is moving on — a combined analysis of TESS and Kepler measurements of Kepler-13Ab. *Monthly Notices of the Royal Astronomical Society Letters*. doi:10.1093/mnrasl/slz177. arXiv:1911.11399
- Yee, S. W., Petigura, E. A. et al. (2026). A TESS disappearing act: the vanishing transits of TOI-2535 b. *The Astrophysical Journal Letters*, published 9 November 2026.
