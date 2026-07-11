"""Motor branch-circuit sizing workflow — NEC Article 430.

Implements the standard Article 430 design chain for a single continuous-duty
motor:

1. FLC from NEC Table 430.248/430.250 (user-supplied transcription; the
   nameplate FLA is used for OVERLOAD sizing only, per 430.6(A)).
2. Branch-circuit conductors >= 125 % of table FLC (430.22).
3. Branch-circuit short-circuit/ground-fault protection maximum per Table
   430.52(C)(1) percentages, with the next-standard-size-up allowance of
   430.52(C)(1) Exception 1 and standard OCPD ratings from 240.6(A).
4. Overload protection from nameplate FLA per 430.32(A)(1): 125 % for
   service factor >= 1.15 or temperature rise <= 40 degC, else 115 %.
"""

from __future__ import annotations

from pathlib import Path

from cst.common.cite import CalcResult, Citation
from cst.common.tables import SAMPLE_WARNING, load_table

# NEC 2023 Table 430.52(C)(1) — maximum rating of the branch-circuit
# short-circuit and ground-fault protective device, % of table FLC.
OCPD_MAX_PERCENT = {
    "nontime_delay_fuse": 300,
    "dual_element_fuse": 175,
    "instantaneous_trip_breaker": 800,
    "inverse_time_breaker": 250,
}

# NEC 2023 240.6(A) — standard ampere ratings for fuses and inverse-time
# circuit breakers.
STANDARD_OCPD_RATINGS = (
    15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175,
    200, 225, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1200, 1600,
    2000, 2500, 3000, 4000, 5000, 6000,
)


def table_flc(
    hp: float,
    voltage: float,
    phases: int = 3,
    tables_dir: Path | None = None,
    allow_sample: bool = True,
) -> tuple[float, bool, str]:
    """Table full-load current for a motor. Returns (flc, is_sample, source)."""
    table = load_table("motor_flc_nec_430_250", tables_dir, allow_sample)
    row = next(
        (
            r
            for r in table.data
            if r["hp"] == hp and r["voltage"] == voltage and r.get("phases", 3) == phases
        ),
        None,
    )
    if row is None:
        raise ValueError(
            f"No FLC entry for {hp} hp at {voltage} V {phases}-phase in table "
            f"{table.name} — add it from your licensed copy (Table 430.248 for "
            "single-phase, 430.250 for three-phase)"
        )
    return float(row["flc_a"]), table.is_sample, table.source_label


def next_standard_ocpd(amps: float) -> int:
    """Smallest standard OCPD rating >= amps (NEC 240.6(A))."""
    for rating in STANDARD_OCPD_RATINGS:
        if rating >= amps:
            return rating
    raise ValueError(f"{amps:g} A exceeds the largest standard rating (6000 A)")


def size_motor_branch(
    hp: float,
    voltage: float,
    phases: int = 3,
    nameplate_fla: float | None = None,
    ocpd_type: str = "inverse_time_breaker",
    service_factor: float = 1.15,
    temp_rise_c: float = 40.0,
    tables_dir: Path | None = None,
    allow_sample: bool = True,
) -> CalcResult:
    """Full Article 430 branch-circuit sizing for one continuous-duty motor.

    Returns minimum conductor ampacity as the primary value; OCPD and
    overload settings are in ``detail``.

    Example (with sample data):
        >>> r = size_motor_branch(hp=10, voltage=460)
        >>> round(r.value, 1), r.detail["ocpd_rating_a"]
        (17.5, 35.0)
    """
    if ocpd_type not in OCPD_MAX_PERCENT:
        raise ValueError(
            f"Unknown ocpd_type {ocpd_type!r}; expected one of {sorted(OCPD_MAX_PERCENT)}"
        )

    flc, is_sample, source_label = table_flc(hp, voltage, phases, tables_dir, allow_sample)

    # 430.22 — conductors at 125 % of TABLE FLC (not nameplate).
    min_conductor_ampacity = 1.25 * flc

    # 430.52 — OCPD maximum percentage of table FLC; Exception 1 permits the
    # next standard size up when the computed value doesn't match 240.6(A).
    percent = OCPD_MAX_PERCENT[ocpd_type]
    ocpd_calc = flc * percent / 100.0
    ocpd_rating = next_standard_ocpd(ocpd_calc)

    # 430.32(A)(1) — overload from NAMEPLATE FLA.
    overload_basis = nameplate_fla if nameplate_fla is not None else flc
    overload_percent = 125 if (service_factor >= 1.15 or temp_rise_c <= 40.0) else 115
    overload_max = overload_basis * overload_percent / 100.0

    result = CalcResult(
        name=f"Motor branch circuit — {hp:g} hp, {voltage:g} V, {phases}-phase",
        value=min_conductor_ampacity,
        unit="A (min conductor ampacity)",
        citations=[
            Citation("NEC 2023", "Table 430.250" if phases == 3 else "Table 430.248",
                     f"table FLC {flc:g} A — {source_label}"),
            Citation("NEC 2023", "430.22", "branch conductors >= 125 % of table FLC"),
            Citation("NEC 2023", "Table 430.52(C)(1) + Exc. 1",
                     f"{ocpd_type.replace('_', ' ')} max {percent} % of FLC, next standard size permitted"),
            Citation("NEC 2023", "240.6(A)", f"standard rating selected: {ocpd_rating} A"),
            Citation("NEC 2023", "430.32(A)(1)",
                     f"overload at {overload_percent} % of nameplate FLA"),
        ],
        assumptions=[
            "Single continuous-duty motor; no other loads on the branch circuit",
            f"Service factor {service_factor:g}, temperature rise {temp_rise_c:g} degC",
            "Nameplate FLA " + (f"= {nameplate_fla:g} A" if nameplate_fla is not None
                                else "not given — table FLC used for overload (verify at build)"),
            "Select actual conductor size from ampacity tables (cst.calc.ampacity) "
            "with the installation's correction/adjustment factors",
        ],
        detail={
            "table_flc_a": flc,
            "ocpd_max_calc_a": ocpd_calc,
            "ocpd_rating_a": float(ocpd_rating),
            "overload_max_a": overload_max,
            "overload_percent": float(overload_percent),
        },
    )
    if is_sample:
        result.warnings.append(SAMPLE_WARNING)
    if nameplate_fla is None:
        result.warnings.append(
            "Overload sized from table FLC — replace with nameplate FLA per 430.6(A)"
        )
    return result
