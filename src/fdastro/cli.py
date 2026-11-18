"""Command-line interface: ``fdastro <command>`` or ``python -m fdastro <command>``."""

from __future__ import annotations

import argparse
import json
import sys

import numpy as np

from . import __version__
from .catalogs import HIGH_INCLINATION_EXAMPLES, INTERSTELLAR_OBJECTS
from .constants import A_JUPITER_AU, A_NEPTUNE_AU


def _cmd_isos(_args: argparse.Namespace) -> int:
    from .kepler import v_infinity_from_q_e_kms

    print(f"{'Object':<22}{'e':>9}{'q (au)':>10}{'i (deg)':>10}{'v_inf (km/s)':>15}")
    for obj in INTERSTELLAR_OBJECTS:
        v = v_infinity_from_q_e_kms(obj["q_au"], obj["e"])
        print(f"{obj['designation']:<22}{obj['e']:>9.4f}{obj['q_au']:>10.4f}{obj['i_deg']:>10.2f}{v:>15.2f}")
    return 0


def _cmd_tisserand(args: argparse.Namespace) -> int:
    from .tisserand import jupiter_class, tisserand_parameter

    a_p = {"jupiter": A_JUPITER_AU, "neptune": A_NEPTUNE_AU}[args.planet]
    if args.examples:
        for rec in HIGH_INCLINATION_EXAMPLES:
            tj = tisserand_parameter(rec["a"], rec["e"], rec["i"], a_p)
            print(f"{rec['name']:<48} T = {tj:+.3f}   ({rec['note']})")
        return 0
    if None in (args.a, args.e, args.i):
        print("give --a --e --i, or use --examples", file=sys.stderr)
        return 2
    tj = tisserand_parameter(args.a, args.e, args.i, a_p)
    print(f"T_{args.planet[0].upper()} = {tj:.4f}")
    if args.planet == "jupiter":
        print(jupiter_class(tj))
    return 0


def _cmd_demo_iso(args: argparse.Namespace) -> int:
    from .catalogs import INTERSTELLAR_OBJECTS
    from .kepler import ecliptic_to_equatorial, elements_to_state
    from .iso import screen_object, simulate_observations

    obj = INTERSTELLAR_OBJECTS[2]  # 3I/ATLAS-like geometry
    state_ecl = elements_to_state(obj["q_au"], obj["e"], obj["i_deg"], obj["node_deg"], obj["peri_deg"], -80.0)
    state = np.concatenate([ecliptic_to_equatorial(state_ecl[:3]), ecliptic_to_equatorial(state_ecl[3:])])
    epoch = 60_850.0
    nights = epoch + np.array([0.0, 2.0, 5.0, 9.0, 14.0, 20.0])
    mjd = np.concatenate([n + np.array([0.0, 0.02, 0.04]) for n in nights])
    obs = simulate_observations(state, epoch, mjd, sigma_arcsec=args.sigma, rng=args.seed)
    print("Synthetic observations of a 3I/ATLAS-like orbit (not real data):")
    print(json.dumps(screen_object(obs, name="synthetic-3I-like"), indent=2))
    return 0


def _cmd_parse_mpc(args: argparse.Namespace) -> int:
    from .mpc import group_by_designation, load_mpc80

    groups = group_by_designation(load_mpc80(args.path), min_obs=args.min_obs)
    print(f"{len(groups)} designations with >= {args.min_obs} observations")
    for name, obs in list(groups.items())[: args.limit]:
        arc = obs[-1].mjd_utc - obs[0].mjd_utc
        codes = ",".join(sorted({o.obscode for o in obs}))
        print(f"{name:<14} n={len(obs):<4} arc={arc:8.3f} d  obs={codes}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="fdastro", description="Future Disclosure: Astronomy tools")
    p.add_argument("--version", action="version", version=f"fdastro {__version__}")
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("isos", help="list known interstellar objects and their v_inf")
    s.set_defaults(func=_cmd_isos)

    s = sub.add_parser("tisserand", help="compute a Tisserand parameter")
    s.add_argument("--a", type=float, help="semi-major axis (au)")
    s.add_argument("--e", type=float, help="eccentricity (0 <= e < 1)")
    s.add_argument("--i", type=float, help="inclination (deg)")
    s.add_argument("--planet", choices=["jupiter", "neptune"], default="jupiter")
    s.add_argument("--examples", action="store_true", help="show real high-inclination examples")
    s.set_defaults(func=_cmd_tisserand)

    s = sub.add_parser("demo-iso", help="fit a synthetic interstellar object and run the bound-orbit test")
    s.add_argument("--sigma", type=float, default=0.3, help="astrometric noise (arcsec)")
    s.add_argument("--seed", type=int, default=1)
    s.set_defaults(func=_cmd_demo_iso)

    s = sub.add_parser("parse-mpc", help="summarize an MPC 80-column file (e.g. the ITF)")
    s.add_argument("path")
    s.add_argument("--min-obs", type=int, default=3)
    s.add_argument("--limit", type=int, default=20)
    s.set_defaults(func=_cmd_parse_mpc)
    return p


def _make_output_safe() -> None:
    """Never crash on names such as Kaʻepaokaʻawela when the terminal or pipe
    uses a legacy encoding (e.g. cp1252 on Windows): unprintable characters
    are replaced instead."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(errors="replace")
            except (ValueError, OSError):  # pragma: no cover - exotic streams
                pass


def main(argv: list[str] | None = None) -> int:
    _make_output_safe()
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
