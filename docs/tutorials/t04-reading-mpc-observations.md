# Tutorial 4 — Reading Minor Planet Center observations

> **In one sentence:** Learn the standard one-line format telescopes use to report moving objects, and turn those lines into orbit-fitting input.

## For young readers

The Minor Planet Center (MPC) is like the world's post office for asteroids and comets. Telescopes all over the world send it the positions of moving dots. Each position is one line of text, always written the same way. Some dots are seen only once or twice and cannot be matched to any known object yet. Those go into a file called the **Isolated Tracklet File**, or ITF. Nobody is hiding it — it is public, and anyone can study it.

## The 80-column format

Each line is exactly 80 characters. The important parts are:

| Columns | Meaning | Example |
|---|---|---|
| 1–12 | Object or tracklet name | `     K25N01A` |
| 15 | Observation type (`C` = CCD camera) | `C` |
| 16–32 | Date and time (UTC), day with decimals | `2025 07 01.12345` |
| 33–44 | Right ascension (hours, minutes, seconds) | `18 06 12.345` |
| 45–56 | Declination (degrees, minutes, seconds) | `-18 34 56.78` |
| 66–71 | Brightness and filter | `18.1 r` |
| 78–80 | Observatory code | `W68` |

## Step 1 — Parse some lines

```python
from fdastro.mpc import parse_mpc80, group_by_designation, to_arrays

lines = [
    "     TRK0001  C2025 07 01.10000 18 06 12.345-18 34 56.78         18.1 r      W68",
    "     TRK0001  C2025 07 01.12000 18 06 12.100-18 34 57.90         18.2 r      W68",
    "     TRK0001  C2025 07 01.14000 18 06 11.855-18 34 59.01         18.1 r      W68",
]
obs = parse_mpc80(lines)
for o in obs:
    print(f"{o.designation}  MJD {o.mjd_utc:.5f}  RA {o.ra_deg:.5f}°  Dec {o.dec_deg:+.5f}°  code {o.obscode}")
```

## Step 2 — Group by tracklet

```python
groups = group_by_designation(obs, min_obs=3)
for name, items in groups.items():
    mjd, ra, dec = to_arrays(items)
    print(name, len(items), "observations spanning", round((mjd[-1] - mjd[0]) * 24, 2), "hours")
```

## Step 3 — Account for where the telescope is

Nearby objects look different from different places on Earth. The MPC publishes each observatory's position as three "parallax constants". `fdastro` turns them into a position in space.

```python
import numpy as np
from fdastro.ephemeris import parse_obscodes, observer_geocentric_offset
from fdastro.iso import make_observations

# One line in the format of the MPC's public observatory-code list.
codes = parse_obscodes("F51 203.74409 0.936241 +0.351543 Pan-STARRS 1, Haleakala")
lon, rho_cos, rho_sin, name = codes["F51"]
mjd, ra, dec = to_arrays(obs)
offset = observer_geocentric_offset(mjd, lon, rho_cos, rho_sin)
ready = make_observations(mjd, ra, dec, sigma_arcsec=0.3, observer_offset_au=offset)
print(f"{name}: offset from Earth's center ≈ {np.linalg.norm(offset[0]) * 149597870.7:.0f} km")
```

(The observation lines above use code W68 for formatting practice, and the station constants are for F51; in real work, look up the code that each line actually reports.)

## Step 4 — Working with the real ITF

The ITF is large and changes as tracklets are linked. Download it from the MPC's ITF page (`itf.txt.gz`), then:

```py
from fdastro.mpc import load_mpc80, group_by_designation

itf = load_mpc80("itf.txt.gz")                 # reads .gz directly
tracklets = group_by_designation(itf, min_obs=3)
print(len(tracklets), "tracklets with at least 3 observations")
```

Or from the command line:

```bash
python -m fdastro parse-mpc itf.txt.gz --min-obs 3 --limit 20
```

Then build `Observations` for each tracklet (Step 3) and try `fdastro.iso.screen_tracklet_pairs` on a **small, well-chosen subset** — for example tracklets from one survey, in one sky region, within a two-week window, with fast or unusual motion.

## Important cautions

- **Times are UTC** in the 80-column format. The orbit tools treat them as TT/TDB; the ~69-second difference is mostly absorbed into the fitted orbit, but use converted times for precise work.
- **Space-based and roving observers** (types `S`, `V`) need a second line with their position. This parser skips second lines and flags the first lines; handle them separately.
- **The ADES format** (XML/PSV) is the MPC's modern standard. This tutorial covers the classic format because the ITF and many archives still use it.
- **Linking is hard.** Professional linkers handle millions of tracklets with clever math. Our pair screen is for learning and for small pilot studies.

## For experts

- Column layout follows the MPC's "Format for optical astrometric observations of comets, minor planets and natural satellites".
- `observer_geocentric_offset` uses GMST (IAU 1982) with UT1 ≈ UTC and neglects precession of the station vector (≲ tens of km over decades).
- Holman et al. (2018, arXiv:1805.02638) applied HelioLinC to the ITF and established orbits for about 41,000 new minor planets, showing that the file contains many linkable objects.

## Next

[Tutorial 5 — Tisserand and backwards orbits](t05-tisserand-and-backwards-orbits.md)
