# The Planet That Stopped Crossing Its Star

**TOI-2535 b used to pass in front of its star every few days. Then its shadow shrank and disappeared. A hidden neighbor is the likely reason — and there may be more planets like it in public data.**

> **Suggested header image:** Illustration of a star with a planet's path drawn as a line across its face; a second, tilted path passes just above the star's edge.
> **Alt text:** "Illustration: a planet's old path crosses the face of its star. A newer, tilted path misses the star. This shows how a tilting orbit can make transits disappear."

**Evidence level:** 🟢 **Level 1 — Confirmed** that tilting orbits can make transits fade (seen in published studies, including TOI-2535 b). 🟡 **Level 3 — Testable idea** that more such planets are waiting to be found in TESS and Kepler data.

---

Imagine a moth flying around a porch light every night at the same time. Each time it passes in front of the bulb, it casts a tiny shadow. You watch this for years.

Then the shadow gets smaller. And smaller. Then it stops.

Did the moth fly away? Maybe not. Maybe its path slowly tilted, so now it flies just above the light instead of in front of it. And maybe something you can't see — a bigger bug flying nearby — is pulling its path sideways.

That is roughly what happened to a real planet.

## What is a transit?

When a planet passes in front of its star, it blocks a tiny bit of the star's light. This is called a **transit**. NASA's TESS space telescope watches hundreds of thousands of stars for these little dips in brightness. Most planets found this way show a dip every orbit, like clockwork.

## The vanishing transits of TOI-2535 b

**TOI-2535 b** is a giant planet, like a hot version of Jupiter. It orbits a star about 1,000 light-years away, in the constellation Corvus. TESS watched it on and off from **April 2019 to March 2026**.

Over those seven years, the transits got **shorter and shallower**. In TESS's March 2026 observations, they were **gone**.

In a paper published on **9 November 2026** in *The Astrophysical Journal Letters*, a team led by Samuel Yee and Erik Petigura at UCLA explained why. The planet's orbit is slowly tilting — astronomers call this **precession**. Something is pulling on it. Their best explanation is an **unseen neighboring planet**, likely at least as heavy as Saturn.

The planet is still there. It just no longer crosses the star from our point of view. It may cross again in a few decades, when its orbit tilts back.

## Not the first, and probably not the last

Astronomers have seen changing transits before. For example, the planet Kepler-13Ab showed changes in its transit shape over time, linked to its orbit slowly turning. In the Kepler-108 system, two giant planets have orbits tilted relative to each other. These systems teach us that planetary systems are not frozen. They move, tilt and wobble.

## What is still open

Here is our question:

> How many other planets in public TESS and Kepler data have transits that are slowly getting shallower or shorter?

Each one could point to an unseen neighbor. That neighbor might later be found with other methods, like measuring the star's wobble.

## How to test it

1. Pick stars with known transiting planets that TESS has observed for several years.
2. Measure each transit's depth (how much light is blocked) and duration (how long it lasts).
3. Look for a **steady trend** over time, not just random scatter.
4. Rule out instrument effects. Different TESS camera setups, background light, and nearby stars can all change the measured depth.
5. If a trend survives, compare it with what a tilting orbit would produce.

Our free `fdastro.transits` code and Tutorial 7 walk through these steps.

## How we could be wrong

- **Contamination.** Light from a nearby star can blend in and make transits look shallower in some data sets but not others.
- **Different pipelines.** Data processed in different ways can give slightly different depths.
- **Star spots.** Spots on the star can change how deep transits look.
- **Too few points.** A "trend" made of three noisy measurements is not a trend.

A real tilting orbit should change both depth and duration in a consistent way. If that pattern is missing, the trend is probably not precession.

## How you can help

- **Kids and families:** Tie a small ball to a string. Swing it in a circle around a lamp so its shadow crosses a wall. Now slowly tilt the circle. Watch the shadow get shorter, then miss the wall completely.
- **Students and coders:** Try Tutorial 7 with a well-known hot Jupiter. Measure its transit depth in every TESS sector.
- **Everyone:** When you hear "a planet vanished," you now know the better story: its path tilted.

*Kids: please ask a parent, guardian or teacher before posting or commenting online.*

## Read more

Full disclosure with references: [D02 — Planets whose transits fade away](../../disclosures/d02-vanishing-transits.md)
