<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: NEC_APPLICATION
MODULE_ID: article_409_practical_workflow
LEARNING_LEVEL: applied

INDEX_TAGS:
  topics: ["article_409", "industrial_control_panel", "ICP", "UL_508A", "SCCR", "panel_marking"]
  systems: ["industrial_control_panel"]
-->

# Practical Article 409 Workflow

## 0. Purpose

This module covers NEC Article 409 scope, required markings, supply conductor sizing, and the relationship between Art 409 (the NEC requirement) and UL 508A (the construction standard). It provides a practical checklist for verifying a panel meets Art 409 before shipping or inspecting.

## 1. What Art 409 covers

Article 409 applies to **industrial control panels (ICPs)** — factory-built assemblies of two or more components (OCPDs, controllers, overloads, pilot devices) that form a coordinated system used to control industrial processes or machinery.

Art 409 does not apply to:
- Motor control centers (covered by Art 430 Part F)
- Switchboards and panelboards (covered by Art 408)
- Simple junction boxes or enclosures with only terminal blocks

An ICP is typically built by a panel shop (the "manufacturer") and installed by an electrical contractor. Art 409 governs the panel as a product; the installation is also governed by the applicable Articles for each circuit type inside (Art 430 for motor circuits, Art 725 for control circuits, etc.).

## 2. Supply conductors — Art 409.20

The conductors supplying an ICP must have an ampacity of at least:

**125% of the full-load current of all resistance heating loads, plus 125% of the highest-rated motor FLA, plus 100% of all remaining loads**

This mirrors the Art 430 feeder formula plus the continuous-load rule from Art 215.

Example — panel with: one 25 HP motor (34 A FLA), one 10 HP motor (14 A FLA), 2 kW of control transformers (4 A at 480V):
- 34 A × 1.25 = 42.5 A (largest motor)
- 14 A × 1.00 = 14 A (remaining motor)
- 4 A × 1.00 = 4 A (non-motor load)
- Total: 42.5 + 14 + 4 = **60.5 A minimum supply conductor ampacity**

## 3. Required markings — Art 409.110

Every ICP must have a nameplate that includes all of the following:

| Required item | Notes |
|---------------|-------|
| Manufacturer name, trademark, or symbol | Panel builder identity |
| Supply voltage, number of phases, and frequency | e.g., 480V, 3-phase, 60 Hz |
| Full-load current | Calculated per Art 409.20 |
| Short-circuit current rating (SCCR) | In kA rms symmetrical |
| Enclosure type designation | e.g., NEMA Type 1, Type 12, Type 4X |

The **SCCR** is the single most-inspected item. AHJs and customers regularly reject panels that omit or under-state the SCCR marking.

## 4. Overcurrent protection — Art 409.22

The main OCPD for the ICP must be:
- Sized to carry the supply load calculated per Art 409.20
- Rated to interrupt the available fault current (its AIC rating must ≥ available fault current)
- Located at the point where the supply conductors enter the panel, unless a remote disconnect is used per Art 409.30

If the panel contains multiple branch circuits with their own OCPDs and no single main OCPD, all branch OCPDs together constitute the disconnecting means — this is the "six-breaker rule" permitted under Art 409.30(B).

## 5. How Art 409 and UL 508A relate

| | NEC Art 409 | UL 508A |
|-|-------------|---------|
| Type | Code requirement (law) | Construction standard (product standard) |
| Enforced by | AHJ (inspector) | Third-party listing body (UL, ETL, etc.) |
| Covers | Electrical safety minimums | Complete panel construction, wiring methods, component selection, SCCR |
| SCCR method | Requires marking; does not specify method | Supplement SB defines component method |

A panel listed to UL 508A satisfies Art 409 requirements for construction. An unlisted panel must be field-evaluated by the AHJ or a qualified testing organization.

Most customers and AHJs prefer or require a listed panel. "Listed to UL 508A" means the panel shop has been audited and the panels are built per the standard.

## 6. Difference between ICP (Art 409) and MCC (Art 430 Part F)

| | ICP — Art 409 | MCC — Art 430 Part F |
|-|---------------|----------------------|
| Typical use | Custom machine control | Multiple motor feeders |
| Construction standard | UL 508A | UL 845 |
| Bus structure | Not required | Horizontal and vertical bus |
| Plug-in units | Not typical | Standard |

A machine builder's control panel is almost always an ICP under Art 409. A utility substation or building services motor lineup is typically an MCC under Art 430 Part F.

## 7. Art 409 inspection checklist

Use this checklist before shipment or AHJ inspection:

- [ ] Nameplate present with manufacturer name
- [ ] Supply voltage, phases, and frequency marked
- [ ] Full-load current marked (calculated per 409.20)
- [ ] SCCR marked in kA (verified via UL 508A SB component method)
- [ ] Enclosure type designation marked
- [ ] Main OCPD AIC rating ≥ available fault current at installation point
- [ ] All conductors sized per applicable articles (430 for motors, 725 for control)
- [ ] Grounding bus bonded to enclosure
- [ ] Wiring clearances per UL 508A (if listed panel)
- [ ] Door interlock on main disconnect (if required by customer or NFPA 79)

## 8. Engineering takeaway

Art 409 is a short article but a high-impact one. The SCCR marking requirement is where most panels fail inspection — either the marking is missing, the value is wrong, or the underlying component method was not followed. Build the SCCR verification into the panel design stage, not as a final step before shipping.

The supply conductor sizing formula in Art 409.20 is also frequently missed on panels that grow incrementally — adding a motor or heater bank changes the required supply conductor ampacity and may require recalculation.

## Related files

- [NEC Code Reading Fundamentals](./nec_code_reading_fundamentals.md)
- [SCCR Workflow for Industrial Control Panels](./sccr_workflow.md)
- [Motor and Panel Code Application](./motor_and_panel_code_application.md)
- [Grounding and Bonding for Control Panels](./grounding_bonding_control_panels.md)
