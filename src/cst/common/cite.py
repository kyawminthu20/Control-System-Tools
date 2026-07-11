"""Citation framework: every calculator result carries its provenance.

A ``CalcResult`` bundles the numeric answer with the standard/formula
citations and the engineering assumptions that produced it, so a value can be
dropped into a design package without losing traceability.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Citation:
    """Reference to a standard clause or published formula backing a result.

    ``standard`` is the document identifier (e.g. "NEC 2023"), ``clause`` the
    article/section/table (e.g. "210.19(A) Informational Note No. 4"), and
    ``note`` a one-line statement of what the reference contributes.
    """

    standard: str
    clause: str
    note: str = ""

    def __str__(self) -> str:
        text = f"{self.standard} {self.clause}".strip()
        return f"{text} — {self.note}" if self.note else text


@dataclass
class CalcResult:
    """A calculated value with units, provenance, and assumptions.

    ``value`` is the primary answer; ``detail`` holds named intermediate or
    secondary values (all floats) so callers can build reports without
    re-deriving them. ``warnings`` carries non-fatal engineering flags such as
    "exceeds recommended voltage drop".
    """

    name: str
    value: float
    unit: str
    citations: list[Citation] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    detail: dict[str, float] = field(default_factory=dict)

    def report(self) -> str:
        """Render a plain-text block suitable for design notes or CLI output."""
        lines = [f"{self.name}: {self.value:g} {self.unit}".rstrip()]
        for key, val in self.detail.items():
            lines.append(f"  {key}: {val:g}")
        if self.warnings:
            lines.append("  Warnings:")
            lines.extend(f"    ! {w}" for w in self.warnings)
        if self.assumptions:
            lines.append("  Assumptions:")
            lines.extend(f"    - {a}" for a in self.assumptions)
        if self.citations:
            lines.append("  References:")
            lines.extend(f"    - {c}" for c in self.citations)
        return "\n".join(lines)
