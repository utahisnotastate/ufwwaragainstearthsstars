# Are There Interstellar Visitors Hiding in Lists of Unconnected Dots?

**Three objects from other star systems have been found passing through ours: ʻOumuamua, Borisov and 3I/ATLAS. Millions of asteroid sightings still wait to be connected into orbits. Could another visitor be among them?**

> **Suggested header image:** Diagram of the Sun with several closed oval orbits of asteroids, and one open curved path (a hyperbola) sweeping in from outside and back out again.
> **Alt text:** "Diagram: closed oval orbits of ordinary asteroids around the Sun, and one open curve that enters from far away and leaves again. The open curve is the path of an interstellar visitor."

**Evidence level:** 🟢 **Level 1 — Confirmed** that interstellar objects exist (three are known). 🟡 **Level 3 — Testable idea** that more are recorded, but not yet recognized, among unlinked asteroid observations.

---

Imagine a playground with a merry-go-round. All the toy horses go around and around in circles. Now imagine a ball thrown from a different playground across town. It zooms in, curves a little around the merry-go-round, and flies out the other side — never to come back.

The horses are like the asteroids and comets that belong to our Sun. They go around in closed loops. The thrown ball is like an **interstellar object**: a visitor from another star system, passing through once.

## Three visitors so far

- **1I/ʻOumuamua** was found on 19 October 2017 by the Pan-STARRS telescope in Hawaiʻi. It was moving too fast to be held by the Sun's gravity. It also sped up slightly in a way scientists are still discussing, without showing an obvious comet tail.
- **2I/Borisov** was found on 30 August 2019 by amateur astronomer Gennadiy Borisov, using a telescope he built himself. It looked like a normal comet — but it came from another star.
- **3I/ATLAS** (also called C/2025 N1) was found on 1 July 2025 by the ATLAS survey telescope in Chile. It was the fastest of the three and was traveling almost exactly backwards compared with the planets.

## How do we know they are from outside?

Astronomers measure an orbit's **eccentricity**, a number that describes its shape.

- A circle has eccentricity 0.
- A stretched oval has eccentricity between 0 and 1. It's still a closed loop.
- An eccentricity **above 1** means the path is open. The object is not tied to the Sun. It will leave and never return.

ʻOumuamua's eccentricity was about **1.2**. Borisov's was about **3.4**. 3I/ATLAS's was about **6.1** — extremely open.

Another way to say it: far from the Sun, these objects move at about **26**, **32** and **58 kilometers per second**. That's fast enough to cross the distance from New York to Los Angeles in between about one and three minutes!

## Connecting the dots

Big sky surveys photograph the sky every night. When something moves, they record a few positions in one night. That short set of sightings is called a **tracklet**.

To know an object's orbit, you need to connect tracklets from **different nights**. That is a giant puzzle. There are millions of tracklets, and many could fit together in many ways. To keep the puzzle solvable, linking methods make reasonable assumptions that fit most asteroids well.

Sightings that can't be connected yet go into a public list kept by the **Minor Planet Center**, called the **Isolated Tracklet File**. In 2018, Matthew Holman and colleagues developed a method called **HelioLinC** and used it to connect many of these leftover tracklets into orbits of new asteroids. That showed the list holds real objects waiting to be identified.

## What is still open

> Are any interstellar objects sitting unrecognized among unlinked observations?

Interstellar visitors move fast and on unusual paths. That can make their tracklets harder to connect. We think it is worth checking carefully.

## How to test it

1. Group tracklets that could belong to one object across several nights.
2. Fit an orbit **without assuming** it must be a closed loop.
3. Run a **"bound-orbit test"**: find the best closed-loop orbit, and the best open orbit. If the closed loop fits much worse, the object may be a visitor.
4. Check that no known object matches.
5. Have someone else repeat the whole thing independently.
6. Report any survivor to the Minor Planet Center **before** telling anyone else.

Our free `fdastro` code (`fdastro.iso`, `fdastro.kepler`, `fdastro.mpc`) and Tutorial 3 show how.

## How we could be wrong

- **Wrong links.** Joining tracklets from two different asteroids can create a fake, strange orbit.
- **Too short a track.** With only a few days of data, an orbit's shape is very uncertain.
- **Small errors in time or location** can bend a fitted path.
- **Comets** can be pushed by their own gas, which changes their paths slightly.

## How you can help

- **Kids and families:** Use two pins, a loop of string and a pencil to draw an oval (an ellipse). Then draw an open curve that never closes. Which one belongs to a visitor?
- **Students:** Use our code to calculate how fast ʻOumuamua, Borisov and 3I/ATLAS move far from the Sun. Compare your answers with published values.
- **Coders:** Try Tutorial 3. Then join our Interstellar Hunt challenge in 2027.

*Kids: please ask a parent, guardian or teacher before posting or commenting online.*

## Read more

Full disclosure with references: [D14 — Interstellar visitors in unlinked asteroid data](../../disclosures/d14-interstellar-objects-unlinked-data.md)
