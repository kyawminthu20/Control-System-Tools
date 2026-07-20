"""Command-line interface for the Control System Tools suite.

Usage examples:
    cst voltage-drop --amps 20 --feet 100 --awg 12 --volts 120
    cst wire-size --amps 32 --feet 250 --volts 480 --phases 3
    cst encoder --ppr 1024 --gear 5 --lead 10 --rpm 3000
    cst enclosure --watts 350 --height 1.6 --width 0.8 --depth 0.5
    cst fan --watts 400 --max-temp 45 --ambient 35
    cst ampacity --awg 12 --ambient 40 --ccc 4
    cst motor-branch --hp 10 --volts 460 --nameplate-fla 13.2
    cst transformer --kva 15 --primary 480 --secondary 208
    cst sccr --component "main breaker:65" --component "contactor:5"
    cst fault-current --kva 1500 --volts 480 --z 5.75
    cst io-check data/examples/io_list_example.csv
    cst bom data/examples/io_list_example.csv --relays
    cst wire-schedule data/examples/io_list_example.csv
    cst legend data/examples/io_list_example.csv
    cst loop-sheets data/examples/io_list_example.csv --out-dir loop_sheets/
    cst fat data/examples/io_list_example.csv --panel CP-01
    cst tags-from-io data/examples/io_list_example.csv
    cst modbus-map data/examples/io_list_example.csv
    cst saleae capture.csv --channel "Channel 0"
    cst modbus-decode capture.pcap --addresses
    cst sbm --train normal.csv --score live.csv
    cst twin-validate data/examples/twin_payload_example.json --ceiling 2
    cst twin-sync data/examples/twin_sync_example.csv --max-age 5
    cst design-package data/examples/io_list_example.csv --project "Demo" --panel CP-01
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cst.calc import (
    ampacity,
    enclosure_thermal,
    motor_branch,
    sccr,
    short_circuit,
    transformer,
    voltage_drop,
)
from cst.commissioning import fat_sat, loop_sheets
from cst.diagnostics import modbus_decode, saleae, sbm as sbm_mod
from cst.docgen.design_package import DesignPackage
from cst.motion.encoder import EncoderScaling
from cst.panel import bom, io_list as io_list_mod, nameplates, wire_schedule
from cst.plc import address_map, tag_db
from cst.twin import contract as twin_contract

# Imported from the submodule, not the package: cst.twin re-exports a
# sync_health *function*, which shadows the module of the same name.
from cst.twin.sync_health import read_sample_csv, sync_health


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


def _cmd_ampacity(args: argparse.Namespace) -> int:
    result = ampacity.corrected_ampacity(
        awg=args.awg,
        material=args.material,
        insulation_rating_c=args.insulation,
        ambient_c=args.ambient,
        current_carrying_conductors=args.ccc,
    )
    print(result.report())
    return 0


def _cmd_motor_branch(args: argparse.Namespace) -> int:
    result = motor_branch.size_motor_branch(
        hp=args.hp,
        voltage=args.volts,
        phases=args.phases,
        nameplate_fla=args.nameplate_fla,
        ocpd_type=args.ocpd,
        service_factor=args.sf,
    )
    print(result.report())
    return 0


def _cmd_transformer(args: argparse.Namespace) -> int:
    result = transformer.size_transformer_protection(
        kva=args.kva,
        primary_v=args.primary,
        secondary_v=args.secondary,
        phases=args.phases,
        secondary_protection=args.secondary_ocpd,
    )
    print(result.report())
    return 0


def _cmd_sccr(args: argparse.Namespace) -> int:
    components = []
    for spec in args.component:
        name, _, rating = spec.rpartition(":")
        if not name:
            raise ValueError(f"--component must be 'name:kA', got {spec!r}")
        components.append(sccr.PanelComponent(name, float(rating)))
    result = sccr.panel_sccr(components, available_fault_ka=args.available)
    print(result.report())
    return 0


def _cmd_fault_current(args: argparse.Namespace) -> int:
    result = short_circuit.transformer_fault_current(
        kva=args.kva, secondary_v=args.volts,
        impedance_percent=args.z, phases=args.phases,
    )
    print(result.report())
    if args.feet is not None:
        if args.c_value is None:
            raise ValueError("--c-value (Bussmann C constant) is required with --feet")
        downstream = short_circuit.point_to_point(
            isc_start_a=result.value, length_ft=args.feet,
            c_value=args.c_value, voltage=args.volts, phases=args.phases,
        )
        print()
        print(downstream.report())
    return 0


def _cmd_io_check(args: argparse.Namespace) -> int:
    problems = io_list_mod.load_io_list(args.csv).validate()
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("I/O list OK")
    return 0


def _cmd_bom(args: argparse.Namespace) -> int:
    loaded = io_list_mod.load_io_list(args.csv)
    lines = bom.generate_bom(
        loaded, spare_fraction=args.spares, interposing_relays_for_do=args.relays
    )
    print(bom.bom_to_csv(lines), end="")
    return 0


def _cmd_wire_schedule(args: argparse.Namespace) -> int:
    loaded = io_list_mod.load_io_list(args.csv)
    rows = wire_schedule.generate_wire_schedule(loaded, strip_prefix=args.strip)
    print(wire_schedule.wire_schedule_to_csv(rows), end="")
    return 0


def _cmd_legend(args: argparse.Namespace) -> int:
    loaded = io_list_mod.load_io_list(args.csv)
    print(nameplates.legend_plates_to_csv(nameplates.legend_plates(loaded)), end="")
    return 0


def _cmd_loop_sheets(args: argparse.Namespace) -> int:
    loaded = io_list_mod.load_io_list(args.csv)
    sheets = loop_sheets.generate_loop_sheets(loaded, project=args.project)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for tag, sheet in sheets.items():
        (out_dir / f"{tag.replace('/', '_')}.md").write_text(sheet, encoding="utf-8")
    print(f"Wrote {len(sheets)} loop sheets to {out_dir}/")
    return 0


def _cmd_fat(args: argparse.Namespace) -> int:
    loaded = io_list_mod.load_io_list(args.csv)
    print(fat_sat.fat_template(
        loaded, project=args.project, panel_id=args.panel, test_type=args.type
    ))
    return 0


def _cmd_tags_from_io(args: argparse.Namespace) -> int:
    loaded = io_list_mod.load_io_list(args.csv)
    db = tag_db.tags_from_io_list(loaded, prefix=args.prefix)
    problems = db.validate()
    print(db.to_csv(), end="")
    if problems:
        print(f"\n{len(problems)} tag problem(s):", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    return 0


def _cmd_modbus_map(args: argparse.Namespace) -> int:
    loaded = io_list_mod.load_io_list(args.csv)
    db = tag_db.tags_from_io_list(loaded)
    print(address_map.modbus_map_to_csv(address_map.modbus_map(db)), end="")
    return 0


def _cmd_saleae(args: argparse.Namespace) -> int:
    edges = saleae.load_digital_export(args.csv)
    if args.channel not in edges:
        raise ValueError(
            f"channel {args.channel!r} not in capture; available: {sorted(edges)}"
        )
    stats = saleae.pulse_stats(edges[args.channel])
    print(f"{args.channel}: {stats.edge_count} edges")
    print(f"  frequency : {stats.frequency_hz:.3f} Hz")
    print(f"  duty      : {stats.duty_cycle:.1%}")
    print(f"  high pulse: {stats.min_high_s * 1e6:.2f} .. {stats.max_high_s * 1e6:.2f} us")
    if args.glitch_us is not None:
        glitches = saleae.find_glitches(edges[args.channel], args.glitch_us * 1e-6)
        print(f"  glitches < {args.glitch_us} us: {len(glitches)}")
        for t, width in glitches[:10]:
            print(f"    t={t:.6f}s width={width * 1e6:.2f}us")
    return 0


def _cmd_modbus_decode(args: argparse.Namespace) -> int:
    frames = modbus_decode.decode_frames(
        modbus_decode.read_capture(args.pcap), server_port=args.port
    )
    if not frames:
        raise ValueError(
            f"no Modbus TCP frames found on port {args.port}; "
            "check --port if the link uses a non-standard server port"
        )
    summary = modbus_decode.summarize(frames)
    print(summary.report())

    if summary.request_count == 0:
        # Direction comes from the server port, so a wrong --port labels every
        # frame a response and silently produces a meaningless summary. A
        # direction-filtered capture can also look like this, so warn, not fail.
        print(
            f"warning: no requests seen — every frame was treated as a response. "
            f"If the server does not listen on port {args.port}, re-run with "
            f"--port; otherwise the capture may hold only one direction.",
            file=sys.stderr,
        )

    if args.exceptions:
        print("\nexception responses:")
        for frame in summary.exceptions:
            print(
                f"  t={frame.timestamp:.6f} unit={frame.unit_id} "
                f"txn={frame.transaction_id} {frame.function_name}: "
                f"{frame.exception_name}"
            )

    if args.unanswered:
        stalled = [
            t for t in modbus_decode.pair_transactions(frames) if t.unanswered
        ]
        print(f"\nunanswered requests: {len(stalled)}")
        for txn in stalled[:20]:
            req = txn.request
            print(
                f"  t={req.timestamp:.6f} unit={req.unit_id} "
                f"txn={req.transaction_id} {req.function_name} "
                f"start={req.start_address} qty={req.quantity}"
            )

    if args.addresses:
        print("\npolled address spans:")
        for span in modbus_decode.polled_addresses(frames):
            print(
                f"  unit {span.unit_id} fc {span.function_code}: "
                f"{span.start}..{span.end} ({span.count} regs, {span.polls} polls)"
            )
    return 0


def _read_numeric_csv(path: str) -> list[list[float]]:
    import csv as _csv
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = _csv.reader(fh)
        header = next(reader)
        try:
            float(header[0])  # headerless file — first row is data
            rows = [[float(v) for v in header]]
        except ValueError:
            rows = []
        rows += [[float(v) for v in row] for row in reader if row and row[0].strip()]
    return rows


def _cmd_sbm(args: argparse.Namespace) -> int:
    model = sbm_mod.train(
        _read_numeric_csv(args.train),
        memory_size=args.memory, bandwidth=args.bandwidth,
    )
    flagged = 0
    for i, row in enumerate(_read_numeric_csv(args.score), start=1):
        score = model.score(row)
        marker = "  <-- ANOMALY" if score > args.threshold else ""
        flagged += bool(marker)
        print(f"row {i}: score {score:.2f}{marker}")
    print(f"\n{flagged} row(s) above threshold {args.threshold:g}")
    return 1 if flagged else 0


def _cmd_twin_validate(args: argparse.Namespace) -> int:
    if args.ceiling is not None and args.register:
        raise ValueError(
            "--ceiling and --register are alternative ways to set the same limit; "
            "pass one or the other"
        )
    ceiling = args.ceiling
    if args.register:
        if not args.method_id:
            raise ValueError("--register also needs --method-id to select a row")
        ceilings = twin_contract.authority_ceilings(args.register)
        if args.method_id not in ceilings:
            # A Planned row is absent by design, so say which case this is
            # rather than letting it read as a typo.
            raise ValueError(
                f"no established ceiling for method {args.method_id!r} in {args.register}; "
                f"either the id is wrong or its authority is still Planned "
                f"(known ids with a ceiling: {len(ceilings)})"
            )
        ceiling = ceilings[args.method_id]

    payload = twin_contract.load_payload(args.payload)
    problems = twin_contract.validate_payload(
        payload, authority_ceiling=ceiling, now=args.now
    )
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("payload OK — well-formed enough for a gate to evaluate (not a safety verdict)")
    return 0


def _cmd_twin_sync(args: argparse.Namespace) -> int:
    samples = read_sample_csv(args.csv)
    health = sync_health(samples, max_age_s=args.max_age, gap_factor=args.gap_factor)
    print(health.report())
    return 1 if health.warnings else 0


def _cmd_design_package(args: argparse.Namespace) -> int:
    loaded = io_list_mod.load_io_list(args.csv)
    package = DesignPackage(
        project=args.project, panel_id=args.panel, prepared_by=args.author
    )
    package.add_io_summary(loaded)
    package.add_bom(loaded)
    package.add_wire_schedule(loaded)
    print(package.render())
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

    amp = sub.add_parser("ampacity", help="corrected conductor ampacity (NEC 310.15)")
    amp.add_argument("--awg", required=True, help="conductor size, e.g. 12 or 4/0")
    amp.add_argument("--material", choices=("cu", "al"), default="cu")
    amp.add_argument("--insulation", type=int, choices=(60, 75, 90), default=75)
    amp.add_argument("--ambient", type=float, default=30.0, help="ambient (degC)")
    amp.add_argument("--ccc", type=int, default=3, help="current-carrying conductors")
    amp.set_defaults(func=_cmd_ampacity)

    mb = sub.add_parser("motor-branch", help="motor branch-circuit sizing (NEC Art. 430)")
    mb.add_argument("--hp", type=float, required=True)
    mb.add_argument("--volts", type=float, required=True)
    mb.add_argument("--phases", type=int, choices=(1, 3), default=3)
    mb.add_argument("--nameplate-fla", type=float, default=None, help="for overload sizing")
    mb.add_argument("--ocpd", choices=sorted(motor_branch.OCPD_MAX_PERCENT),
                    default="inverse_time_breaker")
    mb.add_argument("--sf", type=float, default=1.15, help="service factor")
    mb.set_defaults(func=_cmd_motor_branch)

    tx = sub.add_parser("transformer", help="transformer OCPD limits (NEC Table 450.3(B))")
    tx.add_argument("--kva", type=float, required=True)
    tx.add_argument("--primary", type=float, required=True, help="primary voltage")
    tx.add_argument("--secondary", type=float, required=True, help="secondary voltage")
    tx.add_argument("--phases", type=int, choices=(1, 3), default=3)
    tx.add_argument("--secondary-ocpd", action="store_true",
                    help="primary+secondary scheme (250 %% / 125 %%)")
    tx.set_defaults(func=_cmd_transformer)

    sc = sub.add_parser("sccr", help="panel SCCR weakest-link (UL 508A SB4)")
    sc.add_argument("--component", action="append", required=True,
                    metavar="NAME:KA", help="repeatable, e.g. 'contactor:5'")
    sc.add_argument("--available", type=float, default=None,
                    help="available fault current (kA) to check against")
    sc.set_defaults(func=_cmd_sccr)

    fc = sub.add_parser("fault-current", help="transformer fault current (+ point-to-point)")
    fc.add_argument("--kva", type=float, required=True)
    fc.add_argument("--volts", type=float, required=True, help="secondary voltage")
    fc.add_argument("--z", type=float, required=True, help="nameplate impedance %%")
    fc.add_argument("--phases", type=int, choices=(1, 3), default=3)
    fc.add_argument("--feet", type=float, default=None, help="conductor run for point-to-point")
    fc.add_argument("--c-value", type=float, default=None, help="Bussmann C constant")
    fc.set_defaults(func=_cmd_fault_current)

    ioc = sub.add_parser("io-check", help="validate an I/O list CSV")
    ioc.add_argument("csv", help="I/O list CSV path")
    ioc.set_defaults(func=_cmd_io_check)

    bm = sub.add_parser("bom", help="BOM from an I/O list (CSV to stdout)")
    bm.add_argument("csv")
    bm.add_argument("--spares", type=float, default=0.20, help="spare I/O fraction")
    bm.add_argument("--relays", action="store_true", help="interposing relays per DO")
    bm.set_defaults(func=_cmd_bom)

    ws = sub.add_parser("wire-schedule", help="wire/terminal schedule (CSV to stdout)")
    ws.add_argument("csv")
    ws.add_argument("--strip", default="TB1", help="terminal strip prefix")
    ws.set_defaults(func=_cmd_wire_schedule)

    lg = sub.add_parser("legend", help="legend-plate engraving list (CSV to stdout)")
    lg.add_argument("csv")
    lg.set_defaults(func=_cmd_legend)

    ls = sub.add_parser("loop-sheets", help="markdown loop test sheet per point")
    ls.add_argument("csv")
    ls.add_argument("--out-dir", required=True, help="directory for generated sheets")
    ls.add_argument("--project", default="", help="project name on sheets")
    ls.set_defaults(func=_cmd_loop_sheets)

    ft = sub.add_parser("fat", help="FAT/SAT protocol skeleton (markdown to stdout)")
    ft.add_argument("csv")
    ft.add_argument("--project", default="")
    ft.add_argument("--panel", default="")
    ft.add_argument("--type", choices=("FAT", "SAT"), default="FAT")
    ft.set_defaults(func=_cmd_fat)

    tg = sub.add_parser("tags-from-io", help="PLC tag database from an I/O list (CSV)")
    tg.add_argument("csv")
    tg.add_argument("--prefix", default="", help="prefix for generated tag names")
    tg.set_defaults(func=_cmd_tags_from_io)

    mm = sub.add_parser("modbus-map", help="Modbus register map from an I/O list (CSV)")
    mm.add_argument("csv")
    mm.set_defaults(func=_cmd_modbus_map)

    sa = sub.add_parser("saleae", help="analyze a Saleae Logic 2 digital export")
    sa.add_argument("csv")
    sa.add_argument("--channel", required=True, help="channel name from the header")
    sa.add_argument("--glitch-us", type=float, default=None,
                    help="report pulses shorter than this (microseconds)")
    sa.set_defaults(func=_cmd_saleae)

    mdc = sub.add_parser(
        "modbus-decode", help="decode Modbus TCP from a pcap/pcapng capture"
    )
    mdc.add_argument("pcap", help="capture file (pcap or pcapng), read offline")
    mdc.add_argument("--port", type=int, default=modbus_decode.MODBUS_TCP_PORT,
                     help="Modbus server port (default 502)")
    mdc.add_argument("--addresses", action="store_true",
                     help="list the register spans actually polled")
    mdc.add_argument("--exceptions", action="store_true",
                     help="list exception responses")
    mdc.add_argument("--unanswered", action="store_true",
                     help="list requests that got no response")
    mdc.set_defaults(func=_cmd_modbus_decode)

    sb = sub.add_parser("sbm", help="SBM anomaly scores (train + score CSVs)")
    sb.add_argument("--train", required=True, help="known-normal numeric CSV")
    sb.add_argument("--score", required=True, help="numeric CSV to score")
    sb.add_argument("--memory", type=int, default=25)
    sb.add_argument("--bandwidth", type=float, default=1.0)
    sb.add_argument("--threshold", type=float, default=3.0)
    sb.set_defaults(func=_cmd_sbm)

    tv = sub.add_parser("twin-validate", help="validate a digital-twin payload against the data contract")
    tv.add_argument("payload", help="JSON payload file")
    tv.add_argument("--ceiling", type=int, help="max authority level the register permits")
    tv.add_argument("--register", help="methods.yml to read the ceiling from (with --method-id)")
    tv.add_argument("--method-id", help="method row id in --register")
    tv.add_argument("--now", type=float, help="epoch seconds to test valid_until against")
    tv.set_defaults(func=_cmd_twin_validate)

    ts = sub.add_parser("twin-sync", help="synchronization health of twin telemetry")
    ts.add_argument("csv", help="two-column CSV: source_ts, acquisition_ts")
    ts.add_argument("--max-age", type=float, required=True, help="freshness bound in seconds")
    ts.add_argument("--gap-factor", type=float, default=3.0)
    ts.set_defaults(func=_cmd_twin_sync)

    dp = sub.add_parser("design-package", help="assemble a design package (markdown)")
    dp.add_argument("csv", help="I/O list CSV")
    dp.add_argument("--project", required=True)
    dp.add_argument("--panel", default="")
    dp.add_argument("--author", default="")
    dp.set_defaults(func=_cmd_design_package)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except (ValueError, FileNotFoundError) as exc:
        # A missing input file (or an unsupplied licensed table) is a condition
        # the user can fix, not a defect — report it like any other bad input.
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
