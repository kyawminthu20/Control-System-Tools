"""Panel short-circuit current rating — UL 508A Supplement SB (weakest link).

Implements the SB4 assessment logic: the panel SCCR is the lowest of

- every power-circuit component's SCCR (SB4.2), where a component protected
  by a listed combination is taken at its combination rating, and
- every branch-circuit protective device's interrupting rating (SB4.3).

Component default SCCRs (UL 508A Table SB4.1) are data the user supplies per
component; this module deliberately does NOT ship default values — enter each
component's marked SCCR/IR or its Table SB4.1 default from a licensed copy.

Current-limiting upstream devices can only raise component SCCRs via a
tested/listed series combination (SB4.3.1) — series ratings must come from
manufacturer combination tables, so this module never infers them.
"""

from __future__ import annotations

from dataclasses import dataclass

from cst.common.cite import CalcResult, Citation


@dataclass(frozen=True)
class PanelComponent:
    """One power-circuit component in the SCCR assessment.

    rating_ka: the component's marked SCCR, its Table SB4.1 default (from
    your licensed copy), or its interrupting rating for OCPDs.
    """

    name: str
    rating_ka: float
    is_ocpd: bool = False

    def __post_init__(self) -> None:
        if self.rating_ka <= 0:
            raise ValueError(f"{self.name}: rating_ka must be positive, got {self.rating_ka}")


def panel_sccr(
    components: list[PanelComponent],
    available_fault_ka: float | None = None,
) -> CalcResult:
    """Weakest-link panel SCCR per UL 508A SB4.

    Example:
        >>> parts = [PanelComponent("main breaker", 65, is_ocpd=True),
        ...          PanelComponent("contactor", 5),
        ...          PanelComponent("VFD", 100)]
        >>> r = panel_sccr(parts, available_fault_ka=10)
        >>> r.value, r.warnings[0][:22]
        (5, 'Panel SCCR 5 kA is BEL')
    """
    if not components:
        raise ValueError("At least one power-circuit component is required")

    weakest = min(components, key=lambda c: c.rating_ka)
    sccr = weakest.rating_ka

    result = CalcResult(
        name=f"Panel SCCR ({len(components)} power-circuit components)",
        value=sccr,
        unit="kA",
        citations=[
            Citation("UL 508A:2022", "SB4.2 / SB4.3",
                     "panel SCCR = lowest component SCCR or OCPD interrupting rating"),
            Citation("UL 508A:2022", "Table SB4.1",
                     "component defaults — user-supplied from licensed copy"),
            Citation("NEC 2023", "409.22 / 670.5",
                     "panel SCCR must be >= available fault current at installation"),
        ],
        assumptions=[
            f"Weakest link: {weakest.name} at {weakest.rating_ka:g} kA",
            "Series/combination ratings only via tested manufacturer tables (SB4.3.1) — "
            "none inferred here",
            "Control-circuit components excluded per SB4.2.1 (power circuit only)",
        ],
        detail={"weakest_link_ka": weakest.rating_ka},
    )
    if available_fault_ka is not None:
        result.detail["available_fault_ka"] = available_fault_ka
        if sccr < available_fault_ka:
            result.warnings.append(
                f"Panel SCCR {sccr:g} kA is BELOW the {available_fault_ka:g} kA available "
                "fault current — non-compliant per NEC 409.22; upgrade the weakest "
                "component or use a listed series combination"
            )
    return result
