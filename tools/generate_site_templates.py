#!/usr/bin/env python3
"""Generate the downloadable example templates served by the site.

Runs the cst suite against the worked example I/O list and writes the results
to docs/assets/templates/. Re-run after changing the cst generators or the
example I/O list:

    uv run python tools/generate_site_templates.py
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from cst.calc.voltage_drop import voltage_drop
from cst.commissioning.fat_sat import fat_template
from cst.commissioning.loop_sheets import loop_sheet
from cst.docgen.design_package import DesignPackage
from cst.panel.bom import bom_to_csv, generate_bom
from cst.panel.io_list import load_io_list
from cst.panel.nameplates import PanelNameplate, legend_plates, legend_plates_to_csv
from cst.panel.wire_schedule import generate_wire_schedule, wire_schedule_to_csv
from cst.twin.contract import schema as twin_schema, validate_payload

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "docs" / "assets" / "templates"
EXAMPLE_CSV = REPO / "data" / "examples" / "io_list_example.csv"
TWIN_PAYLOAD = REPO / "data" / "examples" / "twin_payload_example.json"

#: The register ceiling the worked twin payload is written against
#: (digital_twin_state_sync). Asserted below so a contract change that orphans
#: the example fails generation instead of shipping a schema its own example
#: violates.
TWIN_EXAMPLE_CEILING = 2

BANNER = (
    "GENERATED EXAMPLE — demonstrates the format produced by the cst toolkit "
    "from the example I/O list. Adapt to your project and review before use."
)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    io_list = load_io_list(EXAMPLE_CSV)

    shutil.copy(EXAMPLE_CSV, OUT / "io_list_example.csv")
    (OUT / "bom_example.csv").write_text(
        bom_to_csv(generate_bom(io_list, interposing_relays_for_do=True)),
        encoding="utf-8",
    )
    (OUT / "wire_schedule_example.csv").write_text(
        wire_schedule_to_csv(generate_wire_schedule(io_list)), encoding="utf-8"
    )
    (OUT / "legend_plates_example.csv").write_text(
        legend_plates_to_csv(legend_plates(io_list)), encoding="utf-8"
    )

    pt401 = next(p for p in io_list.points if p.tag == "PT-401")
    (OUT / "loop_sheet_example.md").write_text(
        f"<!-- {BANNER} -->\n\n" + loop_sheet(pt401, project="Example Skid"),
        encoding="utf-8",
    )
    (OUT / "fat_protocol_example.md").write_text(
        f"<!-- {BANNER} -->\n\n"
        + fat_template(io_list, project="Example Skid", panel_id="CP-01"),
        encoding="utf-8",
    )

    package = DesignPackage(project="Example Skid", panel_id="CP-01", prepared_by="—")
    package.add_io_summary(io_list)
    package.add_bom(io_list)
    package.add_wire_schedule(io_list, limit=10)
    package.add_calc(voltage_drop(20, 100, "12", 120))
    package.add_nameplate(PanelNameplate(
        manufacturer="(your company)", panel_id="CP-01",
        supply_voltage="480Y/277 V", phases=3, frequency_hz=60,
        full_load_amps=42, sccr_ka=65, diagram_number="E-1001",
    ))
    (OUT / "design_package_example.md").write_text(
        f"<!-- {BANNER} -->\n\n" + package.render(), encoding="utf-8"
    )

    _write_twin_contract()

    generated = sorted(p.name for p in OUT.glob("*_example.*"))
    print(f"wrote {len(generated)} generated examples to {OUT}:")
    for name in generated:
        print(f"  {name}")


def _write_twin_contract() -> None:
    """Publish the twin data contract as a schema plus a worked payload.

    The schema is generated from ``cst.twin.contract.FIELD_SPECS`` — the same
    definition the validator enforces — so the published file cannot drift from
    the check. JSON has no comment syntax, hence ``$comment`` for the banner.
    """
    contract = twin_schema()
    contract["$comment"] = BANNER
    (OUT / "twin_data_contract.schema.json").write_text(
        json.dumps(contract, indent=2) + "\n", encoding="utf-8"
    )

    payload = json.loads(TWIN_PAYLOAD.read_text(encoding="utf-8"))
    problems = validate_payload(payload, authority_ceiling=TWIN_EXAMPLE_CEILING)
    if problems:
        raise SystemExit(
            f"{TWIN_PAYLOAD} no longer satisfies the contract it illustrates:\n  - "
            + "\n  - ".join(problems)
        )
    # Published verbatim, with no banner key: the schema sets
    # additionalProperties=false, so a "$comment" here would make the worked
    # example violate the very contract it demonstrates. The schema carries the
    # banner instead, where $comment is a legal keyword rather than instance data.
    (OUT / "twin_payload_example.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
