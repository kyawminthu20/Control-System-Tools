"""Command-line interface for the Control System Tools suite.

Usage examples:
    cst voltage-drop --amps 20 --feet 100 --awg 12 --volts 120
    cst wire-size --amps 32 --feet 250 --volts 480 --phases 3
    cst encoder --ppr 1024 --gear 5 --lead 10 --rpm 3000
    cst enclosure --watts 350 --height 1.6 --width 0.8 --depth 0.5
    cst fan --watts 400 --max-temp 45 --ambient 35
"""

from __future__ import annotations

import argparse
import sys

from cst.calc import enclosure_thermal, voltage_drop
from cst.motion.encoder import EncoderScaling


def _cmd_voltage_drop(args: argparse.Namespace) -> int:
    result = voltage_drop.voltage_drop(
        current_a=args.amps,
        length_ft=args.feet,
        awg=args.awg,
        system_voltage=args.volts,
        material=args.material,
        phases=args.phases,
        limit_percent=args.limit,
    )
    print(result.report())
    return 0


def _cmd_wire_size(args: argparse.Namespace) -> int:
    result = voltage_drop.minimum_conductor_size(
        current_a=args.amps,
        length_ft=args.feet,
        system_voltage=args.volts,
        material=args.material,
        phases=args.phases,
        limit_percent=args.limit,
    )
    awg = voltage_drop.awg_label_from_result(result)
    print(f"Selected size: {awg} AWG")
    print(result.report())
    return 0


def _cmd_encoder(args: argparse.Namespace) -> int:
    scaling = EncoderScaling(
        pulses_per_rev=args.ppr,
        quadrature=args.quadrature,
        gear_ratio=args.gear,
        lead=args.lead,
    )
    print(f"Counts/motor rev : {scaling.counts_per_motor_rev:g}")
    print(f"Counts/load rev  : {scaling.counts_per_load_rev:g}")
    if args.lead is not None:
        print(f"Counts/unit      : {scaling.counts_per_unit:g}")
    print(f"Resolution       : {scaling.resolution:.6g} "
          f"{'units' if args.lead is not None else 'deg'}/count")
    if args.rpm is not None:
        print(f"{args.rpm:g} RPM -> {scaling.rpm_to_counts_per_sec(args.rpm):g} counts/s")
        if args.lead is not None:
            print(f"{args.rpm:g} RPM -> {scaling.rpm_to_linear_speed(args.rpm):g} units/s")
    return 0


def _cmd_enclosure(args: argparse.Namespace) -> int:
    result = enclosure_thermal.temperature_rise(
        heat_load_w=args.watts,
        height_m=args.height,
        width_m=args.width,
        depth_m=args.depth,
        mounting=args.mounting,
        ambient_c=args.ambient,
    )
    print(result.report())
    return 0


def _cmd_fan(args: argparse.Namespace) -> int:
    result = enclosure_thermal.required_fan_airflow(
        heat_load_w=args.watts,
        max_internal_c=args.max_temp,
        ambient_c=args.ambient,
    )
    print(result.report())
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cst", description="Control System Tools — standards-cited calculators"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    vd = sub.add_parser("voltage-drop", help="conductor voltage drop (K-factor method)")
    ws = sub.add_parser("wire-size", help="minimum AWG for a voltage-drop target")
    for p in (vd, ws):
        p.add_argument("--amps", type=float, required=True, help="load current (A)")
        p.add_argument("--feet", type=float, required=True, help="one-way length (ft)")
        p.add_argument("--volts", type=float, required=True, help="system voltage (V)")
        p.add_argument("--material", choices=("cu", "al"), default="cu")
        p.add_argument("--phases", type=int, choices=(1, 3), default=1)
        p.add_argument("--limit", type=float, default=3.0, help="warn threshold (%%)")
    vd.add_argument("--awg", required=True, help="conductor size, e.g. 12 or 4/0")
    vd.set_defaults(func=_cmd_voltage_drop)
    ws.set_defaults(func=_cmd_wire_size)

    enc = sub.add_parser("encoder", help="encoder scaling / counts conversions")
    enc.add_argument("--ppr", type=int, required=True, help="pulses per rev (pre-quadrature)")
    enc.add_argument("--quadrature", type=int, choices=(1, 2, 4), default=4)
    enc.add_argument("--gear", type=float, default=1.0, help="motor revs per load rev")
    enc.add_argument("--lead", type=float, default=None, help="travel per load rev (linear axes)")
    enc.add_argument("--rpm", type=float, default=None, help="also convert this motor speed")
    enc.set_defaults(func=_cmd_encoder)

    box = sub.add_parser("enclosure", help="sealed-enclosure temperature rise")
    box.add_argument("--watts", type=float, required=True, help="internal heat load (W)")
    box.add_argument("--height", type=float, required=True, help="height (m)")
    box.add_argument("--width", type=float, required=True, help="width (m)")
    box.add_argument("--depth", type=float, required=True, help="depth (m)")
    box.add_argument(
        "--mounting",
        choices=sorted(enclosure_thermal.MOUNTING_EXPOSED_FACES),
        default="wall_mounted",
    )
    box.add_argument("--ambient", type=float, default=35.0, help="ambient (degC)")
    box.set_defaults(func=_cmd_enclosure)

    fan = sub.add_parser("fan", help="required filter-fan airflow")
    fan.add_argument("--watts", type=float, required=True, help="internal heat load (W)")
    fan.add_argument("--max-temp", type=float, required=True, help="max internal air (degC)")
    fan.add_argument("--ambient", type=float, default=35.0, help="ambient (degC)")
    fan.set_defaults(func=_cmd_fan)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
