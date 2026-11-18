# Guide for Amateur Astronomers

> **In one sentence:** Small telescopes can make real scientific contributions — asteroid astrometry, occultation timing, transit timing, comet monitoring — but some ideas in circulation (such as backyard exoplanet polarimetry) are far beyond what small apertures can do, and this page explains which is which.

## For young readers

Lots of grown-ups have their own telescopes at home. They help real scientists! They measure where asteroids are, time when stars wink out behind space rocks, and watch planets pass in front of stars. Some of them have found new comets. If you have a telescope, always use it with an adult — and **never point it at the Sun** without a proper certified solar filter.

## What small telescopes do well

| Contribution | Typical equipment | Why it matters | Who collects it |
|---|---|---|---|
| **Asteroid and comet astrometry** | 20–40 cm telescope, CCD/CMOS camera, accurate time | Improves orbits; confirms new near-Earth objects | Minor Planet Center (MPC) |
| **Follow-up of new discoveries** | Same as above | New candidates on the MPC's NEO Confirmation Page need quick follow-up | MPC |
| **Stellar occultation timing** | Small telescope, sensitive video camera, GPS-based time | Measures asteroid sizes and shapes; finds satellites and rings | International Occultation Timing Association (IOTA) and regional groups |
| **Exoplanet transit timing** | 15 cm+ telescope, camera, photometry software | Keeps transit predictions accurate for big telescopes | NASA's Exoplanet Watch; the ExoClock project (ephemerides for ESA's Ariel mission targets); AAVSO |
| **Variable stars** | Almost any telescope, or binoculars | Long-term records of stellar behavior | AAVSO |
| **Comet monitoring and discovery** | Wide-field telescopes | Activity and outbursts; occasional discoveries | MPC, comet observing groups |

### A real example

On 30 August 2019, **Gennady Borisov**, an amateur astronomer in Crimea, discovered comet 2I/Borisov with a 0.65 m telescope he built himself. It turned out to be only the second known interstellar object (🟢 Level 1).

## Submitting astrometry to the Minor Planet Center

1. **Read the MPC's current documentation** on reporting observations and observatory codes. Rules are updated; for example, observatory-code requests must now use the **ADES** format (PSV or XML), not the older 80-column format.
2. **Get an observatory code.** You first submit good-quality astrometry of known, designated objects under the temporary code `XXX`, together with an Observatory Code Request Form giving your site's longitude, latitude and altitude. The MPC checks the astrometry before assigning a code.
3. **Measure carefully.** Use a modern astrometric reference catalog (Gaia-based), accurate timing (synchronize your computer clock), and report realistic uncertainties.
4. **Report the time of mid-exposure** in UTC.
5. **Never guess an identification.** Report positions; the MPC links them.

Common software for measuring positions includes Astrometrica, Tycho Tracker, Astrometry.net-based tools and PixInsight scripts. Choose what fits your setup.

## Connecting your observing to the disclosures

| Disclosure | What amateurs can realistically do | Evidence level of the open question |
|---|---|---|
| [D02 Vanishing transits](../disclosures/d02-vanishing-transits.md) | Time transits of known hot Jupiters (bright host stars) to track changes in timing or depth over years | 🟡 Level 3 |
| [D11 Inner Solar System Trojans](../disclosures/d11-inner-solar-system-trojans.md) | Twilight follow-up astrometry of newly reported low-elongation objects (difficult; low altitude, bright sky) | 🟡 Level 3 |
| [D14 Interstellar visitors](../disclosures/d14-interstellar-objects-unlinked-data.md) | Rapid follow-up of unusual objects on the NEO Confirmation Page; astrometry of known interstellar comets when bright enough | 🟡 Level 3 |
| [D15 Captured interstellar objects](../disclosures/d15-captured-interstellar-objects.md) | Photometry (colors, rotation periods) of brighter retrograde or high-inclination objects | 🟡 Level 3 |
| [D06 Earth–Moon L4/L5](../disclosures/d06-earth-moon-trojan-points.md) | Wide-field imaging polarimetry of the Kordylewski clouds is possible in principle with careful calibration; solid bodies are very unlikely | 🟠 Level 4 |

## What small telescopes cannot do (honest limits)

Some popular claims about backyard capabilities are not realistic. These limits come from basic physics, not from a lack of effort.

### Detecting exoplanets by polarization

The idea: a planet's reflected light is partly polarized, while its star's light is nearly unpolarized, so a polarizing beam splitter could "subtract out" the star.

**Why a backyard setup cannot do this (🟠 Level 4 for small telescopes):**

- The planet's light is tiny compared with the star's: about 10⁻⁵–10⁻⁴ for the most favorable hot Jupiters, and about 10⁻⁹ for a Jupiter-like planet at Jupiter-like distance.
- Only part of that planet light is polarized, so the expected **net** polarization of the unresolved system is of order 10⁻⁵ or less.
- Photon noise sets a hard floor: to measure a fractional polarization of 10⁻⁶ you need roughly 10¹² detected photons, plus instrumental polarization calibrated to the same level. Even the brightest stars give a 20–30 cm telescope nowhere near that in a practical observing time.
- Professional instruments on 4–8 m telescopes, built specifically for this, have reached the 10⁻⁶ level on the brightest stars and still mostly report upper limits for exoplanets.

Polarimetry **is** a valuable professional technique, especially for imaging dusty disks with large telescopes and coronagraphs.

### Intensity interferometry for planets

Intensity interferometry (the Hanbury Brown–Twiss effect) is real and is used today with large Cherenkov telescope arrays to measure **stellar diameters**. It needs very large collecting areas and nanosecond timing, and its sensitivity scales poorly for faint targets. It is not a way to detect planets with a backyard telescope.

### Sensing positions "faster than light"

Some older literature claims that special sensors at a telescope's focus can detect an object's "true present position" instantly. This conflicts with well-tested physics; gravitational effects travel at the speed of light (confirmed in 2017 by the neutron-star merger GW170817). Astronomers compute present positions from orbits. See [Lesson 9](../lessons/l09-light-from-the-past.md) and the [editorial notes](../about/editorial-notes.md).

## Good practices that make your data useful

- **Calibrate:** darks, flats, bias frames.
- **Time accurately:** use GPS or network time; record the time of mid-exposure.
- **Report uncertainties honestly.**
- **Keep raw data** and an observing log.
- **Coordinate:** join a network (IOTA, AAVSO, Exoplanet Watch, ExoClock) so your observations fit a campaign.

## Safety

- **Never look at the Sun** through any optical instrument without a certified solar filter correctly fitted to the front of the telescope. Eyepiece "sun filters" can crack.
- Supervise children at all times around telescopes in daylight.
- Dress for the cold, and watch for trip hazards in the dark.

## References and resources

- Minor Planet Center documentation: reporting observations, ADES format, observatory codes (docs.minorplanetcenter.net).
- Wiktorowicz, S. J. (2009). Nondetection of polarized, scattered light from the HD 189733b hot Jupiter. *The Astrophysical Journal*, 696, 1116–1124.
- Abbott, B. P., et al. (2017). Gravitational waves and gamma-rays from a binary neutron star merger: GW170817 and GRB 170817A. *The Astrophysical Journal Letters*, 848, L13.
- Guzik, P., et al. (2020). Initial characterization of interstellar comet 2I/Borisov. *Nature Astronomy*, 4, 53–57.
- Zellem, R. T., et al. (2020). Utilizing small telescopes operated by citizen scientists for transiting exoplanet follow-up. *Publications of the Astronomical Society of the Pacific*, 132, 054401.
