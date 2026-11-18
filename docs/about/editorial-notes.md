# Editorial notes — what we changed, and why

> **In one sentence:** This project started from private brainstorming notes; we kept every idea that real physics and public data can test, rewrote it plainly, fixed mistakes, and left out the rest.

## For young readers

Before a book is printed, an editor checks it. They fix mistakes and take out parts that are not true. We did the same thing here. Some ideas in our first notes were exciting but wrong, so we removed them. Some numbers were wrong, so we fixed them. Good scientists always show what they changed. That is what this page does.

## Our rules for keeping an idea

We kept an idea only if **all** of these are true:

1. It follows well-tested physics (Newton's and Einstein's gravity, optics, electromagnetism, statistics).
2. It can be tested with public data or ordinary instruments.
3. There is a result that would show it is **wrong**.

Kept ideas became the 15 [disclosures](../disclosures/README.md). Each one has an evidence level.

## What we removed

| Removed material | Why |
|---|---|
| Story framing: "non-local telemetry", "future timelines", "probability matrices", mission code names, and similar | It is fiction, not evidence. It also makes honest science look like a secret, which it is not. |
| Claims that scientists or agencies are "foolish" or are throwing discoveries away out of ignorance | Not supported, and unfair. Data go unexamined because of limited time, noise and the cost of false alarms. We describe those real reasons instead. |
| "Scalar", "space-flux", "chug", "conformon", "dual-closure", "damplifier" and "Fourth Law of Logic" physics (attributed to T. E. Bearden, S. Inomata, A. P. Dubrov and others) | These ideas are not part of tested physics and make no confirmed predictions. Where they were used to explain a real phenomenon (gravity, dust gaps, lensing), we kept the phenomenon and used the accepted explanation. |
| "Seeing a planet's true present position" with a crystal bridge (Kozyrev-style claims) | Not reproduced by independent experiments. The real, interesting physics — light takes time to travel, and astronomers already correct for it — became [Lesson 9](../lessons/l09-light-from-the-past.md). |
| Electrical "gap clearing" making small planets carve disk gaps "1,000 times more efficiently" | No supporting evidence. Real kinematic planet detections in disks are in [D09](../disclosures/d09-planets-in-young-disks.md). |
| Neutrino-driven "masers" and VLF amplification in molecules | Not supported. Real planetary and brown-dwarf radio auroras are in [D08](../disclosures/d08-radio-auroras.md). |
| Claims that "two undiscovered planets" sit at stated positions in Taurus/Orion | No data or method was given. The real, testable method (timing and ranging limits) is in [D01](../disclosures/d01-unseen-planets-far-solar-system.md). |
| All health, wellness, breathing, light-therapy, "frequency" and "biofield" advice (including 7.83 Hz, 40 Hz, 528 Hz and 142.857 kHz "harmonic lock" protocols, and skin "keratin diode" claims) | Out of scope for an astronomy project, and not supported by reliable evidence. We do not give medical advice. |
| Instructions to drive LEDs, piezo discs or capacitive plates near the body | Health claims are unsupported; infrared LEDs can also harm eyes because infrared light is invisible and does not trigger blinking. |
| A tool for "camouflaging" ideas in aerospace vocabulary to win grants or patents | Hiding the real basis of a proposal from reviewers is misrepresentation. We will never do this. |
| A tool that writes a finished "discovery paper" automatically | Discoveries need human checking and independent confirmation. Instead, we explain [how to report a candidate](how-to-report-a-discovery.md). |
| A commercial satellite-tracking product | Outside the project's scope. |

## Facts we corrected

| Original statement | Correction |
|---|---|
| Tisserand parameter of 2015 BZ509 is −1.39 | About **−0.75**, computed from JPL elements (a ≈ 5.14 au, e ≈ 0.378, i ≈ 163.1°). See [Tutorial 5](../tutorials/t05-tisserand-and-backwards-orbits.md). |
| Survey linkers dump interstellar objects because they "force" circular or elliptical guesses | Some initial-orbit methods do assume bound orbits, but modern linkers (for example HelioLinC) search over distance and radial-velocity hypotheses. Whether interstellar objects sit unlinked in the ITF is an **open question**, not a known fact. See [D14](../disclosures/d14-interstellar-objects-unlinked-data.md). |
| The ITF holds "15 to 20 million unlinked observations" | We could not verify a current total, so we do not quote one. Holman et al. (2018) linked ITF data into orbits for about 41,000 new minor planets. |
| Any chain of tracklets with an orbit fit with e > 1 and small residuals "is an unannounced interstellar object discovery" | A good hyperbolic fit is a **candidate** only. Short arcs, wrong uncertainties and wrong linkages all produce false hyperbolic orbits. Confirmation needs new, independent observations. |
| Dark bodies tens of meters across at the Earth–Moon L4/L5 points would be magnitude 22–24 | At about 380,000 km, such bodies would be far brighter near opposition (roughly magnitude 11–14 for 100 m to 30 m and a dark surface; fainter at larger phase angles). See [D06](../disclosures/d06-earth-moon-trojan-points.md). |
| Backyard telescopes can detect exoplanet polarization or separate a planet with intensity interferometry | Planet-to-star contrast (about 10⁻⁵ to 10⁻⁹) makes this far beyond small telescopes. See [D05](../disclosures/d05-polarized-light-from-planets.md). |
| Nearly every tilted planet has an undiscovered outer giant holding it in resonance | Not supported. The resonance formula is useful for deciding **where to look**, not for predicting that a planet exists. See [D13](../disclosures/d13-tilted-orbits-hidden-companions.md). |
| 2011 KT19 is called "Niku" | "Niku" is a nickname. Its official name is now **471325 Taowu**. |

## Code we rewrote

The original notes included a short Python program for hunting interstellar objects. We replaced it with the tested `fdastro.iso` module because the original had problems that would produce wrong answers:

1. **Earth's position was wrong.** It used the Sun's *mean anomaly* as if it were the Earth's *longitude*, which misplaces the Earth by roughly 100° around its orbit.
2. **Motion was approximated as constant acceleration**, which is not accurate over days to weeks near the Sun. We use exact two-body motion (and numerical integration when a comet-like push is included).
3. **No light-travel-time correction.**
4. **The test data were made with the same wrong model**, so the self-test could not catch these errors.
5. **The "significance" was invented**: it used an arbitrary formula fed into a Gaussian, labeled as an extreme-value (Gumbel) return period. We use a likelihood-ratio test against the best possible bound orbit.
6. **The "radiant" was the current direction of motion**, not the direction the object came from. We compute the true incoming asymptote.
7. **It labeled results "CONFIRMED".** No single fit can confirm a discovery.

## Where the original ideas went

| Original section | Now |
|---|---|
| Discovery 01 | [D01](../disclosures/d01-unseen-planets-far-solar-system.md) |
| Discovery 02 | [D02](../disclosures/d02-vanishing-transits.md) and [D03](../disclosures/d03-single-transit-planets.md) |
| Discovery 03 and the optical demodulator | [D05](../disclosures/d05-polarized-light-from-planets.md) |
| Discovery 04 and the rogue-planet linker | [D04](../disclosures/d04-nearby-cold-worlds-wise.md), `fdastro.astrometry`, [Tutorial 6](../tutorials/t06-parallax-and-proper-motion.md) |
| Discovery 05 (target list) | Folded into [D02](../disclosures/d02-vanishing-transits.md) and [D13](../disclosures/d13-tilted-orbits-hidden-companions.md) |
| Discovery 06 | Removed; light travel time taught in [Lesson 9](../lessons/l09-light-from-the-past.md) |
| Discovery 07 | [D06](../disclosures/d06-earth-moon-trojan-points.md) |
| Discovery 08 | [D07](../disclosures/d07-short-microlensing-free-floating-planets.md), `fdastro.microlensing` |
| Discovery 09 | [D08](../disclosures/d08-radio-auroras.md) |
| Discovery 10 | [D09](../disclosures/d09-planets-in-young-disks.md) |
| Discovery 11 | [D10](../disclosures/d10-caves-and-buried-masses-gravity.md) |
| Discovery 12 | [D11](../disclosures/d11-inner-solar-system-trojans.md) |
| Discovery 13 | [D12](../disclosures/d12-exomoons-timing-duration.md), `fdastro.exomoon` |
| Discovery 14 | [D13](../disclosures/d13-tilted-orbits-hidden-companions.md), `fdastro.obliquity` |
| Discovery 15 and the interstellar-object hunter | [D14](../disclosures/d14-interstellar-objects-unlinked-data.md), `fdastro.kepler`, `fdastro.iso`, `fdastro.mpc` |
| Discovery 16 | [D15](../disclosures/d15-captured-interstellar-objects.md), `fdastro.tisserand` |
| Transit hunting engine | `fdastro.transits`, [Tutorial 7](../tutorials/t07-single-and-fading-transits.md) |
| Hardware firmware, crystal and infrared benches, biometric sections | Removed (see above) |

## A fun fact we kept

One true thing from the notes is a nice piece of math: 1 ÷ 7 = 0.142857 142857…, and 142857 is a **cyclic number** — multiply it by 2, 3, 4, 5 or 6 and you get the same six digits in a rotated order (285714, 428571, 571428, 714285, 857142), while 142857 × 7 = 999999. It is a lovely math puzzle. It has no special effect on the body or on telescopes.

## Found a mistake?

Please open an issue. We correct errors in public and keep a record in the [changelog](../../CHANGELOG.md).
