"""Golden-value tests for the Phase 2 NEC/UL calculators (sample table data)."""

from __future__ import annotations

import math

import pytest

from cst.calc.ampacity import (
    ambient_correction_factor,
    bundle_adjustment_percent,
    corrected_ampacity,
)
from cst.calc.motor_branch import next_standard_ocpd, size_motor_branch
from cst.calc.sccr import PanelComponent, panel_sccr
from cst.calc.short_circuit import point_to_point, transformer_fault_current
from cst.calc.transformer import size_transformer_protection, transformer_fla


# --- ampacity ---------------------------------------------------------------

def test_base_case_no_derating() -> None:
    r = corrected_ampacity("12")  # 30 degC, 3 CCC — table conditions
    assert r.value == pytest.approx(25.0)
    assert any("SAMPLE" in w for w in r.warnings)


def test_ambient_correction_formula() -> None:
    # 40 degC on a 75 degC column: sqrt((75-40)/(75-30)) = 0.882
    assert ambient_correction_factor(40, 75) == pytest.approx(math.sqrt(35 / 45))


def test_ambient_at_insulation_rating_rejected() -> None:
    with pytest.raises(ValueError, match="insulation rating"):
        ambient_correction_factor(75, 75)


@pytest.mark.parametrize(("ccc", "pct"), [(3, 100), (4, 80), (9, 70), (10, 50), (30, 45), (41, 35)])
def test_bundle_adjustment_bands(ccc: int, pct: int) -> None:
    assert bundle_adjustment_percent(ccc) == pct


def test_combined_derating() -> None:
    # 12 AWG: 25 * 0.88192 * 0.8 = 17.64 A
    r = corrected_ampacity("12", ambient_c=40, current_carrying_conductors=4)
    assert r.value == pytest.approx(25 * math.sqrt(35 / 45) * 0.8)


def test_unknown_size_gives_actionable_error() -> None:
    with pytest.raises(ValueError, match="transcription"):
        corrected_ampacity("500")  # kcmil not in sample data


# --- motor branch (Art. 430) -------------------------------------------------

def test_10hp_460v_reference_case() -> None:
    # FLC 14 A: conductor 17.5 A (430.22), ITB max 250% = 35 A -> 35 A std.
    r = size_motor_branch(hp=10, voltage=460)
    assert r.value == pytest.approx(17.5)
    assert r.detail["ocpd_rating_a"] == 35.0


def test_next_size_up_rule() -> None:
    # 25 hp / 460 V: FLC 34 A -> ITB 85 A calc -> next standard 90 A.
    r = size_motor_branch(hp=25, voltage=460)
    assert r.detail["ocpd_max_calc_a"] == pytest.approx(85.0)
    assert r.detail["ocpd_rating_a"] == 90.0


def test_overload_uses_nameplate_and_service_factor() -> None:
    r_high_sf = size_motor_branch(10, 460, nameplate_fla=13.2, service_factor=1.15)
    r_low_sf = size_motor_branch(10, 460, nameplate_fla=13.2, service_factor=1.0, temp_rise_c=50)
    assert r_high_sf.detail["overload_max_a"] == pytest.approx(13.2 * 1.25)
    assert r_low_sf.detail["overload_max_a"] == pytest.approx(13.2 * 1.15)
    assert not any("table FLC" in w for w in r_high_sf.warnings)


def test_dual_element_fuse_percentage() -> None:
    r = size_motor_branch(10, 460, ocpd_type="dual_element_fuse")
    assert r.detail["ocpd_max_calc_a"] == pytest.approx(14 * 1.75)
    assert r.detail["ocpd_rating_a"] == 25.0  # 24.5 -> next std 25


def test_next_standard_ocpd_bounds() -> None:
    assert next_standard_ocpd(21) == 25
    assert next_standard_ocpd(15) == 15
    with pytest.raises(ValueError):
        next_standard_ocpd(6001)


def test_unknown_motor_gives_actionable_error() -> None:
    with pytest.raises(ValueError, match="licensed copy"):
        size_motor_branch(hp=350, voltage=460)


# --- transformer (Art. 450) --------------------------------------------------

def test_transformer_fla_three_phase() -> None:
    assert transformer_fla(15, 480, 3) == pytest.approx(18.04, abs=0.01)


def test_primary_only_125_percent_next_size_up() -> None:
    # 18.04 A * 1.25 = 22.55 -> next standard 25 A.
    r = size_transformer_protection(15, 480, 208)
    assert r.detail["primary_ocpd_a"] == 25.0


def test_small_transformer_167_percent_no_next_up() -> None:
    # 1 kVA 1-ph @ 480 V: FLA 2.08 A -> 167% = 3.48 A -> no standard rating
    # at or below; must raise with guidance.
    with pytest.raises(ValueError, match="supplementary"):
        size_transformer_protection(1, 480, 120, phases=1)


def test_primary_plus_secondary_scheme() -> None:
    r = size_transformer_protection(15, 480, 208, secondary_protection=True)
    # secondary FLA = 15000/(sqrt(3)*208) = 41.64 A * 1.25 = 52.05 -> 60 A
    assert r.detail["secondary_ocpd_a"] == 60.0
    # primary max 250% of 18.04 = 45.1 -> largest at-or-below = 45 A
    assert r.detail["primary_ocpd_a"] == 45.0


# --- SCCR (UL 508A SB4) -------------------------------------------------------

def test_weakest_link() -> None:
    parts = [
        PanelComponent("main breaker", 65, is_ocpd=True),
        PanelComponent("contactor", 5),
        PanelComponent("VFD", 100),
    ]
    r = panel_sccr(parts)
    assert r.value == 5.0
    assert "contactor" in r.assumptions[0]
    assert any("3rd Ed. (2018), rev. 2025-06-26" in str(c) for c in r.citations)


def test_sccr_below_available_fault_warns() -> None:
    r = panel_sccr([PanelComponent("contactor", 5)], available_fault_ka=10)
    assert any("non-compliant" in w for w in r.warnings)


def test_sccr_meets_available_fault_no_warning() -> None:
    r = panel_sccr([PanelComponent("main breaker", 65)], available_fault_ka=35)
    assert not r.warnings


def test_sccr_input_validation() -> None:
    with pytest.raises(ValueError):
        panel_sccr([])
    with pytest.raises(ValueError):
        PanelComponent("bad", 0)


# --- short circuit -------------------------------------------------------------

def test_infinite_bus_transformer() -> None:
    # 1500 kVA, 480 V, 5.75 %Z: FLA 1804 A -> 31.4 kA.
    r = transformer_fault_current(1500, 480, 5.75)
    assert r.value == pytest.approx(31378, rel=1e-3)


def test_point_to_point_attenuation() -> None:
    r = point_to_point(30000, length_ft=50, c_value=5907, voltage=480)
    f = math.sqrt(3) * 50 * 30000 / (5907 * 480)
    assert r.value == pytest.approx(30000 / (1 + f))
    assert 0 < r.detail["attenuation_percent"] < 100


def test_short_circuit_input_validation() -> None:
    with pytest.raises(ValueError):
        transformer_fault_current(1500, 480, 0)
    with pytest.raises(ValueError):
        point_to_point(30000, 50, -1, 480)
