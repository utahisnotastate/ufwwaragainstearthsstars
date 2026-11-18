# Tilted Orbits That Point to Unseen Planets

**Some planets orbit their stars at steep angles — even over the poles. Often, something must have tipped them. An unseen outer planet is one strong suspect, and Gaia's new data release gives us a fresh way to look.**

> **Suggested header image:** Illustration of a spinning star with its equator drawn as a ring, and a planet's orbit tilted steeply across it; a faint, larger outer planet orbit is drawn as a dashed line.
> **Alt text:** "Illustration: a spinning star with a planet orbiting at a steep tilt compared with the star's equator. A dashed outer orbit shows a possible unseen planet that could have tipped the inner orbit."

**Evidence level:** 🟢 **Level 1 — Confirmed** that many planets have tilted orbits compared with their star's spin. 🔵 **Level 2 — Strong evidence** that outer companions can cause such tilts (published theory and some observed systems). 🟡 **Level 3 — Testable idea** that tilted planets can tell us where to search for unseen outer planets.

---

Imagine a merry-go-round that is spinning while tipped sideways at a strange angle. You can't see anyone near it. But you know something — or someone — must have pushed it to tilt it like that.

Some planets are like that. Their orbits are tipped compared with the way their star spins. Scientists want to know: **what tipped them?**

## How do we know a star's spin and a planet's tilt?

Stars spin. As a star turns, one side moves toward us and the other side moves away. Light from the side moving toward us is shifted slightly bluer. Light from the side moving away is shifted slightly redder.

When a planet passes in front of the star, it first blocks one side, then the other. That makes the star's light shift in a special pattern. By measuring this pattern, astronomers can tell whether the planet's orbit lines up with the star's spin, or is tilted. This is called the **Rossiter–McLaughlin effect**, named after two astronomers who studied it in eclipsing stars in 1924.

## Tilted planets are common

Since the first measurement for an exoplanet in 2000, astronomers have measured this tilt for many planets. Many line up nicely, like the planets in our Solar System. But many do not. Some orbit at steep angles. A few even orbit backwards, or over the star's poles.

One famous example is **HAT-P-11 b**, a Neptune-sized planet on a nearly polar orbit. In 2018, astronomers found a much bigger planet, **HAT-P-11 c**, far out in the same system on a tilted orbit. That outer giant is a strong suspect for tipping the inner planet.

## How can an outer planet tip an inner one?

Planets slowly tug on each other's orbits. These slow tugs make orbits wobble, like a spinning top that slowly circles. A star's own slightly squashed shape adds its own slow wobble.

When two of these slow wobbles have just the right speed to match, they can **resonate** — a bit like pushing a swing at the right moment. Then a small push can build up into a big tilt. In 2020, Cristobal Petrovich and colleagues showed how this kind of matching, happening as a young planet-forming disk fades away, could tip close-in planets onto steep orbits.

## What is still open

> If a planet is steeply tilted, can we use the star's properties and the planet's orbit to predict what kind of outer planet would be needed, and where?

That prediction would be a **search map**: "Look for a planet of about this mass at about this distance."

## A new tool arrives: Gaia Data Release 4

The European Space Agency's **Gaia** spacecraft measured the positions of more than a billion stars with incredible precision. A giant planet makes its star wobble slightly in the sky. Gaia's fourth data release, scheduled for **2 December 2026**, was expected to include the first large list of planet candidates found this way. That makes this the perfect time to compare tilted inner planets with possible outer giants.

*(Editor's note before posting: update this paragraph with what Gaia DR4 actually contains once it is public.)*

## How to test it

1. Start with a public catalog of measured planet tilts.
2. For each tilted planet, use our `fdastro.obliquity` code to compute which outer-planet masses and distances could cause a matching wobble.
3. Check Gaia DR4 and radial-velocity surveys for outer companions in that range.
4. Count how often the prediction is right — and how often it is wrong.

Tutorial 9 walks through the steps.

## How we could be wrong

- Some tilts may come from other causes: a passing star, early chaos among planets, or the star's own history.
- A matching wobble is not proof. Many combinations of mass and distance can give similar effects.
- Measured tilts and star properties have real uncertainties.

## How you can help

- **Kids and families:** Spin a top, then gently tap it. Watch it wobble in a slow circle. That slow circle is like the slow wobble of an orbit.
- **Students:** Find three tilted planets in a public catalog. Which ones have known outer companions?
- **Coders:** Use Tutorial 9 to make a search map for one tilted planet.

*Kids: please ask a parent, guardian or teacher before posting or commenting online.*

## Read more

Full disclosure with references: [D13 — Tilted orbits that point to unseen planets](../../disclosures/d13-tilted-orbits-hidden-companions.md)
