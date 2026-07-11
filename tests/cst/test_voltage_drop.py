"""Golden-value tests for the voltage-drop calculator (K-factor method)."""

from __future__ import annotations

import math

import pytest

from cst.calc.voltage_drop import (
    awg_label_from_result,
    minimum_conductor_size,
    voltage_drop,
)


def test_textbook_single_phase_case() -> None:
    # Classic worked example: 20 A, 100 ft one-way, 12 AWG Cu, 120 V.
    # VD = 2 * 12.9 * 20 * 100 / 6530 ~= 7.90 V (6.6 %).
    result = voltage_drop(current_a=20, length_ft=100, awg="12", system_voltage=120)
    assert result.value == pytest.approx(7.90, abs=0.01)
    assert result.detail["percent_drop"] == pytest.approx(6.58, abs=0.01)
    assert result.warnings, "6.6 % must trip the 3 % recommendation warning"


def test_three_phase_uses_sqrt3() -> None:
    one_ph = voltage_drop(30, 150, "10", 480, phases=1)
    three_ph = voltage_drop(30, 150, "10", 480, phases=3)
    assert three_ph.value == pytest.approx(one_ph.value * math.sqrt(3) / 2)


def test_aluminum_uses_higher_k() -> None:
    cu = voltage_drop(20, 100, "12", 120, material="cu")
    al = voltage_drop(20, 100, "12", 120, material="al")
    assert al.value == pytest.approx(cu.value * 21.2 / 12.9)


def test_within_limit_has_no_warning() -> None:
    result = voltage_drop(current_a=10, length_ft=30, awg="10", system_voltage=480)
    assert not result.warnings


def test_result_carries_citations_and_assumptions() -> None:
    result = voltage_drop(20, 100, "12", 120)
    assert any("NEC 2023" in str(c) for c in result.citations)
    assert any("75 degC" in a for a in result.assumptions)


def test_minimum_size_20a_100ft_120v_is_8awg() -> None:
    # Required cmil = 2*12.9*20*100 / 3.6 V ~= 14,333 -> 10 AWG (10,380) fails,
    # 8 AWG (16,510) passes.
    result = minimum_conductor_size(20, 100, 120)
    assert awg_label_from_result(result) == "8"
    assert any("ampacity" in w for w in result.warnings), (
        "must remind that ampacity check still applies"
    )


def test_minimum_size_raises_when_beyond_4_0() -> None:
    with pytest.raises(ValueError, match="parallel conductors"):
        minimum_conductor_size(current_a=400, length_ft=1000, system_voltage=120)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"current_a": -5, "length_ft": 100, "awg": "12", "system_voltage": 120},
        {"current_a": 20, "length_ft": 0, "awg": "12", "system_voltage": 120},
        {"current_a": 20, "length_ft": 100, "awg": "12", "system_voltage": 120, "phases": 2},
        {"current_a": 20, "length_ft": 100, "awg": "12", "system_voltage": 120, "material": "gold"},
    ],
)
def test_invalid_inputs_raise_value_error(kwargs: dict) -> None:
    with pytest.raises(ValueError):
        voltage_drop(**kwargs)
