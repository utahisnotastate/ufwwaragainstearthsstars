# D14 — Interstellar visitors in unlinked asteroid data

> **In one sentence:** Objects from other star systems sometimes fly through our Solar System on open, curved paths, and some of their telescope sightings may be sitting in public files of observations that have never been connected together.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (interstellar objects hidden in unlinked observations). Interstellar objects themselves are 🟢 **Level 1 — Confirmed** (three known as of November 2026).
>
> *Last reviewed: November 2026.*

## For young readers

Picture a merry-go-round in a park. The wooden horses go around and around in slow circles. A camera is set up to follow them. Now imagine a baseball from another neighborhood flies straight across the park. The camera takes a few quick pictures of it. But the computer expects everything to go in circles, so it has a hard time joining the baseball's dots together.

Asteroids and comets in our Solar System travel around the Sun in closed loops called ellipses. But a few visitors come from other stars! They swoop past the Sun on an open path called a **hyperbola** and then leave forever. We know of three so far: **ʻOumuamua** (2017), **Borisov** (2019) and **3I/ATLAS** (2025). Telescopes take millions of pictures of moving dots. Some dots have never been matched up into paths. A few of them might belong to visitors from other stars.

## The big idea

Every night, survey telescopes record moving points of light. A few detections of the same object on one night form a **tracklet**. To find an orbit, software must link tracklets from different nights. This is a huge puzzle: there are vast numbers of tracklets and many possible combinations.

The Minor Planet Center (MPC), the international clearinghouse for asteroid and comet observations, keeps observations that have not yet been linked to any known object in the **Isolated Tracklet File (ITF)**. It is public. In 2018, a new method called **HelioLinC** linked ITF tracklets into orbits for about 41,000 new minor planets (Holman et al. 2018). That showed the ITF holds real discoveries waiting to be connected.

Interstellar objects (ISOs) are special. They move fast, often at steep angles to the planets' orbits, and their paths are open hyperbolas instead of closed ellipses. Linking methods make assumptions to keep the search manageable — for example, about an object's distance from the Sun or how that distance changes. Fast or unusual paths can fall outside the assumptions a particular search used, which can make them harder to link. Not every method assumes a closed orbit, so this is a question to test, not a known flaw.

There is good reason to look: after 3I/ATLAS was discovered on 1 July 2025, astronomers found it in older images from other telescopes taken weeks earlier, before anyone knew what it was.

## What we already know

- 🟢 **Level 1 — Confirmed.** **1I/ʻOumuamua**, found by Pan-STARRS in October 2017, was the first known interstellar object: eccentricity *e* ≈ 1.20 and speed far from the Sun (*v*<sub>∞</sub>) ≈ 26 km/s (Meech et al. 2017). It showed a small non-gravitational acceleration, most likely from outgassing (Micheli et al. 2018).
- 🟢 **Level 1 — Confirmed.** **2I/Borisov**, discovered in August 2019 by amateur astronomer Gennadiy Borisov, was an active comet with *e* ≈ 3.36 and *v*<sub>∞</sub> ≈ 32 km/s (Guzik et al. 2020).
- 🟢 **Level 1 — Confirmed.** **3I/ATLAS** (C/2025 N1), discovered by the ATLAS survey on 1 July 2025, has *e* ≈ 6.1, *v*<sub>∞</sub> ≈ 58 km/s, and an almost fully retrograde orbit (inclination ≈ 175°) (Seligman et al. 2025).
- 🟢 **Level 1 — Confirmed.** 3I/ATLAS appears in archived TESS images from May–June 2025 and in Zwicky Transient Facility images from June 2025, before its discovery (Feinstein, Noonan & Seligman 2025; Seligman et al. 2025).
- 🟢 **Level 1 — Confirmed.** HelioLinC linked MPC Isolated Tracklet File data into orbits for about 41,000 new minor planets (Holman et al. 2018, arXiv:1805.02638). Rubin Observatory uses an evolved version for its own linking.
- 🔵 **Level 2 — Strong evidence.** Predictions for how many ISOs Rubin will find range from about one per year to dozens per year, depending on assumptions about their sizes and brightness (Hoover et al. 2022; Marčeta & Seligman 2023).

## What is still open

**Are any interstellar objects sitting unrecognized among the unlinked observations in the MPC Isolated Tracklet File or in other survey archives?**

## How you could test it

1. **Download the ITF** from the Minor Planet Center (`itf.txt.gz`). It uses the MPC's 80-column observation format.
2. **Group observations into tracklets** by their temporary designation.
3. **Pre-select fast or unusual tracklets**, for example those with high sky motion or at high ecliptic latitude.
4. **Link tracklets across nights** using hypotheses that include unbound (hyperbolic) motion.
5. **Fit a full orbit** to each linked set with an exact two-body model, light-travel-time correction and the observatory's position on Earth.
6. **Test whether a closed orbit can fit.** Compare the best fit allowing any orbit with the best fit forced to stay bound. If forcing a bound orbit makes the fit much worse, the object may be interstellar.
7. **Check precoveries and recoveries** in other archives, then report to the MPC.

## How we could be wrong

- **Short arcs mislead.** With only a few days of data, distance and speed are poorly known, and a bound orbit can look hyperbolic (or the reverse). This is the biggest source of false ISO claims.
- **Mislinked tracklets.** Joining observations of different asteroids can produce a fake, wildly hyperbolic orbit.
- **Comets.** Ordinary long-period comets have orbits very close to *e* = 1. Gas jets push on them, which can make a bound orbit look slightly hyperbolic. A true ISO usually has *e* clearly greater than 1 and a large *v*<sub>∞</sub>.
- **Timing and observatory position.** Wrong time scales or ignoring the observer's location on Earth can create big errors for nearby objects.
- **A clear "no" result.** If a bound orbit fits the data as well as an unbound one, there is no evidence that the object is interstellar.

## For experts

**Energy and eccentricity.** With μ = *GM*<sub>⊙</sub>, heliocentric position **r** and velocity **v**,

$$ \mathcal{E} = \frac{v^2}{2} - \frac{\mu}{r}, \qquad e = \sqrt{1 + \frac{2\mathcal{E}h^2}{\mu^2}}, \qquad \mathbf{h} = \mathbf{r}\times\mathbf{v}. $$

Unbound orbits have ℰ > 0, *e* > 1 and *a* = −μ/(2ℰ) < 0. The hyperbolic excess speed is

$$ v_\infty = \sqrt{2\mathcal{E}} = \sqrt{\frac{\mu(e-1)}{q}}, $$

with *q* the perihelion distance. Check: for 3I/ATLAS, *q* ≈ 1.36 au and *e* ≈ 6.1 give *v*<sub>∞</sub> ≈ 58 km s⁻¹.

**Radiant.** The incoming asymptote direction (where the object came from) is opposite to the incoming velocity at infinity, not the current velocity. It can be computed from the orbital elements: the asymptote makes the angle θ<sub>∞</sub> = arccos(−1/*e*) with the perihelion direction.

**Bound-orbit test.** Fit the six-parameter state vector by nonlinear least squares with an exact two-body propagator (universal variables), including light-time iteration and topocentric observer positions. Then refit with the constraint ℰ ≤ 0. The statistic Δχ² = χ²<sub>bound</sub> − χ²<sub>free</sub> follows (asymptotically) a 50:50 mixture of χ²₀ and χ²₁ under the bound hypothesis because the constraint is on a boundary. Report Δχ² and the corresponding significance, along with the range of *e* allowed within Δχ² thresholds (systematic ranging is recommended for arcs of a few nights).

**Linking.** HelioLinC hypothesizes a heliocentric distance *r* and radial velocity *ṙ* for each tracklet, propagates to a common epoch, and clusters in phase space. Grids in (*r*, *ṙ*) that include large |*ṙ*| and short-perihelion geometries are needed to cover typical ISO trajectories.

**Notes on the original script.** The original notes included a script that approximated Earth's position with the wrong angle, propagated orbits with a constant-acceleration step, and reported a "return period" that was not a valid significance. These were replaced in this project with an exact propagator and a proper bound-orbit test.

The project's code modules `fdastro.kepler` (exact two-body orbits and elements), `fdastro.iso` (orbit fitting and the bound-orbit test) and `fdastro.mpc` (reading 80-column observations) support this disclosure; see the tutorials for current functions.

## Try it

- Tutorial: [Orbits, ellipses and hyperbolas](../tutorials/t02-orbits-ellipses-and-hyperbolas.md)
- Tutorial: [Fit an orbit and test if it is bound](../tutorials/t03-fit-an-orbit-and-test-if-bound.md)
- Tutorial: [Reading MPC observations](../tutorials/t04-reading-mpc-observations.md)
- Lessons: [Visitors from other stars](../lessons/l04-visitors-from-other-stars.md), [High school: hyperbolic orbits](../lessons/l12-high-school-hyperbolic-orbits.md), [University lab: orbit fitting](../lessons/l13-university-lab-orbit-fitting.md)
- Code modules: `fdastro.kepler`, `fdastro.iso`, `fdastro.mpc`
- Data: [data sources](../about/data-sources.md); reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Feinstein, A. D., Noonan, J. W. & Seligman, D. Z. (2025). Precovery observations of 3I/ATLAS from TESS suggest possible distant activity. arXiv:2507.21967
- Guzik, P. et al. (2020). Initial characterization of interstellar comet 2I/2019 Q4 (Borisov). *Nature Astronomy* 4, 53.
- Holman, M. J., Payne, M. J., Blankley, P., Janssen, R. & Kuindersma, S. (2018). HelioLinC: a novel approach to the minor planet linking problem (arXiv title: "Finding asteroids down the back of the couch"). *The Astronomical Journal* 156, 135. arXiv:1805.02638
- Hoover, D. J. et al. (2022). [Predicted LSST detection rates of interstellar objects.] *The Planetary Science Journal*. (Bracketed text describes the paper; check ADS for the exact title.)
- Marčeta, D. & Seligman, D. Z. (2023). Synthetic detections of interstellar objects with the Rubin Observatory Legacy Survey of Space and Time. *The Planetary Science Journal*. arXiv:2310.17575
- Meech, K. J. et al. (2017). A brief visit from a red and extremely elongated interstellar asteroid. *Nature* 552, 378.
- Micheli, M. et al. (2018). Non-gravitational acceleration in the trajectory of 1I/2017 U1 (ʻOumuamua). *Nature* 559, 223.
- Minor Planet Center. Isolated Tracklet File (ITF). https://www.minorplanetcenter.net/iau/ITF/itf.txt.gz
- Seligman, D. Z. et al. (2025). Discovery and preliminary characterization of a third interstellar object: 3I/ATLAS. *The Astrophysical Journal Letters* 989, L36. arXiv:2507.02757
