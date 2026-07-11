"""Unit conversions used across the toolkit.

AWG geometry follows the ASTM B258 definition (public-domain mathematics):
diameter in inches d(n) = 0.005 * 92**((36 - n) / 39), where n is the AWG
number and 0000 (4/0) maps to n = -3. Circular mils = (diameter in mils)**2.
"""

from __future__ import annotations

# AWG "aught" sizes map to negative indices in the ASTM B258 progression.
_AUGHT = {"1/0": 0, "2/0": -1, "3/0": -2, "4/0": -3}

# Standard building-wire sizes for iteration (NEC Chapter 9 ordering, small to large).
STANDARD_AWG_SIZES: tuple[str, ...] = (
    "14", "12", "10", "8", "6", "4", "3", "2", "1",
    "1/0", "2/0", "3/0", "4/0",
)


def _awg_index(awg: str) -> int:
    """Normalize an AWG label ("12", "4/0") to its ASTM B258 index n."""
    label = awg.strip().upper().removesuffix(" AWG").strip()
    if label in _AUGHT:
        return _AUGHT[label]
    try:
        return int(label)
    except ValueError:
        raise ValueError(
            f"Unrecognized AWG size {awg!r}; expected e.g. '12' or '4/0'"
        ) from None


def awg_to_circular_mils(awg: str) -> float:
    """Conductor area in circular mils for an AWG size (ASTM B258 formula)."""
    n = _awg_index(awg)
    diameter_mils = 5.0 * 92.0 ** ((36 - n) / 39)
    return diameter_mils**2


def circular_mils_to_mm2(cmil: float) -> float:
    """Circular mils to square millimetres (1 cmil = 5.067e-4 mm^2)."""
    if cmil <= 0:
        raise ValueError(f"Conductor area must be positive, got {cmil}")
    return cmil * 5.067074790975e-4


def feet_to_meters(feet: float) -> float:
    """Feet to metres (exact: 1 ft = 0.3048 m)."""
    return feet * 0.3048


def meters_to_feet(meters: float) -> float:
    """Metres to feet (exact: 1 ft = 0.3048 m)."""
    return meters / 0.3048


def hp_to_watts(hp: float) -> float:
    """Mechanical horsepower to watts (1 hp = 745.699872 W)."""
    return hp * 745.699872


def celsius_to_kelvin_delta(delta_c: float) -> float:
    """Temperature *difference* in °C equals the difference in K."""
    return delta_c
