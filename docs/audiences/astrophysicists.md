# Guide for Astrophysicists and Planetary Scientists

> **In one sentence:** Each disclosure is framed as a concrete research question with named public data products, known systematics and a falsification criterion — and we would welcome corrections, collaborators and pointers to work we have missed.

## For young readers

This page is for professional scientists. It lists each idea in the project as a question that real research could answer, and says which data to use and what can go wrong. Kids can find the fun versions in the [lessons](../lessons/README.md)!

## How to read this project

- Each disclosure page has a simple layer for the public and a "For experts" layer with methods and references.
- Every claim carries an evidence label: 🟢 Level 1 Confirmed, 🔵 Level 2 Strong evidence, 🟡 Level 3 Testable idea, 🟠 Level 4 Long shot. Definitions: [style guide](../STYLE.md#4-evidence-levels).
- We do not claim discoveries. We propose searches, document methods, and route any candidates through the established channels (MPC, TNS, ExoFOP, journals). See [how to report a discovery](../about/how-to-report-a-discovery.md).
- If you find an error, an overstatement, or missing prior work, please open an issue. Corrections are logged publicly.

## The disclosures as research questions

### D01 — Unseen planets in the far Solar System ([page](../disclosures/d01-unseen-planets-far-solar-system.md))
- **Question:** What region of mass–distance–sky position for an undiscovered distant planet remains allowed by planetary ephemerides, spacecraft ranging and pulsar-timing ephemeris constraints, combined with survey non-detections?
- **Data:** published ephemeris residuals (e.g., INPOP, JPL DE series); spacecraft ranging results; pulsar-timing-array Solar System ephemeris analyses; survey depth maps (including early Rubin data).
- **Systematics:** asteroid- and Kuiper-belt mass modeling, solar plasma delays, spacecraft non-gravitational forces, ephemeris frame ties.
- **Falsification:** joint constraints that exclude the parameter space proposed to explain the clustering of distant TNO orbits, or an unbiased survey showing no clustering.

### D02 — Vanishing transits ([page](../disclosures/d02-vanishing-transits.md))
- **Question:** How many transiting planets show statistically significant, monotonic changes in depth and duration consistent with nodal precession driven by an unseen companion?
- **Data:** TESS SPOC and QLP light curves; Kepler long- and short-cadence data; published TTV/TDV catalogs; ground-based archival photometry.
- **Systematics:** inter-sector dilution changes and background contamination, detrending that suppresses transit depth, stellar activity, cadence differences between missions.
- **Prior art:** Kepler-13Ab's changing impact parameter; TOI-2535 b (Yee et al. 2026).

### D03 — Single-transit planets ([page](../disclosures/d03-single-transit-planets.md))
- **Question:** What is the occurrence rate of long-period planets implied by single transits in TESS, after correcting for completeness and false positives?
- **Data:** TESS full-frame-image light curves; Gaia DR3 stellar parameters; radial-velocity follow-up archives.
- **Systematics:** momentum dumps, scattered light, eclipsing binaries in the aperture, stellar variability, sector-edge effects.

### D04 — Cold neighbors in infrared sky maps ([page](../disclosures/d04-nearby-cold-worlds-wise.md))
- **Question:** Are there undiscovered Y dwarfs or planetary-mass objects within ~20 pc whose large motions defeat standard cross-epoch matching?
- **Data:** WISE/NEOWISE single-exposure source tables; unWISE and CatWISE2020 catalogs; Backyard Worlds candidate lists.
- **Systematics:** latent images, diffraction spikes, ghosts, confusion in the Galactic plane, variable sources.
- **Constraints:** Luhman (2014) excluded Saturn-mass and larger objects to substantial distances with WISE; any "closer than Proxima Centauri" claim is a long shot (🟠).

### D05 — Polarized light from planets ([page](../disclosures/d05-polarized-light-from-planets.md))
- **Question:** Where does reflected-light polarimetry add unique information for exoplanets with current and planned high-contrast instruments?
- **Data:** archival imaging polarimetry from SPHERE/ZIMPOL, GPI and similar; published unresolved-system polarimetric limits.
- **Systematics:** instrumental and interstellar polarization at the 10⁻⁵–10⁻⁶ level; telescope polarization; seeing.
- **Note:** consumer-telescope detection of exoplanet polarization is not realistic (🟠 Level 4).

### D06 — Earth–Moon L4/L5 ([page](../disclosures/d06-earth-moon-trojan-points.md))
- **Question:** Do independent polarimetric and photometric observations confirm the Kordylewski clouds, and do any deep searches constrain solid bodies?
- **Systematics:** zodiacal light, gegenschein, airglow, solar perturbations limiting long-term stability.

### D07 — Short microlensing events ([page](../disclosures/d07-short-microlensing-free-floating-planets.md))
- **Question:** What is the free-floating planet mass function at Earth-mass and below, once survey efficiency and finite-source effects are modeled?
- **Data:** OGLE, MOA and KMTNet event catalogs; Roman Galactic Bulge Time Domain Survey (future).
- **Systematics:** short-timescale false positives (flares, CVs, detector artifacts), blending, wide-orbit bound planets mimicking free-floating ones.

### D08 — Radio auroras ([page](../disclosures/d08-radio-auroras.md))
- **Question:** How many currently unknown brown dwarfs or exoplanetary magnetospheres are detectable as circularly polarized low-frequency sources?
- **Data:** LOFAR Two-metre Sky Survey (including circular polarization products); other low-frequency surveys.
- **Systematics:** RFI, ionospheric effects, pulsars and active stars as false positives, leakage from Stokes I into V.
- **Prior art:** the radio discovery of the T dwarf BDR J1750+3809 (Vedantham et al. 2020).

### D09 — Planets in young disks ([page](../disclosures/d09-planets-in-young-disks.md))
- **Question:** Do kinematic signatures ("kinks") in ALMA CO channel maps reveal planets not seen in continuum or direct imaging, and how robust are planet mass estimates from them?
- **Data:** ALMA Science Archive line cubes; large programs such as exoALMA.
- **Systematics:** disk winds, warps, gravitational instability, vortices, thermal structure, channel spacing and beam effects.
- **Prior art:** Pinte et al. (2018) kinematic detection in HD 163296.

### D10 — Subsurface structure from gravity ([page](../disclosures/d10-caves-and-buried-masses-gravity.md))
- **Question:** Can localized analyses of Level-1 tracking data (GRAIL KBRR, MRO/ODY Doppler) detect sub-kilometer density anomalies such as lava tubes beyond what regularized global models show?
- **Data:** NASA PDS Geosciences Node (GRAIL, MRO radio science); LRO imagery and radar.
- **Systematics:** spacecraft non-gravitational accelerations, thermal effects, regularization (Kaula constraint), topographic correction errors, noise at high degree.
- **Prior art:** GRAIL-based lava tube candidates; radar confirmation of a lunar pit cave (Carrer et al. 2024).

### D11 — Inner Solar System co-orbitals ([page](../disclosures/d11-inner-solar-system-trojans.md))
- **Question:** What is the population of Venus and Earth co-orbitals, given twilight-survey selection functions?
- **Data:** twilight surveys (DECam, ZTF), Gaia Solar System object astrometry, early Rubin data, MPC unlinked observations.
- **Systematics:** high airmass, bright sky, low phase-angle coverage, short visibility windows.

### D12 — Exomoons from TTV/TDV ([page](../disclosures/d12-exomoons-timing-duration.md))
- **Question:** Do any Kepler/TESS planets show TTV and TDV-V in phase quadrature at a significance robust to aliasing, red noise and stellar activity?
- **Data:** Kepler TTV/TDV catalogs; TESS timings; JWST and HST transit observations for selected targets.
- **Systematics:** spot crossings, granulation, detrending-induced duration bias, aliasing of short moon periods.
- **Status:** Kepler-1625 b-i and Kepler-1708 b-i remain disputed; no confirmed exomoon.

### D13 — Tilted orbits and hidden companions ([page](../disclosures/d13-tilted-orbits-hidden-companions.md))
- **Question:** For misaligned planets without known outer companions, which (*m*₂, *a*₂) loci would allow secular resonance, and do RV and Gaia astrometry exclude them?
- **Data:** TEPCat obliquity catalog; RV archives (e.g., HARPS, HIRES); Hipparcos–Gaia proper-motion anomalies; future Gaia epoch astrometry.
- **Systematics:** uncertain stellar *J*₂ and ages, tidal realignment, alternative misalignment channels.

### D14 — Interstellar objects in unlinked data ([page](../disclosures/d14-interstellar-objects-unlinked-data.md))
- **Question:** Do any multi-night chains of tracklets in the MPC Isolated Tracklet File (ITF) require unbound orbits at a calibrated significance?
- **Data:** MPC ITF; survey tracklets; tools such as HelioLinC/HelioLinC3D and THOR.
- **Systematics:** false linkages (the dominant failure mode), time-scale errors, topocentric corrections, astrometric catalog biases, outliers.
- **Prior art:** Holman et al. (2018) linked large numbers of ITF tracklets with HelioLinC.

### D15 — Captured interstellar objects ([page](../disclosures/d15-captured-interstellar-objects.md))
- **Question:** Are any retrograde or polar small bodies more consistent with an interstellar origin than with known Solar System delivery channels, using long-term dynamics plus spectra and colors?
- **Data:** JPL SBDB/MPC orbit catalogs; spectral and color surveys; dynamical integrations.
- **Status:** Namouni & Morais (2018) proposed an interstellar origin for Kaʻepaokaʻawela; subsequent studies dispute it.

## Collaboration

- **Open science:** all code is MIT-licensed and all text is CC BY 4.0. We cite prior work and expect the same.
- **Credit:** contributors who supply analysis, review or data products are credited in the repository and in any resulting notes.
- **Conflicts with ongoing work:** if a disclosure overlaps with your unpublished research, tell us; we will not race professional teams to announcements.

## References (selected)

- Carrer, L., et al. (2024). Radar evidence of an accessible cave conduit on the Moon below the Mare Tranquillitatis pit. *Nature Astronomy*, 8, 1119–1126.
- Holman, M. J., et al. (2018). HelioLinC: a novel approach to the minor planet linking problem. *The Astronomical Journal*, 156, 135.
- Luhman, K. L. (2014). A search for a distant companion to the Sun with the Wide-field Infrared Survey Explorer. *The Astrophysical Journal*, 781, 4.
- Namouni, F., & Morais, M. H. M. (2018). *Monthly Notices of the Royal Astronomical Society: Letters*, 477, L117–L121.
- Pinte, C., et al. (2018). Kinematic evidence for an embedded protoplanet in a circumstellar disk. *The Astrophysical Journal Letters*, 860, L13.
- Vedantham, H. K., et al. (2020). Direct radio discovery of a cold brown dwarf. *The Astrophysical Journal Letters*, 903, L33.
- Yee, S. W., et al. (2026). A TESS disappearing act: the vanishing transits of TOI-2535 b. *The Astrophysical Journal Letters*.
