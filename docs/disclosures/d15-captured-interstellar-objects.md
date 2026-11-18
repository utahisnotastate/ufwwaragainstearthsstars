# D15 — Captured interstellar objects already orbiting the Sun

> **In one sentence:** A few small bodies in our Solar System orbit the Sun backwards or nearly over its poles, and some scientists have proposed that a few of them were captured from other stars long ago — an idea that is still debated and can be tested.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (some retrograde or polar objects are captured interstellar bodies). The unusual orbits themselves are 🟢 **Level 1 — Confirmed**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine a big roundabout where all the cars drive the same way. Suddenly you see a car driving the opposite way! Or one driving straight across the middle! You would wonder where it came from.

In our Solar System, almost all planets and asteroids go around the Sun in the same direction, on nearly flat paths. That is because they all formed from one flat, spinning disk of gas and dust. But a few small objects go **backwards** (we call this **retrograde**) or nearly straight over the Sun's poles. One famous example is an asteroid named **Kaʻepaokaʻawela**. It shares Jupiter's orbit but goes the opposite way! Some scientists think a few objects like this might have been captured from other stars a very long time ago. Other scientists think they came from the far edges of our own Solar System. Finding out who is right is a real science puzzle.

## The big idea

The Sun formed in a cluster with many other stars. Back then, stars passed close to each other, and small bodies could be swapped between systems. Some scientists estimate that a small fraction of objects in the outer Solar System could be captured "immigrants".

How could we spot one? Orbits change over billions of years, so there is no simple label. But some orbits are hard to make from the normal flat disk. Retrograde orbits and nearly polar orbits stand out. Astronomers also use a quantity called the **Tisserand parameter**, which stays nearly constant for a small body even as Jupiter's gravity changes its orbit. Objects that formed in the main asteroid belt usually have a Tisserand parameter above 3 with respect to Jupiter. Comets from the far Oort Cloud often have values below 2, and backwards orbits have negative values.

However, unusual orbits can also come from our own Solar System — for example from the Oort Cloud, or from a planet's influence over time. So an unusual orbit alone is not proof of an interstellar origin. Composition (what the object is made of) may help. The interstellar comet 2I/Borisov, for example, had much more carbon monoxide than most comets.

## What we already know

- 🟢 **Level 1 — Confirmed.** Asteroid (514107) **Kaʻepaokaʻawela** (2015 BZ509) shares Jupiter's orbit but moves retrograde, with inclination ≈ 163° (Wiegert, Connors & Veillet 2017).
- 🟢 **Level 1 — Confirmed.** Computed from JPL orbital elements (*a* ≈ 5.14 au, *e* ≈ 0.38, *i* ≈ 163°), its Tisserand parameter with respect to Jupiter is *T*<sub>J</sub> ≈ −0.75. (The original notes quoted −1.39; we corrected it.)
- 🔵 **Level 2 — Strong evidence, contested.** Namouni & Morais (2018) used backward simulations to argue that Kaʻepaokaʻawela has been on its retrograde orbit since the Solar System's birth and was therefore captured from interstellar space.
- 🔵 **Level 2 — Strong evidence for the opposing view.** Morbidelli, Batygin, Brasser & Raymond (2020) argued there is no evidence for trapped interstellar planetesimals, because such populations would have needed to be implausibly large; they point to the Oort Cloud and Halley-type comets as more likely sources. A reply defending the interstellar view was posted in 2020 (arXiv:2009.09773). The debate continues.
- 🟢 **Level 1 — Confirmed.** Trans-Neptunian objects with very tilted orbits exist, including "Drac" (2008 KV42, inclination ≈ 103°; Gladman et al. 2009) and "Niku" (2011 KT19, inclination ≈ 110°; since officially named 471325 Taowu). Niku, Drac and several other highly inclined objects appear to share a common orbital plane (Chen et al. 2016).
- 🟢 **Level 1 — Confirmed.** "Damocloids" are inactive bodies on comet-like, often retrograde, orbits (Jewitt 2005).
- 🟢 **Level 1 — Confirmed.** Interstellar comet 2I/Borisov was unusually rich in carbon monoxide (Bodewits et al. 2020; Cordiner et al. 2020), showing that interstellar bodies can differ chemically from Solar System comets.
- 🔵 **Level 2 — Strong evidence.** Studies of capture during close encounters show that capture is possible but rare; estimates of how many captured objects remain today vary widely (Siraj & Loeb 2019; Napier, Adams & Batygin 2021).

## What is still open

**Are some retrograde or polar objects in today's Solar System really captured from other stars, and what measurement could tell them apart from objects that formed here?**

## How you could test it

1. **Build a list** of retrograde and high-inclination objects from the JPL Small-Body Database or the Minor Planet Center (for example, inclination above 90°, or Tisserand parameter below 2).
2. **Compute the Tisserand parameter** for each object with respect to Jupiter (and Neptune for distant objects).
3. **Group the objects** by orbit type: Jupiter co-orbitals, Centaurs, Damocloids, trans-Neptunian objects.
4. **Collect colors and spectra** from published surveys, and compare each group with comets and asteroids of known origin.
5. **Run orbit simulations** backward and forward with many slightly different starting orbits ("clones") to measure how long each object stays on its orbit. Very long-lived retrograde orbits are the most interesting.
6. **Propose observations** of the best candidates, such as spectra to look for unusual ices or colors.

## How we could be wrong

- **Chaos limits backward simulations.** Orbits become unpredictable over long times, so "it has always been here" can be hard to prove.
- **Our own Oort Cloud** can supply retrograde objects, as can planets' long-term effects.
- **Small samples.** With only a few unusual objects, statistical arguments are weak.
- **No clear chemical fingerprint yet.** We do not yet know a reliable test that marks a body as interstellar from its color or reflectance alone. The original notes suggested specific spectral and polarization "fingerprints"; we found no published support for them, so they were removed.
- **A clear "no" result.** If careful simulations show that a candidate's orbit is easily produced from the Oort Cloud, and its composition matches Solar System comets, there is no need for an interstellar origin.

## For experts

**Tisserand parameter** with respect to a planet of semi-major axis *a*<sub>P</sub>:

$$ T_P = \frac{a_P}{a} + 2\sqrt{\frac{a}{a_P}\,(1-e^2)}\,\cos i. $$

For Kaʻepaokaʻawela with *a*<sub>J</sub> = 5.2026 au, *a* ≈ 5.14 au, *e* ≈ 0.38, *i* ≈ 163°:
*a*<sub>J</sub>/*a* ≈ 1.012; 2√(0.988 × 0.855) cos 163° ≈ 2 × 0.919 × (−0.956) ≈ −1.758; so *T*<sub>J</sub> ≈ −0.75.

*T*<sub>P</sub> is derived from the Jacobi integral of the circular restricted three-body problem and is approximately conserved through close encounters with that planet. Common dynamical classes: *T*<sub>J</sub> > 3 (main belt), 2 < *T*<sub>J</sub> < 3 (Jupiter-family comets), *T*<sub>J</sub> < 2 (Halley-type and long-period comets, Damocloids), and *T*<sub>J</sub> < 0 for strongly retrograde orbits.

**Capture.** Permanent capture of an unbound body requires energy loss, typically through a three-body interaction (for example with Jupiter, or with the Sun and a passing star in the birth cluster). Capture cross-sections fall steeply with the incoming hyperbolic excess speed *v*<sub>∞</sub>, so low-speed objects from the birth cluster dominate any captured population.

**Retrograde co-orbital stability.** Retrograde 1:1 resonances with Jupiter can be stable over long times because encounter speeds are high and the interaction geometry differs from prograde co-orbitals (Wiegert et al. 2017; Namouni & Morais 2018).

The project's code module `fdastro.tisserand` computes the Tisserand parameter and helps filter orbit lists; see the tutorial for current functions.

## Try it

- Tutorial: [Tisserand and backwards orbits](../tutorials/t05-tisserand-and-backwards-orbits.md)
- Lesson: [Backwards orbits](../lessons/l06-backwards-orbits.md)
- Code module: `fdastro.tisserand`
- Related: [D14 — Interstellar visitors in unlinked asteroid data](d14-interstellar-objects-unlinked-data.md)
- Data: [data sources](../about/data-sources.md); reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Bodewits, D. et al. (2020). The carbon monoxide-rich interstellar comet 2I/Borisov. *Nature Astronomy* 4, 867.
- Chen, Y.-T. et al. (2016). Discovery of a new retrograde trans-Neptunian object: hint of a common orbital plane for low semimajor axis, high-inclination TNOs and Centaurs. *The Astrophysical Journal Letters* 827, L24.
- Cordiner, M. A. et al. (2020). Unusually high CO abundance of the first active interstellar comet. *Nature Astronomy* 4, 861.
- Gladman, B. et al. (2009). Discovery of the first retrograde transneptunian object. *The Astrophysical Journal Letters* 697, L91.
- Jewitt, D. (2005). A first look at the Damocloids. *The Astronomical Journal* 129, 530.
- Morbidelli, A., Batygin, K., Brasser, R. & Raymond, S. N. (2020). No evidence for interstellar planetesimals trapped in the Solar System. *Monthly Notices of the Royal Astronomical Society Letters* 497, L46. arXiv:2006.04534
- Namouni, F. & Morais, M. H. M. (2018). An interstellar origin for Jupiter's retrograde co-orbital asteroid. *Monthly Notices of the Royal Astronomical Society Letters* 477, L117. arXiv:1805.09013
- Napier, K. J., Adams, F. C. & Batygin, K. (2021). On the capture of interstellar objects by our Solar System. *The Planetary Science Journal* 2, 53.
- Siraj, A. & Loeb, A. (2019). Identifying interstellar objects trapped in the Solar System through their orbital parameters. *The Astrophysical Journal Letters* 872, L10.
- Wiegert, P., Connors, M. & Veillet, C. (2017). A retrograde co-orbital asteroid of Jupiter. *Nature* 543, 687.
- Reply defending the interstellar origin of high-inclination Centaurs (2020). "On the interstellar origin of high-inclination Centaurs." arXiv:2009.09773
