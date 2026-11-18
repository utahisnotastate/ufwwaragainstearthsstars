# D01 — Unseen planets in the far Solar System

> **In one sentence:** A large planet far beyond Neptune would be very hard to see, but its gravity would gently pull on everything else — and very precise tracking of spacecraft and pulsars can measure that pull.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (main open question). Each claim below has its own label.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine you are standing on a big trampoline in a dark room. A heavy bowling ball is rolling around somewhere on it. You cannot see the ball. But you can feel your feet wobble when the ball moves!

Our Solar System is a bit like that trampoline. A big, dark planet very far from the Sun would be too faint to see easily. But its gravity would tug on spacecraft, planets and even the way we time signals from faraway stars. Scientists measure those signals very carefully. If they find a tiny, unexplained tug, it could point to a hidden planet. So far, nobody has found one this way — but the search is real, and it is getting better.

## The big idea

Far beyond Neptune is a cold, dim region full of icy objects. Some of these objects have orbits that seem to line up in surprising ways. In 2016, Konstantin Batygin and Michael Brown suggested that an unseen planet, now often called "Planet Nine", might be shaping those orbits. Their later estimates put it at roughly five to ten times Earth's mass, hundreds of times farther from the Sun than Earth.

A planet that far away is extremely faint. Sunlight has to travel out to it, bounce off, and travel all the way back. The light we receive drops roughly with the fourth power of distance, so doubling the distance makes it about sixteen times fainter. That is why telescopes have not yet found it, if it exists.

There is a second way to search. Any planet pulls on everything else in the Solar System. Engineers track spacecraft such as Cassini with radio signals so precise that they can measure distances to within tens of meters across more than a billion kilometers. Radio astronomers also time the pulses of millisecond pulsars — spinning dead stars that tick like clocks. To time pulsars well, they must know exactly where the Sun's center of mass (the barycenter) is. An unknown planet would shift that point a tiny bit. Both kinds of data can be used to test whether a hidden planet is there.

## What we already know

- 🟢 **Level 1 — Confirmed.** Some distant trans-Neptunian objects have unusual, high-eccentricity orbits that do not come close to Neptune (for example 2012 VP113; Trujillo & Sheppard 2014).
- 🔵 **Level 2 — Strong evidence, still debated.** The clustering of the most distant orbits has been interpreted as the signature of an unseen planet (Batygin & Brown 2016; Batygin et al. 2019). Other teams argue that the clustering may be partly caused by where surveys happened to look (Napier et al. 2021).
- 🟢 **Level 1 — Confirmed.** Spacecraft radio ranging constrains where a Planet Nine-like body could be. Fienga et al. (2016) used Cassini ranging to Saturn to exclude part of the proposed orbit. Holman & Payne (2016) and later reanalyses found that the exact limits depend on the planetary ephemeris model used, so the excluded regions are less sharp than first reported.
- 🟢 **Level 1 — Confirmed.** Pulsar timing arrays can measure masses of Solar System bodies and place upper limits on unknown masses. Caballero et al. (2018) used the International Pulsar Timing Array to improve mass measurements of the planetary systems and to give the first generic limits on unknown objects from real pulsar data.
- 🟢 **Level 1 — Confirmed.** Large new surveys keep finding big distant bodies. In October 2026, Vera C. Rubin Observatory reported **2026 ED138**, a trans-Neptunian dwarf-planet candidate estimated at roughly 600–1,500 km across. It is a candidate, not yet a confirmed dwarf planet.

## What is still open

**Can the combined data from spacecraft tracking, planetary ephemerides and pulsar timing narrow down — or rule out — where an undiscovered distant planet could be?**

No single data set is enough today. The useful question is how much of the sky and mass range each data set can exclude, and whether combining them leaves a small enough region for telescopes to search.

## How you could test it

1. **Start from published orbit predictions.** Use the predicted mass, distance and orbit ranges from the Planet Nine literature (Brown & Batygin 2021 is a good starting point).
2. **Compute the expected pull.** For each trial position, compute the extra (tidal) acceleration the planet would cause on Saturn, Jupiter or a spacecraft. This is a simple Newtonian calculation.
3. **Compare with measurement precision.** Compare that effect with the published residuals of a modern ephemeris (JPL DE or INPOP series) and with pulsar timing array sensitivity curves.
4. **Map what is excluded.** Mark the sky positions where the planet would have produced a detectable signal that is not seen.
5. **Hand the allowed region to observers.** Wide-field surveys such as Rubin can then focus on the regions that remain allowed.

Public data: pulsar timing data from NANOGrav, the European Pulsar Timing Array and the International Pulsar Timing Array; planetary ephemerides from JPL and IMCCE; trans-Neptunian orbits from the Minor Planet Center. See [data sources](../about/data-sources.md).

## How we could be wrong

- **Model choices matter.** Ephemeris fits include hundreds of asteroid masses and a ring model for the Kuiper Belt. A small error in these can mimic or hide a distant planet's pull. This is exactly why the early Cassini limits were revised.
- **"Unexplained residuals" are usually not planets.** Tiny leftover differences in tracking data more often come from spacecraft thermal effects, solar plasma delay, clock errors or unmodeled asteroids. These must be ruled out before claiming anything.
- **The planet might not exist.** If survey selection effects explain the orbital clustering, there may be nothing to find. A full-sky survey that finds no such planet to the needed depth would show the idea is wrong.
- **What this project removed.** The original notes claimed that two specific hidden masses sit in Taurus and Orion. We found no published evidence for this, so we removed it.

## For experts

**Reflected-light flux.** For a body at heliocentric distance *r* observed from distance Δ ≈ *r*, reflected flux scales as

$$ F \propto \frac{p\,R^2}{r^2\,\Delta^2} \approx \frac{p\,R^2}{r^4}, $$

so the magnitude penalty from 50 au to 500 au is 10 log₁₀(10) = 10 magnitudes before thermal emission is considered.

**Tidal acceleration on a planet.** A distant mass *M* at distance *d* produces a differential (tidal) acceleration across the inner Solar System of order

$$ a_{\rm tid} \sim \frac{G M\, r}{d^3}, $$

where *r* is the heliocentric distance of the tracked body. For *M* = 5 M⊕, *d* = 500 au and *r* = 9.5 au (Saturn), *a*<sub>tid</sub> ≈ 7 × 10⁻¹⁵ m s⁻². Over ten years this corresponds to a displacement of order 0.5 *a* *t*² ≈ 300 m, which is comparable to the tens-of-meters precision of Cassini ranging. This order-of-magnitude estimate shows why ranging is sensitive, and also why systematic errors at the 10–100 m level matter.

**Pulsar timing.** An error δ**b** in the assumed Solar System barycenter produces a timing residual

$$ \delta t = -\frac{\delta\mathbf{b}\cdot\hat{\mathbf{n}}}{c} $$

for a pulsar in direction **n̂**. Because the error is common to all pulsars with a dipolar sky pattern, it can be separated from intrinsic pulsar noise using many pulsars. See Caballero et al. (2018) and the Bayesian method of Guo, Lee & Caballero (arXiv:1802.05452).

**Practical note.** Do not filter out low-frequency residuals arbitrarily. Instead, add a parameterized perturber to the timing or ephemeris model and compare models with a proper likelihood ratio or Bayesian evidence, accounting for red noise.

## Try it

- Lesson: [Finding what we cannot see](../lessons/l01-finding-what-we-cannot-see.md)
- Tutorial: [Orbits, ellipses and hyperbolas](../tutorials/t02-orbits-ellipses-and-hyperbolas.md) (orbit basics used here)
- Code module: `fdastro.kepler` (two-body orbits)
- If you think you have found something: [How to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Batygin, K. & Brown, M. E. (2016). Evidence for a distant giant planet in the Solar System. *The Astronomical Journal* 151, 22. arXiv:1601.05438
- Batygin, K., Adams, F. C., Brown, M. E. & Becker, J. C. (2019). The Planet Nine hypothesis. *Physics Reports* 805, 1. arXiv:1902.10103
- Brown, M. E. & Batygin, K. (2021). The orbit of Planet Nine. *The Astronomical Journal* 162, 219.
- Caballero, R. N. et al. (2018). Studying the Solar system with the International Pulsar Timing Array. *Monthly Notices of the Royal Astronomical Society*. arXiv:1809.10744
- Fienga, A., Laskar, J., Manche, H. & Gastineau, M. (2016). Constraints on the location of a possible 9th planet derived from the Cassini data. *Astronomy & Astrophysics* 587, L8. arXiv:1602.06116
- Guo, Y. J., Lee, K. J. & Caballero, R. N. (2018). A dynamical approach in exploring the unknown mass in the Solar system using pulsar timing arrays. arXiv:1802.05452
- Holman, M. J. & Payne, M. J. (2016). Observational constraints on Planet Nine: Cassini range observations. *The Astronomical Journal* 152. arXiv:1604.03180
- Napier, K. J. et al. (2021). No evidence for orbital clustering in the extreme trans-Neptunian objects. *The Planetary Science Journal* 2, 59.
- Trujillo, C. A. & Sheppard, S. S. (2014). A Sedna-like body with a perihelion of 80 astronomical units. *Nature* 507, 471.
- Vera C. Rubin Observatory (October 2026). News release on the dwarf-planet candidate 2026 ED138. See rubinobservatory.org.
