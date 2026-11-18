"""fdastro — open tools for the Future Disclosure: Astronomy project.

Each module matches one or more disclosures in ``docs/disclosures``:

========================  ===========================================
Module                    What it does
========================  ===========================================
``fdastro.kepler``        Orbits of every shape (ellipse to hyperbola)
``fdastro.ephemeris``     Where the Earth and observatories are
``fdastro.iso``           Orbit fitting and the bound-orbit test (D14)
``fdastro.mpc``           Read Minor Planet Center observations (D14)
``fdastro.tisserand``     Tisserand screening of odd orbits (D15)
``fdastro.astrometry``    Parallax and proper motion (D04)
``fdastro.transits``      Single and fading transits (D02, D03)
``fdastro.exomoon``       Timing/duration exomoon test (D12)
``fdastro.obliquity``     Tilted orbits and hidden companions (D13)
``fdastro.microlensing``  Lensing timescales and achromaticity (D07)
``fdastro.stats``         Significance and look-elsewhere helpers
``fdastro.catalogs``      Reference orbital elements
========================  ===========================================
"""

__version__ = "0.1.0"

__all__ = ["__version__"]
