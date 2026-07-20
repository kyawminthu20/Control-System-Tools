"""Synchronization-health checks over a twin's inbound telemetry.

The corpus note ``digital_twin.md`` §3 lists what the physical-to-digital
direction owes before anything downstream can be trusted: preserve both
timestamps (step 2), and reject or mark stale, substituted, frozen, and
out-of-sequence data (step 4). This module measures those properties on a
recorded sequence so the claim "the twin is synchronized" can be checked rather
than asserted.

Each sample is a ``(source_timestamp, acquisition_timestamp)`` pair in epoch
seconds: when the observation was taken, and when the twin received it. Their
difference is the transport delay plus any clock skew — a quantity that is
invisible if only one timestamp is kept, which is exactly why the corpus
requires both.

Like :mod:`cst.twin.contract`, this reports and never acts.
"""

from __future__ import annotations

import math
import statistics
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from cst.common.cite import Citation

CITATIONS = (
    Citation(
        standard="Control System Tools corpus",
        clause="design_framework/ai_integration/digital_twin.md §3 steps 2 and 4",
        note="preserve both timestamps; reject or mark stale, frozen, out-of-sequence data",
    ),
)


@dataclass(frozen=True)
class Gap:
    """A run of missing telemetry, inferred from an oversized sample interval."""

    start_s: float
    duration_s: float


@dataclass(frozen=True)
class SyncHealth:
    """Measured synchronization properties of a telemetry sequence."""

    sample_count: int
    span_s: float
    median_interval_s: float
    max_gap_s: float
    gaps: tuple[Gap, ...]
    out_of_order_count: int
    stale_count: int
    stale_fraction: float
    mean_skew_s: float
    max_abs_skew_s: float
    skew_drift_s_per_s: float
    warnings: tuple[str, ...]
    citations: tuple[Citation, ...] = CITATIONS

    def report(self) -> str:
        """Render a plain-text block, matching ``CalcResult.report()`` shape."""
        lines = [
            f"Twin synchronization health: {self.sample_count} samples "
            f"over {self.span_s:g} s",
            f"  median interval: {self.median_interval_s:g} s",
            f"  max gap: {self.max_gap_s:g} s ({len(self.gaps)} gap(s) detected)",
            f"  out-of-order samples: {self.out_of_order_count}",
            f"  stale samples: {self.stale_count} ({self.stale_fraction:.1%})",
            f"  mean skew: {self.mean_skew_s:g} s (max |skew| {self.max_abs_skew_s:g} s)",
            f"  skew drift: {self.skew_drift_s_per_s:.3g} s/s",
        ]
        if self.gaps:
            lines.append("  Gaps:")
            lines.extend(
                f"    - {g.duration_s:g} s starting at {g.start_s:.3f}" for g in self.gaps
            )
        if self.warnings:
            lines.append("  Warnings:")
            lines.extend(f"    ! {w}" for w in self.warnings)
        lines.append("  References:")
        lines.extend(f"    - {c}" for c in self.citations)
        return "\n".join(lines)


def sync_health(
    samples: Sequence[tuple[float, float]],
    *,
    max_age_s: float,
    gap_factor: float = 3.0,
) -> SyncHealth:
    """Measure synchronization health over ``(source_ts, acquisition_ts)`` samples.

    ``max_age_s`` is the freshness bound: a sample whose acquisition lagged its
    source by more than this was already stale on arrival. ``gap_factor``
    multiplies the median interval to set the threshold above which a quiet
    stretch counts as a gap rather than ordinary jitter.

    Samples are analysed in the order given, because arrival order is itself the
    signal — sorting them first would erase the out-of-order condition that
    §3 step 4 requires be detected.
    """
    if len(samples) < 2:
        raise ValueError(
            f"need at least 2 samples to measure intervals and drift, got {len(samples)}"
        )
    if max_age_s <= 0:
        raise ValueError(f"max_age_s must be positive, got {max_age_s}")
    if gap_factor <= 1:
        raise ValueError(
            f"gap_factor must exceed 1 (it multiplies the median interval), got {gap_factor}"
        )
    for i, pair in enumerate(samples):
        if len(pair) != 2:
            raise ValueError(f"sample {i} has {len(pair)} values; expected (source, acquisition)")
        if not all(math.isfinite(v) for v in pair):
            raise ValueError(f"sample {i} holds a non-finite timestamp: {pair}")

    sources = [float(s) for s, _ in samples]
    skews = [float(a) - float(s) for s, a in samples]

    intervals = [b - a for a, b in zip(sources, sources[1:])]
    forward = [d for d in intervals if d > 0]
    # An all-backwards or all-identical series has no forward interval to take a
    # median of; 0.0 makes every interval count as a gap, which is the honest
    # reading of a stream that never advances.
    median_interval = statistics.median(forward) if forward else 0.0

    gap_threshold = median_interval * gap_factor
    gaps = tuple(
        Gap(start_s=a, duration_s=d)
        for a, d in zip(sources, intervals)
        if median_interval > 0 and d > gap_threshold
    )
    out_of_order = sum(1 for d in intervals if d < 0)

    stale = [s for s in skews if s > max_age_s]
    span = sources[-1] - sources[0]

    return SyncHealth(
        sample_count=len(samples),
        span_s=span,
        median_interval_s=median_interval,
        max_gap_s=max(gaps, key=lambda g: g.duration_s).duration_s if gaps else 0.0,
        gaps=gaps,
        out_of_order_count=out_of_order,
        stale_count=len(stale),
        stale_fraction=len(stale) / len(samples),
        mean_skew_s=statistics.fmean(skews),
        max_abs_skew_s=max(abs(s) for s in skews),
        skew_drift_s_per_s=_slope(sources, skews),
        warnings=_warnings(gaps, out_of_order, len(stale), len(samples), skews, sources),
    )


def _slope(xs: Sequence[float], ys: Sequence[float]) -> float:
    """Least-squares slope of *ys* against *xs*; 0.0 when *xs* has no spread.

    A drifting skew means the two clocks are running at different rates, which
    a mean or max skew alone cannot reveal.
    """
    mean_x = statistics.fmean(xs)
    mean_y = statistics.fmean(ys)
    denom = sum((x - mean_x) ** 2 for x in xs)
    if denom == 0:
        return 0.0
    return sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)) / denom


def _warnings(
    gaps: tuple[Gap, ...],
    out_of_order: int,
    stale_count: int,
    total: int,
    skews: Sequence[float],
    sources: Sequence[float],
) -> tuple[str, ...]:
    out: list[str] = []
    if gaps:
        worst = max(gaps, key=lambda g: g.duration_s)
        out.append(
            f"{len(gaps)} telemetry gap(s); longest {worst.duration_s:g} s at "
            f"{worst.start_s:.3f} — twin state was unsynchronized across it"
        )
    if out_of_order:
        out.append(
            f"{out_of_order} sample(s) arrived out of sequence — §3 step 4 requires "
            f"these be rejected or marked, never silently absorbed"
        )
    if stale_count:
        out.append(
            f"{stale_count} of {total} sample(s) exceeded the freshness bound on arrival"
        )
    if any(s < 0 for s in skews):
        out.append(
            "negative skew present: acquisition precedes its own source timestamp, "
            "which means the two clocks disagree — treat both as suspect"
        )
    drift = _slope(sources, skews)
    if abs(drift) > 1e-3:
        out.append(
            f"skew is drifting at {drift:.3g} s/s — the source and acquisition clocks "
            f"are running at different rates and will diverge without correction"
        )
    return tuple(out)


def read_sample_csv(path: str | Path) -> list[tuple[float, float]]:
    """Read a two-column ``source_ts,acquisition_ts`` CSV, header optional."""
    p = Path(path)
    try:
        raw = p.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"sample file not found: {p}") from None

    samples: list[tuple[float, float]] = []
    for lineno, line in enumerate(raw.splitlines(), start=1):
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        parts = [c.strip() for c in text.split(",")]
        if len(parts) < 2:
            raise ValueError(
                f"{p} line {lineno}: expected 2 columns "
                f"(source_ts, acquisition_ts), got {len(parts)}"
            )
        try:
            samples.append((float(parts[0]), float(parts[1])))
        except ValueError:
            if lineno == 1:
                continue  # a header row, not a defect
            raise ValueError(
                f"{p} line {lineno}: {parts[:2]} are not numeric timestamps"
            ) from None
    if not samples:
        raise ValueError(f"{p} holds no numeric sample rows")
    return samples
