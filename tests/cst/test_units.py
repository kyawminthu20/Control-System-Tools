"""Golden-value tests for unit conversions (ASTM B258 AWG geometry)."""

from __future__ import annotations

import pytest

from cst.common.units import (
    awg_to_circular_mils,
    circular_mils_to_mm2,
    feet_to_meters,
    hp_to_watts,
)


def test_awg_4_0_is_exactly_211600_cmil() -> None:
    # ASTM B258 anchors 4/0 at 0.46 in = 460 mil diameter -> 460^2 cmil.
    assert awg_to_circular_mils("4/0") == pytest.approx(211600, rel=1e-9)


@pytest.mark.parametrize(
    ("awg", "published_cmil"),
    [("14", 4110), ("12", 6530), ("10", 10380), ("8", 16510), ("6", 26240),
     ("4", 41740), ("2", 66360), ("1/0", 105600), ("2/0", 133100)],
)
def test_awg_matches_nec_chapter9_published_areas(awg: str, published_cmil: int) -> None:
    # NEC Ch.9 Table 8 lists rounded values; formula should agree within 0.5 %.
    assert awg_to_circular_mils(awg) == pytest.approx(published_cmil, rel=5e-3)


def test_awg_accepts_suffix_and_whitespace() -> None:
    assert awg_to_circular_mils(" 12 AWG ") == awg_to_circular_mils("12")


def test_awg_rejects_garbage() -> None:
    with pytest.raises(ValueError, match="Unrecognized AWG"):
        awg_to_circular_mils("banana")


def test_cmil_to_mm2_known_value() -> None:
    # 12 AWG ~= 3.31 mm^2 (published conversion)
    assert circular_mils_to_mm2(6530) == pytest.approx(3.31, rel=1e-2)


def test_cmil_to_mm2_rejects_nonpositive() -> None:
    with pytest.raises(ValueError):
        circular_mils_to_mm2(0)


def test_exact_conversions() -> None:
    assert feet_to_meters(100) == pytest.approx(30.48)
    assert hp_to_watts(1) == pytest.approx(745.7, rel=1e-4)
