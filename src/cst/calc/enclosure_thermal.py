"""Enclosure thermal estimate — sealed-enclosure temperature rise and fan sizing.

Method: the effective-cooling-surface approach used by IEC/TR 60890 and the
major enclosure vendors' application guides (Rittal, nVent Hoffman):

    delta_T = Q / (k * A_eff)          sealed enclosure, natural convection
    q_v     = f * Q / delta_T          forced-air (fan) volume flow

where Q is internal heat load (W), k the enclosure heat-transfer coefficient
(W/m^2.K — ~5.5 for painted sheet steel per vendor guides), A_eff the exposed
surface area (m^2) reduced for mounting arrangement, and f ~= 3.1 m^3.K.h/W
the air constant at sea level (rises with altitude).

This is a screening estimate for panel layout decisions. Final cooling
selection should be verified with the enclosure vendor's sizing software
(e.g. Rittal Therm, nVent HOFFMAN specifier) — geometry factors, solar load,
and altitude corrections vary by product line.
"""

from __future__ import annotations

from cst.common.cite import CalcResult, Citation

# Painted sheet steel, per vendor application guides. Stainless is similar;
# aluminum higher (~12); plastic/GRP lower (~3.5). Exposed parameter, not magic.
DEFAULT_K_W_M2K = 5.5

# Sea-level air constant for fan sizing (m^3/h per W/K). Vendor guides use 3.1.
DEFAULT_AIR_FACTOR = 3.1

# Fraction of gross surface counted as effective, by mounting arrangement.
# Follows the IEC/TR 60890 surface-factor concept: surfaces against a wall or
# floor don't radiate/convect.
MOUNTING_EXPOSED_FACES = {
    "freestanding": ("top", "front", "back", "left", "right"),
    "wall_mounted": ("top", "front", "left", "right"),
    "freestanding_against_wall": ("top", "front", "left", "right"),
    "end_of_row": ("top", "front", "back", "left"),
    "mid_row": ("top", "front", "back"),
    "mid_row_against_wall": ("top", "front"),
}

_CITATIONS = [
    Citation(
        "IEC/TR 60890",
        "effective cooling surface method",
        "temperature-rise assessment by extrapolation for LV assemblies",
    ),
    Citation(
        "Vendor application guides (Rittal / nVent Hoffman)",
        "k ~= 5.5 W/m^2.K painted steel; fan factor ~= 3.1 m^3.h.K/W at sea level",
        "screening values — verify final selection with vendor sizing software",
    ),
]


def effective_surface_area(
    height_m: float, width_m: float, depth_m: float, mounting: str = "wall_mounted"
) -> float:
    """Exposed enclosure surface area (m^2) for a mounting arrangement.

    Face areas: top/bottom = W*D, front/back = H*W, sides = H*D. The bottom
    is never counted (gland plates, poor convection).
    """
    if min(height_m, width_m, depth_m) <= 0:
        raise ValueError(
            f"Enclosure dimensions must be positive, got "
            f"{height_m} x {width_m} x {depth_m} m"
        )
    try:
        faces = MOUNTING_EXPOSED_FACES[mounting]
    except KeyError:
        raise ValueError(
            f"Unknown mounting {mounting!r}; expected one of "
            f"{sorted(MOUNTING_EXPOSED_FACES)}"
        ) from None
    areas = {
        "top": width_m * depth_m,
        "front": height_m * width_m,
        "back": height_m * width_m,
        "left": height_m * depth_m,
        "right": height_m * depth_m,
    }
    return sum(areas[f] for f in faces)


def temperature_rise(
    heat_load_w: float,
    height_m: float,
    width_m: float,
    depth_m: float,
    mounting: str = "wall_mounted",
    ambient_c: float = 35.0,
    k_w_m2k: float = DEFAULT_K_W_M2K,
) -> CalcResult:
    """Internal temperature rise of a sealed enclosure at steady state.

    Example:
        >>> r = temperature_rise(heat_load_w=200, height_m=1.2, width_m=0.8,
        ...                      depth_m=0.4, mounting="wall_mounted")
        >>> round(r.value, 1)
        16.2
    """
    if heat_load_w <= 0:
        raise ValueError(f"heat_load_w must be positive, got {heat_load_w}")
    area = effective_surface_area(height_m, width_m, depth_m, mounting)
    delta_t = heat_load_w / (k_w_m2k * area)
    internal_c = ambient_c + delta_t

    result = CalcResult(
        name=f"Sealed-enclosure temperature rise ({mounting})",
        value=delta_t,
        unit="K",
        citations=list(_CITATIONS),
        assumptions=[
            f"k = {k_w_m2k} W/m^2.K (painted sheet steel)",
            f"Effective area {area:.2f} m^2 ({mounting}); bottom face excluded",
            "Uniform internal air, no solar load, steady state",
        ],
        detail={
            "effective_area_m2": area,
            "internal_air_c": internal_c,
            "ambient_c": ambient_c,
        },
    )
    if internal_c > 50.0:
        result.warnings.append(
            f"Estimated internal air {internal_c:.1f} degC exceeds 50 degC — "
            "typical component/drive derating threshold; add cooling"
        )
    return result


def required_fan_airflow(
    heat_load_w: float,
    max_internal_c: float,
    ambient_c: float = 35.0,
    air_factor: float = DEFAULT_AIR_FACTOR,
) -> CalcResult:
    """Forced-air volume flow (m^3/h) to hold the enclosure at max_internal_c.

    Example:
        >>> r = required_fan_airflow(heat_load_w=400, max_internal_c=45,
        ...                          ambient_c=35)
        >>> round(r.value)
        124
    """
    delta_t = max_internal_c - ambient_c
    if delta_t <= 0:
        raise ValueError(
            f"max_internal_c ({max_internal_c}) must exceed ambient_c "
            f"({ambient_c}) — a fan cannot cool below ambient; use an air "
            "conditioner or heat exchanger"
        )
    if heat_load_w <= 0:
        raise ValueError(f"heat_load_w must be positive, got {heat_load_w}")
    flow = air_factor * heat_load_w / delta_t

    return CalcResult(
        name="Required filter-fan airflow",
        value=flow,
        unit="m^3/h",
        citations=list(_CITATIONS),
        assumptions=[
            f"Air factor {air_factor} m^3.h.K/W (sea level; increase ~10 % per 1000 m altitude)",
            "Free-blowing flow — apply the fan's installed/filtered curve, not its open rating",
        ],
        detail={"delta_t_k": delta_t, "cfm": flow * 0.588578},
    )
