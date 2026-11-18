# D03 — Planets seen only once

> **In one sentence:** Planets with long orbits may cross in front of their star only once while a telescope is watching, so searches built to find repeating dips can miss them — but a single, well-shaped dip still carries a lot of information.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (how many such planets remain in the archives). Single-transit planets themselves are 🟢 **Level 1 — Confirmed**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine a security camera that only sounds an alarm if a person walks past three times in a row. A big truck drives past once and leaves. The camera says, "Only once? That doesn't count." But the truck was real!

Space telescopes watch stars for small dips in light. A dip happens when a planet passes in front of its star. Planets close to their star pass in front every few days, so the dips repeat many times. But planets far from their star, like Jupiter is from our Sun, take years to go around. A telescope that watches a star for one month may see only one dip. That one dip can still tell us a planet is there — and even roughly how far from its star it is.

## The big idea

TESS (the Transiting Exoplanet Survey Satellite) watches most patches of sky for about 27 days at a time. Kepler watched one patch for four years. A planet with an orbit longer than the observing window can show just one transit. Astronomers call this a **single transit** or **monotransit**.

Standard search methods, such as Box Least Squares (BLS) and Transit Least Squares (TLS), work by folding the light curve at many trial periods and adding up repeated dips. This is very powerful for short-period planets. But by design, folding needs at least two events. NASA's main TESS pipeline (the Science Processing Operations Center, SPOC) also requires at least two transits before it reports a detection. This is a sensible choice: one dip is much easier to fake with noise or instrument problems.

So single transits are mostly found by dedicated searches: special algorithms, careful human inspection, and citizen scientists. These planets matter because they are colder, more like the giant planets in our own Solar System, and they are rare in current catalogs.

## What we already know

- 🟢 **Level 1 — Confirmed.** Single-transit events have been found in Kepler, K2 and TESS data, and some have been confirmed as planets after follow-up (for example, Osborn et al. 2016; Foreman-Mackey et al. 2016).
- 🟢 **Level 1 — Confirmed.** Citizen scientists in the Planet Hunters TESS project have found many long-period and single-transit candidates that automated pipelines did not report (Eisner et al. 2021).
- 🔵 **Level 2 — Strong evidence.** Simulations predict that TESS should record a large number of single-transit events from planets with periods longer than the observing window (Villanueva, Dragomir & Gaudi 2019).
- 🟢 **Level 1 — Confirmed.** The shape and length of a single transit, combined with the star's density, give a rough estimate of the orbital period (Seager & Mallén-Ornelas 2003).

## What is still open

**How many long-period planets show only one transit in TESS and Kepler data, and how many of them can be recovered with follow-up?**

TESS has now re-observed much of the sky in later years. A planet seen once in 2019 may have been seen once more in a later sector. Pairing these "orphan" single transits across years is a promising and testable way to recover periods.

## How you could test it

1. **Download light curves** for a set of bright stars from MAST, using the `lightkurve` Python package.
2. **Remove slow brightness changes** from the star itself with a gentle filter that does not erase transit-length dips.
3. **Search for single dips** using a matched filter (slide a box-shaped template along the light curve and measure the signal-to-noise ratio at each position).
4. **Vet each event.** Check that the dip is symmetric, has a plausible depth and duration for a planet, does not coincide with a spacecraft event (such as a momentum dump), and does not appear in nearby stars' light curves.
5. **Estimate the period** from the duration and the star's density.
6. **Look for a second event** in other TESS sectors or other surveys at the predicted times.
7. **Report** strong candidates through ExoFOP-TESS or to Planet Hunters TESS so that professionals can follow up.

## How we could be wrong

- **Eclipsing binary stars.** A faint background pair of stars can make a planet-like dip. Check the centroid (where the light comes from) during the event.
- **Instrument events.** Momentum dumps, scattered light and pointing jitter can make single dips. Compare with the spacecraft quality flags.
- **Stellar activity.** Some stars dim briefly for other reasons.
- **Detrending damage.** Filtering too aggressively can make a real dip disappear; too gently, and noise can look like a dip. Always test with injected fake transits.
- **A clear "no" result.** If follow-up observations at the predicted times show no second transit over the allowed period range, or if radial-velocity data rule out a planet of the needed mass, the candidate fails.

## For experts

**Matched-filter detection.** For a box of duration *D* and depth δ in white noise of per-point scatter σ with *N*<sub>in</sub> in-transit points,

$$ \mathrm{SNR} \approx \frac{\delta}{\sigma}\sqrt{N_{\rm in}}. $$

Use a robust noise estimate (1.4826 × median absolute deviation) and account for correlated (red) noise, for example with the "time-averaged" noise σ<sub>r</sub> at the transit timescale.

**Period from a single transit.** For a circular orbit, the stellar density ρ<sub>⋆</sub> links duration and period:

$$ \frac{a}{R_\star} = \left(\frac{G\rho_\star P^2}{3\pi}\right)^{1/3}, \qquad T_{14} \approx \frac{P}{\pi}\frac{R_\star}{a}\sqrt{(1+k)^2-b^2}. $$

With ρ<sub>⋆</sub> from Gaia-based stellar parameters and the measured *T*₁₄, *k* and *b* (which is degenerate with *P* for low signal-to-noise events), this gives a posterior on *P*. Eccentricity broadens the posterior considerably.

**Duotransits.** When a second transit is found years later, the allowed periods form a discrete set *P* = Δ*t*/*n*. Non-detections in other sectors remove many aliases. Targeted photometry (for example CHEOPS or ground-based networks) or radial velocities can select the right alias.

**Statistics.** A blind search over many stars and positions must correct for the number of independent trials. Injection–recovery tests give both completeness and false-alarm rates.

The project's code module `fdastro.transits` provides tools for single-event searches; see the tutorial for current functions.

## Try it

- Tutorial: [Single and fading transits](../tutorials/t07-single-and-fading-transits.md)
- Lesson: [Shadows on a star](../lessons/l02-shadows-on-a-star.md)
- Code module: `fdastro.transits`
- Related: [D02 — Planets whose transits fade away](d02-vanishing-transits.md)
- Data: [data sources](../about/data-sources.md); reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Eisner, N. L. et al. (2021). Planet Hunters TESS II: findings from the first two years of TESS. *Monthly Notices of the Royal Astronomical Society* 501, 4669.
- Foreman-Mackey, D. et al. (2016). The population of long-period transiting exoplanets. *The Astronomical Journal* 152, 206.
- Hippke, M. & Heller, R. (2019). Optimized transit detection algorithm to search for periodic transits of small planets. *Astronomy & Astrophysics* 623, A39.
- Jenkins, J. M. et al. (2016). The TESS science processing operations center. *Proceedings of the SPIE* 9913.
- Kovács, G., Zucker, S. & Mazeh, T. (2002). A box-fitting algorithm in the search for periodic transits. *Astronomy & Astrophysics* 391, 369.
- Osborn, H. P. et al. (2016). Single transit candidates from K2: detection and period estimation. *Monthly Notices of the Royal Astronomical Society* 457, 2273.
- Seager, S. & Mallén-Ornelas, G. (2003). A unique solution of planet and star parameters from an extrasolar planet transit light curve. *The Astrophysical Journal* 585, 1038.
- Villanueva, S., Dragomir, D. & Gaudi, B. S. (2019). An estimate of the yield of single-transit planetary events from the Transiting Exoplanet Survey Satellite. *The Astronomical Journal* 157, 84.
