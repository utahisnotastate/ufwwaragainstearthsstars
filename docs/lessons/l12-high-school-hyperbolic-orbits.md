# Lesson 12 — High School: Speeds of Interstellar Visitors

| | |
|---|---|
| **Ages** | 15–18 |
| **Time** | 50–60 minutes |
| **Group size** | Individuals or pairs |
| **Connects to** | [D14 — Interstellar visitors in unlinked asteroid data](../disclosures/d14-interstellar-objects-unlinked-data.md) and [D15 — Captured interstellar objects](../disclosures/d15-captured-interstellar-objects.md) |

## Big question

**Using only two numbers from an orbit, can we work out how fast an interstellar object was moving before it met the Sun?**

## For young readers

An object from another star comes in fast, swings around the Sun, and leaves. Its path is an open curve called a **hyperbola**. Astronomers describe the curve with two numbers: how close it gets to the Sun, and how "open" the curve is. From just those two numbers, and the strength of the Sun's gravity, you can calculate how fast it was going when it was still far away. In this lesson you will do that calculation for all three known interstellar visitors.

## Learning goals

Students will be able to:

1. Use conservation of energy to relate speed and distance in an orbit.
2. Calculate the hyperbolic excess speed *v*∞ from perihelion distance *q* and eccentricity *e*.
3. Decide whether a body at a given distance and speed is bound to the Sun.

## NGSS alignment

- **HS-ESS1-4** — mathematical representations of the motion of orbiting objects.
- **HS-PS2-4** — Newton's law of universal gravitation.

## Materials

- Calculator or spreadsheet
- This worksheet

## Constants

| Quantity | Value |
|---|---|
| Sun's gravitational parameter, *GM*☉ | 1.327 × 10²⁰ m³ s⁻² |
| Astronomical unit (au) | 1.496 × 10¹¹ m |
| Light-year | 9.461 × 10¹⁵ m |
| Seconds in a year | 3.156 × 10⁷ s |

## Background

For an object moving only under the Sun's gravity, the **specific orbital energy** (energy per kilogram) is constant:

ε = *v*²/2 − *GM*/*r*

- If ε < 0, the object is **bound** (ellipse).
- If ε > 0, the object is **unbound** (hyperbola) and keeps a speed *v*∞ far from the Sun, with ε = *v*∞²/2.

For a hyperbola with perihelion distance *q* and eccentricity *e* > 1, it can be shown that

***v*∞ = √[ *GM* (*e* − 1) / *q* ]**

and the speed at perihelion is

***v*_q = √[ *GM* (1 + *e*) / *q* ]**.

You can check that these two agree with energy conservation: *v*_q² − 2*GM*/*q* = *v*∞².

## Steps

1. **Escape speed at 1 au.** Calculate *v*_esc = √(2*GM*/*r*) at *r* = 1 au. Give your answer in km/s.
2. **Bound or not?** An object is seen at 1 au moving at 50 km/s relative to the Sun. Is it bound? Explain using ε.
3. **Interstellar visitors.** Use the table to calculate *v*∞ (in km/s) for each object. Convert *q* to metres first.

| Object | *q* (au) | *e* |
|---|---|---|
| 1I/ʻOumuamua | 0.255 | 1.201 |
| 2I/Borisov | 2.007 | 3.36 |
| 3I/ATLAS | 1.357 | 6.14 |

4. **Perihelion speed.** Calculate *v*_q for 1I/ʻOumuamua.
5. **Bending angle.** A hyperbolic orbit turns the object's direction by an angle δ = 2 arcsin(1/*e*). Calculate δ for each object. Which visitor was bent the most by the Sun? Why?
6. **Travel time.** If 1I/ʻOumuamua kept moving at *v*∞ in a straight line, how many years would it take to travel 4.25 light-years (the distance to Proxima Centauri)?

## Discussion questions

1. Why does a larger eccentricity mean a larger *v*∞ for the same *q*?
2. Why is 3I/ATLAS bent much less than 1I/ʻOumuamua?
3. Real orbits are fitted from a few weeks of sky positions. Why might the eccentricity of a newly found object be uncertain at first?
4. Could a backwards (retrograde) object with *e* < 1 still have come from another star long ago? What evidence would you need? (See [D15](../disclosures/d15-captured-interstellar-objects.md).)

## Check for understanding (answer key for the teacher)

1. *v*_esc = √(2 × 1.327×10²⁰ / 1.496×10¹¹) = √(1.774×10⁹) ≈ 4.21×10⁴ m/s ≈ **42.1 km/s**.
2. ε = (5.0×10⁴)²/2 − 1.327×10²⁰/1.496×10¹¹ = 1.25×10⁹ − 8.87×10⁸ ≈ **+3.6×10⁸ J/kg > 0 → unbound**. (Equivalently, 50 km/s > 42.1 km/s.)
3. *v*∞:
   - 1I: *q* = 3.815×10¹⁰ m; *v*∞ = √(1.327×10²⁰ × 0.201 / 3.815×10¹⁰) = √(6.99×10⁸) ≈ **26.4 km/s**
   - 2I: *q* = 3.002×10¹¹ m; *v*∞ = √(1.327×10²⁰ × 2.36 / 3.002×10¹¹) = √(1.043×10⁹) ≈ **32.3 km/s**
   - 3I: *q* = 2.030×10¹¹ m; *v*∞ = √(1.327×10²⁰ × 5.14 / 2.030×10¹¹) = √(3.36×10⁹) ≈ **58.0 km/s**
   These match published values (about 26, 32 and 58 km/s).
4. *v*_q (1I) = √(1.327×10²⁰ × 2.201 / 3.815×10¹⁰) = √(7.66×10⁹) ≈ **87.5 km/s**.
5. δ: 1I: 2 arcsin(1/1.201) = 2 arcsin(0.833) ≈ **113°**; 2I: 2 arcsin(0.298) ≈ **35°**; 3I: 2 arcsin(0.163) ≈ **19°**. ʻOumuamua was bent most, because it passed closer to the Sun and moved more slowly relative to the Sun's pull (lower *e*).
6. 4.25 ly = 4.02×10¹⁶ m. Time = 4.02×10¹⁶ / 2.64×10⁴ ≈ 1.52×10¹² s ≈ **48,000 years**.

## Extension

- Derive *v*∞ = √[*GM*(*e* − 1)/*q*] from ε = −*GM*/(2*a*) and *q* = *a*(1 − *e*), noting that *a* < 0 for a hyperbola.
- Look up the current orbital solutions for these objects in the JPL Small-Body Database and recompute. How much do your answers change?
- Programming students: [Tutorial 2](../tutorials/t02-orbits-ellipses-and-hyperbolas.md) does this calculation with the `fdastro` package and plots the orbits.

## For the teacher: the science behind it

**Derivation.** For a conic with semi-major axis *a* and eccentricity *e*, the vis-viva equation gives *v*² = *GM*(2/*r* − 1/*a*). For a hyperbola, *a* < 0 and *q* = *a*(1 − *e*), so −1/*a* = (*e* − 1)/*q*. As *r* → ∞, *v*∞² = −*GM*/*a* = *GM*(*e* − 1)/*q*. At *r* = *q*, *v*_q² = *GM*(2/*q* + (*e* − 1)/*q*) = *GM*(1 + *e*)/*q*. The asymptotes make angle θ∞ with the perihelion direction where cos θ∞ = −1/*e*, giving the total turning angle δ = 2 arcsin(1/*e*).

**Values used (🟢 Level 1).** The orbital elements are rounded values from published solutions (Meech et al. 2017; Guzik et al. 2020; Seligman et al. 2025). Current solutions are in the JPL Small-Body Database and at the Minor Planet Center.

**Common errors:** forgetting to convert au to metres; using *e* + 1 for *v*∞; mixing km/s and m/s.

### References

- Meech, K. J., et al. (2017). *Nature*, 552, 378–381. doi:10.1038/nature25020
- Guzik, P., et al. (2020). *Nature Astronomy*, 4, 53–57. doi:10.1038/s41550-019-0931-8
- Seligman, D. Z., et al. (2025). *The Astrophysical Journal Letters*, 989, L36. arXiv:2507.02757
- Curtis, H. D. *Orbital Mechanics for Engineering Students* (any edition), chapter on hyperbolic trajectories.

## Connects to

- Disclosures: [D14](../disclosures/d14-interstellar-objects-unlinked-data.md), [D15](../disclosures/d15-captured-interstellar-objects.md)
- Next lesson: [Lesson 13 — University lab: fitting an orbit](l13-university-lab-orbit-fitting.md)
