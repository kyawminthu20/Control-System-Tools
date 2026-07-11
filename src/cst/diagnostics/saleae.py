"""Saleae Logic 2 digital-export post-processing.

Parses the Logic 2 digital CSV export (header ``Time [s], Channel 0, ...``;
one row per transition) and computes the field-debug quantities: pulse
statistics, frequency/duty, glitch detection, and A/B quadrature decode for
encoder work (pairs with cst.motion.encoder for counts -> engineering units).
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Edge:
    time_s: float
    level: int  # level AFTER the transition


def load_digital_export(csv_path: str | Path) -> dict[str, list[Edge]]:
    """Parse a Logic 2 digital export into {channel_name: [Edge, ...]}.

    Only rows where a channel's level differs from its previous level are
    recorded as edges for that channel.
    """
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Saleae export not found: {path}")
    with path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.reader(fh)
        header = next(reader, None)
        if not header or "time" not in header[0].lower():
            raise ValueError(
                f"{path}: expected a Logic 2 digital export with a 'Time [s]' first column"
            )
        channels = [name.strip() for name in header[1:]]
        edges: dict[str, list[Edge]] = {name: [] for name in channels}
        last: dict[str, int | None] = {name: None for name in channels}
        for row in reader:
            if not row or not row[0].strip():
                continue
            t = float(row[0])
            for name, cell in zip(channels, row[1:]):
                level = int(float(cell))
                if last[name] is None:
                    # First row is the initial state at capture start,
                    # not a transition — record nothing.
                    last[name] = level
                elif level != last[name]:
                    edges[name].append(Edge(t, level))
                    last[name] = level
    return edges


@dataclass
class PulseStats:
    edge_count: int
    frequency_hz: float
    duty_cycle: float
    min_high_s: float
    max_high_s: float


def pulse_stats(edges: list[Edge]) -> PulseStats:
    """Frequency, duty cycle, and high-pulse width extremes for one channel."""
    rising = [e.time_s for e in edges if e.level == 1]
    if len(rising) < 2:
        raise ValueError(
            f"need at least 2 rising edges to compute frequency, got {len(rising)}"
        )
    periods = [b - a for a, b in zip(rising, rising[1:])]
    frequency = 1.0 / (sum(periods) / len(periods))

    highs: list[float] = []
    rise_time: float | None = None
    for e in edges:
        if e.level == 1:
            rise_time = e.time_s
        elif rise_time is not None:
            highs.append(e.time_s - rise_time)
            rise_time = None
    if not highs:
        raise ValueError("no complete high pulses in capture")
    duty = (sum(highs) / len(highs)) * frequency

    return PulseStats(
        edge_count=len(edges),
        frequency_hz=frequency,
        duty_cycle=duty,
        min_high_s=min(highs),
        max_high_s=max(highs),
    )


def find_glitches(edges: list[Edge], min_width_s: float) -> list[tuple[float, float]]:
    """(time, width) of pulses (either polarity) shorter than min_width_s."""
    glitches = []
    for prev, cur in zip(edges, edges[1:]):
        width = cur.time_s - prev.time_s
        if width < min_width_s:
            glitches.append((prev.time_s, width))
    return glitches


def quadrature_decode(a_edges: list[Edge], b_edges: list[Edge]) -> dict[str, float]:
    """x4 decode of an A/B pair: net counts, direction reversals, total edges.

    Standard quadrature rule: on each A edge, B's level decides direction;
    on each B edge, A's level decides the opposite sense.
    """
    events = sorted(
        [("A", e) for e in a_edges] + [("B", e) for e in b_edges],
        key=lambda pair: pair[1].time_s,
    )
    # State BEFORE each channel's first edge (an edge toggles the level).
    level = {"A": 1 - a_edges[0].level if a_edges else 0,
             "B": 1 - b_edges[0].level if b_edges else 0}
    count = 0
    reversals = 0
    last_dir = 0
    for name, edge in events:
        other = "B" if name == "A" else "A"
        if name == "A":
            direction = 1 if edge.level != level["B"] else -1
        else:
            direction = 1 if edge.level == level["A"] else -1
        level[name] = edge.level
        count += direction
        if last_dir and direction != last_dir:
            reversals += 1
        last_dir = direction
    return {
        "net_counts": float(count),
        "direction_reversals": float(reversals),
        "total_edges": float(len(events)),
    }
