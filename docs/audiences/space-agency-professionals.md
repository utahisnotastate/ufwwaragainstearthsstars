# Guide for Space Agency Professionals

> **In one sentence:** This is an independent, volunteer, open-source project that builds on the public data your missions produce; it aims to help with archival follow-up and public education, routes any candidates through official channels, and is not affiliated with or endorsed by NASA, ESA or any other agency.

## For young readers

This page is for people who work at space agencies like NASA. It explains that this project is run by volunteers, not by NASA, and that we are thankful for the free data that space agencies share with everyone.

## Who we are, and who we are not

- **Independent.** Future Disclosure: Astronomy & Alien Planets is a community project. It is **not** affiliated with, sponsored by, or endorsed by NASA, ESA, JAXA, CSA, ISRO, CNSA, any national laboratory, or any observatory.
- **No branding.** We do not use agency insignia or logos, and we follow agency media-usage guidelines when we credit images or data. Data credits name the mission and archive.
- **Public data only.** Everything we use comes from public archives (for example MAST, IRSA, the PDS, the MPC, ESA archives, and the ALMA Science Archive).
- **No accusation.** The word "disclosure" in our name refers to openly reporting where discoveries **might** be found in public data. We do **not** suggest that agencies withhold information. Unexplored signals usually reflect finite staff time, telescope time and the cost of false alarms.

## Why this project exists

Public archives are enormous. Mission teams publish catalogs, data products and pipelines, and the community has always mined them for discoveries — from Kepler planets found by volunteers to brown dwarfs found in WISE data by citizen scientists. This project tries to:

1. **Document open questions** where archival data could add value, with clear evidence levels ([registry](../disclosures/README.md)).
2. **Provide tested, open tools** (the `fdastro` Python package) with documented assumptions and limitations.
3. **Teach** the methods to students and the public with accurate, accessible materials ([lessons](../lessons/README.md)).
4. **Filter before forwarding.** Candidates must pass documented checks before anyone contacts a professional channel, to avoid adding noise.

## Our commitments to you

| Commitment | In practice |
|---|---|
| **Use official channels** | Astrometry and candidate objects go to the Minor Planet Center; transients to the Transient Name Server; TESS planet candidates to ExoFOP via its established process. We do not ask staff for special handling. |
| **No premature announcements** | We do not issue press statements about "discoveries". Candidates are described as candidates, with false-alarm estimates. |
| **Respect data policies** | We honor proprietary periods, data-use and acknowledgment policies, and citation requirements of each archive and mission. |
| **Accurate attribution** | We cite mission papers, pipeline papers and data DOIs. |
| **Public corrections** | Errors, including errors about missions or agencies, are corrected openly in the repository history and the [editorial notes](../about/editorial-notes.md). |
| **Accessibility and accuracy in outreach** | Educational materials follow a [style guide](../STYLE.md) with evidence labels and fact-checking rules. |

## How you could help (only if you wish, and within your organization's rules)

- **Point out errors.** If a description of your mission, instrument or pipeline is wrong, an issue or pull request is enormously helpful.
- **Point to existing work.** Many of our open questions may already be addressed in internal or published studies. A reference saves volunteers from duplicating effort.
- **Suggest better data products.** For example, which archive table is appropriate for a given search, or which known systematics affect it.
- **Mentor students.** Our [university lab](../lessons/l13-university-lab-orbit-fitting.md) and [tutorials](../tutorials/) benefit from expert review.

We understand that staff may need to comment in a personal capacity and may not be able to engage at all. That is completely fine.

## What we do not want

- We do **not** want to burden operations staff, help desks or follow-up networks with low-quality candidates.
- We do **not** want to imply agency endorsement through quotes, logos or images.
- We do **not** want to spread hype about agencies "missing" or "hiding" discoveries.

## Areas where archival work may be most useful

| Area | Disclosure | Relevant archive | Why archival work could help |
|---|---|---|---|
| Single and fading transits | [D02](../disclosures/d02-vanishing-transits.md), [D03](../disclosures/d03-single-transit-planets.md) | MAST (TESS, Kepler) | Long time baselines across missions reveal slow changes. |
| Cold nearby objects | [D04](../disclosures/d04-nearby-cold-worlds-wise.md) | IRSA (WISE/NEOWISE) | More than a decade of epochs enables motion-based searches. |
| Interstellar and unusual small bodies | [D14](../disclosures/d14-interstellar-objects-unlinked-data.md), [D15](../disclosures/d15-captured-interstellar-objects.md) | MPC, JPL SBDB | Unlinked observations and orbit catalogs support dynamical searches. |
| Subsurface gravity structure | [D10](../disclosures/d10-caves-and-buried-masses-gravity.md) | PDS Geosciences Node | Level-1 tracking data support localized analyses. |
| Microlensing populations | [D07](../disclosures/d07-short-microlensing-free-floating-planets.md) | Survey archives; Roman (future) | Population studies benefit from independent analyses. |

## Contact and governance

- Open an issue in the repository for corrections or questions.
- Project decisions, the corrections log, and the disclosure plan are public in the repository.

## Thank you

Every page in this project depends on missions designed, built and operated by agency and contractor teams, and on their decision to make data public. We are grateful.
