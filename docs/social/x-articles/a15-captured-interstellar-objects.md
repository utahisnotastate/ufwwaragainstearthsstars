# Did a Visitor From Another Star Move In and Stay?

**Almost everything in our Solar System orbits the Sun in the same direction. A few objects go backwards or over the top. Some scientists think one of them might have been captured from another star billions of years ago. Others disagree. Here is how we could find out more.**

> **Suggested header image:** Diagram of the Solar System's flat plane with planets orbiting counterclockwise, Jupiter's orbit highlighted, and one small asteroid traveling the same path clockwise.
> **Alt text:** "Diagram: planets orbit the Sun counterclockwise in a flat plane. One small asteroid follows Jupiter's orbit but travels clockwise, the opposite way. This is asteroid 2015 BZ509."

**Evidence level:** 🟢 **Level 1 — Confirmed** that some objects orbit the Sun backwards or steeply tilted. 🟡 **Level 3 — Testable idea** that some of them were captured from other stars. This is published but debated.

---

Imagine a big roundabout where all the cars drive the same way, around and around. Then you notice one car driving the **opposite** way, right along with the traffic, lap after lap, without crashing.

You might wonder: where did that car come from? Did it start here and get turned around? Or did it drive in from somewhere else?

Astronomers wonder the same thing about a few objects in our Solar System.

## Why almost everything goes the same way

Our Solar System formed about 4.6 billion years ago from a flat, spinning disk of gas and dust. Because the disk was spinning one way, the planets that formed from it all orbit the Sun in that same direction, on nearly the same flat plane.

So when we find something going **backwards** (astronomers say **retrograde**) or orbiting over the top, it stands out.

## A backwards companion of Jupiter

Asteroid **2015 BZ509**, now named **Kaʻepaokaʻawela**, was found in 2015 by the Pan-STARRS telescope in Hawaiʻi. It shares Jupiter's path around the Sun — but goes the **opposite way**. Its orbit is tilted about 163 degrees, which means nearly upside down compared with the planets.

In 2018, Fathi Namouni and Helena Morais published simulations suggesting it has been in this kind of orbit since the Solar System was very young. Because it is hard to explain how a native object could end up there that early, they argued it may have been **captured from another star** while the Sun was still in the cluster of stars where it was born.

Other scientists have questioned this conclusion. Some argue that objects from our own Solar System could also end up in such orbits. That debate is still going.

## Other strange orbits

Far beyond Neptune, there are icy objects with very steep orbits. **2008 KV42**, nicknamed **"Drac,"** is tilted about 103 degrees. **2011 KT19**, nicknamed **"Niku"** (its official name is now Taowu), is tilted about 110 degrees. These are past "straight up and over" — slightly backwards.

But here is an important lesson: **going backwards does not automatically mean "from another star."** Halley's Comet orbits the Sun backwards, and it is a member of our own Solar System. Gravity from planets and passing stars can flip and tilt orbits over billions of years.

## A helpful number

Astronomers use a number called the **Tisserand parameter** to sort objects by how they move compared with a big planet like Jupiter. It stays roughly the same even after an object has a close pass by that planet. That makes it a useful "fingerprint."

- Most main-belt asteroids have values **above 3**.
- Many comets have values **between 2 and 3**.
- Objects that go backwards often have **negative** values.

For 2015 BZ509, we calculate a value of about **−0.75** from its published orbit.

Our free `fdastro.tisserand` code and Tutorial 5 let you calculate this for any object.

## What is still open

> Are some backwards or steeply tilted objects really captured from other stars — and what evidence could tell captured objects apart from native ones?

## How to test it

1. Make a list of known retrograde and steeply tilted objects from NASA JPL's Small-Body Database.
2. Calculate their Tisserand parameters to group similar orbits.
3. Run long simulations: can each orbit be reached from inside our Solar System? How often?
4. Compare colors and spectra (how they reflect different colors of light) with native objects — while remembering that our own Solar System's objects are very varied.
5. Treat any result as a statistical clue, not a final answer.

## How we could be wrong

- Native objects can be flipped by planets and passing stars.
- Simulations depend on assumptions about the early Solar System.
- Color and composition alone can't prove where an object was born.
- With only a few strange objects known, chance plays a big role.

## How you can help

- **Kids and families:** Play the roundabout game. Everyone walks in a circle one way. One "visitor" walks the other way. How does the visitor have to move to avoid bumping into anyone?
- **Students:** Calculate the Tisserand parameter for Halley's Comet and for 2015 BZ509. Both are negative. What does that tell you — and what doesn't it tell you?
- **Coders:** Use Tutorial 5 to flag every retrograde object in a downloaded list.

*Kids: please ask a parent, guardian or teacher before posting or commenting online.*

## Read more

Full disclosure with references: [D15 — Captured interstellar objects already orbiting the Sun](../../disclosures/d15-captured-interstellar-objects.md)
