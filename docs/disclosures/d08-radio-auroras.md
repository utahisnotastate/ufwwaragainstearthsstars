# D08 — Radio auroras from planets and brown dwarfs

> **In one sentence:** Planets and brown dwarfs with strong magnetic fields make powerful radio bursts near their magnetic poles, so low-frequency radio surveys can discover cold objects that are almost invisible to ordinary telescopes.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (unknown brown dwarfs and exoplanets in radio archives). Radio discovery of brown dwarfs is 🟢 **Level 1 — Confirmed**; radio detection of exoplanets is 🔵 **Level 2 — Strong evidence, not yet confirmed**.
>
> *Last reviewed: November 2026.*

## For young readers

Have you seen pictures of the northern lights? They are glowing curtains of color near Earth's North and South Poles. They happen when tiny charged particles from space crash into the air, guided by Earth's magnetic field.

The same magnetic dance also makes **radio waves** — invisible light that a radio can pick up. Earth, Jupiter and Saturn all "sing" in radio. Jupiter is so loud that people with homemade radio antennas can hear it hiss and pop! Cold brown dwarfs, and maybe planets around other stars, can sing too. In 2020, astronomers in Europe found a brand-new brown dwarf by listening to its radio song first, before anyone had seen it with a regular telescope.

## The big idea

When charged particles stream along a planet's magnetic field lines toward its poles, they can produce intense radio emission through a process called the **electron cyclotron maser**. The radio waves come out near a frequency set by the strength of the magnetic field. They are often strongly **circularly polarized** — the radio wave's direction spins like a corkscrew — which is rare for most other radio sources and makes them easy to recognize.

Earth's version is called **auroral kilometric radiation** and comes out at a few hundred kilohertz. Jupiter's strongest emission reaches about 40 megahertz. Brown dwarfs can have magnetic fields thousands of times stronger than Earth's, so their bursts can reach gigahertz frequencies.

There is a problem for listening from the ground: Earth's upper atmosphere (the ionosphere) blocks radio waves below roughly 10 megahertz. So planets with Earth-like fields can only be heard from space. Jupiter-like and stronger fields, however, can be heard by ground arrays such as LOFAR in Europe.

Large radio surveys now map the whole northern sky at low frequencies, including circular polarization. Every circularly polarized point source that matches no known star or galaxy is a candidate for a magnetically active cold object.

## What we already know

- 🟢 **Level 1 — Confirmed.** Earth is a strong natural radio source at kilometer wavelengths, similar in kind to Jupiter and Saturn (Gurnett 1974; Zarka 2007).
- 🟢 **Level 1 — Confirmed.** Brown dwarfs produce auroral radio emission and even optical aurorae (Hallinan et al. 2015; Kao et al. 2016).
- 🟢 **Level 1 — Confirmed.** The cold T dwarf BDR J1750+3809 ("Elegast") was discovered first as a circularly polarized LOFAR radio source and then confirmed with infrared spectra (Vedantham et al. 2020b).
- 🔵 **Level 2 — Strong evidence.** LOFAR detected circularly polarized radio emission from the quiet red dwarf GJ 1151, interpreted as possible star–planet interaction (Vedantham et al. 2020a). Whether a planet is responsible is still debated.
- 🔵 **Level 2 — Strong evidence, not confirmed.** A tentative LOFAR detection of radio emission from the τ Boötis system, possibly from its planet, has not yet been confirmed by follow-up (Turner et al. 2021).
- 🟢 **Level 1 — Confirmed.** LOFAR surveys in circular polarization have found many radio-emitting M dwarfs (Callingham et al. 2021, 2023).

## What is still open

**Do low-frequency radio surveys already contain circularly polarized signals from brown dwarfs or exoplanets that have not yet been identified?**

This is a direct, testable cross-matching problem. The radio catalogs exist. Infrared and Gaia catalogs exist. Matching them carefully, and following up the leftovers, is how Elegast was found.

## How you could test it

1. **Download a circular-polarization catalog**, such as V-LoTSS from the LOFAR Two-metre Sky Survey.
2. **Cross-match** each source with Gaia, WISE/CatWISE and optical catalogs. Remember that nearby objects move, so allow for proper motion between the radio and infrared epochs.
3. **Keep the leftovers**: circularly polarized sources with no star or galaxy counterpart, or with only a faint, very red infrared counterpart.
4. **Check variability.** Auroral emission is often bursty or rotates in and out of view.
5. **Request follow-up** infrared imaging or spectroscopy for the best candidates.

For Solar System radio emission (an excellent learning project), NASA's CDAWeb and the Planetary Data System provide data from space radio receivers on Wind, STEREO, Cassini and Juno.

## How we could be wrong

- **Radio interference.** Human-made signals can leak into data. Real sky sources stay fixed on the sky as Earth rotates; interference does not. Interferometers like LOFAR localize sources, which separates them.
- **Pulsars and active galaxies** can be polarized. Pulsars can be checked for periodic pulses; galaxies usually show weak circular polarization.
- **Flare stars.** Faint red dwarfs also emit polarized bursts. Their infrared colors differ from cold brown dwarfs.
- **Positional mismatch.** Radio positions have uncertainties; a chance alignment with an unrelated infrared source is possible. Estimate the false-match rate.
- **A clear "no" result.** If deep infrared imaging finds no counterpart, or finds an ordinary star, the cold-object idea is ruled out for that source.

## For experts

**Electron cyclotron frequency.** Emission occurs near the local electron gyrofrequency

$$ f_{ce} = \frac{e B}{2\pi m_e} \approx 2.8\ \mathrm{MHz}\ \left(\frac{B}{1\ \mathrm{G}}\right). $$

The maximum emitted frequency traces the maximum surface field. Jupiter's ~14 G polar fields give a ~40 MHz cutoff. A 25 G field gives ~70 MHz; kG fields on brown dwarfs give GHz emission.

**Observability from the ground** requires *f* above the ionospheric cutoff (typically ~10 MHz, varying with solar activity and time of day). Emission from Earth-strength fields (~0.5 G, *f* ≲ 1.5 MHz) needs space-based or lunar far-side receivers.

**Flux scaling.** The "radiometric Bode's law" relates emitted radio power to the incident solar-wind (or stellar-wind) energy flux on the magnetosphere; it is used to predict exoplanet radio fluxes but carries order-of-magnitude uncertainty (Zarka 2007).

**RFI flagging.** Automated flaggers (for example, AOFlagger; Offringa et al. 2012) remove time–frequency pixels that look like interference. Very narrowband or bursty astrophysical signals can occasionally be partly flagged. Checking flagged fractions at a candidate's position and time, and imaging with and without flagging, is good practice. Note that genuine celestial sources are distinguished from ground transmitters by their fixed sky position and interferometric localization rather than by Doppler shift.

## Try it

- Lesson: [Radio auroras](../lessons/l08-radio-auroras.md)
- Related: [D04 — Cold, dark neighbors in infrared sky maps](d04-nearby-cold-worlds-wise.md)
- Data: [data sources](../about/data-sources.md); reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Callingham, J. R. et al. (2021). The population of M dwarfs observed at low radio frequencies. *Nature Astronomy* 5, 1233.
- Callingham, J. R. et al. (2023). V-LoTSS: the circularly polarised LOFAR Two-metre Sky Survey. *Astronomy & Astrophysics* 670, A124.
- Gurnett, D. A. (1974). The Earth as a radio source: terrestrial kilometric radiation. *Journal of Geophysical Research* 79, 4227.
- Hallinan, G. et al. (2015). Magnetospherically driven optical and radio aurorae at the end of the stellar main sequence. *Nature* 523, 568.
- Kao, M. M. et al. (2016). Auroral radio emission from late L and T dwarfs: a new constraint on dynamo theory in the substellar regime. *The Astrophysical Journal* 818, 24.
- Offringa, A. R., van de Gronde, J. J. & Roerdink, J. B. T. M. (2012). A morphological algorithm for improving radio-frequency interference detection. *Astronomy & Astrophysics* 539, A95.
- Turner, J. D. et al. (2021). The search for radio emission from the exoplanetary systems 55 Cancri, υ Andromedae, and τ Boötis using LOFAR beam-formed observations. *Astronomy & Astrophysics* 645, A59.
- Vedantham, H. K. et al. (2020a). Coherent radio emission from a quiescent red dwarf indicative of star–planet interaction. *Nature Astronomy* 4, 577.
- Vedantham, H. K. et al. (2020b). Direct radio discovery of a cold brown dwarf. *The Astrophysical Journal Letters* 903, L33. doi:10.3847/2041-8213/abc256
- Zarka, P. (2007). Plasma interactions of exoplanets with their parent star and associated radio emissions. *Planetary and Space Science* 55, 598.
