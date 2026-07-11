"""Tests for encoder scaling math (pure kinematics, exact expectations)."""

from __future__ import annotations

import pytest

from cst.motion.encoder import EncoderScaling


@pytest.fixture
def linear_axis() -> EncoderScaling:
    # 1024-line encoder, x4 quadrature, 5:1 reducer, 10 mm/rev ballscrew.
    return EncoderScaling(pulses_per_rev=1024, quadrature=4, gear_ratio=5.0, lead=10.0)


def test_counts_per_motor_rev(linear_axis: EncoderScaling) -> None:
    assert linear_axis.counts_per_motor_rev == 4096


def test_counts_per_load_rev_through_gearing(linear_axis: EncoderScaling) -> None:
    assert linear_axis.counts_per_load_rev == 20480


def test_counts_per_unit_and_resolution(linear_axis: EncoderScaling) -> None:
    assert linear_axis.counts_per_unit == 2048  # counts per mm
    assert linear_axis.resolution == pytest.approx(1 / 2048)


def test_position_round_trip(linear_axis: EncoderScaling) -> None:
    counts = linear_axis.position_to_counts(123.456)
    assert linear_axis.counts_to_position(counts) == pytest.approx(123.456)


def test_rpm_to_counts_per_sec(linear_axis: EncoderScaling) -> None:
    # 3000 RPM = 50 rev/s * 4096 counts/rev = 204,800 counts/s.
    assert linear_axis.rpm_to_counts_per_sec(3000) == 204800


def test_rpm_to_linear_speed(linear_axis: EncoderScaling) -> None:
    # 3000 motor RPM / 5 gear = 600 load RPM = 10 rev/s * 10 mm = 100 mm/s.
    assert linear_axis.rpm_to_linear_speed(3000) == pytest.approx(100.0)


def test_rotary_axis_degrees() -> None:
    rotary = EncoderScaling(pulses_per_rev=2500, quadrature=4)
    assert rotary.counts_to_position(2500) == pytest.approx(90.0)
    assert rotary.resolution == pytest.approx(360 / 10000)


def test_counts_per_sec_round_trip() -> None:
    enc = EncoderScaling(pulses_per_rev=360, quadrature=1)
    assert enc.counts_per_sec_to_rpm(enc.rpm_to_counts_per_sec(1750)) == pytest.approx(1750)


def test_linear_helpers_reject_rotary_axis() -> None:
    rotary = EncoderScaling(pulses_per_rev=1024)
    with pytest.raises(ValueError, match="linear axis"):
        _ = rotary.counts_per_unit
    with pytest.raises(ValueError, match="linear axis"):
        rotary.rpm_to_linear_speed(1000)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"pulses_per_rev": 0},
        {"pulses_per_rev": 1024, "quadrature": 3},
        {"pulses_per_rev": 1024, "gear_ratio": 0},
        {"pulses_per_rev": 1024, "lead": -1},
    ],
)
def test_invalid_construction_raises(kwargs: dict) -> None:
    with pytest.raises(ValueError):
        EncoderScaling(**kwargs)
