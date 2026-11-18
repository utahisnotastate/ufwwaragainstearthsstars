# D11 — Trojan and co-orbital asteroids near Venus, Earth and Mars

> **In one sentence:** Some asteroids share an orbit with a planet, leading or trailing it around the Sun, and the ones that travel with Venus and Earth are hard to see because they stay close to the Sun's glare.
>
> **Evidence level:** 🟡 **Level 3 — Testable idea** (more inner-planet co-orbitals remain undiscovered). Earth and Mars Trojans are 🟢 **Level 1 — Confirmed**.
>
> *Last reviewed: November 2026.*

## For young readers

Imagine a fast river with a big boulder in it. Right behind the boulder, the water swirls in a calm spot. Leaves can get trapped there and spin around for a long time.

Planets make calm spots like that in their orbits around the Sun. Two of them are 60 degrees ahead of and behind the planet. Asteroids trapped there are called **Trojans**. Jupiter has thousands! Earth has two known Trojans, and Mars has more than ten. Venus has none that stay for a long time — as far as we know. The ones near Venus and Earth are hard to spot, because we have to look toward the twilight sky near the Sun, where it is bright and the asteroids are low on the horizon. There may be more waiting to be found.

## The big idea

When an asteroid has the same orbital period as a planet, it is called a **co-orbital**. Co-orbitals follow a few kinds of paths when seen from the planet's moving point of view:

- **Tadpole orbits** loop around the L4 or L5 points (60° ahead or behind). These are Trojans.
- **Horseshoe orbits** sweep around both points in a long horseshoe shape.
- **Quasi-satellite orbits** stay near the planet itself and seem to circle it, although they actually orbit the Sun.

For Venus and Earth, these objects are hard to find. Earth's L4 and L5 points sit about 60° from the Sun in the sky, so they are visible only in twilight, low on the horizon. Venus co-orbitals never get more than about 47° from the Sun as seen from Earth. Most surveys look farther from the Sun, where the sky is darker.

Recent dedicated twilight searches have begun to explore this region, and the Vera C. Rubin Observatory adds another powerful tool. The question is not whether these objects exist — some do — but how many are still unknown, and how long they stay.

## What we already know

- 🟢 **Level 1 — Confirmed.** **2010 TK7** was the first known Earth Trojan, roughly 300 m across (Connors, Wiegert & Veillet 2011).
- 🟢 **Level 1 — Confirmed.** **2020 XL5** is the second known Earth Trojan, about 1.2 km across, and expected to stay a Trojan for at least about 4,000 years (Santana-Ros et al. 2022). Both known Earth Trojans are temporary.
- 🟢 **Level 1 — Confirmed.** OSIRIS-REx searched Earth's L4 region in February 2017 on its way to asteroid Bennu and found no new Trojans (NASA, 2017).
- 🟢 **Level 1 — Confirmed.** Mars has more than ten known Trojans, most in a cluster near L5 called the Eureka family, which appears to be rich in the mineral olivine (Christou 2013; Borisov et al. 2017).
- 🟢 **Level 1 — Confirmed.** Venus has known temporary co-orbitals, including the quasi-satellite 2002 VE68 (Mikkola et al. 2004) and the temporary Trojan 2013 ND15 (de la Fuente Marcos & de la Fuente Marcos 2014).
- 🔵 **Level 2 — Strong evidence.** A dust ring along Venus's orbit may be fed by an undiscovered population of Venus co-orbital asteroids (Pokorný & Kuchner 2019). A deep twilight survey placed strong limits on any stable Venus co-orbital population (Sheppard et al. 2022).
- 🟢 **Level 1 — Confirmed.** The same twilight survey discovered 2021 PH27, the asteroid with the smallest known orbit, and other objects inside Earth's orbit (Sheppard et al. 2022).

## What is still open

**How many asteroids share orbits with Venus, Earth and Mars, and are some of them hiding in twilight survey data or unlinked observations?**

## How you could test it

1. **Compute where to look.** Use the planet's orbit to compute the sky positions of its L4 and L5 points for each date.
2. **Gather archival detections** near those positions from public archives, including unlinked observations at the Minor Planet Center (see [D14](d14-interstellar-objects-unlinked-data.md)).
3. **Predict sky motion.** A co-orbital has nearly the same orbital period as the planet. Use this to predict how it moves across the sky and to link observations from different nights.
4. **Fit orbits** to linked observations and check whether the semi-major axis matches the planet's.
5. **Integrate the orbit** forward and backward to classify it as tadpole, horseshoe or quasi-satellite, and estimate how long it stays.
6. **Report** new objects and linkages to the Minor Planet Center.

## How we could be wrong

- **Low altitude, bad seeing.** Twilight observations are low on the sky and noisy, which leads to false detections.
- **Mislinking.** Combining observations of different objects can produce a fake co-orbital orbit. Require multiple nights and good residuals.
- **Short arcs.** A few nights of data often cannot pin down the semi-major axis well enough to prove a co-orbital state.
- **A clear "no" result.** Deep twilight surveys that find nothing set upper limits on how many co-orbitals of a given size exist.

## For experts

**Elongation of triangular points.** For a planet at heliocentric distance *a*<sub>p</sub> and Earth at 1 au, the L4/L5 points lie 60° from the planet along its orbit. For Earth's own Trojans, the solar elongation of L4/L5 is 60°. For Venus co-orbitals (*a* ≈ 0.723 au), the maximum elongation is arcsin(0.723) ≈ 46°.

**Co-orbital dynamics.** In the circular restricted three-body problem, the Jacobi constant

$$ C_J = 2U(x,y,z) - (\dot x^2+\dot y^2+\dot z^2), \qquad U = \tfrac12(x^2+y^2) + \frac{1-\mu}{r_1} + \frac{\mu}{r_2}, $$

defines zero-velocity surfaces that bound the motion in the rotating frame. Tadpole and horseshoe orbits correspond to different ranges of *C*<sub>J</sub>. Real Earth and Venus co-orbitals are strongly perturbed by other planets and switch between orbit types on timescales of centuries to thousands of years.

**Sky motion.** Near the turning points of their libration, co-orbitals move slowly relative to the planet, but their apparent sky motion is still dominated by heliocentric motion and Earth's parallax. Linking algorithms should search a range of rates appropriate for *a* ≈ *a*<sub>p</sub>.

**Hype check.** The original notes claimed enormous metal value in these objects. Composition is known only for a few (for example, olivine-rich Mars Trojans), so that claim was removed.

The project's code module `fdastro.kepler` provides orbit propagation and element conversion used in these calculations.

## Try it

- Lesson: [Balance points in space](../lessons/l05-balance-points-in-space.md)
- Tutorial: [Orbits, ellipses and hyperbolas](../tutorials/t02-orbits-ellipses-and-hyperbolas.md)
- Tutorial: [Reading MPC observations](../tutorials/t04-reading-mpc-observations.md)
- Code module: `fdastro.kepler`
- Related: [D06](d06-earth-moon-trojan-points.md), [D14](d14-interstellar-objects-unlinked-data.md)
- Reporting: [how to report a discovery](../about/how-to-report-a-discovery.md)

## References

- Borisov, G. et al. (2017). The olivine-dominated composition of the Eureka family of Mars Trojan asteroids. *Monthly Notices of the Royal Astronomical Society* 466, 489.
- Christou, A. A. (2013). Orbital clustering of martian Trojans: an asteroid family in the inner solar system? *Icarus* 224, 144.
- Connors, M., Wiegert, P. & Veillet, C. (2011). Earth's Trojan asteroid. *Nature* 475, 481.
- de la Fuente Marcos, C. & de la Fuente Marcos, R. (2014). Asteroid 2013 ND15: Trojan companion to Venus, PHA to the Earth. *Monthly Notices of the Royal Astronomical Society* 439, 2970.
- Mikkola, S. et al. (2004). Asteroid 2002 VE68, a quasi-satellite of Venus. *Monthly Notices of the Royal Astronomical Society* 351, L63.
- NASA / OSIRIS-REx mission team (2017). OSIRIS-REx Earth-Trojan asteroid search results (mission news release, March 2017).
- Pokorný, P. & Kuchner, M. (2019). Co-orbital asteroids as the source of Venus's zodiacal dust ring. *The Astrophysical Journal Letters* 873, L16.
- Santana-Ros, T. et al. (2022). Orbital stability analysis and photometric characterization of the second Earth Trojan asteroid 2020 XL5. *Nature Communications* 13, 447.
- Sheppard, S. S. et al. (2022). A deep and wide twilight survey for asteroids interior to Earth and Venus. *The Astronomical Journal* 164, 168. doi:10.3847/1538-3881/ac8cff
