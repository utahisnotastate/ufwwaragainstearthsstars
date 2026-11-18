"""Tisserand's parameter: a "fingerprint" of how an orbit relates to a planet.

For young readers
-----------------
Almost everything in our Solar System goes around the Sun in the same
direction, like cars on a roundabout. A few objects go the other way, or
cross at a steep angle. One number, called the Tisserand parameter, helps
astronomers spot these unusual orbits quickly.

For experts
-----------
T_P = a_P / a + 2 sqrt((a / a_P)(1 - e^2)) cos i, an approximate invariant of
the circular restricted three-body problem derived from the Jacobi integral.
Conventional Jupiter classes: T_J > 3 asteroidal, 2 < T_J < 3 Jupiter-family
comets, T_J < 2 Halley-type / long-period comets and Damocloids. Negative
values require retrograde orbits (cos i < 0).

A low or negative T_J is a *screening flag*, not evidence of interstellar
origin. Most retrograde small bodies are thought to come from the Oort cloud.
Origin claims require dynamical modelling (for example backward integrations
of clone swarms) and, ideally, composition data.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike

from .constants import A_JUPITER_AU

__all__ = ["tisserand_parameter", "jupiter_class", "CaptureScreenResult", "capture_candidate_screen"]


def tisserand_parameter(a: ArrayLike, e: ArrayLike, i_deg: ArrayLike, a_planet: float = A_JUPITER_AU):
    """Tisserand parameter for bound orbits (a > 0, 0 <= e < 1). Returns float or array."""
    a = np.asarray(a, dtype=np.float64)
    e = np.asarray(e, dtype=np.float64)
    i = np.deg2rad(np.asarray(i_deg, dtype=np.float64))
    if np.any(a <= 0) or np.any(e < 0) or np.any(e >= 1):
        raise ValueError("Tisserand parameter here requires bound orbits: a > 0 and 0 <= e < 1")
    t = a_planet / a + 2.0 * np.sqrt((a / a_planet) * (1.0 - e * e)) * np.cos(i)
    return float(t) if t.ndim == 0 else t


def jupiter_class(tj: float) -> str:
    """Conventional dynamical class from T_J (with respect to Jupiter)."""
    if tj > 3.0:
        return "asteroid-like (T_J > 3)"
    if tj > 2.0:
        return "Jupiter-family-comet-like (2 < T_J < 3)"
    if tj >= 0.0:
        return "Halley-type / Damocloid-like (0 <= T_J < 2)"
    return "retrograde, Damocloid-like (T_J < 0)"


@dataclass(frozen=True)
class CaptureScreenResult:
    name: str
    a: float
    e: float
    i_deg: float
    tj: float
    jupiter_class: str
    reasons: tuple[str, ...]


def capture_candidate_screen(
    records,
    *,
    tj_max: float = 2.0,
    i_min_deg: float = 70.0,
    a_planet: float = A_JUPITER_AU,
) -> list[CaptureScreenResult]:
    """Flag orbits worth a closer look as *possible* captured interstellar objects.

    ``records`` is an iterable of mappings with keys ``name``, ``a``, ``e``, ``i``
    (degrees). Hyperbolic or parabolic records are skipped. Results are sorted by
    increasing T_J. Every flagged object still needs dynamical modelling.
    """
    out: list[CaptureScreenResult] = []
    for rec in records:
        a, e, inc = float(rec["a"]), float(rec["e"]), float(rec["i"])
        if a <= 0 or not (0.0 <= e < 1.0):
            continue
        tj = tisserand_parameter(a, e, inc, a_planet)
        reasons = []
        if tj < tj_max:
            reasons.append(f"T_J = {tj:.3f} < {tj_max}")
        if inc >= i_min_deg:
            reasons.append(f"i = {inc:.1f} deg >= {i_min_deg}")
        if inc > 90.0:
            reasons.append("retrograde orbit")
        if tj < tj_max and inc >= i_min_deg:
            out.append(CaptureScreenResult(str(rec.get("name", "?")), a, e, inc, tj,
                                           jupiter_class(tj), tuple(reasons)))
    return sorted(out, key=lambda r: r.tj)
