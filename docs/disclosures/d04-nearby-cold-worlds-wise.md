# D04 — Cold, dark neighbors in infrared sky maps

> **In one sentence:** Cold brown dwarfs and free-floating planets near the Sun glow faintly in infrared light and move quickly across the sky, so the right search through NASA's WISE and NEOWISE images can still turn up new neighbors.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (more nearby cold objects remain to be found). Finding such objects this way is 🟢 **Level 1 — Confirmed**. An undiscovered brown dwarf *closer than Proxima Centauri* is 🟠 **Level 4 — Long shot**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine taking two photos of a racetrack, six months apart. Cars parked far away in the parking lot barely move between the photos. But a racecar zooming right past you jumps from one side of the picture to the other!

Objects close to the Sun do something like that racecar. They seem to move a lot across the sky, and they also wiggle back and forth each year as Earth goes around the Sun. Some of these nearby objects are **brown dwarfs**. A brown dwarf is bigger than a planet but too small to shine like a star. Cold ones are darker than a chocolate bar in visible light, but they glow in **infrared** light, which we feel as heat. A NASA space telescope called WISE took infrared pictures of the whole sky again and again for more than ten years. People are still finding new cold neighbors hiding in those pictures — including kids and families who volunteer online!

## The big idea

NASA's Wide-field Infrared Survey Explorer (WISE) mapped the whole sky in infrared light starting in 2010. Its later mission, NEOWISE, kept scanning the sky about every six months until August 2024. That gives more than a decade of repeated pictures.

Very cold brown dwarfs (and planet-mass objects that float alone in space) are faint at the short infrared wavelength of WISE's W1 band (3.4 micrometers) but brighter in the W2 band (4.6 micrometers). This makes them look very "red" in WISE data.

Nearby objects have two kinds of motion on the sky. **Proper motion** is their steady drift as they travel through space. **Parallax** is a yearly back-and-forth wobble caused by Earth's own orbit. The closer an object is, the larger both motions are. These large motions are a powerful clue — but they can also make an object harder to match from one picture to the next. Special catalogs and citizen-science projects were created to find exactly these fast-moving objects.

## What we already know

- 🟢 **Level 1 — Confirmed.** **WISE J085510.83−071442.5** (WISE 0855−0714), the coldest known brown dwarf, was found in 2014 from its large motion in WISE data. It lies about 2.3 parsecs (about 7.4 light-years) away (Luhman 2014b).
- 🟢 **Level 1 — Confirmed.** **Luhman 16 AB**, a pair of brown dwarfs only about 2.0 parsecs away, was discovered in WISE data in 2013, even though it is one of the Sun's closest neighbors (Luhman 2013).
- 🟢 **Level 1 — Confirmed.** The **Backyard Worlds: Planet 9** citizen-science project lets volunteers flip through WISE images to spot moving objects. Volunteers have found many new brown dwarfs, including some of the coldest known (Kuchner et al. 2017; Meisner et al. 2020).
- 🟢 **Level 1 — Confirmed.** Motion-aware catalogs such as CatWISE2020 and the "unTimely" time-domain catalog were built to measure fast motions across many WISE epochs (Marocco et al. 2021; Meisner et al. 2023).
- 🟢 **Level 1 — Confirmed.** A WISE search for a distant companion to the Sun found none brighter than W2 = 14.5. Using planet models, this rules out a Saturn-like body within about 28,000 au, and a Jupiter-mass brown dwarf within about 26,000 au (Luhman 2014a).
- 🔵 **Level 2 — Strong evidence.** The census of L, T and Y dwarfs within 20 parsecs is now fairly complete for warmer types but still incomplete for the coldest Y dwarfs (Kirkpatrick et al. 2021).

## What is still open

**Are there still undiscovered cold brown dwarfs or free-floating planetary-mass objects within about 20 parsecs that appear in WISE/NEOWISE data but are not yet in any catalog?**

The most likely places for them to hide are crowded regions near the Milky Way's plane, where many background stars confuse the images, and among the faintest, coldest objects near the detection limit.

**What about objects closer than Proxima Centauri (1.3 parsecs)?** A brown dwarf that close and as warm as WISE 0855 would be brighter than WISE's limit and very likely already found, given the searches above. Much colder, smaller planet-mass bodies that close would be too faint for WISE. So this idea is a 🟠 **Level 4 — Long shot** for WISE data.

## How you could test it

1. **Join Backyard Worlds** (on Zooniverse) — the easiest way to start.
2. **Query the catalogs.** Use the NASA/IPAC Infrared Science Archive (IRSA) to select sources with very red W1 − W2 colors and large catalog motions from CatWISE2020 or unTimely.
3. **Link detections across epochs.** For candidates without a good catalog motion, collect single-epoch detections near the position and fit a model with position, proper motion and parallax (five parameters).
4. **Check the fit.** A real nearby object follows the parallax ellipse predicted from Earth's orbit. Random noise does not.
5. **Cross-check other surveys.** Look in Gaia, 2MASS, Pan-STARRS, the Legacy Surveys and Spitzer archives for the same moving object.
6. **Report** strong candidates to Backyard Worlds' science team for spectroscopic follow-up.

## How we could be wrong

- **Artifacts.** Bright-star halos, diffraction spikes, latent images and cosmic rays can look like red, moving sources.
- **Mismatched pairs.** Linking unrelated detections can produce a fake "motion". Require many epochs that all fit one parallax-plus-motion solution.
- **Background galaxies or quasars.** Some are red in WISE colors but do not move.
- **A clear "no" result.** If the five-parameter fit has no significant parallax, or other surveys show the source does not move, it is not a nearby object.

## For experts

**Astrometric model.** For epochs *t* and observer barycentric position **R**(*t*) = (*X*, *Y*, *Z*) in au (equatorial), the offsets from a reference position (α₀, δ₀) are

$$ \Delta\alpha^*(t) = \Delta\alpha^*_0 + \mu_{\alpha^*}(t-t_0) + \varpi\,\Pi_\alpha(t), $$
$$ \Delta\delta(t) = \Delta\delta_0 + \mu_\delta(t-t_0) + \varpi\,\Pi_\delta(t), $$

with parallax factors

$$ \Pi_\alpha = X\sin\alpha - Y\cos\alpha, \qquad \Pi_\delta = X\cos\alpha\sin\delta + Y\sin\alpha\sin\delta - Z\cos\delta. $$

This is linear in the five unknowns and can be solved by weighted least squares.

**Typical sizes.** At distance *d* (pc), ϖ = 1/*d* arcsec. Tangential velocity *v*<sub>t</sub> = 4.74 μ *d* km s⁻¹ (μ in arcsec yr⁻¹). At 2 pc, ϖ = 0.5″ and a 25 km s⁻¹ object moves about 2.6″ yr⁻¹. WISE 0855 moves about 8″ yr⁻¹. The WISE W2 beam is about 6″ wide, so fast movers shift by a large fraction of a beam between visits roughly six months apart.

**Colors.** Late T and Y dwarfs have W1 − W2 colors that grow redder with lower temperature, roughly 2 or more for late T dwarfs and about 3 or more for Y dwarfs (Kirkpatrick et al. 2021). Many Y dwarfs are undetected in W1.

**Statistics.** When linking candidate detections, the number of possible combinations grows quickly. Estimate the false-link rate with simulations using random detections at the real source density.

The project's code module `fdastro.astrometry` provides the five-parameter fit and parallax factors.

## Try it

- Tutorial: [Parallax and proper motion](../tutorials/t06-parallax-and-proper-motion.md)
- Lesson: [Thumb parallax](../lessons/l03-thumb-parallax.md)
- Code module: `fdastro.astrometry`
- Data: [data sources](../about/data-sources.md); reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Kirkpatrick, J. D. et al. (2021). The field substellar mass function based on the full-sky 20 pc census of 525 L, T, and Y dwarfs. *The Astrophysical Journal Supplement Series* 253, 7.
- Kuchner, M. J. et al. (2017). The first brown dwarf discovered by the Backyard Worlds: Planet 9 citizen science project. *The Astrophysical Journal Letters* 841, L19.
- Luhman, K. L. (2013). Discovery of a binary brown dwarf at 2 pc from the Sun. *The Astrophysical Journal Letters* 767, L1.
- Luhman, K. L. (2014a). A search for a distant companion to the Sun with the Wide-field Infrared Survey Explorer. *The Astrophysical Journal* 781, 4.
- Luhman, K. L. (2014b). Discovery of a ~250 K brown dwarf at 2 pc from the Sun. *The Astrophysical Journal Letters* 786, L18.
- Marocco, F. et al. (2021). The CatWISE2020 catalog. *The Astrophysical Journal Supplement Series* 253, 8.
- Meisner, A. M. et al. (2020). Spitzer follow-up of extremely cold brown dwarfs discovered by the Backyard Worlds: Planet 9 citizen science project. *The Astrophysical Journal* 889, 74.
- Meisner, A. M. et al. (2023). unTimely: a full-sky, time-domain unWISE catalog. *The Astronomical Journal* 165, 36.
