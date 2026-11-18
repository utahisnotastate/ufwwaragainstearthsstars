# Future Disclosure: Astronomy & Alien Planets

**Where tomorrow's discoveries may already be hiding in today's public data — explained simply, tested honestly, open to everyone.**

[![tests](https://github.com/utahisnotastate/ufwwaragainstearthsstars/actions/workflows/tests.yml/badge.svg)](https://github.com/utahisnotastate/ufwwaragainstearthsstars/actions/workflows/tests.yml) [![code: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE) [![docs: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey)](LICENSE-docs.md) ![python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)

---

## For young readers

Telescopes and spacecraft take more pictures than anyone can look at closely. Some discoveries — new planets, cold dark worlds near the Sun, even visitors from other stars — are probably sitting in those pictures right now. This project is a treasure map. It shows where to look, tells you how sure we are, and gives you free tools to search. You can help!

> "Alien planets" here means **planets around other stars**. This project is about real astronomy. It makes no claims about aliens.

## Start here

| I am… | Start with |
|---|---|
| A kid (about 6–12) | [Kids' guide](docs/audiences/kids.md) → [Lesson 1](docs/lessons/l01-finding-what-we-cannot-see.md) |
| A parent or curious adult | [Families and adults](docs/audiences/families-and-adults.md) |
| A teacher or tutor | [Teachers and tutors](docs/audiences/teachers-and-tutors.md) → [Lessons](docs/lessons/README.md) |
| A student / future NASA scientist or engineer | [Students and NASA hopefuls](docs/audiences/students-and-nasa-hopefuls.md) → [Tutorials](docs/tutorials/README.md) |
| An amateur astronomer | [Amateur astronomers](docs/audiences/amateur-astronomers.md) |
| A physicist | [Physicists](docs/audiences/physicists.md) |
| An astrophysicist or planetary scientist | [Astrophysicists](docs/audiences/astrophysicists.md) → [Disclosures](docs/disclosures/README.md) |
| At NASA, ESA or another space agency | [Space agency professionals](docs/audiences/space-agency-professionals.md) |
| A SETI researcher | [SETI researchers](docs/audiences/seti-researchers.md) |

## The 15 disclosures

Each **disclosure** is one testable idea about where discoveries may be waiting, with an honest evidence level:
🟢 **Level 1 — Confirmed** · 🔵 **Level 2 — Strong evidence** · 🟡 **Level 3 — Testable idea** · 🟠 **Level 4 — Long shot**

| ID | Disclosure | Main level |
|---|---|---|
| D01 | [Unseen planets in the far Solar System](docs/disclosures/d01-unseen-planets-far-solar-system.md) | 🟡 Level 3 |
| D02 | [Planets whose transits fade away](docs/disclosures/d02-vanishing-transits.md) | 🟡 Level 3 |
| D03 | [Planets seen only once](docs/disclosures/d03-single-transit-planets.md) | 🟡 Level 3 |
| D04 | [Cold, dark neighbors in infrared sky maps](docs/disclosures/d04-nearby-cold-worlds-wise.md) | 🟡 Level 3 |
| D05 | [Polarized light from planets](docs/disclosures/d05-polarized-light-from-planets.md) | 🟠 Level 4 |
| D06 | [Dust clouds and possible mini-moons at the Earth–Moon balance points](docs/disclosures/d06-earth-moon-trojan-points.md) | 🟠 Level 4 |
| D07 | [Free-floating planets in brief lensing flashes](docs/disclosures/d07-short-microlensing-free-floating-planets.md) | 🔵 Level 2 |
| D08 | [Radio auroras from planets and brown dwarfs](docs/disclosures/d08-radio-auroras.md) | 🟡 Level 3 |
| D09 | [Baby planets hidden in dusty disks](docs/disclosures/d09-planets-in-young-disks.md) | 🔵 Level 2 |
| D10 | [Caves and buried masses mapped by gravity](docs/disclosures/d10-caves-and-buried-masses-gravity.md) | 🟡 Level 3 |
| D11 | [Trojan and co-orbital asteroids near Venus, Earth and Mars](docs/disclosures/d11-inner-solar-system-trojans.md) | 🟡 Level 3 |
| D12 | [Exomoons from timing and duration wobbles](docs/disclosures/d12-exomoons-timing-duration.md) | 🟡 Level 3 |
| D13 | [Tilted orbits that point to unseen planets](docs/disclosures/d13-tilted-orbits-hidden-companions.md) | 🟡 Level 3 |
| D14 | [Interstellar visitors in unlinked asteroid data](docs/disclosures/d14-interstellar-objects-unlinked-data.md) | 🟡 Level 3 |
| D15 | [Captured interstellar objects already orbiting the Sun](docs/disclosures/d15-captured-interstellar-objects.md) | 🟡 Level 3 |

Full registry and how to propose a new one: [docs/disclosures/README.md](docs/disclosures/README.md).

## The code: `fdastro`

A small, tested Python package (needs only `numpy` and `scipy`).

```bash
git clone https://github.com/utahisnotastate/ufwwaragainstearthsstars.git
cd ufwwaragainstearthsstars
python -m pip install -e ".[test]"
python -m pytest                    # run the test suite
python -m fdastro isos              # the three known interstellar objects
python -m fdastro tisserand --examples
python -m fdastro demo-iso          # fit a synthetic 3I/ATLAS-like object
```

| Module | What it does | Disclosure |
|---|---|---|
| `fdastro.kepler` | Exact orbits of every shape, elements, hyperbolic excess speed, radiants | D14 |
| `fdastro.iso` | Orbit fitting from sky positions and a bound-orbit likelihood-ratio test | D14 |
| `fdastro.mpc` | Reads Minor Planet Center 80-column observations (including the ITF) | D14 |
| `fdastro.tisserand` | Tisserand parameter and odd-orbit screening | D15 |
| `fdastro.astrometry` | Parallax and proper motion (five-parameter fits) | D04 |
| `fdastro.transits` | Single-transit search, fading-transit trend test | D02, D03 |
| `fdastro.exomoon` | TTV/TDV 90° phase test with permutation false-alarm probability | D12 |
| `fdastro.obliquity` | Secular-resonance locus for unseen outer companions | D13 |
| `fdastro.microlensing` | Einstein radius/time, light curves, achromaticity | D07 |
| `fdastro.stats` | Significance and look-elsewhere corrections | all |

Every Python code block in the [tutorials](docs/tutorials/README.md) is executed by the test suite, so the documentation always matches the code.

> **Windows tip:** if security settings block newly installed helper programs, always use `python -m pytest` and `python -m fdastro` rather than the bare commands.

## Everything else

- **Lessons** for ages 6 to university, with NGSS alignment: [docs/lessons](docs/lessons/README.md)
- **Release plan** (15-week schedule, review process, risks, metrics): [docs/plan/disclosure-plan.md](docs/plan/disclosure-plan.md)
- **X (Twitter) articles and threads**, ready for review: [docs/social](docs/social/README.md)
- **Glossary** and **FAQ**: [docs/about/glossary.md](docs/about/glossary.md), [docs/about/faq.md](docs/about/faq.md)
- **How to report a possible discovery**: [docs/about/how-to-report-a-discovery.md](docs/about/how-to-report-a-discovery.md)
- **Public data sources**: [docs/about/data-sources.md](docs/about/data-sources.md)
- **What we changed from the original notes, and why**: [docs/about/editorial-notes.md](docs/about/editorial-notes.md)
- **Writing and evidence style guide**: [docs/STYLE.md](docs/STYLE.md)

## Principles

1. **Honest evidence levels** on every claim.
2. **Respect for scientists.** Unexamined data is normal, not a scandal.
3. **Every idea comes with a way to prove it wrong.**
4. **Simple first, detailed second.** Every page opens with a part a child can read.
5. **No health advice, no hype, no secrets.**

## Independence

This is an independent, community-run project. It is not affiliated with or endorsed by NASA, ESA, the Minor Planet Center, the SETI Institute, or any other organization it mentions.

## Contributing and license

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).
Code is released under the [MIT License](LICENSE). Documentation, lessons and articles are released under [CC BY 4.0](LICENSE-docs.md). If you use this work, please cite it ([CITATION.cff](CITATION.cff)).
