# D09 — Baby planets hidden in dusty disks

> **In one sentence:** Young stars are surrounded by disks of gas and dust with rings and gaps, and small "kinks" in how the gas moves can reveal baby planets that are too faint to photograph.
>
> **Evidence level:** 🔵 **Level 2 — Strong evidence** (gas-motion kinks reveal young planets). Whether *most* gaps contain planets is 🟡 **Level 3 — Testable idea**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine a big, snowy field. A snowplow drives around and around in a circle. Even if you cannot see the snowplow in the dark, you can see the clean circle it leaves behind!

Young stars have giant, flat disks of gas and dust around them, like a dusty vinyl record. Planets form inside these disks. A powerful radio telescope in Chile called **ALMA** takes amazing pictures of these disks. Many disks have bright rings and dark gaps, like the grooves of a record. A baby planet may be clearing each gap, like the snowplow. Astronomers have found another clue too: the planet's gravity makes the gas swirl a little differently right next to it. It's like seeing a ripple in a stream where a hidden rock sits. That ripple has helped find baby planets that no camera could see.

## The big idea

ALMA (the Atacama Large Millimeter/submillimeter Array) images the cold dust and gas around young stars in fine detail. Since 2015, it has shown that rings and gaps are common.

Gaps can be made by forming planets, but also by other processes, such as the way ices freeze at certain distances or the way magnetic fields and turbulence shape the gas. Telling these apart is hard if the planet itself is too faint to see.

The gas offers a second clue. ALMA can measure the speed of gas (for example, carbon monoxide) through the Doppler shift of its spectral lines. In a smooth disk, the gas follows a regular, nearly Keplerian rotation pattern. A planet disturbs the flow nearby and creates a localized "kink" in the velocity pattern. Finding a kink at the location of a gap is strong evidence that a planet is there, and the size of the kink indicates the planet's mass.

## What we already know

- 🟢 **Level 1 — Confirmed.** Rings and gaps are common in protoplanetary disks observed at high resolution (ALMA Partnership 2015; Andrews et al. 2018).
- 🟢 **Level 1 — Confirmed.** Young planets have been directly imaged inside a disk gap in the PDS 70 system (Keppler et al. 2018; Haffert et al. 2019).
- 🔵 **Level 2 — Strong evidence.** Kinematic signatures in gas velocity maps indicate embedded planets of roughly Jupiter mass in disks such as HD 163296 (Pinte et al. 2018; Teague et al. 2018) and HD 97048 (Pinte et al. 2019).
- 🔵 **Level 2 — Strong evidence.** Not every gap requires a planet; other physical processes can create rings and gaps (for example, Flock et al. 2015).
- 🟢 **Level 1 — Confirmed.** Large ALMA programs dedicated to disk kinematics, such as exoALMA, published coordinated results in 2025.

## What is still open

**Do gas-velocity kinks in public ALMA data reveal more young planets than images alone show, and which gaps are truly planet-made?**

Many disks in the ALMA archive have high-quality gas data that have not been searched with the newest kinematic tools. A systematic, consistent search with a careful false-positive analysis is testable now.

## How you could test it

1. **Search the ALMA Science Archive** for disks with high-resolution carbon monoxide (CO) line data. Most data become public after a one-year proprietary period.
2. **Fit a smooth rotation model** to the gas velocities using open tools such as `eddy` or `discminer`.
3. **Subtract the model** and look for localized residuals that are stronger than the noise.
4. **Compare residual locations** with gaps in the dust continuum image.
5. **Estimate the planet mass** from the amplitude of the velocity perturbation using published calibrations.
6. **Check consistency** across different CO isotopologues and channels.

## How we could be wrong

- **Imperfect disk models.** A wrong disk inclination, warp, or vertical structure can leave fake residuals.
- **Noise and imaging artifacts.** Interferometric images can contain artifacts from incomplete sampling.
- **Other dynamics.** Infall from the surrounding cloud, spirals from gravitational instability, or vortices can also disturb the flow.
- **A clear "no" result.** If careful modeling leaves no significant localized residual at a gap, a planet massive enough to make a kink is ruled out there (though a lower-mass planet may remain).

## For experts

**Keplerian background.** For a thin disk around a star of mass *M*<sub>⋆</sub>, the projected line-of-sight velocity is

$$ v_{\rm los}(r,\phi) = \sqrt{\frac{G M_\star}{r}}\,\cos\phi\,\sin i + v_{\rm sys}, $$

modified by pressure support, disk self-gravity and the elevated emission surface of optically thick CO (which requires a surface height model *z*(*r*)).

**Planet-driven perturbations.** A planet of mass *M*<sub>p</sub> perturbs gas velocities by a fraction of the local sound speed near its Hill sphere and launches spiral wakes. The perturbation amplitude scales with the "thermal mass" ratio *q*/*q*<sub>th</sub>, where *q* = *M*<sub>p</sub>/*M*<sub>⋆</sub> and *q*<sub>th</sub> = (*h*/*r*)³. Kinks of order 0.1 km s⁻¹ in channel maps correspond to roughly Jupiter-mass planets for typical disk parameters; quantitative mass estimates require hydrodynamic simulations matched to each disk.

**Gaps without planets.** Mechanisms include condensation fronts, secular gravitational instability, and magnetohydrodynamic zonal flows (Flock et al. 2015). Magnetic fields matter for gas dynamics, but no special electrical mechanism lets small planets clear gaps far more efficiently than gravity; claims to that effect in the original notes were removed.

**Statistics.** Use injection–recovery tests with simulated planets inserted into real data cubes to calibrate detection thresholds and false-alarm rates.

## Try it

- Guide: [For astrophysicists](../audiences/astrophysicists.md)
- Data: [data sources](../about/data-sources.md); reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- ALMA Partnership et al. (2015). The 2014 ALMA Long Baseline Campaign: first results from high angular resolution observations toward the HL Tau region. *The Astrophysical Journal Letters* 808, L3.
- Andrews, S. M. et al. (2018). The Disk Substructures at High Angular Resolution Project (DSHARP). I. Motivation, sample, calibration, and overview. *The Astrophysical Journal Letters* 869, L41.
- Flock, M. et al. (2015). Gaps, rings, and non-axisymmetric structures in protoplanetary disks: from simulations to ALMA observations. *Astronomy & Astrophysics* 574, A68.
- Haffert, S. Y. et al. (2019). Two accreting protoplanets around the young star PDS 70. *Nature Astronomy* 3, 749.
- Izquierdo, A. F. et al. (2021). The Disc Miner. I. A statistical framework to detect and quantify kinematical perturbations driven by young planets in discs. *Astronomy & Astrophysics* 650, A179.
- Keppler, M. et al. (2018). Discovery of a planetary-mass companion within the gap of the transition disk around PDS 70. *Astronomy & Astrophysics* 617, A44.
- Pinte, C. et al. (2018). Kinematic evidence for an embedded protoplanet in a circumstellar disk. *The Astrophysical Journal Letters* 860, L13.
- Pinte, C. et al. (2019). Kinematic detection of a planet carving a gap in a protoplanetary disk. *Nature Astronomy* 3, 1109.
- Teague, R. et al. (2018). A kinematical detection of two embedded Jupiter-mass planets in HD 163296. *The Astrophysical Journal Letters* 860, L12.
- Teague, R. et al. (2025). exoALMA. I. Science goals, project design, and data products. *The Astrophysical Journal Letters* (exoALMA focus issue).
