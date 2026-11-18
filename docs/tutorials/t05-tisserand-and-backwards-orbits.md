# Tutorial 5 — Tisserand and backwards orbits

> **In one sentence:** Use one number, the Tisserand parameter, to spot orbits that go "backwards" or steeply tilted — places where captured visitors from other stars might hide.

## For young readers

Imagine a roundabout where every car drives the same way. Now you spot a car going the wrong way! You would wonder where it came from. In our Solar System, almost everything orbits the Sun in the same direction. A few objects go backwards. Most of them probably came from the far edge of our own Solar System. But a few scientists think one or two might have been captured from another star. A number called the **Tisserand parameter** helps us find these odd ones quickly.

## The big idea

The Tisserand parameter with respect to a planet P is

T_P = a_P / a + 2 √( (a / a_P)(1 − e²) ) · cos i

It stays nearly the same even when the planet's gravity changes the small body's orbit. It works like a fingerprint. With respect to Jupiter:

| T_J | Usual meaning |
|---|---|
| above 3 | ordinary asteroid |
| 2 to 3 | Jupiter-family comet |
| 0 to 2 | Halley-type or long-period comet, or a "Damocloid" |
| below 0 | backwards (retrograde) orbit |

## Step 1 — Compute it

```python
from fdastro.tisserand import tisserand_parameter, jupiter_class

tj = tisserand_parameter(a=5.2026, e=0.0, i_deg=0.0)
print(f"Jupiter's own orbit: T_J = {tj:.3f}")  # exactly 3

tj_bz = tisserand_parameter(a=5.14348, e=0.37772, i_deg=163.1355)
print(f"2015 BZ509: T_J = {tj_bz:.2f} -> {jupiter_class(tj_bz)}")
```

2015 BZ509 (now named Kaʻepaokaʻawela) shares Jupiter's orbit but goes around the Sun **backwards**. Its T_J is about −0.75.

> **Correction note:** the original brainstorming notes for this project gave T_J = −1.39 for this object. Using the JPL elements, the correct value is about −0.75.

## Step 2 — Screen a list

```python
from fdastro.catalogs import HIGH_INCLINATION_EXAMPLES
from fdastro.tisserand import capture_candidate_screen

for hit in capture_candidate_screen(HIGH_INCLINATION_EXAMPLES, tj_max=2.0, i_min_deg=70.0):
    print(f"{hit.name:<48} T_J = {hit.tj:+.2f}  i = {hit.i_deg:5.1f}°  ({'; '.join(hit.reasons)})")
```

The example main-belt asteroid is not flagged. The backwards objects are.

## Step 3 — Use real catalogs

The JPL Small-Body Database has a query tool that can export orbital elements for every known asteroid and comet as a CSV file. Download `a`, `e`, `i` and the name, then:

```py
import csv
from fdastro.tisserand import capture_candidate_screen

with open("sbdb_export.csv", newline="") as fh:
    rows = [{"name": r["full_name"], "a": r["a"], "e": r["e"], "i": r["i"]}
            for r in csv.DictReader(fh) if r["a"] and r["e"] and float(r["e"]) < 1]
hits = capture_candidate_screen(rows)
print(len(hits), "objects flagged for a closer look")
```

## A flag is not a discovery

A low T_J tells you an orbit is **unusual**. It does not tell you where the object came from. Most backwards objects are thought to come from the Oort cloud, the far edge of our own Solar System. To test an interstellar origin, scientists:

1. make thousands of "clone" orbits that fit the observations,
2. run them backwards in time for millions or billions of years with all planets included, and
3. ask whether the clones could have formed in our Solar System.

Namouni & Morais (2018) did this for 2015 BZ509 and suggested it could be interstellar. Other researchers disagree. That debate is exactly how science should work. See [D15](../disclosures/d15-captured-interstellar-objects.md).

## For experts

- T_P derives from the Jacobi integral of the circular restricted three-body problem under the assumption a ≫ planet's Hill radius scale, small planet mass, and the planet on a circular orbit; it is not conserved through close encounters with other planets.
- `a_J = 5.2026 au` (Murray & Dermott 1999). Using JPL's osculating value changes T_J at the ~1e-3 level.
- For trans-Neptunian objects, `tisserand_parameter(a, e, i, a_planet=30.07)` (Neptune) is more meaningful.

## Next

[Tutorial 6 — Parallax and proper motion](t06-parallax-and-proper-motion.md)
