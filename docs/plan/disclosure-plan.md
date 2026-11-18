# The Disclosure Plan

> **In one sentence:** This is our step-by-step plan to share 15 science ideas with the world, one week at a time, in a way that is careful, honest and fun for everyone, including kids.

## For young readers

We have 15 ideas about where new space discoveries might be hiding. We will share one idea each week. Each week there will be a story to read, an activity to try at home or school, and a puzzle for grown-up helpers. Before we share anything, real scientists will check it. If we make a mistake, we will fix it and say so out loud. That is how good science works.

---

## Contents

1. [Mission and principles](#1-mission-and-principles)
2. [Who this is for](#2-who-this-is-for)
3. [Phase 0 — Get ready (November–December 2026)](#3-phase-0--get-ready-novemberdecember-2026)
4. [Phase 1 — Fifteen weeks, fifteen disclosures (January–April 2027)](#4-phase-1--fifteen-weeks-fifteen-disclosures-januaryapril-2027)
5. [Phase 2 — Community data challenges (April–September 2027)](#5-phase-2--community-data-challenges-aprilseptember-2027)
6. [Phase 3 — Education rollout (February–November 2027)](#6-phase-3--education-rollout-februarynovember-2027)
7. [Phase 4 — Research outputs (June–November 2027)](#7-phase-4--research-outputs-junenovember-2027)
8. [Scientific review process](#8-scientific-review-process)
9. [From "flag" to "report": what happens to a possible discovery](#9-from-flag-to-report-what-happens-to-a-possible-discovery)
10. [Corrections and retractions policy](#10-corrections-and-retractions-policy)
11. [Risk register](#11-risk-register)
12. [How we measure success](#12-how-we-measure-success)
13. [Governance and roles](#13-governance-and-roles)
14. [Budget: free and low-cost options](#14-budget-free-and-low-cost-options)
15. [Twelve-month calendar (December 2026 – November 2027)](#15-twelve-month-calendar-december-2026--november-2027)

---

## 1. Mission and principles

### Mission

Help people of every age learn real astronomy by showing **where new discoveries may already be waiting in public data**, and give them honest tools to look.

### Principles

1. **Honest first.** Every claim carries an [evidence level](../STYLE.md#4-evidence-levels). We say "we don't know" when we don't know.
2. **Open by default.** All code is open source (MIT). All writing is shared under CC BY 4.0. All data we use is public.
3. **Simple, then deep.** Every page starts simple enough for a 10-year-old. Expert detail comes after.
4. **Respect the people who do this work.** Survey teams, archive staff and researchers built every data set we use. Unexplored data exists because time and telescopes are limited — not because anyone is hiding anything.
5. **Check before we share.** No public post makes a science claim until a second person has checked it (see [Section 8](#8-scientific-review-process)).
6. **Fix mistakes in public.** Corrections are fast, visible and kind (see [Section 10](#10-corrections-and-retractions-policy)).
7. **Keep children safe.** Kids learn and take part through parents, guardians, teachers and tutors. We never collect children's personal information.
8. **Stay in our lane.** We share astronomy. We do not give medical, wellness or financial advice. "Alien planets" means planets around other stars; we make no claims about alien life or technology.

### What "disclosure" means in this project

A **disclosure** is a short public report about a place where a discovery *might* be hiding. It is **not** a claim that anything has been kept secret. Every disclosure says how sure we are, how to test the idea, and how it could turn out to be wrong. We repeat this in every launch post because the word can be misread (see the [risk register](#11-risk-register)).

---

## 2. Who this is for

| Audience | What they need from us | Main entry point |
|---|---|---|
| Children (about 6–12) | Short stories, pictures-in-words, hands-on activities | [Kids guide](../audiences/kids.md), [lessons](../lessons/) |
| Teens and NASA hopefuls | Real data, real code, career paths | [Students guide](../audiences/students-and-nasa-hopefuls.md), [tutorials](../tutorials/) |
| Parents, families, adults | Clear explanations, what's real vs. hype | [Families and adults guide](../audiences/families-and-adults.md) |
| Teachers and tutors | Ready lessons with standards links and answer keys | [Teachers and tutors guide](../audiences/teachers-and-tutors.md) |
| Amateur astronomers | Observing projects and data projects | [Amateur astronomers guide](../audiences/amateur-astronomers.md) |
| Physicists | Clear models, assumptions and error budgets | [Physicists guide](../audiences/physicists.md) |
| Astrophysicists | Testable hypotheses, archives, prior work | [Astrophysicists guide](../audiences/astrophysicists.md) |
| Space agency professionals | Respectful, accurate use of mission data; reporting channels | [Space agency professionals guide](../audiences/space-agency-professionals.md) |
| SETI researchers | Which ideas touch technosignature work, and which do not | [SETI researchers guide](../audiences/seti-researchers.md) |

---

## 3. Phase 0 — Get ready (November–December 2026)

**Goal:** A complete, reviewed, working repository before the first public disclosure.

### 3.1 Repository

- [ ] README with a kid-friendly opening and an expert summary.
- [ ] Licenses: MIT for code, CC BY 4.0 for documentation.
- [ ] `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `CITATION.cff`, `CHANGELOG.md`.
- [ ] Issue templates: bug report, candidate report, new disclosure idea, correction request.
- [ ] Continuous integration: tests run on every pull request.
- [ ] Branch protection: no direct pushes to `main`; every change needs one review.

### 3.2 Code (`fdastro` package)

- [ ] Every module has unit tests that check against known physics (for example, the speeds of 1I/ʻOumuamua, 2I/Borisov and 3I/ATLAS computed from their published orbits).
- [ ] Tests pass on Linux, Windows and macOS with Python 3.11 or newer.
- [ ] Every tutorial runs from start to finish on a clean install.

### 3.3 Documentation

- [ ] All 15 disclosure dossiers follow the [page template](../STYLE.md#5-page-template-for-a-disclosure).
- [ ] Every claim has an evidence label and a reference.
- [ ] Simple layer checked with a readability tool (target: about grade 4–6).
- [ ] Accessibility pass: headings, alt text, link text, no color-only meaning.
- [ ] [Editorial notes](../about/editorial-notes.md) list everything removed from the original notes, and why.

### 3.4 Review before launch

| Step | Who | When |
|---|---|---|
| Internal science check of all 15 dossiers | Science Lead + one other maintainer | 1–11 Dec 2026 |
| Invite external expert reviewers (one per topic area) | Science Lead | by 4 Dec 2026 |
| External review window | Volunteer experts | 7 Dec 2026 – 8 Jan 2027 |
| Reading check with real kids (with parent/teacher present) | Education Lead | 7–18 Dec 2026 |
| Fix list closed | All maintainers | by 8 Jan 2027 |

We ask experts to review **as individuals**. A review is not an endorsement by their employer, and we never say otherwise.

### 3.5 Soft launch

- **15 Dec 2026:** Repository made public for feedback. No social media push yet.
- **21 Dec 2026 – 3 Jan 2027:** Holiday quiet period. Only urgent fixes.
- **5 Jan 2027:** Public launch article ([a00](../social/x-articles/a00-launch.md)) and launch thread.

---

## 4. Phase 1 — Fifteen weeks, fifteen disclosures (January–April 2027)

**Rhythm:** One disclosure every **Tuesday**. The order starts with the most solid and most timely ideas and ends with the long shots.

### 4.1 Why this order

1. **D14 first:** Interest in interstellar visitors is high after 3I/ATLAS (discovered 1 July 2025).
2. **D02 second:** TOI-2535 b's vanishing transits were published in November 2026 (Yee et al. 2026, *ApJL*).
3. **D01 third:** The Vera C. Rubin Observatory reported the large distant object 2026 ED138 in October 2026, so the far Solar System is in the news.
4. **Level 2 topics early** (D07, D09) build trust: people see we report confirmed science accurately.
5. **Level 4 topics last** (D06, D05), after readers understand our evidence levels.

### 4.2 Weekly package

Every week ships the same seven pieces:

1. **Dossier** — the full disclosure page in `docs/disclosures/`.
2. **Learn-by-doing** — a tutorial (code) or a lesson (no code).
3. **X Article** — long-form post in `docs/social/x-articles/`.
4. **X Thread** — short version in [x-threads.md](../social/x-threads.md).
5. **Kid activity** — 15–30 minutes, low-cost materials, adult nearby.
6. **Community challenge** — a small, safe task for older students and adults.
7. **Office hour** — a 45-minute live Q&A (Thursday), recorded with captions.

### 4.3 The schedule

| Week | Date (Tue) | Disclosure | Level | Learn-by-doing | Kid activity | Community challenge |
|---|---|---|---|---|---|---|
| 1 | 12 Jan 2027 | [D14 Interstellar visitors in unlinked asteroid data](../disclosures/d14-interstellar-objects-unlinked-data.md) | 🟡 Level 3 | [Tutorial 3: fit an orbit and test if it is bound](../tutorials/t03-fit-an-orbit-and-test-if-bound.md) | Draw an ellipse with two pins and string; then a "fly-by" curve that never closes | Compute the speed far from the Sun (v∞) for 1I, 2I and 3I from their published orbits; compare with papers |
| 2 | 19 Jan 2027 | [D02 Planets whose transits fade away](../disclosures/d02-vanishing-transits.md) | 🟡 Level 3 | [Tutorial 7: single and fading transits](../tutorials/t07-single-and-fading-transits.md) | Spin a ball on a tilted string around a lamp; watch its shadow miss the wall | Measure transit depth per TESS sector for a list of known hot Jupiters; look for steady trends |
| 3 | 26 Jan 2027 | [D01 Unseen planets in the far Solar System](../disclosures/d01-unseen-planets-far-solar-system.md) | 🟡 Level 3 | [Lesson 1: finding what we cannot see](../lessons/l01-finding-what-we-cannot-see.md) | Bedsheet "trampoline": find a hidden ball by watching marbles roll | Summarize published limits on a distant planet from spacecraft ranging and pulsar timing |
| 4 | 2 Feb 2027 | [D07 Free-floating planets in brief lensing flashes](../disclosures/d07-short-microlensing-free-floating-planets.md) | 🔵 Level 2 | [Tutorial 10: microlensing timescales](../tutorials/t10-microlensing-timescales.md) | Look at a printed dot through the bottom of a clear glass; slide the glass past it | Compute how long a lensing flash lasts for a star, a Jupiter and an Earth |
| 5 | 9 Feb 2027 | [D04 Cold, dark neighbors in infrared sky maps](../disclosures/d04-nearby-cold-worlds-wise.md) | 🟡 Level 3 | [Tutorial 6: parallax and proper motion](../tutorials/t06-parallax-and-proper-motion.md) | Thumb-blink parallax: near things jump more | Join [Backyard Worlds: Planet 9](https://www.zooniverse.org/projects/marckuchner/backyard-worlds-planet-9) and classify 50 flipbooks |
| 6 | 16 Feb 2027 | [D15 Captured interstellar objects already orbiting the Sun](../disclosures/d15-captured-interstellar-objects.md) | 🟡 Level 3 | [Tutorial 5: Tisserand and backwards orbits](../tutorials/t05-tisserand-and-backwards-orbits.md) | Roundabout game: everyone walks one way; one "visitor" walks the other | Compute the Tisserand parameter for known retrograde objects from the JPL Small-Body Database |
| 7 | 23 Feb 2027 | [D03 Planets seen only once](../disclosures/d03-single-transit-planets.md) | 🟡 Level 3 | [Tutorial 7: single and fading transits](../tutorials/t07-single-and-fading-transits.md) | "Blink and you'll miss it": one card held up once during a story | Join [Planet Hunters TESS](https://www.zooniverse.org/projects/nora-dot-eisner/planet-hunters-tess) and look for single dips |
| 8 | 2 Mar 2027 | [D09 Baby planets hidden in dusty disks](../disclosures/d09-planets-in-young-disks.md) | 🔵 Level 2 | Astrophysicists guide + matching lesson | Drag a finger through water in a round tray; watch the wake | Find three ALMA disk papers that report gas "kinks" and list the planet masses they suggest |
| 9 | 9 Mar 2027 | [D11 Trojan and co-orbital asteroids near Venus, Earth and Mars](../disclosures/d11-inner-solar-system-trojans.md) | 🟡 Level 3 | [Lesson 5: balance points in space](../lessons/l05-balance-points-in-space.md) | Two kids walk a circle; a third "Trojan" keeps the same distance ahead | List known Earth and Mars Trojans and the year each was found |
| 10 | 16 Mar 2027 | [D12 Exomoons from timing and duration wobbles](../disclosures/d12-exomoons-timing-duration.md) | 🟡 Level 3 | [Tutorial 8: exomoon timing test](../tutorials/t08-exomoon-timing-test.md) | Run a lap holding a friend's hand while they swing around you; time each lap | Run the timing test on published transit-timing tables |
| 11 | 23 Mar 2027 | [D13 Tilted orbits that point to unseen planets](../disclosures/d13-tilted-orbits-hidden-companions.md) | 🟡 Level 3 | [Tutorial 9: tilted orbits and hidden companions](../tutorials/t09-tilted-orbits-and-hidden-companions.md) | Spinning top that wobbles when you tap it | Compare tilted planets with Gaia DR4 companion candidates (released 2 Dec 2026) |
| 12 | 30 Mar 2027 | [D10 Caves and buried masses mapped by gravity](../disclosures/d10-caves-and-buried-masses-gravity.md) | 🟡 Level 3 | Physicists guide + matching lesson | Knock on a wall to find a hollow spot | Read the GRAIL and Mare Tranquillitatis cave papers; write a 200-word summary |
| 13 | 6 Apr 2027 | [D08 Radio auroras from planets and brown dwarfs](../disclosures/d08-radio-auroras.md) | 🟡 Level 3 | [Lesson 8: radio auroras](../lessons/l08-radio-auroras.md) | Listen to recorded Jupiter radio sounds; tune an AM radio between stations | Learn about NASA's Radio JOVE kits; list radio-loud brown dwarfs from published papers |
| 14 | 13 Apr 2027 | [D06 Dust clouds and possible mini-moons at the Earth–Moon balance points](../disclosures/d06-earth-moon-trojan-points.md) | 🟠 Level 4 | [Lesson 5: balance points in space](../lessons/l05-balance-points-in-space.md) | Spot dust in a sunbeam; it shows up only at certain angles | Plan (do not yet run) a safe amateur polarization observation; list the false signals |
| 15 | 20 Apr 2027 | [D05 Polarized light from planets](../disclosures/d05-polarized-light-from-planets.md) | 🟠 Level 4 | [Lesson 7: light has a direction](../lessons/l07-light-has-a-direction.md) | Look at a phone screen and the sky through polarized sunglasses; tilt your head | Estimate how small a planet's polarized signal is compared with its star |

### 4.4 Week-by-week checklist (repeat every week)

| Day | Task | Owner |
|---|---|---|
| Wednesday (week before) | Final dossier frozen; tutorial or lesson tested on a clean install | Science Lead |
| Thursday (week before) | Article, thread and image drafted | Comms Lead |
| Friday (week before) | Second-person science check of every post | Science reviewer |
| Monday | Kid activity tested by a parent or teacher volunteer | Education Lead |
| **Tuesday** | Publish dossier, article and thread | Comms Lead |
| Wednesday | Kid fact post + myth vs. fact post | Comms Lead |
| Thursday | Live office hour (captioned, recorded) | Science Lead + Education Lead |
| Friday | Collect questions and corrections; update FAQ | All |

### 4.5 Phase 1 wrap-up

- **27 Apr 2027:** "What we learned" article: most-asked questions, corrections made, community results.
- **Survey:** Short anonymous feedback form for teachers and adults (no data collected from children).

---

## 5. Phase 2 — Community data challenges (April–September 2027)

**Goal:** Turn reading into doing, safely and carefully.

### 5.1 How we work with existing projects

Several citizen-science projects already do excellent work in these areas. **We complement them; we do not compete with them.**

- We point people **to** their platforms and follow their rules.
- We do **not** claim any partnership, endorsement or official tie unless the project agrees in writing.
- Before any formal collaboration, co-branding or shared data release, we ask the project team for permission.
- If a project asks us to change how we describe them, we change it.

### 5.2 The three challenges

#### Challenge A — "Interstellar Hunt" (MPC Isolated Tracklet File)

| Item | Detail |
|---|---|
| Dates | 4 May – 31 Jul 2027 |
| Question | Do any groups of unlinked observations in the Minor Planet Center's Isolated Tracklet File (ITF) fit an orbit that is *not* bound to the Sun? |
| Data | MPC Isolated Tracklet File (public) |
| Tools | `fdastro.mpc`, `fdastro.iso`, `fdastro.kepler`; [Tutorial 3](../tutorials/t03-fit-an-orbit-and-test-if-bound.md) |
| Who | Adults and older students (with supervision) comfortable with Python |
| Prior work | Holman et al. (2018) used the HelioLinC method to link many ITF observations into new minor-planet orbits. We build on that idea; we do not replace it. |
| Pass rule | A candidate must (1) link at least three nights, (2) fail the bound-orbit test at high significance, (3) not match any known object, and (4) be reproduced by a second, independent person. |
| Reporting | Candidates that pass go to the Science Lead, then to the Minor Planet Center through its normal channels. No social media announcement before the MPC has responded. |

#### Challenge B — "Cold Neighbors" (WISE / NEOWISE motion)

| Item | Detail |
|---|---|
| Dates | 1 Jun – 31 Aug 2027 |
| Question | Can more volunteers help find nearby cold brown dwarfs and possible free-floating planets moving across infrared sky maps? |
| Where | On [Backyard Worlds: Planet 9](https://www.zooniverse.org/projects/marckuchner/backyard-worlds-planet-9), following its rules |
| Our role | Teaching materials ([Tutorial 6](../tutorials/t06-parallax-and-proper-motion.md), lessons) that help people get started |
| Reporting | Through the Backyard Worlds platform and team, as that project directs |

#### Challenge C — "Seen Only Once" (TESS single transits)

| Item | Detail |
|---|---|
| Dates | 1 Jul – 30 Sep 2027 |
| Question | How many long-period planets show only one transit in TESS data? |
| Where | On [Planet Hunters TESS](https://www.zooniverse.org/projects/nora-dot-eisner/planet-hunters-tess), following its rules; plus our own open notebooks for people who want to code |
| Tools | `fdastro.transits`; [Tutorial 7](../tutorials/t07-single-and-fading-transits.md) |
| Reporting | Through Planet Hunters TESS as that project directs; independently found candidates go through our review and then to ExoFOP-TESS as Community TOIs (CTOIs) only if they pass |

### 5.3 Challenge safety rules

1. Children take part only with a parent, guardian or teacher, and only on platforms with their own child-safety rules.
2. No one posts a "discovery" publicly. Possible finds go through the [flag-to-report pipeline](#9-from-flag-to-report-what-happens-to-a-possible-discovery).
3. Credit is shared fairly. Everyone who contributed is named (with permission) in any report.
4. No prizes of money. Recognition only (certificates, thank-you lists).

---

## 6. Phase 3 — Education rollout (February–November 2027)

### 6.1 Schools

- **Lesson packs** for each grade band, linked to standards (for the US, NGSS performance expectations such as MS-ESS1-2 and HS-ESS1-4). Teachers adapt freely.
- **Printable PDFs** of every lesson and every dossier's "For young readers" section, in large type and black-and-white-friendly layouts.
- **"Space Detective" certificate** for classes that complete five lessons.
- **Back-to-school pack** (August 2027): a 6-week unit built from the best-tested lessons.

### 6.2 Libraries and clubs

- One-hour "Hidden Worlds" library program with a slide deck, a script and a materials list (under US$20).
- Astronomy club guide: how to run a 4-week data night using the tutorials.

### 6.3 Tutors and home educators

- One-page lesson cards with a 5-minute warm-up, main activity, and three check questions.
- Answer keys and "common wrong ideas" notes for each lesson.

### 6.4 Accessibility

- All pages: real headings, alt text, descriptive link text, no color-only meaning.
- Audio versions of every "For young readers" section.
- Captioned videos and office hours.
- Tactile activity versions where possible (for example, raised-line orbit diagrams).
- Dyslexia-friendly printable versions.

### 6.5 Translation

| Order | Language | Target date |
|---|---|---|
| 1 | Spanish | Jun 2027 |
| 2 | French | Aug 2027 |
| 3 | Portuguese | Sep 2027 |
| 4 | Hindi | Oct 2027 |
| 5 | Arabic | Nov 2027 |

Translators are volunteers with a reviewer for each language. Translated pages keep the same evidence labels and the same references.

---

## 7. Phase 4 — Research outputs (June–November 2027)

### 7.1 What we will publish

| Output | Venue | When | Condition |
|---|---|---|---|
| Methods note: bound-orbit test for short arcs | *Research Notes of the AAS* (RNAAS) | Jul 2027 | Passes external review by at least one orbit-determination expert |
| Challenge A results (including null results) | RNAAS or arXiv preprint | Sep–Oct 2027 | Regardless of whether candidates are found |
| Software release `fdastro` v1.0 | Zenodo (DOI) | Nov 2027 | All tests pass; docs complete |
| Data release: challenge candidate lists, with reasons for rejection | Zenodo (DOI) | Nov 2027 | Personal data removed; contributors credited with permission |
| Year One report | Repository + arXiv (if suitable) | Nov 2027 | — |

### 7.2 Research rules

- **Null results are results.** We publish what we did not find and how sensitive our search was.
- **Pre-register challenge methods.** Before each challenge starts, we post the exact pass rules and freeze them.
- **Authorship** follows standard practice: people who did substantial work are offered authorship; others are acknowledged.
- **Data and code** for every publication are archived with a DOI.

---

## 8. Scientific review process

### 8.1 Internal checklist (every dossier, article and post)

- [ ] Every claim has an evidence label.
- [ ] Every number is checked against a primary source, with a date if it can change.
- [ ] Every reference exists and says what we say it says.
- [ ] Simple layer has no equations and no unexplained jargon.
- [ ] Nothing says or suggests that anyone is hiding data.
- [ ] No health, wellness or alien-technology claims.
- [ ] "How we could be wrong" section is present and specific.
- [ ] Code examples run.
- [ ] A second person (not the author) has signed off.

### 8.2 External expert review

- Each disclosure topic has at least one external reviewer with published work in that area.
- Reviewers get a simple form: *Is anything wrong? Is anything overstated? Is anything important missing?*
- Reviewers may stay anonymous or be thanked by name (their choice).
- We record what changed after review in the changelog.

### 8.3 Disagreements

If reviewers disagree, we show both views on the page and choose the more cautious evidence level.

---

## 9. From "flag" to "report": what happens to a possible discovery

```
FLAG  →  TRIAGE  →  CANDIDATE  →  EXPERT CHECK  →  REPORT  →  (only then) PUBLIC POST
```

| Stage | What happens | Who | Exit rule |
|---|---|---|---|
| **1. Flag** | A script or a person notices something interesting. | Anyone | Logged in a private candidate issue (not public social media). |
| **2. Triage** | Check against known objects and known problems. | Two maintainers | Rejected if it matches a known object, a known artifact, or bad data. |
| **3. Candidate** | A second person reproduces the result from raw public data with their own run. | Independent volunteer | Rejected if it cannot be reproduced. |
| **4. Expert check** | An external expert reviews the method and result. | External reviewer | Rejected or sent back if the expert finds a problem. |
| **5. Report** | Sent to the right authority (table below). | Science Lead | We wait for acknowledgment. |
| **6. Public post** | Only after the authority responds, and worded as a **candidate** unless it is independently confirmed. | Comms Lead + Science Lead | Two-person sign-off. |

### Where reports go

| Kind of object | Where we report | Notes |
|---|---|---|
| Asteroids, comets, interstellar objects, unlinked observations | **Minor Planet Center (MPC)** | Follow MPC submission guidelines. Never announce before the MPC responds. |
| TESS planet candidates found independently | **ExoFOP-TESS** as a Community TOI (CTOI) | Only after vetting for eclipsing binaries and artifacts. |
| Transients (fast-changing objects in the sky) | **Transient Name Server (TNS)**, when the object type is in its scope | Follow TNS rules. |
| Microlensing events | The relevant survey team, through their published contact routes | Many events are already in survey alert systems. |
| WISE motion candidates found on Backyard Worlds | The **Backyard Worlds** team | Follow that project's process. |
| Published results | Peer-reviewed journals, RNAAS, arXiv | With data and code archived. |

---

## 10. Corrections and retractions policy

1. **Anyone can request a correction** using the "Correction request" issue template.
2. **We respond within 3 days** and fix confirmed errors within 7 days.
3. **Corrections are visible.** Every corrected page gets a dated note at the bottom: what was wrong, what changed, who reported it (with permission).
4. **Social posts:** If a post was wrong, we quote-post the correction from the same account. We do not quietly delete posts unless they contain private information or harm someone; if we delete, we post that we did and why.
5. **Retractions:** If a whole disclosure turns out to be wrong, we keep the page, mark it **Retracted** at the top with the reason, and lower its evidence level or remove the level.
6. **Changelog:** Every correction is listed in `CHANGELOG.md`.
7. **Thank people.** Finding our mistakes is a gift.

---

## 11. Risk register

| # | Risk | Likelihood | Impact | What we do about it | Owner |
|---|---|---|---|---|---|
| 1 | **Hype:** posts sound more certain than the science | Medium | High | Evidence labels in every post; banned-words list; two-person sign-off | Comms Lead |
| 2 | **Misinformation spread by others** using our name | Medium | High | Clear "what we are not" statement; correction posts; pinned FAQ | Comms Lead |
| 3 | **False positives:** a "candidate" turns out to be noise or a known object | High | Medium | Flag-to-report pipeline; independent reproduction; publish rejection reasons | Science Lead |
| 4 | **"Disclosure" misread** as "secret files" or conspiracy | High | High | Definition repeated in every launch post; respectful tone rules; never imply hiding | Comms Lead |
| 5 | **Harassment of scientists** by readers who think discoveries were "missed" | Low–Medium | High | Never name individuals as having "missed" anything; moderate replies; condemn harassment publicly | Moderation Lead |
| 6 | **Privacy:** contributor data exposed | Low | High | Collect the minimum; no children's data; credit only with consent | Maintainers |
| 7 | **Child safety online** | Medium | High | Kids participate through adults; no DMs with minors; no children's photos, names, schools or locations posted; follow platform age rules and child-privacy laws such as COPPA in the US | Moderation Lead |
| 8 | **Wrong facts in kid materials** | Medium | High | Expert review of every lesson; answer keys checked | Education Lead |
| 9 | **Unsafe activities** (e.g., looking at the Sun) | Low | Very high | Every activity has a safety box; never direct anyone to look at the Sun without certified solar filters | Education Lead |
| 10 | **Burnout of volunteers** | Medium | Medium | Release buffer of two weeks; any week can slip; holiday quiet periods | Project Lead |
| 11 | **Platform changes** (X features, rules, reach) | Medium | Low | All content lives in the repository first; social is a copy | Comms Lead |
| 12 | **Implied endorsement** by agencies or projects | Low | High | Never use agency logos; never claim partnership without written permission | Project Lead |
| 13 | **Code bugs** produce wrong results | Medium | Medium | Tests against known physics; pin versions; changelog | Science Lead |
| 14 | **Pressure to add pseudoscience** back in | Medium | Medium | Style guide rules; editorial notes explain removals kindly | Science Lead |

---

## 12. How we measure success

We care most about **understanding and accuracy**, not likes.

| Area | Measure | Year One target |
|---|---|---|
| Accuracy | External reviewer sign-off per dossier | 15 of 15 |
| Accuracy | Median time to fix a confirmed error | ≤ 7 days |
| Readability | "For young readers" sections at about grade 4–6 | 15 of 15 |
| Accessibility | Pages passing our accessibility checklist | 100% |
| Learning | Teachers reporting they used a lesson (voluntary form, no student data) | 100 classrooms |
| Code | Tests passing on main branch | 100% of the time |
| Code | Tutorials that run on a clean install | 100% |
| Community | Challenge candidates submitted and triaged with written reasons | All |
| Research | Published research notes (including null results) | ≥ 2 |
| Translation | Languages beyond English | ≥ 3 |
| Social (secondary) | Average replies that are questions (sign of curiosity) | Tracked, no target |

---

## 13. Governance and roles

| Role | Responsibilities |
|---|---|
| **Project Lead** | Overall direction, partnerships (only with written permission), final say on releases |
| **Science Lead** | Evidence levels, review process, candidate pipeline, expert reviewer list |
| **Education Lead** | Lessons, kid activities, safety boxes, teacher feedback |
| **Comms Lead** | Articles, threads, calendar, corrections on social media |
| **Moderation and Child-Safety Lead** | Community rules, reply moderation, child-safety policies |
| **Maintainers** | Code review, tests, releases |
| **External reviewers** | Volunteer subject experts, reviewing as individuals |
| **Translators** | Volunteer translation with a second reviewer per language |

One person may hold more than one role while the project is small, **except** that no one may be the only reviewer of their own science content.

### Decisions

- Day-to-day: maintainers decide in pull requests.
- Evidence levels: Science Lead decides, after review; disagreements are shown on the page.
- Big changes (new disclosures, partnerships, policies): discussed in a public issue for at least 7 days.

---

## 14. Budget: free and low-cost options

### Free

| Need | Free option |
|---|---|
| Code hosting and issue tracking | GitHub (public repository) |
| Website | GitHub Pages |
| Tests | GitHub Actions (free for public repositories) |
| DOIs for software and data | Zenodo |
| Notebooks people can run in a browser | Binder or Google Colab |
| Citizen-science platforms | Existing Zooniverse projects (we send people there) |
| Data | MAST (TESS, Kepler), IRSA (WISE/NEOWISE), MPC, JPL Small-Body Database, ALMA Science Archive, NASA PDS |
| Live sessions | Free tiers of video platforms with auto-captions |

### Low-cost (optional)

| Item | Approximate cost |
|---|---|
| Custom domain name | about US$10–20 per year |
| Kid activity kits for libraries (string, pins, flashlights, polarized film) | about US$15–30 per kit |
| Printing lesson packs for a school | about US$20–50 |
| Professional captioning for recorded videos | varies; use auto-captions plus volunteer correction first |

We do not need money to start. If we ever accept donations, we will publish how every amount is used.

---

## 15. Twelve-month calendar (December 2026 – November 2027)

| Month | What happens | Timely hooks |
|---|---|---|
| **Dec 2026** | Phase 0 review; external review window opens (7 Dec); soft launch of repository (15 Dec); holiday quiet period (21 Dec–3 Jan) | Gaia Data Release 4 (planned for 2 Dec 2026) — a teaching moment for D13; Geminid meteor shower (mid-December) |
| **Jan 2027** | Public launch (5 Jan); Phase 1 weeks 1–3: D14 (12 Jan), D02 (19 Jan), D01 (26 Jan) | Interest in 3I/ATLAS, TOI-2535 b and 2026 ED138 |
| **Feb 2027** | Weeks 4–7: D07 (2 Feb), D04 (9 Feb), D15 (16 Feb), D03 (23 Feb); teacher lesson packs v1 | International Day of Women and Girls in Science (11 Feb): spotlight women in astronomy history and today |
| **Mar 2027** | Weeks 8–12: D09 (2 Mar), D11 (9 Mar), D12 (16 Mar), D13 (23 Mar), D10 (30 Mar) | — |
| **Apr 2027** | Weeks 13–15: D08 (6 Apr), D06 (13 Apr), D05 (20 Apr); Phase 1 wrap-up (27 Apr) | Global Astronomy Month; Yuri's Night (12 Apr) |
| **May 2027** | Challenge A opens (4 May); pre-registered methods posted; library program v1 | — |
| **Jun 2027** | Challenge B opens (1 Jun); Spanish translation; methods note submitted | Asteroid Day (30 Jun) |
| **Jul 2027** | Challenge C opens (1 Jul); Challenge A closes (31 Jul); RNAAS methods note (if accepted) | Two years since 3I/ATLAS discovery (1 Jul) |
| **Aug 2027** | Challenge B closes (31 Aug); back-to-school pack; French translation | Total solar eclipse on 2 Aug 2027 (visible from parts of Spain, North Africa and the Middle East) — safety-first eclipse lesson; Perseid meteors |
| **Sep 2027** | Challenge C closes (30 Sep); challenge results written up; Portuguese translation | — |
| **Oct 2027** | Results preprints; Hindi translation | Ten years since 1I/ʻOumuamua was discovered (19 Oct 2017); World Space Week (4–10 Oct) |
| **Nov 2027** | `fdastro` v1.0 and data release with Zenodo DOIs; Year One report; Arabic translation; plan for Year Two | One year since launch planning began |

---

*This plan is a living document. Changes are tracked in the repository history and summarized in `CHANGELOG.md`.*
