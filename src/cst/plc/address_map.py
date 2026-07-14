"""Modbus register map generator.

Assigns Modbus addresses to a tag database using the conventional data-model
split (Modbus Application Protocol V1.1b, section 4.3):

    discrete outputs (coils, 0x)      <- BOOL tags for DO
    discrete inputs (1x)              <- BOOL tags for DI
    input registers (3x)              <- analog inputs (AI/RTD/TC)
    holding registers (4x)            <- analog outputs and R/W values

Register widths: INT/UINT 1 register, DINT/REAL 2 registers (word order is a
project decision — flagged in the output). Addresses are reported both as
0-based protocol offsets and traditional 1-based table numbers.
"""

from __future__ import annotations

import csv
import io

from cst.plc.tag_db import Tag, TagDatabase

REGISTERS_PER_TYPE = {"BOOL": 1, "INT": 1, "DINT": 2, "REAL": 2}

_TABLE_BASE = {"coil": 1, "discrete_input": 10001, "input_register": 30001,
               "holding_register": 40001}


def _table_for(tag_datatype: str, address_hint: str, writable: bool) -> str:
    if tag_datatype == "BOOL":
        return "coil" if writable else "discrete_input"
    return "holding_register" if writable else "input_register"


def _default_writable(tag: Tag) -> bool:
    """Use canonical I/O direction, falling back to a naming convention."""
    if tag.io_type:
        if tag.io_type in ("DO", "AO"):
            return True
        if tag.io_type in ("DI", "AI", "RTD", "TC"):
            return False
        raise ValueError(
            f"{tag.name}: unknown io_type {tag.io_type!r}; "
            "expected DI/DO/AI/AO/RTD/TC"
        )
    return any(
        marker in tag.name.upper()
        for marker in ("CMD", "_SP", "OUT", "SOL", "FCV")
    )


def modbus_map(
    tag_db: TagDatabase,
    writable_names: set[str] | None = None,
) -> list[dict[str, str | int]]:
    """Assign sequential Modbus addresses per table.

    ``writable_names``: explicit tag names that are commands/setpoints
    (coils/holding registers). When omitted, canonical I/O direction wins;
    tags without an I/O type fall back to the legacy name convention.
    """
    if writable_names is None:
        writable_names = {t.name for t in tag_db.tags if _default_writable(t)}
    next_offset = {k: 0 for k in _TABLE_BASE}
    rows: list[dict[str, str | int]] = []
    for tag in tag_db.tags:
        if tag.datatype not in REGISTERS_PER_TYPE:
            raise ValueError(f"{tag.name}: no Modbus mapping for datatype {tag.datatype!r}")
        table = _table_for(tag.datatype, tag.address, tag.name in writable_names)
        width = REGISTERS_PER_TYPE[tag.datatype]
        offset = next_offset[table]
        rows.append({
            "tag": tag.name,
            "datatype": tag.datatype,
            "table": table,
            "protocol_offset": offset,
            "table_address": _TABLE_BASE[table] + offset,
            "registers": width,
            "note": "verify word order (hi/lo) against device" if width == 2 else "",
        })
        next_offset[table] = offset + width
    return rows


def modbus_map_to_csv(rows: list[dict[str, str | int]]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(
        buffer,
        fieldnames=["tag", "datatype", "table", "protocol_offset",
                    "table_address", "registers", "note"],
    )
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()
