# How to report a possible discovery

> **In one sentence:** If you think you found something new, check it carefully, write it down clearly, and send it to the right professional clearinghouse — never announce it as "confirmed" yourself.

## For young readers

Finding something new is exciting! Scientists have a careful way to share it, so nobody gets fooled by a mistake. First, check your work. Second, ask a teacher or a grown-up to look too. Third, send it to the official group that collects that kind of discovery. Do not post your name, school or address online. Let a grown-up help you.

## Step 1 — Is it already known?

| If you found… | Check here first |
|---|---|
| A moving object (asteroid, comet, possible interstellar object) | The MPC's [MPChecker](https://www.minorplanetcenter.net/cgi-bin/checkmp.cgi) and the JPL [Small-Body Database](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html) |
| A transit-like dip in TESS data | [ExoFOP-TESS](https://exofop.ipac.caltech.edu/tess/) and the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) |
| A fast-moving infrared source (possible brown dwarf) | [SIMBAD](https://simbad.cds.unistra.fr/simbad/), Gaia, and the [Backyard Worlds](https://www.zooniverse.org/projects/marckuchner/backyard-worlds-planet-9) discussion boards |
| A brief brightening (transient, possible microlensing) | The [Transient Name Server](https://www.wis-tns.org/) and the survey's own alert pages |

## Step 2 — Try hard to prove yourself wrong

Use the "How we could be wrong" section of the matching [disclosure](../disclosures/README.md). For every candidate, ask:

1. **Is it in the raw images,** not just in a processed catalog?
2. **Could it be an artifact?** Cosmic rays, satellite trails, spacecraft events, bad pixels, ghosts.
3. **Did I search many places?** If you tested a million possibilities, one-in-a-million flukes are expected. Correct for the number of trials (`fdastro.stats.trials_corrected_p`).
4. **Are my error bars realistic?** Too-small errors make everything look significant.
5. **Does it hold up with a different method or a different data set?**

## Step 3 — Write a clear candidate report

Include:

- **What:** one sentence ("a hyperbolic-orbit candidate from two linked ITF tracklets").
- **Data:** archive, file names, IDs, dates, and versions.
- **Method:** software and version (`fdastro` version), settings, and random seeds.
- **Result:** numbers with uncertainties, and the evidence level you think it deserves.
- **Checks done:** everything from Step 2, including what failed.
- **What would confirm or refute it:** the observation that would settle it.

## Step 4 — Send it to the right place

| Kind of candidate | Where it goes | Notes |
|---|---|---|
| Asteroid/comet astrometry | The [Minor Planet Center](https://www.minorplanetcenter.net/) | Submissions must follow MPC rules and formats (ADES). Observers need an observatory code. Re-measuring archival images can count, but read the MPC's guidance first. |
| Possible interstellar object | MPC first; then contact professional orbit computers | Ask an experienced observer or a university astronomer to help. Fast follow-up matters. |
| TESS planet candidate | [ExoFOP-TESS](https://exofop.ipac.caltech.edu/tess/) (Community TOIs) or via a citizen-science project | Planet Hunters TESS is a friendly route for newcomers. |
| Brown dwarf / fast mover | Backyard Worlds: Planet 9 | Their team vets and follows up candidates. |
| Transient | Transient Name Server | Requires an account; follow their reporting rules. |

## Step 5 — Talk about it responsibly

- Say **"candidate"** until independent confirmation.
- Credit the data providers and the people who helped.
- Share your code and data so others can check.
- If you were wrong, say so publicly and kindly. That is good science.

## For children and families

- A parent, guardian or teacher should make any account and send any report.
- Never share a child's full name, school, address or photo publicly.
- Citizen-science platforms credit volunteers by username. That is the safest way for young people to take part.

## For experts

- Astrometric reports for hyperbolic candidates should include per-observation uncertainties, timing source, catalog (e.g., Gaia DR3), and star-catalog debiasing.
- Consider submitting a short note to the *Research Notes of the AAS* after confirmation, and archive code and data with a DOI (e.g., Zenodo).
- The project's own review path for candidates is described in the [disclosure plan](../plan/disclosure-plan.md).
