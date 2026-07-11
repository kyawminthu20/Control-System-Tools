"""Encoder scaling: counts <-> engineering units <-> speed.

Pure kinematics — no standards data involved. Definitions:

    counts/rev  = pulses_per_rev * quadrature (x4 for A/B quadrature decode)
    counts/unit = counts/rev * gear_ratio / lead        (linear axes)
    counts/s    = rpm_load * counts/rev * gear_ratio / 60

``gear_ratio`` is motor revs per load rev (> 1 for a reducer). ``lead`` is
linear travel per LOAD revolution (e.g. ballscrew lead in mm/rev).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EncoderScaling:
    """Scaling for a rotary encoder on a (possibly geared, possibly linear) axis.

    pulses_per_rev: encoder line count (pre-quadrature), e.g. 1024
    quadrature:     decode multiplier — 4 for A/B quadrature, 1 for pulse-count
    gear_ratio:     motor revolutions per load revolution (1.0 = direct drive)
    lead:           linear travel per load revolution; None for rotary axes
    """

    pulses_per_rev: int
    quadrature: int = 4
    gear_ratio: float = 1.0
    lead: float | None = None

    def __post_init__(self) -> None:
        if self.pulses_per_rev <= 0:
            raise ValueError(f"pulses_per_rev must be positive, got {self.pulses_per_rev}")
        if self.quadrature not in (1, 2, 4):
            raise ValueError(f"quadrature must be 1, 2, or 4, got {self.quadrature}")
        if self.gear_ratio <= 0:
            raise ValueError(f"gear_ratio must be positive, got {self.gear_ratio}")
        if self.lead is not None and self.lead <= 0:
            raise ValueError(f"lead must be positive when given, got {self.lead}")

    @property
    def counts_per_motor_rev(self) -> float:
        """Encoder counts per MOTOR revolution (post-quadrature)."""
        return float(self.pulses_per_rev * self.quadrature)

    @property
    def counts_per_load_rev(self) -> float:
        """Encoder counts per LOAD revolution, through the gear ratio."""
        return self.counts_per_motor_rev * self.gear_ratio

    @property
    def counts_per_unit(self) -> float:
        """Counts per linear unit (same unit as ``lead``). Linear axes only."""
        if self.lead is None:
            raise ValueError("counts_per_unit requires a linear axis (set lead=...)")
        return self.counts_per_load_rev / self.lead

    @property
    def resolution(self) -> float:
        """Smallest measurable increment: linear units/count, or deg/count."""
        if self.lead is not None:
            return 1.0 / self.counts_per_unit
        return 360.0 / self.counts_per_load_rev

    def position_to_counts(self, position: float) -> float:
        """Linear position (lead units) or rotary angle (degrees) -> counts."""
        if self.lead is not None:
            return position * self.counts_per_unit
        return position / 360.0 * self.counts_per_load_rev

    def counts_to_position(self, counts: float) -> float:
        """Counts -> linear position (lead units) or rotary angle (degrees)."""
        if self.lead is not None:
            return counts / self.counts_per_unit
        return counts / self.counts_per_load_rev * 360.0

    def rpm_to_counts_per_sec(self, motor_rpm: float) -> float:
        """Motor shaft speed (RPM) -> encoder counts per second."""
        return motor_rpm / 60.0 * self.counts_per_motor_rev

    def counts_per_sec_to_rpm(self, counts_per_sec: float) -> float:
        """Encoder counts per second -> motor shaft speed (RPM)."""
        return counts_per_sec * 60.0 / self.counts_per_motor_rev

    def rpm_to_linear_speed(self, motor_rpm: float) -> float:
        """Motor RPM -> linear speed in lead-units/second. Linear axes only."""
        if self.lead is None:
            raise ValueError("rpm_to_linear_speed requires a linear axis (set lead=...)")
        return motor_rpm / 60.0 / self.gear_ratio * self.lead
