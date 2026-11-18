# Lesson 11 — Moons That Make Planets Wobble

| | |
|---|---|
| **Ages** | 11–15 |
| **Time** | 50 minutes |
| **Group size** | Groups of 3 (walker, timer, recorder) |
| **Connects to** | [D12 — Exomoons from timing and duration wobbles](../disclosures/d12-exomoons-timing-duration.md) |

## Big question

**Can we find a moon around a planet in another solar system, even if the moon is too small to see?**

## For young readers

The Earth and the Moon pull on each other. They both spin around a balance point between them. So the Earth wobbles a tiny bit as the Moon goes around.

Planets around other stars can have moons too. We call them **exomoons**. No one has confirmed one yet!

Here is a clever trick. When a planet with a moon passes in front of its star, the wobble makes it arrive a little **early** or a little **late**. The wobble also makes it move a bit **faster** or **slower**, so it spends a bit **less** or **more** time crossing the star.

If you draw "early or late" on one side of a graph and "short or long" on the other, a moon makes the dots go around in a loop. That loop is a clue!

## Learning goals

Learners will be able to:

1. Explain that a planet and its moon orbit their shared balance point (barycenter).
2. Measure "early/late" timing and "short/long" crossing time in a model.
3. Explain why plotting the two together can reveal a hidden moon.

## NGSS alignment

- **MS-ESS1-2** — gravity and orbital motion.
- **MS-PS2-4** — gravitational interactions depend on mass.

## Materials

- A meter stick (or a 1 m dowel)
- Two balls of modeling clay: one large (the planet, about the size of a tennis ball) and one small (the moon, about the size of a grape)
- Masking tape for a large floor circle and a "star" strip (a 30 cm wide strip of tape across the circle)
- A stopwatch, or a phone that can record slow-motion video
- Graph paper

## Safety

- Walk slowly. Hold the meter stick at waist height. Keep a clear space around the walker.
- Rotate the stick slowly; stop if anyone feels dizzy.

## Steps

1. **Build the planet–moon pair.** Stick the big clay ball near one end of the meter stick and the small ball at the other end.
2. **Find the balance point.** Balance the stick on one finger. Mark the balance point with tape. This is the **barycenter**. It is much closer to the big ball. The walker always holds the stick here.
3. **Set up the "star."** Make a big circle on the floor (about 3 m across). Put a 30 cm wide tape strip across one part of the circle. This strip is the star. When the big clay ball passes over it, that is a transit.
4. **First, no moon.** Remove the small ball and hold the stick at the big ball. Walk the circle at a steady pace. The timer records the time each lap when the big ball **enters** and **leaves** the strip. Do 5 laps. The crossings should be evenly spaced and the same length.
5. **Now, with the moon.** Put the small ball back and hold the stick at the barycenter mark. Walk at the same steady pace while **slowly turning** the stick (about one full turn every 1–2 laps — it does not need to be exact). Record entry and exit times for 8–10 laps.
6. **Calculate.**
   - **Mid-time** of each crossing = (enter + leave) ÷ 2.
   - **Duration** = leave − enter.
   - Find the average time between mid-times. For each lap, how much **early** (−) or **late** (+) was it compared with the even schedule? This is the **timing wobble**.
   - For each lap, how much **shorter** (−) or **longer** (+) than average was the duration? This is the **duration wobble**.
7. **Graph.** Plot each lap as a dot with timing wobble across and duration wobble up. Connect the dots in lap order. Do they go around in a loop? (They often will, roughly.)

**Accessible version:** Use slow-motion phone video with audio beeps, or place a pressure-sensitive mat or a doorway light gate on the "star" strip. Learners can also do the tabletop version: a toy car carrying a small rotating dumbbell along a track.

## Discussion questions

1. Why is the barycenter closer to the big ball?
2. Why did the crossings become early and late when the moon was added?
3. Why did the crossing **length** change too?
4. Other things can make a planet early or late — for example, another planet pulling on it. Why is the loop pattern a better clue for a moon?

## Check for understanding (answers for the teacher)

| Question | Expected answer |
|---|---|
| What is a barycenter? | The balance point that two objects orbit around together. |
| What is a timing wobble (TTV)? | A transit happening earlier or later than an even schedule. |
| What is a duration wobble (TDV)? | A transit lasting shorter or longer than usual. |
| What pattern suggests a moon? | Timing and duration wobbles that are a quarter-cycle apart, tracing a loop when plotted together. |
| Has an exomoon been confirmed? | No, not as of November 2026. There are debated candidates. |

## Extension

- Make the moon heavier. Does the wobble get bigger? (Yes.)
- Older learners: try [Tutorial 8](../tutorials/t08-exomoon-timing-test.md), which tests real-style timing data for this pattern and estimates how often noise alone could fake it.

## For the teacher: the science behind it

**Barycentric wobble.** A planet of mass *M*ₚ with a moon of mass *M*ₛ at separation *a*ₛ orbits their common barycenter at distance *a*ₛ*M*ₛ/(*M*ₚ + *M*ₛ). This shifts the planet along its orbit (changing transit **timing**, TTV) and changes its sky-projected speed (changing transit **duration**, the velocity component TDV-V).

**The quadrature signature (🟢 Level 1 as theory).** Kipping (2009a, b) showed that for a moon on a circular, coplanar orbit, TTV ∝ sin(φ) and TDV-V ∝ cos(φ), where φ is the moon's orbital phase at each transit — a 90° (π/2) phase offset. Plotted together, they trace an ellipse. TTVs caused by other planets do not generally show this specific relationship. In practice, the moon's period is shorter than the planet's, so the sampled signal is **aliased**; real analyses also consider TDV contributions from changes in impact parameter, and must assess how often noise alone produces an apparent loop.

**Status (🟡 Level 3).** Candidate exomoons around Kepler-1625 b and Kepler-1708 b have been proposed (Teachey & Kipping 2018; Kipping et al. 2022), and both have been challenged (for example, Heller & Hippke 2024). No exomoon is confirmed as of November 2026. See [D12](../disclosures/d12-exomoons-timing-duration.md).

### References

- Kipping, D. M. (2009a). Transit timing effects due to an exomoon. *Monthly Notices of the Royal Astronomical Society*, 392, 181–189.
- Kipping, D. M. (2009b). Transit timing effects due to an exomoon — II. *Monthly Notices of the Royal Astronomical Society*, 396, 1797–1804.
- Teachey, A., & Kipping, D. M. (2018). Evidence for a large exomoon orbiting Kepler-1625b. *Science Advances*, 4, eaav1784. doi:10.1126/sciadv.aav1784
- Kipping, D., et al. (2022). An exomoon survey of 70 cool giant exoplanets and the new candidate Kepler-1708 b-i. *Nature Astronomy*, 6, 367–380. doi:10.1038/s41550-021-01539-1
- Heller, R., & Hippke, M. (2024). Large exomoons unlikely around Kepler-1625 b and Kepler-1708 b. *Nature Astronomy*, 8, 193–206.

## Connects to

- Disclosure: [D12 — Exomoons from timing and duration wobbles](../disclosures/d12-exomoons-timing-duration.md)
- Tutorial: [Tutorial 8 — Exomoon timing test](../tutorials/t08-exomoon-timing-test.md)
- Next lesson: [Lesson 12 — High school: speeds of interstellar visitors](l12-high-school-hyperbolic-orbits.md)
