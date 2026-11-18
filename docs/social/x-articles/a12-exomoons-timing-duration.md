# The Search for the First Moon Around Another Planet

**Our Solar System has hundreds of moons. Around other stars, not one moon has been confirmed yet. A clever timing pattern — early-late plus fast-slow, a quarter-step apart — could help.**

> **Suggested header image:** Illustration of a giant planet with a large moon passing in front of a bright star, with a small graph inset showing a looping oval pattern.
> **Alt text:** "Illustration: a giant planet and its moon cross in front of a star. An inset graph shows an oval loop made by plotting transit timing against transit duration. A moon can make this loop pattern."

**Evidence level:** 🟢 **Level 1 — Confirmed** that the timing method is sound physics, published since 2009. 🔵 **Level 2** for two published exomoon *candidates*, which are actively debated. 🟡 **Level 3 — Testable idea** that a careful search of public transit-timing data could turn up new candidates.

---

Imagine you are running laps around a track while holding hands with a little brother or sister. They are spinning around you as you run.

When they swing ahead of you, they pull you forward — you cross the finish line a little **early**. When they swing behind, you cross a little **late**.

But there's more. When they swing out to the side, they change how **fast** you are moving as you cross the line. So the **time you spend** crossing the finish-line stripe gets a little shorter or longer.

Here is the clever bit: the "early or late" pattern and the "fast or slow" pattern don't peak at the same time. They are a **quarter-step apart** — what scientists call 90 degrees out of phase.

## What is an exomoon?

An **exoplanet** is a planet around another star. An **exomoon** would be a moon around one of those planets. Our Solar System has hundreds of moons. Saturn alone has more than two hundred known moons. So exomoons should be common.

But they are small and far away. Finding one is very hard. As of today, **no exomoon has been confirmed**.

## The two famous candidates

- **Kepler-1625 b-i.** In 2018, Alex Teachey and David Kipping reported signs of a large moon around a giant planet, using data from the Kepler and Hubble space telescopes.
- **Kepler-1708 b-i.** In 2022, Kipping and colleagues reported a second candidate.

In 2024, René Heller and Michael Hippke reanalyzed both and argued that planet-only explanations fit better. The original team replied that both candidates remain possible and need more observations.

This back-and-forth is normal and healthy. It is exactly how science should test surprising claims.

## The timing trick

In 2009, David Kipping showed that a moon makes its planet wobble in two ways that can be measured from transits (when the planet passes in front of its star):

1. **Timing changes** — the planet arrives a little early or late. Astronomers call these **transit timing variations**.
2. **Duration changes** — the transit lasts a little longer or shorter. These are **transit duration variations**.

For a moon, these two patterns are shifted by a quarter-cycle. If you plot one against the other, the points trace a loop, like an oval.

Other planets in the system can also cause timing changes. But they usually don't produce this neat quarter-step pattern. That makes the pattern a useful clue.

## What is still open

> Do any known planets show the quarter-step timing–duration pattern that a moon would cause?

Large public tables of transit times and durations exist for Kepler planets. Few people have tested them all in a consistent, open way.

## How to test it

1. Collect a planet's transit times and durations, with their error bars.
2. Search for a repeating pattern in both.
3. Measure the phase difference between the two patterns.
4. Check how often random shuffling of the data gives a pattern that strong (a "false alarm" test).
5. Treat any survivor as a **candidate** that needs more data.

Our free `fdastro.exomoon` code and Tutorial 8 walk through these steps.

## How we could be wrong

- Star spots can shift transit times and durations.
- Another planet can cause timing changes that sometimes look moon-like.
- With only a few transits, random noise can create a fake pattern.
- Because a planet is seen only once per orbit, a fast moon's wobble can look like a slower one (this is called **aliasing**).

## How you can help

- **Kids and families:** Do the running-and-spinning activity outside with a timer. Record each lap time. Do you see the pattern?
- **Students:** Read Kipping's 2009 idea in a simple summary. Draw the loop by hand using sine and cosine.
- **Coders:** Try Tutorial 8 on fake data first. Then test it on a real published table.

*Kids: please ask a parent, guardian or teacher before posting or commenting online.*

## Read more

Full disclosure with references: [D12 — Exomoons from timing and duration wobbles](../../disclosures/d12-exomoons-timing-duration.md)
