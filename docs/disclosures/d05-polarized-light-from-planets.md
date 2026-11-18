# D05 — Polarized light from planets

> **In one sentence:** Starlight that bounces off a planet becomes partly polarized (its waves line up in one direction), which can help astronomers pick out a planet's faint light from its star's glare — but the signal is tiny.
>
> **Evidence level:** 🟠 **Level 4 — Long shot** for detecting exoplanets with small or backyard telescopes. Polarimetry as a professional exoplanet technique is 🔵 **Level 2 — Strong evidence**.
>
> *Last reviewed: November 2026.*

## For young readers

Light is a wave, like a wiggle on a jump rope. In ordinary starlight, the wiggles go in every direction at once: up and down, side to side, and everything in between. When light bounces off something — a lake, a road, or a planet's air — many of the wiggles line up in one direction. Scientists call this **polarized** light. Polarized sunglasses work by blocking the lined-up wiggles from shiny surfaces.

A planet near a star is like a firefly next to a stadium floodlight. The star is billions of times brighter. But the star's light is mostly *not* polarized, and the planet's reflected light *is*. Special instruments can look only for polarized light, which makes the star seem dimmer and the planet easier to find. This is very hard. Today it takes the biggest telescopes on Earth. You can still try polarization at home on the Moon, the sky, and the planets in our Solar System!

## The big idea

Stars like the Sun emit light that is almost unpolarized when you add up the whole star. When that light scatters off a planet's atmosphere, clouds or surface, it becomes partly polarized. The amount depends on the angle between the star, planet and observer, and on what the planet is made of. Near a "half-lit" view (around 90° phase angle), Rayleigh scattering by gas can polarize light strongly.

This means a polarimeter can, in principle, suppress the star and enhance the planet. Large telescopes already use this idea. The SPHERE instrument on the Very Large Telescope includes a polarimetric mode used to image dust disks and to search for planets. Polarization of Earth's own reflected light (earthshine on the Moon) has even been proposed as a way to recognize life-related features such as vegetation and oceans on other worlds.

There is a catch. A planet's reflected light is extremely faint compared with its star: roughly one part in 100,000 for the hottest close-in giant planets, and about one part in a billion or less for a Jupiter-like planet far from its star. Only part of that light is polarized. So the polarized signal from a planet is a few parts per million or less of the total light.

A second idea, **intensity interferometry**, measures how photon arrival times are correlated. It is a real and growing technique for measuring the sizes of bright stars. However, starlight reflected by a planet is still ordinary "thermal" light, with the same photon statistics as the star. Intensity interferometry cannot separate the two by "texture". Its strength is high angular resolution, not planet detection with small telescopes.

## What we already know

- 🟢 **Level 1 — Confirmed.** Light scattered by planetary atmospheres is polarized; this is measured routinely for planets in our Solar System and predicted for exoplanets (Seager, Whitney & Sasselov 2000; Stam 2008).
- 🔵 **Level 2 — Strong evidence.** Polarization from clouds on the nearby brown dwarf pair Luhman 16 has been detected (Millar-Blanchaer et al. 2020).
- 🔵 **Level 2 — Strong evidence, disputed.** A polarization signal from the hot Jupiter HD 189733 b was reported (Berdyugina et al. 2008), but later, more sensitive measurements did not confirm it (Wiktorowicz et al. 2015).
- 🔵 **Level 2 — Strong evidence.** Spectropolarimetry of earthshine shows signatures of Earth's atmosphere, clouds and vegetation, supporting polarization as a future tool for characterizing exoplanets (Sterzik, Bagnulo & Palle 2012).
- 🟢 **Level 1 — Confirmed.** Intensity interferometry measures stellar diameters. It began with Hanbury Brown and Twiss in the 1950s and has been revived with modern telescope arrays such as VERITAS (Hanbury Brown & Twiss 1956; Abeysekara et al. 2020). Small-telescope experiments have measured photon bunching from bright stars (Guerin et al. 2017).
- 🟠 **Level 4 — Long shot.** Detecting an exoplanet's polarized light with an 8–14 inch amateur telescope is far beyond current capability, for the reasons given below.

## What is still open

**How far can polarimetry go in separating planet light from starlight, and which planets will be the first to be characterized this way?**

This is mainly a question for large ground telescopes, the Roman Space Telescope's coronagraph, and future missions such as NASA's planned Habitable Worlds Observatory. For small telescopes, the open and achievable goal is **education and Solar System science**: measuring polarization of the Moon, sky, planets, comets and asteroids.

## How you could test it

**At home or school (achievable):**

1. Put a linear polarizing filter in front of a camera.
2. Photograph the blue sky at different angles from the Sun. The sky is most polarized about 90° from the Sun.
3. Photograph the Moon or Venus through the filter at several rotations. Measure how the brightness changes.
4. Compare with published phase-angle polarization curves for the Moon and planets.

**At a research observatory (professional):**

1. Use a dual-beam polarimeter with fast modulation to cancel atmospheric flicker and instrument effects.
2. Observe a known planet host star through the planet's orbit.
3. Look for a polarization change that repeats with the planet's orbital period.
4. Compare to models for different atmospheres and cloud types.

## How we could be wrong

- **Instrument polarization.** Telescope mirrors and optics polarize light at the level of 10⁻⁵ to 10⁻³, often more than any planet signal. This must be calibrated with unpolarized standard stars.
- **Interstellar polarization.** Dust between us and the star polarizes starlight. It is constant in time, so only a changing signal can be the planet.
- **Stellar activity.** Starspots and magnetic fields can create small, changing polarization.
- **Photon noise.** Too few photons means the measurement cannot reach the needed precision, no matter how good the instrument.

## For experts

**Planet–star contrast in reflected light:**

$$ \frac{F_p}{F_\star} = A_g\,\Phi(\alpha)\left(\frac{R_p}{a}\right)^2, $$

where *A*<sub>g</sub> is the geometric albedo and Φ(α) the phase function. For a hot Jupiter with *R*<sub>p</sub> = 0.1 *R*<sub>⊙</sub> and *a* = 0.05 au, (*R*<sub>p</sub>/*a*)² ≈ 9 × 10⁻⁵, so with *A*<sub>g</sub> ≈ 0.1 the contrast is about 10⁻⁵. For Jupiter at 5.2 au it is about 10⁻⁹; for Earth at 1 au about 10⁻¹⁰.

**Polarized contrast.** The planet's polarized fraction *P*<sub>p</sub>(α) can reach tens of percent near quadrature, so the polarized signal relative to the total is roughly *P*<sub>p</sub> × *F*<sub>p</sub>/*F*<sub>⋆</sub> ≲ 10⁻⁶ for the most favorable hot Jupiters (and the system is unresolved, so the signal is diluted further by orbital averaging).

**Photon-noise limit.** For *N* detected photons, the uncertainty on a normalized Stokes parameter is σ<sub>q</sub> ≈ √(2/*N*). Reaching σ ≈ 10⁻⁶ needs *N* ≈ 2 × 10¹². A *V* ≈ 5 star through a 20 cm aperture with a broad optical band and 30% efficiency gives of order 10⁶ photons s⁻¹, so the photon-noise limit alone requires about 10⁶ s (roughly 12 days) of perfect integration — before instrumental systematics, which are typically far larger.

**Intensity interferometry.** The second-order coherence of chaotic (thermal) light is *g*⁽²⁾(0) = 2 regardless of whether the light was emitted by a star or scattered by a planet's atmosphere. Scattering by an unresolved planet does not create a distinct *g*⁽²⁾(τ) signature. The measured correlation depends on the spatial coherence of the source, which is why the method measures stellar angular diameters.

## Try it

- Lesson: [Light has a direction](../lessons/l07-light-has-a-direction.md)
- Related: [D06 — Dust clouds and possible mini-moons at the Earth–Moon balance points](d06-earth-moon-trojan-points.md) (polarization of dust and regolith)
- Data: [data sources](../about/data-sources.md)

## References

- Abeysekara, A. U. et al. (2020). Demonstration of stellar intensity interferometry with the four VERITAS telescopes. *Nature Astronomy* 4, 1164.
- Berdyugina, S. V. et al. (2008). First detection of polarized scattered light from an exoplanetary atmosphere. *The Astrophysical Journal Letters* 673, L83.
- Guerin, W. et al. (2017). Temporal intensity interferometry: photon bunching in three bright stars. *Monthly Notices of the Royal Astronomical Society* 472, 4126.
- Hanbury Brown, R. & Twiss, R. Q. (1956). A test of a new type of stellar interferometer on Sirius. *Nature* 178, 1046.
- Millar-Blanchaer, M. A. et al. (2020). Detection of polarization due to cloud bands in the nearby Luhman 16 brown dwarf binary. *The Astrophysical Journal* 894, 42.
- Seager, S., Whitney, B. A. & Sasselov, D. D. (2000). Photometric light curves and polarization of close-in extrasolar giant planets. *The Astrophysical Journal* 540, 504.
- Stam, D. M. (2008). Spectropolarimetric signatures of Earth-like extrasolar planets. *Astronomy & Astrophysics* 482, 989.
- Sterzik, M. F., Bagnulo, S. & Palle, E. (2012). Biosignatures as revealed by spectropolarimetry of Earthshine. *Nature* 483, 64.
- Wiktorowicz, S. J. et al. (2015). [Polarimetric non-detection of scattered light from HD 189733 b.] *The Astrophysical Journal* 813, 48. (Bracketed text describes the paper; check ADS for the exact title.)
