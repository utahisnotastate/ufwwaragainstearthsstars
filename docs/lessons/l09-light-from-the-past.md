# Lesson 9 — Light from the Past

| | |
|---|---|
| **Ages** | 8–12 |
| **Time** | 40 minutes |
| **Group size** | Whole class |
| **Connects to** | [D01 — Unseen planets in the far Solar System](../disclosures/d01-unseen-planets-far-solar-system.md) and [D14 — Interstellar visitors in unlinked asteroid data](../disclosures/d14-interstellar-objects-unlinked-data.md) |

## Big question

**When we look at something in space, are we seeing it as it is right now?**

## For young readers

Light is the fastest thing there is. But it still takes time to travel.

Light from the Sun takes about **8 minutes** to reach us. So when you see the Sun (never look straight at it!), you see it as it was 8 minutes ago.

Light from the nearest star after the Sun takes more than **4 years** to get here. Light from some galaxies has traveled for millions of years!

So looking into space is like looking at old photographs. Astronomers know this. When they work out where a planet or asteroid is **right now**, they use the laws of motion to figure out how far it moved while its light was traveling to us.

## Learning goals

Learners will be able to:

1. Explain that light takes time to travel.
2. Compare light travel times to the Moon, Sun, planets and nearest stars.
3. Explain that astronomers correct for this delay when they track moving objects.

## NGSS alignment

- **5-ESS1-1** — stars look different because of their distance.
- **MS-ESS1-3** — scale of the Solar System.

## Materials

- A long hallway, playground or field
- Cards labeled Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
- A tape measure or a known step length
- A stopwatch

## Safety

- Walk, do not run. Stay inside the school grounds.
- Never look directly at the Sun.

## Steps

1. **Set the scale.** One normal step = **1 light-minute** (the distance light travels in 1 minute — about 18 million km).
2. **Place the planets.** Start at the Sun card. Walk and drop cards at these step counts from the Sun:

| Object | Steps from the Sun (light-minutes, rounded) |
|---|---|
| Mercury | 3 |
| Venus | 6 |
| Earth | 8 |
| Mars | 13 |
| Jupiter | 43 |
| Saturn | 79 |
| Uranus | 160 |
| Neptune | 250 |

3. **Walk at light speed.** If each step takes 1 second, then 1 second of walking = 1 minute of light travel. Time how long it takes to walk from the Sun to Earth (8 seconds = 8 minutes for real light) and from the Sun to Neptune (about 4 minutes of walking = about 4 hours for real light).
4. **The nearest star.** Ask: how many steps to Proxima Centauri, the nearest star after the Sun? (About 2.2 million steps! That is more than 1,500 km of walking — about 950 miles.)
5. **The moving target.** Have one learner walk slowly across the field. Another learner closes their eyes, counts to 3, opens them and points to where the walker *was* when they closed their eyes. Discuss: to point at where the walker is *now*, you need to know how fast they move and how much time passed. Astronomers do exactly this.

**Accessible version:** Use a long strip of paper (adding-machine tape) on a table at a smaller scale, such as 1 cm = 1 light-minute (Neptune at 2.5 m).

## Discussion questions

1. If the Sun suddenly changed, how long until we would know? (About 8 minutes.)
2. Why do messages to spacecraft on Mars take several minutes?
3. When you see a star, is it possible that it has changed since its light left? (Yes, especially for far stars.)
4. How can astronomers know where a fast asteroid is *right now*?

## Check for understanding (answers for the teacher)

| Question | Expected answer |
|---|---|
| How long does sunlight take to reach Earth? | About 8 minutes (8 min 20 s). |
| How long does light take from the nearest star after the Sun? | More than 4 years (about 4.2 years for Proxima Centauri). |
| Do astronomers see objects "as they are now"? | No, as they were when the light left. |
| How do they find where an object is now? | They calculate its motion during the light's travel time, using the laws of motion and gravity. |

## Extension

- Research **Ole Rømer**, who in 1676 used the timing of eclipses of Jupiter's moon Io to show that light has a finite speed.
- NASA's Voyager 1 spacecraft is so far away that its radio signals take almost a whole day to reach Earth.
- Older learners: light travels about 300,000 km per second. Calculate the light travel time from the Moon (about 384,000 km). (About 1.3 seconds.)

## For the teacher: the science behind it

**Light travel time (🟢 Level 1).** The speed of light in vacuum is exactly 299,792,458 m/s (by definition of the metre). One astronomical unit is about 499 light-seconds. Rømer's 1676 analysis of Io's eclipse timings gave the first evidence that light speed is finite.

**Light-time correction in practice (🟢 Level 1).** When astronomers compute an asteroid's or planet's position for comparison with an observation, they solve for the time the light **left** the object (the "retarded" time) and compute the object's position at that time, then apply stellar aberration. Orbit determination software, including the `fdastro` package in this project, includes this light-time correction. See [Tutorial 3](../tutorials/t03-fit-an-orbit-and-test-if-bound.md).

**Gravity also travels at the speed of light (🟢 Level 1).** In 2017, gravitational waves from the neutron-star merger GW170817 and the gamma-ray burst from the same event arrived about 1.7 seconds apart after traveling about 130 million years. This showed that gravitational waves travel at the speed of light to within about one part in 10¹⁵ (Abbott et al. 2017). There is no known faster signal that would show where a distant object is "right now"; instead, we calculate it.

**Editorial note.** An early project note proposed instruments that would detect an object's "instantaneous" position. That idea conflicts with well-tested physics, so it was removed and replaced by this lesson. See [editorial notes](../about/editorial-notes.md).

### References

- Abbott, B. P., et al. (2017). Gravitational waves and gamma-rays from a binary neutron star merger: GW170817 and GRB 170817A. *The Astrophysical Journal Letters*, 848, L13. doi:10.3847/2041-8213/aa920c
- Bureau International des Poids et Mesures. *The International System of Units (SI)*, 9th edition (2019).

## Connects to

- Disclosures: [D01](../disclosures/d01-unseen-planets-far-solar-system.md), [D14](../disclosures/d14-interstellar-objects-unlinked-data.md)
- Next lesson: [Lesson 10 — The space magnifying glass](l10-space-magnifying-glass.md)
