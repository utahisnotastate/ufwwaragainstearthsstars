# Lesson 13 — University Lab: Fitting an Orbit and Testing Whether It Is Bound

| | |
|---|---|
| **Level** | Undergraduate (second or third year physics, astronomy or engineering) |
| **Time** | 2–3 hours, plus a written report |
| **Prerequisites** | Newtonian mechanics, vectors, basic Python, least squares |
| **Software** | Python 3.11+ with the `fdastro` package from this repository |
| **Connects to** | [D14 — Interstellar visitors in unlinked asteroid data](../disclosures/d14-interstellar-objects-unlinked-data.md) |

## Big question

**Given a few nights of sky positions for a moving object, can we tell whether it is bound to the Sun or just passing through — and how sure can we be?**

## In plain words

Telescopes measure where an object appears on the sky (its right ascension and declination) at a few times. They do not directly measure how far away it is. From these angles alone, you must work out the object's full 3D position and velocity. With only a short stretch of observations, many different orbits fit almost equally well. In this lab you will see this problem for yourself, and you will learn a fair statistical test for whether the data **require** an unbound (interstellar) orbit.

## Learning goals

Students will be able to:

1. Propagate two-body orbits of any eccentricity, including hyperbolic ones.
2. Simulate realistic astrometric observations, including light-time delay and measurement noise.
3. Fit a six-parameter orbit to angles-only data by nonlinear least squares.
4. Explain the short-arc degeneracy between distance and velocity.
5. Carry out and interpret a constrained-refit (likelihood-ratio) test of the bound-orbit hypothesis.

## Before the lab

Work through these two tutorials. They show the exact functions and arguments to use, so this lab sheet does not repeat them:

- [Tutorial 2 — Orbits: ellipses and hyperbolas](../tutorials/t02-orbits-ellipses-and-hyperbolas.md)
- [Tutorial 3 — Fit an orbit and test if it is bound](../tutorials/t03-fit-an-orbit-and-test-if-bound.md)

## Tasks

### Task 1 — Orbits and energy (20 min)

1. Using the package's two-body propagation, set up a heliocentric state with perihelion distance 1.36 au and eccentricity 6.1 (similar to 3I/ATLAS).
2. Propagate it over ±1 year and check that the specific energy ε = *v*²/2 − *μ*/*r* and the angular momentum vector are conserved to near machine precision.
3. Convert the state to orbital elements and compute *v*∞. Compare with √[*μ*(*e* − 1)/*q*].

**Deliverable:** a plot of the orbit in the ecliptic plane and a table of conserved quantities and their relative drift.

### Task 2 — Simulated observations (20 min)

1. Generate geocentric right ascension and declination for 9 epochs: three per night on three nights spread over 12 days.
2. Include the light-time correction. Measure how large the effect is in arcseconds by comparing with and without it.
3. Add Gaussian noise of 0.3″ per coordinate.

**Deliverable:** a short paragraph on the size of the light-time effect and why it matters for a fast object.

### Task 3 — Fit the orbit (30 min)

1. Fit a six-parameter state to your simulated data.
2. Report the RMS residual and the best-fit eccentricity.
3. Repeat with different starting guesses. Do they converge to the same answer?

**Deliverable:** best-fit elements with uncertainties from the covariance matrix, and a comment on whether the covariance-based uncertainty in *e* looks believable.

### Task 4 — The short-arc problem (30 min)

1. Re-fit using only the first night (3 points). Then nights 1–2, then all three nights, then extend the simulation to a 30-day arc.
2. For each arc length, record the best-fit *e* and its uncertainty.
3. Plot the uncertainty in *e* against arc length.

**Deliverable:** the plot, and a one-paragraph explanation of why the distance–velocity degeneracy makes *e* poorly constrained for very short arcs. Use the terms "admissible region" and "statistical ranging" (see references).

### Task 5 — Is it bound? (30 min)

1. Run the bound-orbit test from Tutorial 3. It refits with the constraint ε ≤ 0 and compares the χ² values: Δχ² = χ²(bound) − χ²(free).
2. Repeat for each arc length from Task 4.
3. Repeat for a simulated **bound** object (for example, a main-belt asteroid with *e* = 0.15 and *a* = 2.7 au). Does the test ever falsely reject the bound hypothesis? How often, over 100 noise realizations?

**Deliverable:** a table of Δχ² and equivalent significance for each case, and a measured false-alarm rate for the bound object.

### Task 6 — Systematics (optional, 30 min)

Explore one of these:

- **Topocentric parallax.** Real observations are made from the Earth's surface, not its center. For an object 0.1 au away, estimate the size of this effect in arcseconds. What happens to the fit if you ignore it?
- **Time scales.** Observations are reported in UTC; orbit integrations use TDB/TT, which differ by about 69 s in 2026. Shift all times by 69 s. Does the fit absorb it?
- **Outliers.** Add one 5″ outlier. How does it affect *e*? Try a robust loss function.

## Report

Write a 3–5 page report in the style of a short research note:

1. Introduction (why bound/unbound matters; cite the discovery of 1I/ʻOumuamua).
2. Method (propagation, observation model, fitting, test statistic).
3. Results (figures and tables from Tasks 1–5).
4. Discussion: under what conditions could real interstellar objects be missed by linking methods tuned for ordinary asteroids? What would a responsible candidate report to the Minor Planet Center contain? (See [How to report a discovery](../about/how-to-report-a-discovery.md).)
5. Conclusion.

## Assessment rubric (suggested)

| Criterion | Excellent (4) | Good (3) | Developing (2) | Beginning (1) |
|---|---|---|---|---|
| Physics correctness | Energy, momentum, light-time handled correctly and checked | Minor slips | Some conceptual errors | Major errors |
| Statistics | Correct Δχ² interpretation, boundary effects noted, false-alarm rate measured | Mostly correct | Partial | Missing |
| Figures | Clear, labeled, with uncertainties | Clear | Hard to read | Missing |
| Critical discussion | Identifies degeneracies and systematics, avoids overclaiming | Good discussion | Superficial | Missing |
| Reproducibility | Code and random seeds provided | Code provided | Partial | None |

## For the instructor: the science behind it

**Short-arc orbit determination.** Angles-only data constrain the "attributable" (α, δ, α̇, δ̇) well, but range ρ and range-rate ρ̇ are poorly constrained over short arcs. Milani et al. (2004) define the **admissible region** in (ρ, ρ̇) space; statistical ranging (Virtanen et al. 2001) samples orbits consistent with the data. Eccentricity is a strongly nonlinear function of (ρ, ρ̇), so covariance-based uncertainties in *e* are often misleading for short arcs.

**The bound-orbit test.** Testing ε ≤ 0 against the unconstrained fit is a likelihood-ratio test with the null hypothesis on the boundary of the parameter space. Under regularity conditions, the asymptotic distribution of Δχ² is a 50:50 mixture of χ²₀ and χ²₁ (Chernoff 1954; Self & Liang 1987), so a one-sided significance is appropriate. Students should verify the false-alarm rate by simulation, because the asymptotic result may not hold for strongly nonlinear, short-arc problems.

**Status of the science question (🟡 Level 3).** Whether interstellar objects exist unrecognized among unlinked observations (such as the Minor Planet Center's Isolated Tracklet File) is open. See [D14](../disclosures/d14-interstellar-objects-unlinked-data.md).

### References

- Meech, K. J., et al. (2017). A brief visit from a red and extremely elongated interstellar asteroid. *Nature*, 552, 378–381. doi:10.1038/nature25020
- Milani, A., Gronchi, G. F., de' Michieli Vitturi, M., & Knežević, Z. (2004). Orbit determination with very short arcs. I. Admissible regions. *Celestial Mechanics and Dynamical Astronomy*, 90, 57–85.
- Virtanen, J., Muinonen, K., & Bowell, E. (2001). Statistical ranging of asteroid orbits. *Icarus*, 154, 412–431.
- Chernoff, H. (1954). On the distribution of the likelihood ratio. *Annals of Mathematical Statistics*, 25, 573–578.
- Self, S. G., & Liang, K.-Y. (1987). Asymptotic properties of maximum likelihood estimators and likelihood ratio tests under nonstandard conditions. *Journal of the American Statistical Association*, 82, 605–610.
- Holman, M. J., Payne, M. J., Blankley, P., Janssen, R., & Kuindersma, S. (2018). HelioLinC: a novel approach to the minor planet linking problem. *The Astronomical Journal*, 156, 135.

## Connects to

- Disclosure: [D14 — Interstellar visitors in unlinked asteroid data](../disclosures/d14-interstellar-objects-unlinked-data.md)
- Guide: [For physicists](../audiences/physicists.md)
