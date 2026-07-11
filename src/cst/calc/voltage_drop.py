"""Conductor voltage drop — K-factor method.

Formula (industry-standard approximation, consistent with the DC resistances
of NEC 2023 Chapter 9 Table 8 at 75 °C):

    single-phase:  VD = 2 * K * I * L / A
    three-phase:   VD = sqrt(3) * K * I * L / A

where K is conductor resistivity in ohm·cmil/ft (copper ~= 12.9, aluminum
~= 21.2 at 75 °C), I is load current in amperes, L is one-way circuit length
in feet, and A is conductor area in circular mils.

NEC 2023 does not mandate a voltage-drop limit for most circuits; 210.19(A)
Informational Note No. 4 and 215.2(A)(1) Informational Note No. 2 recommend
<= 3 % for branch circuits/feeders and <= 5 % combined. This module flags,
not fails, results above the recommendation.
"""

from __future__ import annotations

import math

from cst.common.cite import CalcResult, Citation
from cst.common.units import STANDARD_AWG_SIZES, awg_to_circular_mils

# Resistivity in ohm·circular-mil/ft at 75 °C conductor temperature.
# Widely published engineering constants; derivable from NEC Ch.9 Table 8.
K_FACTORS = {"cu": 12.9, "al": 21.2}

_CITATIONS = [
    Citation(
        "NEC 2023",
        "210.19(A) Info. Note 4 / 215.2(A)(1) Info. Note 2",
        "recommended max 3 % branch/feeder, 5 % combined (informational, not mandatory)",
    ),
    Citation(
        "NEC 2023",
        "Chapter 9 Table 8",
        "K-factor method consistent with published DC conductor resistances at 75 degC",
    ),
]


def _k_factor(material: str) -> float:
    try:
        return K_FACTORS[material.lower()]
    except KeyError:
        raise ValueError(
            f"Unknown conductor material {material!r}; expected 'cu' or 'al'"
        ) from None


def voltage_drop(
    current_a: float,
    length_ft: float,
    awg: str,
    system_voltage: float,
    material: str = "cu",
    phases: int = 1,
    limit_percent: float = 3.0,
) -> CalcResult:
    """Voltage drop for a circuit of one-way length ``length_ft``.

    ``phases`` is 1 (also covers DC and 120/240 V single-phase line-to-line
    runs) or 3. ``limit_percent`` sets the warning threshold, defaulting to
    the NEC-recommended 3 %.

    Example:
        >>> r = voltage_drop(current_a=20, length_ft=100, awg="12",
        ...                  system_voltage=120)
        >>> round(r.value, 2), round(r.detail["percent_drop"], 2)
        (7.9, 6.59)
    """
    if current_a <= 0 or length_ft <= 0 or system_voltage <= 0:
        raise ValueError(
            "current_a, length_ft, and system_voltage must all be positive "
            f"(got {current_a}, {length_ft}, {system_voltage})"
        )
    if phases not in (1, 3):
        raise ValueError(f"phases must be 1 or 3, got {phases}")

    k = _k_factor(material)
    cmil = awg_to_circular_mils(awg)
    multiplier = 2.0 if phases == 1 else math.sqrt(3.0)
    drop_v = multiplier * k * current_a * length_ft / cmil
    percent = 100.0 * drop_v / system_voltage

    result = CalcResult(
        name=f"Voltage drop ({awg} AWG {material.upper()}, {phases}-phase)",
        value=drop_v,
        unit="V",
        citations=list(_CITATIONS),
        assumptions=[
            f"K = {k} ohm-cmil/ft ({material.upper()} at 75 degC conductor temperature)",
            "One-way circuit length; reactance neglected (valid for sizes <= ~4/0 "
            "and near-unity power factor — use NEC Ch.9 Table 9 impedance method otherwise)",
        ],
        detail={
            "percent_drop": percent,
            "circular_mils": cmil,
            "voltage_at_load": system_voltage - drop_v,
        },
    )
    if percent > limit_percent:
        result.warnings.append(
            f"{percent:.2f} % exceeds the {limit_percent:g} % recommendation"
        )
    return result


def minimum_conductor_size(
    current_a: float,
    length_ft: float,
    system_voltage: float,
    material: str = "cu",
    phases: int = 1,
    limit_percent: float = 3.0,
) -> CalcResult:
    """Smallest standard AWG size meeting the voltage-drop recommendation.

    Voltage drop only — the returned size must still be checked against
    ampacity (NEC 310.16 with corrections) and termination ratings, which
    frequently govern instead.

    Example:
        >>> r = minimum_conductor_size(20, 100, 120)
        >>> r.detail["circular_mils"] > 14000
        True
    """
    for awg in STANDARD_AWG_SIZES:
        candidate = voltage_drop(
            current_a, length_ft, awg, system_voltage, material, phases, limit_percent
        )
        if not candidate.warnings:
            candidate.name = f"Minimum conductor size for <= {limit_percent:g} % drop"
            candidate.assumptions.append(f"Selected size: {awg} AWG")
            candidate.warnings.append(
                "Sized for voltage drop only — verify ampacity per NEC 310.16 "
                "and termination temperature limits per 110.14(C)"
            )
            candidate.detail["selected_awg_index"] = float(
                STANDARD_AWG_SIZES.index(awg)
            )
            return candidate
    raise ValueError(
        f"No size up to 4/0 AWG meets {limit_percent:g} % at {current_a} A / "
        f"{length_ft} ft — consider parallel conductors, kcmil sizes, or a "
        "higher distribution voltage"
    )


def awg_label_from_result(result: CalcResult) -> str:
    """Recover the AWG label chosen by :func:`minimum_conductor_size`."""
    return STANDARD_AWG_SIZES[int(result.detail["selected_awg_index"])]
