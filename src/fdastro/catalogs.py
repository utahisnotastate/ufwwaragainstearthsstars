"""Small reference tables used in tutorials and tests.

Values are osculating heliocentric elements (J2000 ecliptic) retrieved from
the JPL Small-Body Database API (ssd-api.jpl.nasa.gov/sbdb.api) on
2026-11-17, rounded. Orbit solutions are updated over time; always pull fresh
values for research use.
"""

from __future__ import annotations

__all__ = ["INTERSTELLAR_OBJECTS", "HIGH_INCLINATION_EXAMPLES"]

#: The three confirmed interstellar objects (as of November 2026).
INTERSTELLAR_OBJECTS: list[dict] = [
    {
        "designation": "1I/2017 U1",
        "name": "ʻOumuamua",
        "discovered": "2017-10-19",
        "discovered_by": "Pan-STARRS1",
        "q_au": 0.255912,
        "e": 1.201134,
        "i_deg": 122.7417,
        "node_deg": 24.5969,
        "peri_deg": 241.8105,
        "solution": "JPL 2018-06-26",
    },
    {
        "designation": "2I/Borisov",
        "name": "C/2019 Q4 (Borisov)",
        "discovered": "2019-08-30",
        "discovered_by": "Gennadiy Borisov (MARGO, Crimea)",
        "q_au": 2.006521,
        "e": 3.356476,
        "i_deg": 44.0526,
        "node_deg": 308.1477,
        "peri_deg": 209.1237,
        "solution": "JPL 2024-06-24",
    },
    {
        "designation": "3I/ATLAS",
        "name": "C/2025 N1 (ATLAS)",
        "discovered": "2025-07-01",
        "discovered_by": "ATLAS (Río Hurtado, Chile)",
        "q_au": 1.351999,
        "e": 6.123467,
        "i_deg": 175.2403,
        "node_deg": 323.0252,
        "peri_deg": 128.7969,
        "solution": "JPL 2026-10-21",
    },
]

#: Real high-inclination / retrograde bodies used in the Tisserand tutorial.
HIGH_INCLINATION_EXAMPLES: list[dict] = [
    {"name": "514107 Kaʻepaokaʻawela (2015 BZ509)", "a": 5.143480, "e": 0.377722, "i": 163.1355,
     "note": "retrograde 1:1 co-orbital of Jupiter; interstellar-capture origin proposed (Namouni & Morais 2018), debated"},
    {"name": "528219 (2008 KV42), nicknamed 'Drac'", "a": 41.509267, "e": 0.490909, "i": 103.4419,
     "note": "first known retrograde trans-Neptunian object"},
    {"name": "471325 Taowu (2011 KT19), nicknamed 'Niku'", "a": 35.618659, "e": 0.332587, "i": 110.2755,
     "note": "retrograde TNO; shares an orbital plane with Drac and others"},
    {"name": "Example main-belt asteroid", "a": 2.7, "e": 0.15, "i": 10.0,
     "note": "illustrative ordinary orbit for comparison (not a real object)"},
]
