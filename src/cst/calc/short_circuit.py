"""Available fault current — infinite-bus transformer estimate and
point-to-point conductor attenuation (Bussmann method).

Transformer secondary fault current (infinite primary bus — conservative):

    I_fla = kVA * 1000 / (sqrt(3) * V_LL)          (three-phase)
    I_sc  = I_fla * 100 / %Z

Point-to-point attenuation down a conductor run (Bussmann SPD handbook):

    f = sqrt(3) * L * I_sc / (C * N * V_LL)        (three-phase)
    f = 2 * L * I_sc / (C * N * V_LN)              (single-phase L-N)
    I_sc_end = I_sc / (1 + f)

where L is length in feet, N conductors per phase, and C is the Bussmann
conductor/raceway constant. C-values are published per conductor size,
material, and raceway type in the Bussmann handbook — supply the value for
your conductor; this module does not embed the C tables.

Use for screening and SCCR planning; a coordination study governs final
values.
"""

from __future__ import annotations

import math

from cst.common.cite import CalcResult, Citation

_CITATIONS = [
    Citation("Bussmann SPD handbook", "point-to-point method",
             "industry-standard published short-circuit estimation method"),
    Citation("NEC 2023", "110.24", "field marking of available fault current"),
]


def transformer_fault_current(
    kva: float, secondary_v: float, impedance_percent: float, phases: int = 3
) -> CalcResult:
    """Infinite-bus secondary fault current of a transformer.

    Example:
        >>> r = transformer_fault_current(kva=1500, secondary_v=480, impedance_percent=5.75)
        >>> round(r.value)
        31378
    """
    if impedance_percent <= 0:
        raise ValueError(f"impedance_percent must be positive, got {impedance_percent}")
    if kva <= 0 or secondary_v <= 0:
        raise ValueError(f"kva and secondary_v must be positive (got {kva}, {secondary_v})")
    fla = kva * 1000.0 / (math.sqrt(3.0) * secondary_v) if phases == 3 else kva * 1000.0 / secondary_v
    isc = fla * 100.0 / impedance_percent

    return CalcResult(
        name=f"Transformer secondary fault current ({kva:g} kVA, {impedance_percent:g} %Z)",
        value=isc,
        unit="A",
        citations=list(_CITATIONS),
        assumptions=[
            "Infinite primary bus (conservative/high); no motor contribution included",
            "Add running-motor contribution (~4-6x motor FLA) for panels with large "
            "motor loads before comparing against SCCR",
            "Nameplate %Z tolerance (typically +/-7.5 %) not applied",
        ],
        detail={"secondary_fla_a": fla},
    )


def point_to_point(
    isc_start_a: float,
    length_ft: float,
    c_value: float,
    voltage: float,
    phases: int = 3,
    conductors_per_phase: int = 1,
) -> CalcResult:
    """Fault current at the end of a conductor run (Bussmann point-to-point).

    ``c_value`` is the Bussmann C constant for your conductor size/material/
    raceway — from the published Bussmann tables (user-supplied).

    Example:
        >>> r = point_to_point(isc_start_a=30000, length_ft=50, c_value=5907,
        ...                    voltage=480, phases=3)
        >>> round(r.value)
        15655
    """
    if min(isc_start_a, length_ft, c_value, voltage) <= 0:
        raise ValueError("isc_start_a, length_ft, c_value, and voltage must all be positive")
    if conductors_per_phase < 1:
        raise ValueError(f"conductors_per_phase must be >= 1, got {conductors_per_phase}")

    multiplier = math.sqrt(3.0) if phases == 3 else 2.0
    f = multiplier * length_ft * isc_start_a / (c_value * conductors_per_phase * voltage)
    isc_end = isc_start_a / (1.0 + f)

    return CalcResult(
        name=f"Point-to-point fault current ({length_ft:g} ft run)",
        value=isc_end,
        unit="A",
        citations=list(_CITATIONS),
        assumptions=[
            f"C = {c_value:g} from the published Bussmann conductor tables (verify for "
            "your conductor size, material, and raceway type)",
            "Three-phase bolted fault" if phases == 3 else "Single-phase L-N fault",
            "Screening estimate — a short-circuit study governs final ratings",
        ],
        detail={"f_factor": f, "attenuation_percent": 100.0 * (1 - isc_end / isc_start_a)},
    )
