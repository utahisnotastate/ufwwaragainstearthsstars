# Planets We Have Seen Only Once

**Some planets take so long to orbit their stars that a telescope sees them pass in front just one time. Finding these "single transits" is hard — and that is exactly why some are still waiting in the data.**

> **Suggested header image:** A simple graph of a star's brightness over 27 days: a flat line with one small, U-shaped dip in the middle.
> **Alt text:** "Graph: a star's brightness stays flat for 27 days except for one small dip. That single dip could be a planet with a long orbit passing in front of the star."

**Evidence level:** 🟢 **Level 1 — Confirmed** that single-transit planets exist and have been found. 🟡 **Level 3 — Testable idea** that many more are still waiting in TESS and Kepler data.

---

Imagine you are watching a racetrack through a small window. You can only watch for one hour. Fast cars go past your window again and again. You see them many times.

But one car is driving a huge, slow lap around the whole city. In your one hour, it passes your window **once**.

Did you see a car? Yes! But you can't tell how long its lap is from one sighting. You'll need more clues.

That is the puzzle of single-transit planets.

## Why some planets show up only once

NASA's TESS telescope looks at each patch of sky for about **27 days** at a time before moving on. A planet that orbits its star every 3 days will cross in front of its star many times in that window. That makes it easy to spot.

But a planet that takes 100 days — or several years — to go around its star might cross just **once** while TESS is watching. Or not at all.

These long-period planets matter. Many of them are cooler and farther from their stars, more like the planets in our own Solar System. Some may be in the zone where liquid water could exist.

## Why they are hard to confirm

A single dip in a star's brightness can be caused by many things:

- A real planet passing in front of the star.
- Two stars eclipsing each other (an **eclipsing binary**), perhaps a faint pair in the background.
- A brief glitch from the spacecraft, such as when it adjusts its pointing.
- Scattered light from Earth or the Moon.
- An asteroid drifting through the image.
- The star itself flickering.

Most automatic searches are tuned to find **repeating** dips, because repetition is a strong sign of a real planet. A single dip needs extra checking. That takes time, and there are far more single dips than people have had time to check.

## Real successes

This is not just an idea. Astronomers have found long-period planets from single and double transits in both Kepler and TESS data. Volunteers in the **Planet Hunters TESS** citizen-science project have flagged long-period candidates by eye, including dips that computer searches missed at first. Follow-up telescopes then catch the next transit or measure the star's wobble to confirm the planet.

## What is still open

> How many long-period planets are recorded as single transits in public TESS and Kepler data, and how many of them can be confirmed with follow-up?

Every confirmed one helps fill in the "long-period" part of the planet family tree, which is still poorly known.

## How to test it

1. Download a star's light curve from the public MAST archive.
2. Remove slow brightness changes from the star itself.
3. Search for single dips with the right **shape**: a planet makes a smooth, U-shaped or flat-bottomed dip with a clear start and end.
4. Check that the dip's length fits the star's size and a reasonable orbit.
5. Check neighboring stars and spacecraft logs for glitches at the same time.
6. Look for a second transit in other TESS years or other telescopes.

Our free `fdastro.transits` code and Tutorial 7 show how.

## How we could be wrong

- Many single dips are eclipsing binaries. Checking whether the dip comes from the target star (not a neighbor) is essential.
- Some dips are spacecraft effects. If many stars dip at the same moment, it is not a planet.
- Without a second transit, the orbit period is uncertain. A "candidate" is not a planet until confirmed.

## How you can help

- **Kids and families:** Play "blink and you'll miss it." One person tells a story while holding up a card for one second at a random moment. Did everyone see it? How sure are you about what was on it?
- **Everyone:** Join **Planet Hunters TESS** on Zooniverse and look at real light curves. Human eyes are still great at spotting odd single dips.
- **Coders:** Try Tutorial 7 on a star you choose. Write down every dip and every reason you rejected one.

*Kids: please ask a parent, guardian or teacher before posting or commenting online.*

## Read more

Full disclosure with references: [D03 — Planets seen only once](../../disclosures/d03-single-transit-planets.md)
