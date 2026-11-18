# Changelog

All notable changes to this project are recorded here. Corrections to facts are listed under **Corrected** so readers can see what changed.

## [Unreleased]

### Fixed
- Command-line tool no longer crashes on Windows when output uses a legacy encoding (cp1252) and a name contains characters such as the ʻokina in Kaʻepaokaʻawela.

## [0.1.0] — 2026-11-17

### Added
- `fdastro` Python package: `kepler`, `ephemeris`, `iso`, `mpc`, `tisserand`, `astrometry`, `transits`, `exomoon`, `obliquity`, `microlensing`, `stats`, `catalogs`, and a command-line interface.
- Test suite, including execution of every tutorial code block.
- 15 disclosure dossiers with evidence levels.
- 10 tutorials, 13 lessons (ages 6 to university), 9 audience guides, glossary and FAQ.
- Release plan, social-media style guide, 16 X articles, threads and a posting calendar.
- Editorial notes documenting what was removed from the original brainstorming notes and why.

### Corrected (relative to the original notes)
- Tisserand parameter of 2015 BZ509: about −0.75 (not −1.39).
- HelioLinC on the ITF: about 41,000 new orbits (Holman et al. 2018).
- 2011 KT19 is officially named 471325 Taowu ("Niku" is a nickname).
- Expected brightness of dark tens-of-meters bodies at Earth–Moon L4/L5: roughly magnitude 11–14 near opposition (not 22–24).
- Interstellar-object hunting code rewritten: correct Earth ephemeris, exact two-body propagation, light-time correction, honest significance test, true incoming radiant, and no "confirmed" labels.
