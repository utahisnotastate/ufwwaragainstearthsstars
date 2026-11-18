# D13 — Tilted orbits that point to unseen planets

> **In one sentence:** Some planets orbit their stars on paths tilted far from the star's equator, and a simple calculation can tell us what kind of hidden outer planet could have tilted them — giving telescopes a place to look.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (tilted inner planets help predict where unseen outer giants are). Tilted orbits themselves are 🟢 **Level 1 — Confirmed**; outer companions explaining some of them are 🔵 **Level 2 — Strong evidence**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine a merry-go-round that is spinning, but it is tipped sideways at a crazy angle. Even if nobody is standing next to it, you would guess that something big pushed it.

Stars spin, too. Most planets in our Solar System orbit close to the Sun's equator, like horses on a flat merry-go-round. But astronomers have found planets around other stars whose orbits are tipped way over — some even go over the star's poles! Something had to tilt them. One good suspect is a big, far-away planet whose gravity slowly tugged on the inner planet's orbit. If we measure the tilt and how the star spins, we can work out what kind of hidden planet could do it, and then search for it.

## The big idea

The angle between a star's spin axis and a planet's orbit is called the **obliquity**. Astronomers measure it during a transit using the **Rossiter–McLaughlin effect**: as the planet crosses the star, it blocks first the side of the star that is spinning toward us (bluer light) and then the side spinning away (redder light). The order and size of this color shift tell us whether the orbit lines up with the star's equator.

Many planets turn out to be misaligned, and some are nearly polar. Several explanations are possible: violent encounters with other planets, slow gravitational nudges from a distant companion, or tilting while the planet-forming disk was still present.

One idea, explored carefully by Petrovich and colleagues (2020), is a **secular resonance**. Two slow "wobble" rates can match: the rate at which the star's slightly flattened shape makes the inner orbit precess, and the rate at which an outer planet makes it precess. When these match — especially while the disk is fading — the inner orbit can be tilted strongly. Matching the rates gives a relationship between the outer planet's mass and distance. That relationship is a **map of where to look**.

## What we already know

- 🟢 **Level 1 — Confirmed.** Many exoplanets have measured obliquities, including some that are strongly misaligned or polar (review: Albrecht, Dawson & Winn 2022).
- 🟢 **Level 1 — Confirmed.** The Neptune-sized planet HAT-P-11 b has a nearly polar orbit (Winn et al. 2010; Sanchis-Ojeda & Winn 2011).
- 🔵 **Level 2 — Strong evidence.** HAT-P-11 c, an eccentric giant planet at about 4 au, was discovered with long-term radial-velocity monitoring and may help explain HAT-P-11 b's tilt (Yee et al. 2018). Later work explored how the system reached its present state.
- 🔵 **Level 2 — Strong evidence.** A disk-driven secular resonance can produce high inclinations of close-in planets, with HAT-P-11 as a proof of concept (Petrovich et al. 2020).
- 🔵 **Level 2 — Strong evidence.** In the π Mensae system, Gaia and Hipparcos astrometry indicate the outer giant planet's orbit is strongly inclined relative to the inner transiting super-Earth (Xuan & Wyatt 2020; De Rosa et al. 2020), and the inner planet's orbit is misaligned with its star's spin (Kunovac Hodžić et al. 2021).
- 🟡 **Level 3 — Testable idea.** Not every misaligned planet needs a present-day outer giant: the tilt may be left over from the past, and tides may be too weak to erase it. Whether a companion exists must be tested system by system.

## What is still open

**For each misaligned planet without a known outer companion, which combinations of companion mass and distance could explain the tilt — and do radial-velocity or Gaia astrometry data already rule them in or out?**

## How you could test it

1. **Collect obliquity measurements** from a catalog such as TEPCat (Southworth 2011) or the literature.
2. **Gather stellar data:** mass, radius, rotation and an estimate of the star's flattening (*J*₂).
3. **Compute the resonance locus** — the line of outer-planet mass versus distance where the two precession rates match (formula below).
4. **Compare with existing limits** from long-term radial-velocity surveys and from Gaia astrometry (Gaia's fourth data release, expected around late 2026, adds epoch astrometry; check ESA for timing).
5. **Rank targets** where the allowed region is still open and within reach of follow-up.
6. **Share predictions** publicly before the follow-up data arrive, so the test is fair.

## How we could be wrong

- **Primordial tilt.** The star's spin may have been misaligned from the start, for example by a tilted birth disk.
- **Past events.** Planet–planet scattering or migration may have tilted the orbit long ago, with no resonance today.
- **Uncertain *J*₂.** Stellar flattening is rarely measured directly, and errors propagate into the locus.
- **Stellar spin precession.** The planet also torques the star, which changes the relevant frequencies.
- **A clear "no" result.** If radial velocities and astrometry exclude every companion along the locus out to the relevant distances, a present-day companion-driven resonance is ruled out for that system.

## For experts

**Stellar quadrupole precession** of an inner orbit (semi-major axis *a*₁, mean motion *n*₁) inclined by ψ to the stellar equator:

$$ g_\star \approx \frac{3}{2}\,J_2\left(\frac{R_\star}{a_1}\right)^2 n_1\cos\psi. $$

**Companion-driven nodal precession** (Laplace–Lagrange, outer companion of mass *m*₂ at *a*₂, α = *a*₁/*a*₂):

$$ g_{12} \approx \frac{1}{4}\,\frac{m_2}{M_\star}\,\alpha^2\, b^{(1)}_{3/2}(\alpha)\, n_1, \qquad b^{(1)}_{3/2}(\alpha) = \frac{1}{\pi}\int_0^{2\pi}\frac{\cos\theta\,d\theta}{(1-2\alpha\cos\theta+\alpha^2)^{3/2}}. $$

For α ≪ 1, *b*<sup>(1)</sup><sub>3/2</sub>(α) ≈ 3α, so *g*<sub>12</sub> ≈ (3/4)(*m*₂/*M*<sub>⋆</sub>) α³ *n*₁.

**Resonance locus.** Setting *g*<sub>⋆</sub> ≈ *g*<sub>12</sub> gives, as an approximation valid for *a*₁ ≪ *a*₂:

$$ \frac{m_2}{M_\star}\left(\frac{a_1}{a_2}\right)^3 \approx 2\,J_2\left(\frac{R_\star}{a_1}\right)^2\cos\psi. $$

**Illustrative example.** With *J*₂ = 10⁻⁶, *R*<sub>⋆</sub> = 1 *R*<sub>⊙</sub> (0.00465 au), *a*₁ = 0.05 au and cos ψ = 0.5, the right-hand side is ≈ 8.6 × 10⁻⁹. A Jupiter-mass companion (*m*₂/*M*<sub>⋆</sub> = 10⁻³) would then sit near *a*₂ ≈ 2.4 au. This illustrates the method only; real systems need measured stellar parameters, eccentricity corrections, general-relativistic precession, stellar spin dynamics and, in the disk-driven scenario, the time-dependent disk potential.

**Caveat on causation.** The original notes claimed that nearly every misaligned planet is held in an active resonance by an undiscovered planet. The literature does not support "nearly every"; we present the locus as a targeting tool, not a proof.

The project's code module `fdastro.obliquity` implements these precession-rate and resonance-locus calculations; see the tutorial for current functions.

## Try it

- Tutorial: [Tilted orbits and hidden companions](../tutorials/t09-tilted-orbits-and-hidden-companions.md)
- Code module: `fdastro.obliquity`
- Related: [D02 — Planets whose transits fade away](d02-vanishing-transits.md)
- Reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Albrecht, S. H., Dawson, R. I. & Winn, J. N. (2022). Stellar obliquities in exoplanetary systems. *Publications of the Astronomical Society of the Pacific* 134, 082001.
- De Rosa, R. J. et al. (2020). [Mutual inclination of the π Mensae planets from Hipparcos–Gaia astrometry.] *Astronomy & Astrophysics* 640, A73. (Bracketed text describes the paper; check ADS for the exact title.)
- Kunovac Hodžić, V. et al. (2021). Orbital misalignment of the super-Earth π Men c with the spin of its star. *Monthly Notices of the Royal Astronomical Society* 502, 2893.
- Petrovich, C., Muñoz, D. J., Kratter, K. M. & Malhotra, R. (2020). A disk-driven resonance as the origin of high inclinations of close-in planets. *The Astrophysical Journal Letters*. arXiv:2008.08587
- Sanchis-Ojeda, R. & Winn, J. N. (2011). Starspots, spin–orbit misalignment, and active latitudes in the HAT-P-11 exoplanetary system. *The Astrophysical Journal* 743, 61.
- Southworth, J. (2011). Homogeneous studies of transiting extrasolar planets – IV. Thirty systems with space-based light curves. *Monthly Notices of the Royal Astronomical Society* 417, 2166. (TEPCat catalog.)
- Winn, J. N. et al. (2010). The oblique orbit of the super-Neptune HAT-P-11b. *The Astrophysical Journal Letters* 723, L223.
- Xuan, J. W. & Wyatt, M. C. (2020). Evidence for a high mutual inclination between the cold Jupiter and transiting super Earth orbiting π Men. *Monthly Notices of the Royal Astronomical Society* 497, 2096.
- Yee, S. W. et al. (2018). HAT-P-11: discovery of a second planet and a clue to understanding exoplanet obliquities. *The Astronomical Journal* 155, 255.
