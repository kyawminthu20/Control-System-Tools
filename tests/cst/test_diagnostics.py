"""Tests for SBM anomaly detection and Saleae post-processing (synthetic data)."""

from __future__ import annotations

import math
from pathlib import Path

import pytest

from cst.diagnostics import sbm
from cst.diagnostics.saleae import (
    find_glitches,
    load_digital_export,
    pulse_stats,
    quadrature_decode,
)


# --- SBM ------------------------------------------------------------------------

def _normal_row(i: int) -> list[float]:
    # Three correlated "sensors": flow, pressure ~ flow, temperature slow drift.
    flow = 50 + 10 * math.sin(i / 8)
    return [flow, 2.0 + flow * 0.04, 60 + 0.01 * i]


@pytest.fixture(scope="module")
def model() -> sbm.SBMModel:
    return sbm.train([_normal_row(i) for i in range(200)], memory_size=25)


def test_normal_data_scores_low(model: sbm.SBMModel) -> None:
    # Held-out rows interleaved within the trained operating envelope
    # (fractional indices interpolate both the sine and the drift).
    scores = [model.score(_normal_row(i + 0.5)) for i in range(100, 140)]
    assert max(scores) < 1.5


def test_broken_correlation_separates_from_baseline(model: sbm.SBMModel) -> None:
    # Pressure decouples from flow — classic sensor/process fault signature.
    # Detection is judged as separation from the normal baseline (how SBM
    # alarm thresholds are set in practice), not an absolute z-value.
    baseline_max = max(model.score(_normal_row(i + 0.5)) for i in range(100, 140))
    row = _normal_row(120)
    row[1] += 1.0  # ~1 bar offset, far outside the correlated band
    fault_score = model.score(row)
    assert fault_score > 2.0
    assert fault_score > 2.0 * baseline_max
    # And the residual localizes to the pressure sensor (index 1).
    residuals = model.residuals(row)
    assert abs(residuals[1]) == max(abs(r) for r in residuals)


def test_reconstruction_tracks_engineering_units(model: sbm.SBMModel) -> None:
    row = _normal_row(123)
    estimate = model.reconstruct(row)
    assert estimate[0] == pytest.approx(row[0], abs=2.0)


def test_train_input_validation() -> None:
    with pytest.raises(ValueError, match="at least 3"):
        sbm.train([[1.0, 2.0]])
    with pytest.raises(ValueError, match="inconsistent"):
        sbm.train([[1.0], [1.0, 2.0], [1.0]])
    with pytest.raises(ValueError, match="bandwidth"):
        sbm.train([[1.0], [2.0], [3.0]], bandwidth=0)


def test_score_rejects_wrong_width(model: sbm.SBMModel) -> None:
    with pytest.raises(ValueError, match="expected 3 sensors"):
        model.score([1.0, 2.0])


def test_far_outside_envelope_still_scores(model: sbm.SBMModel) -> None:
    score = model.score([500.0, 50.0, 500.0])  # nowhere near training data
    assert score > 10


# --- Saleae ----------------------------------------------------------------------

def _write_capture(path: Path) -> None:
    # 1 kHz square wave on Ch0 (25 % duty), quadrature pair on Ch1/Ch2,
    # one 2 us glitch on Ch0 at t=0.010.
    lines = ["Time [s],Channel 0,Channel 1,Channel 2"]
    state = [0, 0, 0]

    def row(t: float) -> str:
        return f"{t:.9f},{state[0]},{state[1]},{state[2]}"

    events: list[tuple[float, int, int]] = []
    for i in range(10):  # Ch0: rising at i*1ms, falling 0.25ms later
        events.append((i * 1e-3, 0, 1))
        events.append((i * 1e-3 + 0.25e-3, 0, 0))
    events.append((0.010, 0, 1))          # glitch: 2 us high pulse
    events.append((0.010 + 2e-6, 0, 0))
    # Quadrature forward x5 cycles: A leads B by 90 deg, period 400 us.
    for i in range(5):
        t0 = i * 400e-6
        events.append((t0 + 0e-6, 1, 1))
        events.append((t0 + 100e-6, 2, 1))
        events.append((t0 + 200e-6, 1, 0))
        events.append((t0 + 300e-6, 2, 0))
    for t, ch, level in sorted(events):
        state[ch] = level
        lines.append(row(t))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


@pytest.fixture
def capture(tmp_path: Path) -> dict:
    path = tmp_path / "digital.csv"
    _write_capture(path)
    return load_digital_export(path)


def test_pulse_stats_frequency_and_duty(capture: dict) -> None:
    stats = pulse_stats(capture["Channel 0"])
    assert stats.frequency_hz == pytest.approx(1000, rel=0.15)
    assert stats.min_high_s == pytest.approx(2e-6, rel=0.01)   # the glitch
    assert stats.max_high_s == pytest.approx(0.25e-3, rel=0.01)


def test_glitch_detection(capture: dict) -> None:
    glitches = find_glitches(capture["Channel 0"], min_width_s=10e-6)
    assert len(glitches) == 1
    assert glitches[0][1] == pytest.approx(2e-6, rel=0.01)


def test_quadrature_forward_counts(capture: dict) -> None:
    result = quadrature_decode(capture["Channel 1"], capture["Channel 2"])
    assert result["net_counts"] == 20          # 5 cycles x 4 counts
    assert result["direction_reversals"] == 0
    assert result["total_edges"] == 20


def test_export_requires_header(tmp_path: Path) -> None:
    bad = tmp_path / "bad.csv"
    bad.write_text("nope\n1,2\n", encoding="utf-8")
    with pytest.raises(ValueError, match="Time"):
        load_digital_export(bad)
