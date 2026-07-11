"""Similarity-based-modeling (SBM) style anomaly detection — stdlib only.

Autoassociative kernel estimate in the SBM family (Wegerich, "Similarity
based modeling of time synchronous averaged vibration signals for machinery
health monitoring", 2004; the classic equipment-condition-monitoring
approach): a memory matrix of normal-operation vectors reconstructs each
observation as a similarity-weighted combination of remembered states; the
residual between observation and reconstruction scores abnormality.

This implementation uses Gaussian-kernel weights (Nadaraya–Watson form) over
z-scored sensors — a recognized simplification that avoids matrix inversion
and is robust for the small memory matrices a commissioning laptop handles.
Train only on data you trust to be NORMAL; that decision is the whole game.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


def _zscore_params(rows: list[list[float]]) -> tuple[list[float], list[float]]:
    n_sensors = len(rows[0])
    means, stds = [], []
    for j in range(n_sensors):
        column = [r[j] for r in rows]
        mean = sum(column) / len(column)
        variance = sum((v - mean) ** 2 for v in column) / len(column)
        means.append(mean)
        stds.append(math.sqrt(variance) or 1.0)  # constant sensor -> unit scale
    return means, stds


@dataclass
class SBMModel:
    """Trained model: z-score params + memory matrix (z-scored vectors)."""

    means: list[float]
    stds: list[float]
    memory: list[list[float]]
    bandwidth: float

    @property
    def n_sensors(self) -> int:
        return len(self.means)

    def _z(self, row: list[float]) -> list[float]:
        return [(v - m) / s for v, m, s in zip(row, self.means, self.stds)]

    def reconstruct(self, row: list[float]) -> list[float]:
        """Similarity-weighted estimate of the row, in engineering units."""
        z = self._z(row)
        weights = []
        for mem in self.memory:
            d2 = sum((a - b) ** 2 for a, b in zip(z, mem))
            weights.append(math.exp(-d2 / (2.0 * self.bandwidth**2)))
        total = sum(weights)
        if total < 1e-12:
            # Observation is far outside every remembered state — return the
            # nearest memory vector so the residual stays meaningful.
            nearest = min(
                self.memory,
                key=lambda mem: sum((a - b) ** 2 for a, b in zip(z, mem)),
            )
            est_z = nearest
        else:
            est_z = [
                sum(w * mem[j] for w, mem in zip(weights, self.memory)) / total
                for j in range(self.n_sensors)
            ]
        return [ez * s + m for ez, s, m in zip(est_z, self.stds, self.means)]

    def residuals(self, row: list[float]) -> list[float]:
        """Per-sensor residuals in z-units — use to localize which sensor moved."""
        if len(row) != self.n_sensors:
            raise ValueError(f"expected {self.n_sensors} sensors, got {len(row)}")
        estimate = self.reconstruct(row)
        return [(v - e) / s for v, e, s in zip(row, estimate, self.stds)]

    def score(self, row: list[float]) -> float:
        """Anomaly score = max |z-residual| across sensors.

        Max (not RMS) so a single-sensor fault isn't diluted by the healthy
        sensors. The score is RELATIVE: reconstruction partially absorbs
        faults, so set the alarm threshold from a held-out normal baseline
        (typically 2-3x the baseline max), not from an absolute z-value.
        """
        return max(abs(r) for r in self.residuals(row))


def train(
    normal_rows: list[list[float]],
    memory_size: int = 25,
    bandwidth: float = 1.0,
) -> SBMModel:
    """Build a model from KNOWN-NORMAL data.

    Memory selection: the vector holding each sensor's min and max (captures
    the operating envelope) plus evenly spaced samples up to ``memory_size``.
    """
    if len(normal_rows) < 3:
        raise ValueError(f"need at least 3 training rows, got {len(normal_rows)}")
    widths = {len(r) for r in normal_rows}
    if len(widths) != 1:
        raise ValueError(f"inconsistent row widths in training data: {sorted(widths)}")
    if bandwidth <= 0:
        raise ValueError(f"bandwidth must be positive, got {bandwidth}")

    means, stds = _zscore_params(normal_rows)
    n_sensors = len(means)

    chosen: list[int] = []
    for j in range(n_sensors):  # envelope vectors first
        column = [r[j] for r in normal_rows]
        for idx in (column.index(min(column)), column.index(max(column))):
            if idx not in chosen:
                chosen.append(idx)
    remaining = max(0, memory_size - len(chosen))
    if remaining:
        step = max(1, len(normal_rows) // remaining)
        for idx in range(0, len(normal_rows), step):
            if idx not in chosen and len(chosen) < memory_size:
                chosen.append(idx)

    memory = [
        [(normal_rows[i][j] - means[j]) / stds[j] for j in range(n_sensors)]
        for i in sorted(chosen)
    ]
    return SBMModel(means=means, stds=stds, memory=memory, bandwidth=bandwidth)
