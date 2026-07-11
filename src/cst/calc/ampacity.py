"""Conductor ampacity with ambient correction and bundle adjustment — NEC 310.15.

Base ampacities come from a user-supplied transcription of NEC Table 310.16
(see data/standards_tables/README.md); a clearly-marked SAMPLE ships for
demonstration. Corrections applied per NEC 2023:

- Ambient temperature correction, 310.15(B) Equation 310.15(B):
      factor = sqrt((Tc - Ta) / (Tc - Ta_table))
  where Tc is the conductor insulation rating and Ta_table = 30 degC for
  Table 310.16.
- More than three current-carrying conductors, Table 310.15(C)(1):
  published adjustment percentages (constants below, cited).
"""

from __future__ import annotations

import math
from pathlib import Path

from cst.common.cite import CalcResult, Citation
from cst.common.tables import SAMPLE_WARNING, load_table

# NEC 2023 Table 310.15(C)(1) — adjustment for >3 current-carrying conductors
# in a raceway/cable. (count_low, count_high, percent of base ampacity)
BUNDLE_ADJUSTMENT = (
    (1, 3, 100),
    (4, 6, 80),
    (7, 9, 70),
    (10, 20, 50),
    (21, 30, 45),
    (31, 40, 40),
    (41, 9999, 35),
)

TABLE_AMBIENT_C = 30.0  # Table 310.16 is based on 30 degC ambient


def bundle_adjustment_percent(current_carrying_conductors: int) -> float:
    """Adjustment percentage per NEC Table 310.15(C)(1)."""
    if current_carrying_conductors < 1:
        raise ValueError(
            f"current_carrying_conductors must be >= 1, got {current_carrying_conductors}"
        )
    for low, high, percent in BUNDLE_ADJUSTMENT:
        if low <= current_carrying_conductors <= high:
            return float(percent)
    raise AssertionError("unreachable — BUNDLE_ADJUSTMENT covers all counts")


def ambient_correction_factor(
    ambient_c: float, insulation_rating_c: float, table_ambient_c: float = TABLE_AMBIENT_C
) -> float:
    """Correction factor per NEC 310.15(B) Equation 310.15(B)."""
    if ambient_c >= insulation_rating_c:
        raise ValueError(
            f"Ambient {ambient_c} degC meets or exceeds the {insulation_rating_c} degC "
            "insulation rating — conductor cannot carry current at this ambient"
        )
    return math.sqrt(
        (insulation_rating_c - ambient_c) / (insulation_rating_c - table_ambient_c)
    )


def corrected_ampacity(
    awg: str,
    material: str = "cu",
    insulation_rating_c: int = 75,
    ambient_c: float = 30.0,
    current_carrying_conductors: int = 3,
    tables_dir: Path | None = None,
    allow_sample: bool = True,
) -> CalcResult:
    """Allowable ampacity of a conductor after correction and adjustment.

    Example (with sample data):
        >>> r = corrected_ampacity("12", ambient_c=40, current_carrying_conductors=4)
        >>> round(r.value, 1)
        17.6
    """
    table = load_table("ampacity_nec_310_16", tables_dir, allow_sample)
    label = awg.strip().upper().removesuffix(" AWG").strip()
    row = next(
        (
            r
            for r in table.data
            if r["size_awg_kcmil"] == label
            and r["material"] == material.lower()
            and r.get("insulation_rating_c", 75) == insulation_rating_c
        ),
        None,
    )
    if row is None:
        raise ValueError(
            f"No {insulation_rating_c} degC {material.upper()} entry for {awg!r} in "
            f"table {table.name} — add it to your transcription"
        )

    base = float(row["ampacity_a"])
    correction = ambient_correction_factor(ambient_c, float(insulation_rating_c))
    adjustment = bundle_adjustment_percent(current_carrying_conductors) / 100.0
    allowable = base * correction * adjustment

    result = CalcResult(
        name=f"Allowable ampacity ({awg} AWG {material.upper()}, {insulation_rating_c} degC col.)",
        value=allowable,
        unit="A",
        citations=[
            Citation(table.source.get("standard", "NEC"), f"Table {table.source.get('table', '310.16')}",
                     f"base ampacity {base:g} A — {table.source_label}"),
            Citation("NEC 2023", "310.15(B) Equation",
                     f"ambient correction {correction:.3f} at {ambient_c:g} degC"),
            Citation("NEC 2023", "Table 310.15(C)(1)",
                     f"adjustment {adjustment:.0%} for {current_carrying_conductors} current-carrying conductors"),
        ],
        assumptions=[
            f"Table basis: {TABLE_AMBIENT_C:g} degC ambient, <=3 current-carrying conductors",
            "Termination temperature limits per 110.14(C) may cap the usable value",
        ],
        detail={
            "base_ampacity_a": base,
            "correction_factor": correction,
            "adjustment_factor": adjustment,
        },
    )
    if table.is_sample:
        result.warnings.append(SAMPLE_WARNING)
    return result
