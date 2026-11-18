# D10 — Caves and buried masses mapped by gravity

> **In one sentence:** Spacecraft flying over the Moon and Mars feel tiny changes in gravity caused by what is underground, so careful analysis of their tracking data can point to hidden lava tubes and buried dense rock.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (more caves and buried masses can be found in existing data). Lunar cave conduits and gravity-based lava-tube candidates are 🔵 **Level 2 — Strong evidence**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine two friends riding bikes one behind the other, holding a long, stretchy rope between them. When the front bike rolls over a bump, it speeds up or slows down a tiny bit, and the rope stretches. The back rider can feel it!

NASA's GRAIL mission sent two small spacecraft, nicknamed Ebb and Flow, around the Moon, one behind the other. They measured the distance between them extremely precisely. Where the Moon has heavy rock underground, gravity pulls a bit harder and the front spacecraft speeds up. Where there is an empty cave, gravity pulls a bit less. By mapping these tiny changes, scientists made the best gravity map of any world except Earth. Some of the clues may be giant lava tubes — long caves made by ancient rivers of lava. Future astronauts might even live in them someday, because caves protect from radiation and temperature swings.

## The big idea

Gravity depends on mass. Dense rock pulls slightly harder; empty spaces pull slightly less. A spacecraft orbiting low over a moon or planet speeds up and slows down by tiny amounts as it passes over these features.

GRAIL (2011–2012) measured the changing distance between its two spacecraft with a radio link precise to well below a micrometer per second in range rate. This produced a lunar gravity map with features only a few kilometers across. Scientists have used it to study the Moon's crust, ancient impact basins, buried volcanic dikes, and possible lava tubes.

Gravity maps are usually expressed as a sum of smooth global patterns called spherical harmonics. To keep the map from being swamped by noise at the finest scales, analysts add a mathematical constraint (often based on the "Kaula rule", which describes how gravity signals typically get weaker at smaller scales). This is a **trade-off between detail and noise**, not hiding information. Local analysis methods, such as working directly with gravity gradients or the original tracking data along specific orbits, can bring out sharper features in particular places.

## What we already know

- 🟢 **Level 1 — Confirmed.** GRAIL produced a high-resolution global gravity field of the Moon showing a highly fractured crust (Zuber et al. 2013).
- 🟢 **Level 1 — Confirmed.** Gravity gradiometry from GRAIL revealed long, linear buried intrusions (ancient dikes) not visible at the surface (Andrews-Hanna et al. 2013).
- 🟢 **Level 1 — Confirmed.** Pits that look like collapsed lava-tube "skylights" have been imaged on the Moon (Haruyama et al. 2009) and possible cave skylights on Mars (Cushing et al. 2007).
- 🔵 **Level 2 — Strong evidence.** GRAIL gravity shows several long, narrow mass deficits consistent with large empty lava tubes (Chappaz et al. 2017).
- 🔵 **Level 2 — Strong evidence.** Radar sounder data suggest an intact lava tube near the Marius Hills pit (Kaku et al. 2017).
- 🔵 **Level 2 — Strong evidence.** Reprocessed Lunar Reconnaissance Orbiter radar data indicate a cave conduit tens of meters long extending from the Mare Tranquillitatis pit; the authors call an empty lava tube the most likely explanation (Carrer et al. 2024).
- 🟢 **Level 1 — Confirmed.** Gravity measured by OSIRIS-REx showed that asteroid Bennu's interior mass is not uniform (Scheeres et al. 2020).

## What is still open

**Can targeted re-analysis of raw spacecraft tracking data reveal more lava tubes, voids and dense buried bodies on the Moon, Mars and asteroids?**

The detection limits depend on the size and depth of the feature and on the spacecraft's altitude. Lava tubes kilometers wide are within GRAIL's reach. Smaller caves, like the Mare Tranquillitatis conduit, need radar or imaging.

## How you could test it

1. **Download data** from NASA's Planetary Data System Geosciences Node: GRAIL gravity models and Level-1B ranging data, and similar products for Mars missions.
2. **Pick targets** where surface clues (sinuous rilles, pits, skylights) suggest lava tubes.
3. **Compute gravity gradients** or use local (regional) inversion over those targets.
4. **Model a buried cylinder** (an idealized tube) and predict its signal for different widths and depths.
5. **Compare** predicted and observed signals; test whether a tube model fits significantly better than no tube.
6. **Combine evidence** with radar and imaging data before calling something a cave.

## How we could be wrong

- **Other low-density features.** Thick regolith, porous crust or buried craters can also cause mass deficits.
- **Edge effects and noise.** Local inversions can create stripes or rings along orbit tracks. Test with simulated data.
- **Altitude limits.** Signals from features much smaller than the spacecraft altitude are strongly smoothed out.
- **A clear "no" result.** If a feature that should be detectable (by its predicted size) produces no gravity signal above the noise, the tube is smaller, deeper or partly filled.

## For experts

**Buried cylinder.** For an infinitely long horizontal cylinder of radius *R* and density contrast Δρ, with its axis at depth *z*, the peak vertical gravity anomaly at the surface is

$$ \Delta g_{\max} = \frac{2\pi G\,\Delta\rho\,R^2}{z}. $$

For an empty tube in basalt (Δρ ≈ −3100 kg m⁻³), *R* = 500 m and *z* = 1 km, Δ*g*<sub>max</sub> ≈ −33 mGal at the surface. At spacecraft altitude *h*, the anomaly is attenuated and broadened (∝ 1/(*z* + *h*) with a width of order *z* + *h*).

**Spherical harmonics and regularization.** The potential is expanded to degree *ℓ*<sub>max</sub>; the half-wavelength resolution at the surface is about π*R*/*ℓ*. A Kaula-type constraint, with power ∝ *ℓ*⁻ⁿ, acts as a prior that stabilizes the least-squares solution where data are weak. Removing the constraint does not create information; it mainly increases noise. Localized solutions (for example, using gradients or Slepian localization) are the appropriate way to sharpen specific regions.

**Original notes.** The source notes attributed gravity to an alternative "flux shadowing" mechanism and proposed a special boundary filter. Standard Newtonian gravity fully describes these measurements, so that framing was removed.

## Try it

- Guide: [For physicists](../audiences/physicists.md)
- Data: [data sources](../about/data-sources.md); reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Andrews-Hanna, J. C. et al. (2013). Ancient igneous intrusions and early expansion of the Moon revealed by GRAIL gravity gradiometry. *Science* 339, 675.
- Carrer, L. et al. (2024). Radar evidence of an accessible cave conduit on the Moon below the Mare Tranquillitatis pit. *Nature Astronomy* 8, 1119.
- Chappaz, L. et al. (2017). Evidence of large empty lava tubes on the Moon using GRAIL gravity. *Geophysical Research Letters* 44, 105. doi:10.1002/2016GL071588
- Cushing, G. E. et al. (2007). THEMIS observes possible cave skylights on Mars. *Geophysical Research Letters* 34, L17201.
- Haruyama, J. et al. (2009). Possible lunar lava tube skylight observed by SELENE cameras. *Geophysical Research Letters* 36, L21206.
- Kaku, T. et al. (2017). Detection of intact lava tubes at Marius Hills on the Moon by SELENE (Kaguya) Lunar Radar Sounder. *Geophysical Research Letters* 44, 10155. doi:10.1002/2017GL074998
- Kaula, W. M. (1966). *Theory of Satellite Geodesy.* Blaisdell.
- Scheeres, D. J. et al. (2020). Heterogeneous mass distribution of the rubble-pile asteroid (101955) Bennu. *Science Advances* 6, eabc3350.
- Zuber, M. T. et al. (2013). Gravity field of the Moon from the Gravity Recovery and Interior Laboratory (GRAIL) mission. *Science* 339, 668.
