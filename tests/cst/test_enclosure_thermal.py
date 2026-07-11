"""Tests for the enclosure thermal screening calculator."""

from __future__ import annotations

import pytest

from cst.calc.enclosure_thermal import (
    effective_surface_area,
    required_fan_airflow,
    temperature_rise,
)


def test_wall_mounted_area_excludes_back_and_bottom() -> None:
    # H=1.2, W=0.8, D=0.4: top 0.32 + front 0.96 + sides 2*0.48 = 2.24 m^2.
    assert effective_surface_area(1.2, 0.8, 0.4, "wall_mounted") == pytest.approx(2.24)


def test_freestanding_adds_back_face() -> None:
    wall = effective_surface_area(1.2, 0.8, 0.4, "wall_mounted")
    free = effective_surface_area(1.2, 0.8, 0.4, "freestanding")
    assert free - wall == pytest.approx(1.2 * 0.8)  # back face H*W


def test_temperature_rise_golden_value() -> None:
    # 200 W / (5.5 W/m^2K * 2.24 m^2) = 16.23 K over 35 -> 51.2 degC internal.
    result = temperature_rise(200, 1.2, 0.8, 0.4, mounting="wall_mounted")
    assert result.value == pytest.approx(16.23, abs=0.01)
    assert result.detail["internal_air_c"] == pytest.approx(51.23, abs=0.01)
    assert result.warnings, "51 degC internal must trip the 50 degC warning"


def test_cool_enclosure_has_no_warning() -> None:
    result = temperature_rise(50, 1.2, 0.8, 0.4, ambient_c=25)
    assert not result.warnings


def test_fan_airflow_golden_value() -> None:
    # 3.1 * 400 / 10 K = 124 m^3/h.
    result = required_fan_airflow(400, max_internal_c=45, ambient_c=35)
    assert result.value == pytest.approx(124.0)
    assert result.detail["cfm"] == pytest.approx(73.0, abs=0.1)


def test_fan_rejects_target_at_or_below_ambient() -> None:
    with pytest.raises(ValueError, match="cannot cool below ambient"):
        required_fan_airflow(400, max_internal_c=35, ambient_c=35)


def test_unknown_mounting_rejected() -> None:
    with pytest.raises(ValueError, match="Unknown mounting"):
        effective_surface_area(1, 1, 1, "ceiling_hung")


def test_nonpositive_dimensions_rejected() -> None:
    with pytest.raises(ValueError):
        effective_surface_area(0, 1, 1)
    with pytest.raises(ValueError):
        temperature_rise(-10, 1, 1, 1)
