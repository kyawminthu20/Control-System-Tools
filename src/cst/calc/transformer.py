"""Transformer full-load current and overcurrent protection — NEC Article 450.

FLA is pure arithmetic:  I = kVA * 1000 / V  (single-phase)
                         I = kVA * 1000 / (sqrt(3) * V_LL)  (three-phase)

Maximum OCPD percentages implement NEC 2023 Table 450.3(B) (transformers
600 V and less, unsupervised):

- Primary-only protection: 125 % (current >= 9 A), 167 % (2–9 A),
  300 % (< 2 A).
- Primary + secondary protection: primary 250 %, secondary 125 %
  (>= 9 A) or 167 % (< 9 A).

Where 125 % lands off-schedule, Note 1 permits the next standard size up
(240.6(A)); the smaller-current percentages do NOT get that allowance.
Control-circuit transformers inside industrial control panels are typically
governed by 430.72(C)/UL 508A 42.3 instead — flagged in assumptions.
"""

from __future__ import annotations

import math

from cst.common.cite import CalcResult, Citation
from cst.calc.motor_branch import next_standard_ocpd


def transformer_fla(kva: float, voltage: float, phases: int = 3) -> float:
    """Full-load amperes on one side of a transformer."""
    if kva <= 0 or voltage <= 0:
        raise ValueError(f"kva and voltage must be positive (got {kva}, {voltage})")
    if phases == 3:
        return kva * 1000.0 / (math.sqrt(3.0) * voltage)
    if phases == 1:
        return kva * 1000.0 / voltage
    raise ValueError(f"phases must be 1 or 3, got {phases}")


def _primary_only_max(fla: float) -> tuple[float, int, bool]:
    """(max amps, percent used, next-size-up allowed) per Table 450.3(B)."""
    if fla >= 9.0:
        return fla * 1.25, 125, True
    if fla >= 2.0:
        return fla * 1.67, 167, False
    return fla * 3.00, 300, False


def size_transformer_protection(
    kva: float,
    primary_v: float,
    secondary_v: float,
    phases: int = 3,
    secondary_protection: bool = False,
) -> CalcResult:
    """OCPD limits for a <=600 V unsupervised transformer per Table 450.3(B).

    Example:
        >>> r = size_transformer_protection(kva=15, primary_v=480, secondary_v=208)
        >>> round(r.detail["primary_fla_a"], 1), r.detail["primary_ocpd_a"]
        (18.0, 25.0)
    """
    p_fla = transformer_fla(kva, primary_v, phases)
    s_fla = transformer_fla(kva, secondary_v, phases)

    citations = [
        Citation("NEC 2023", "Table 450.3(B)",
                 "max OCPD percentages, transformers 600 V or less (unsupervised)"),
        Citation("NEC 2023", "240.6(A)", "standard OCPD ratings"),
    ]
    detail: dict[str, float] = {"primary_fla_a": p_fla, "secondary_fla_a": s_fla}

    if secondary_protection:
        # Primary at 250 %, secondary at 125 % (>=9 A) / 167 % (<9 A).
        # Note 1's next-size-up allowance applies to the 125 % values only.
        p_max = p_fla * 2.50
        s_max, s_pct = (s_fla * 1.25, 125) if s_fla >= 9.0 else (s_fla * 1.67, 167)
        p_ocpd = _at_or_below(p_max)
        s_ocpd = next_standard_ocpd(s_max) if s_pct == 125 else _at_or_below(s_max)
        scheme = "primary (250 %) + secondary"
        detail.update(primary_ocpd_a=float(p_ocpd), secondary_ocpd_a=float(s_ocpd))
    else:
        p_max, pct, next_up = _primary_only_max(p_fla)
        p_ocpd = next_standard_ocpd(p_max) if next_up else _at_or_below(p_max)
        scheme = f"primary-only ({pct} %)"
        detail.update(primary_ocpd_a=float(p_ocpd))

    result = CalcResult(
        name=f"Transformer protection — {kva:g} kVA, {primary_v:g}/{secondary_v:g} V, {phases}-ph ({scheme})",
        value=detail["primary_ocpd_a"],
        unit="A (primary OCPD)",
        citations=citations,
        assumptions=[
            "Transformer 600 V or less, unsupervised location (Table 450.3(B))",
            "Next-size-up applied only where Table 450.3(B) Note 1 permits (125 % rows)",
            "Control transformers in industrial control panels: check 430.72(C) / UL 508A "
            "Sec. 42 instead — different rules",
            "Conductors sized separately per 240.21(C) tap rules where applicable",
        ],
        detail=detail,
    )
    return result


def _standard_at_or_below(amps: float):
    from cst.calc.motor_branch import STANDARD_OCPD_RATINGS
    return tuple(r for r in STANDARD_OCPD_RATINGS if r <= amps)


def _at_or_below(amps: float) -> int:
    """Largest standard rating <= amps (for rows without next-size-up)."""
    candidates = _standard_at_or_below(amps)
    if not candidates:
        raise ValueError(
            f"No standard OCPD rating at or below {amps:.1f} A — use a "
            "supplementary protector or fuse rated for the computed maximum"
        )
    return candidates[-1]
