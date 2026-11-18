# The Disclosures

> **In one sentence:** These are 15 places where new discoveries about planets, moons and space rocks may already be waiting inside public science data.

## For young readers

Telescopes and spacecraft collect huge amounts of data. Scientists cannot look at all of it closely. Some of it gets saved for later. We think a few exciting discoveries may be hiding in those saved files. Each "disclosure" below is one idea about where to look. Some ideas are already proven. Some are guesses that you can help test!

## What "disclosure" means here

A **disclosure** is a short, honest report that says:

1. **What might be hiding** in public data.
2. **How sure we are** (the evidence level).
3. **How anyone could check** — and how the idea could turn out to be wrong.

Nothing here is secret. Every data set is public. Every method is published. We are not claiming that anyone has hidden anything.

## Evidence levels

| Label | Name | Simple meaning |
|---|---|---|
| 🟢 **Level 1** | **Confirmed** | Seen and checked more than once. |
| 🔵 **Level 2** | **Strong evidence** | Good results exist; experts still discuss them. |
| 🟡 **Level 3** | **Testable idea** | Follows normal physics; not shown yet; you can test it. |
| 🟠 **Level 4** | **Long shot** | Physics allows it, but today's tools may be too weak. |

Full definitions are in the [style guide](../STYLE.md#4-evidence-levels). Each disclosure page labels every individual claim. The level in the table below is for the **main open question** on that page.

## The registry

| ID | Title | The open question | Main level | Code module | Start here |
|---|---|---|---|---|---|
| D01 | [Unseen planets in the far Solar System](d01-unseen-planets-far-solar-system.md) | Can spacecraft tracking and pulsar timing narrow down where an undiscovered distant planet could be? | 🟡 Level 3 | — | [Lesson 1](../lessons/l01-finding-what-we-cannot-see.md) |
| D02 | [Planets whose transits fade away](d02-vanishing-transits.md) | How many more planets like TOI-2535 b have transits that shrink because a hidden neighbor tilts their orbit? | 🟡 Level 3 | `fdastro.transits` | [Tutorial 7](../tutorials/t07-single-and-fading-transits.md) |
| D03 | [Planets seen only once](d03-single-transit-planets.md) | How many long-period planets show only one transit in TESS and Kepler data? | 🟡 Level 3 | `fdastro.transits` | [Tutorial 7](../tutorials/t07-single-and-fading-transits.md) |
| D04 | [Cold, dark neighbors in infrared sky maps](d04-nearby-cold-worlds-wise.md) | Are there still undiscovered cold brown dwarfs or rogue planets near the Sun in WISE/NEOWISE data? | 🟡 Level 3 | `fdastro.astrometry` | [Tutorial 6](../tutorials/t06-parallax-and-proper-motion.md) |
| D05 | [Polarized light from planets](d05-polarized-light-from-planets.md) | Can polarization help separate a planet's light from its star's light? | 🟠 Level 4 (small telescopes) | — | [Lesson 7](../lessons/l07-light-has-a-direction.md) |
| D06 | [Dust clouds and possible mini-moons at the Earth–Moon balance points](d06-earth-moon-trojan-points.md) | Are there solid bodies, not just dust, near the Earth–Moon L4 and L5 points? | 🟠 Level 4 | — | [Lesson 5](../lessons/l05-balance-points-in-space.md) |
| D07 | [Free-floating planets in brief lensing flashes](d07-short-microlensing-free-floating-planets.md) | How common are Earth-mass planets drifting between the stars? | 🔵 Level 2 | `fdastro.microlensing` | [Tutorial 10](../tutorials/t10-microlensing-timescales.md) |
| D08 | [Radio auroras from planets and brown dwarfs](d08-radio-auroras.md) | Do low-frequency radio archives contain auroral signals from unknown brown dwarfs or exoplanets? | 🟡 Level 3 | — | [Lesson 8](../lessons/l08-radio-auroras.md) |
| D09 | [Baby planets hidden in dusty disks](d09-planets-in-young-disks.md) | Do ALMA gas-velocity "kinks" reveal more young planets than images show? | 🔵 Level 2 | — | [Astrophysicists guide](../audiences/astrophysicists.md) |
| D10 | [Caves and buried masses mapped by gravity](d10-caves-and-buried-masses-gravity.md) | Can raw spacecraft tracking data reveal more lava tubes and buried masses on the Moon and Mars? | 🟡 Level 3 | — | [Physicists guide](../audiences/physicists.md) |
| D11 | [Trojan and co-orbital asteroids near Venus, Earth and Mars](d11-inner-solar-system-trojans.md) | How many asteroids share orbits with the inner planets, hidden in twilight? | 🟡 Level 3 | `fdastro.kepler` | [Lesson 5](../lessons/l05-balance-points-in-space.md) |
| D12 | [Exomoons from timing and duration wobbles](d12-exomoons-timing-duration.md) | Do any known planets show the 90° timing–duration pattern that a moon would cause? | 🟡 Level 3 | `fdastro.exomoon` | [Tutorial 8](../tutorials/t08-exomoon-timing-test.md) |
| D13 | [Tilted orbits that point to unseen planets](d13-tilted-orbits-hidden-companions.md) | Do tilted inner planets tell us where to look for unseen outer giants? | 🟡 Level 3 | `fdastro.obliquity` | [Tutorial 9](../tutorials/t09-tilted-orbits-and-hidden-companions.md) |
| D14 | [Interstellar visitors in unlinked asteroid data](d14-interstellar-objects-unlinked-data.md) | Are any interstellar objects sitting unrecognized among unlinked asteroid observations? | 🟡 Level 3 | `fdastro.kepler`, `fdastro.iso`, `fdastro.mpc` | [Tutorial 3](../tutorials/t03-fit-an-orbit-and-test-if-bound.md) |
| D15 | [Captured interstellar objects already orbiting the Sun](d15-captured-interstellar-objects.md) | Are some backwards (retrograde) or tilted objects really captured from other stars? | 🟡 Level 3 | `fdastro.tisserand` | [Tutorial 5](../tutorials/t05-tisserand-and-backwards-orbits.md) |

## How these relate to the original notes

This project began from a set of private brainstorming notes. We kept every idea that can be tested with accepted physics and public data. We rewrote it in plain, professional language and added real references. Ideas that conflict with well-tested physics, and all health or "frequency" advice, were removed. The full list of what changed, and why, is in [editorial notes](../about/editorial-notes.md).

## How to suggest a new disclosure

Open an issue using the "New disclosure idea" template. Please include:

1. The question, in one sentence.
2. The public data that could answer it.
3. A result that would show the idea is **wrong**.
4. At least one published reference.
