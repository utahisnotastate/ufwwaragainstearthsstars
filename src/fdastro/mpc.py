"""Read Minor Planet Center (MPC) 80-column optical observations.

For young readers
-----------------
When a telescope spots a moving dot, the position is written as one line of
text in a standard format. This file turns those lines into numbers a
computer can use.

For experts
-----------
Implements the classic 80-column optical format (MPC "Format for optical
astrometric observations"): columns 1-12 designation, 15 note 2 (observation
type), 16-32 UTC date, 33-44 RA (J2000), 45-56 Dec, 66-71 magnitude and band,
78-80 observatory code. The MPC's Isolated Tracklet File (ITF) is distributed
in this format, with tracklet identifiers in the designation field.

Second lines of two-line observations (satellite ``s``, roving ``v``, radar
``r``) and radar lines are skipped by default; satellite first lines ``S``
are kept but flagged, because their positions need the second line.
The newer ADES (XML/PSV) format is not parsed here.
"""

from __future__ import annotations

import gzip
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import numpy as np

__all__ = ["MPCObservation", "parse_mpc80_line", "parse_mpc80", "load_mpc80", "group_by_designation"]

_MJD_EPOCH_ORDINAL = date(1858, 11, 17).toordinal()
_SKIP_NOTE2 = {"s", "v", "r", "R"}


@dataclass(frozen=True)
class MPCObservation:
    designation: str
    note2: str
    mjd_utc: float
    ra_deg: float
    dec_deg: float
    mag: float | None
    band: str
    obscode: str

    @property
    def needs_second_line(self) -> bool:
        return self.note2 in {"S", "V"}


def _mjd_from_mpc_date(text: str) -> float:
    parts = text.split()
    if len(parts) != 3:
        raise ValueError(f"bad MPC date field: {text!r}")
    year, month = int(parts[0]), int(parts[1])
    day = float(parts[2])
    whole = int(day)
    return float(date(year, month, whole).toordinal() - _MJD_EPOCH_ORDINAL) + (day - whole)


def _sexagesimal(text: str, hours: bool) -> float:
    s = text.strip()
    sign = -1.0 if s.startswith("-") else 1.0
    parts = s.lstrip("+-").split()
    if not parts:
        raise ValueError(f"empty angle field: {text!r}")
    vals = [float(p) for p in parts] + [0.0] * (3 - len(parts))
    value = vals[0] + vals[1] / 60.0 + vals[2] / 3600.0
    return sign * value * (15.0 if hours else 1.0)


def parse_mpc80_line(line: str) -> MPCObservation | None:
    """Parse one 80-column line. Returns ``None`` for lines that should be skipped."""
    raw = line.rstrip("\n\r")
    if len(raw) < 80:
        raw = raw.ljust(80)
    if not raw.strip():
        return None
    note2 = raw[14]
    if note2 in _SKIP_NOTE2:
        return None
    designation = raw[0:12].strip()
    mag_text = raw[65:70].strip()
    return MPCObservation(
        designation=designation,
        note2=note2.strip(),
        mjd_utc=_mjd_from_mpc_date(raw[15:32]),
        ra_deg=_sexagesimal(raw[32:44], hours=True),
        dec_deg=_sexagesimal(raw[44:56], hours=False),
        mag=float(mag_text) if mag_text else None,
        band=raw[70].strip(),
        obscode=raw[77:80].strip(),
    )


def parse_mpc80(lines, *, strict: bool = False) -> list[MPCObservation]:
    """Parse many lines. Malformed lines are skipped unless ``strict`` is True."""
    out: list[MPCObservation] = []
    for n, line in enumerate(lines, start=1):
        try:
            obs = parse_mpc80_line(line)
        except (ValueError, IndexError) as exc:
            if strict:
                raise ValueError(f"line {n}: {exc}") from exc
            continue
        if obs is not None:
            out.append(obs)
    return out


def load_mpc80(path: str | Path, *, strict: bool = False) -> list[MPCObservation]:
    """Load an 80-column observation file (plain text or ``.gz``)."""
    p = Path(path)
    opener = gzip.open if p.suffix == ".gz" else open
    with opener(p, "rt", encoding="ascii", errors="replace") as fh:
        return parse_mpc80(fh, strict=strict)


def group_by_designation(observations: list[MPCObservation], min_obs: int = 1) -> dict[str, list[MPCObservation]]:
    """Group observations by designation (tracklet id in the ITF), sorted by time."""
    groups: dict[str, list[MPCObservation]] = defaultdict(list)
    for o in observations:
        groups[o.designation].append(o)
    return {k: sorted(v, key=lambda o: o.mjd_utc) for k, v in groups.items() if len(v) >= min_obs}


def to_arrays(observations: list[MPCObservation]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (mjd_utc, ra_deg, dec_deg) arrays."""
    return (np.array([o.mjd_utc for o in observations]),
            np.array([o.ra_deg for o in observations]),
            np.array([o.dec_deg for o in observations]))
