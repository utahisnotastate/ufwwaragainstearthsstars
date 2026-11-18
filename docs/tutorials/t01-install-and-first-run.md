# Tutorial 1 — Install and first run

> **In one sentence:** Set up Python, install `fdastro`, and run your first calculation about visitors from other stars.

## For young readers

You need a computer with Python on it. Python is free. Ask a grown-up to help with installing. Then you will type one command and see a table of the three known space visitors from other stars!

## What you need

- Python 3.11 or newer (from [python.org](https://www.python.org/downloads/)).
- About 200 MB of free space.
- 15 minutes.

## Step 1 — Get the code

Download this repository as a ZIP file from [its GitHub page](https://github.com/utahisnotastate/ufwwaragainstearthsstars) (green **Code** button → **Download ZIP**) and unzip it, or use git:

```bash
git clone https://github.com/utahisnotastate/ufwwaragainstearthsstars.git future-disclosure-astronomy
cd future-disclosure-astronomy
```

## Step 2 — Make a private Python space (a "virtual environment")

This keeps the project's packages separate from the rest of your computer.

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## Step 3 — Install

```bash
python -m pip install -e ".[test]"
```

The core tools only need `numpy` and `scipy`. To download real data from archives later, add the optional extra:

```bash
python -m pip install -e ".[archives,test]"
```

> **Windows note:** some security settings block newly installed `.exe` helper programs. If `fdastro` or `pytest` is blocked, use `python -m fdastro` and `python -m pytest` instead. They do the same thing.

## Step 4 — Check that everything works

```bash
python -m pytest
```

You should see a line of dots and a message that all tests passed.

## Step 5 — Your first calculation

```bash
python -m fdastro isos
```

You will see something like:

```text
Object                        e    q (au)   i (deg)   v_inf (km/s)
1I/2017 U1               1.2011    0.2559    122.74          26.41
2I/Borisov               3.3565    2.0065     44.05          32.28
3I/ATLAS                 6.1235    1.3520    175.24          57.98
```

**What this means:**

- `e` is the **eccentricity** — how stretched the path is. Below 1 means a closed loop. Above 1 means the object will leave forever.
- `q` is the closest distance to the Sun, in **astronomical units** (au). One au is the Earth–Sun distance.
- `i` is the tilt of the path. Above 90° means it goes around "backwards".
- `v_inf` is how fast the object moves when it is very far from the Sun.

## Step 6 — The same thing in Python

```python
from fdastro.catalogs import INTERSTELLAR_OBJECTS
from fdastro.kepler import v_infinity_from_q_e_kms

for obj in INTERSTELLAR_OBJECTS:
    v = v_infinity_from_q_e_kms(obj["q_au"], obj["e"])
    print(f"{obj['designation']:<12} arrives at {v:5.1f} km/s, about {v * 3600:,.0f} km per hour")
```

3I/ATLAS was moving about 58 km/s far from the Sun. That is more than 200,000 km per hour!

## For experts

- `v_inf = sqrt(GM_sun (e - 1) / q)`, with GM_sun = k² au³/day² (Gaussian constant k = 0.01720209895).
- Elements in `fdastro.catalogs` are J2000 ecliptic osculating elements from the JPL Small-Body Database (retrieved 2026-11-17). For research, query fresh solutions.

## Next

[Tutorial 2 — Ellipses and hyperbolas](t02-orbits-ellipses-and-hyperbolas.md)
