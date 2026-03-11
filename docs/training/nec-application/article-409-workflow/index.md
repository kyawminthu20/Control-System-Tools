---
layout: training-module
title: "Practical Article 409 Workflow"
description: "NEC Article 409 scope, required ICP markings, supply conductor sizing, the relationship between Art 409 and UL 508A, and a pre-shipment inspection checklist."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "NEC for Machines and Panels"
    url: "/training/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/article_409_practical_workflow.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
---

## Purpose

This module covers NEC Article 409, which governs industrial control panels (ICPs) as factory-built assemblies. It explains supply conductor sizing, required panel markings, the relationship between the NEC and UL 508A, and the distinction between an ICP under Art 409 and a motor control center (MCC) under Art 430 Part F.

---

## Article 409 scope — what is an ICP?

Art 409.2 defines an **industrial control panel (ICP)** as:

> An assembly of two or more components consisting of one of the following: (1) power circuit components only, such as switches, circuit breakers, fuses, relays, and contactors; (2) control circuit components only, such as push buttons, pilot lights, selector switches, timers, switches, control relays; (3) a combination of power and control circuit components.

The key characteristic is that an ICP is a **factory-built assembly** — it is assembled at a location other than where it is installed (typically a panel shop or OEM), tested, and then shipped to the installation site. This distinguishes it from field-wired assemblies, which are governed only by the articles covering their individual components.

Article 409 applies to the panel as a **whole assembly**, not just its parts. An individual circuit breaker in a panel is governed by Art 240; the panel that contains that breaker is governed by Art 409.

---

## Art 409.20 — supply conductor sizing

The supply conductors to the ICP must be sized to handle the total calculated load of the panel. Art 409.20 provides the sizing formula:

> The ampacity of the supply conductors shall not be less than the sum of:
> 1. **125 % of the full-load current rating of all resistance heating loads**
> 2. **125 % of the full-load current rating of the largest motor**
> 3. **100 % of the full-load current ratings of all other loads**

This formula combines the requirements of Art 430.24 (motor feeder sizing) and Art 424 (resistance heating) into a single rule for the ICP supply.

### Worked example — ICP with two motors

**Given:**
- Motor A: 25 HP, 460 V, three-phase — Table 430.250 FLC = 34 A
- Motor B: 10 HP, 460 V, three-phase — Table 430.250 FLC = 14 A
- No resistance heating loads
- Wiring: THHN copper, 75 °C terminations

**Calculation per Art 409.20:**

| Load | FLC | Factor | Contribution |
|---|---|---|---|
| Motor A (largest) | 34 A | 125 % | 42.5 A |
| Motor B | 14 A | 100 % | 14.0 A |
| **Total minimum ampacity** | | | **56.5 A** |

From Table 310.15(B)(16), 75 °C copper:

- 6 AWG = 65 A ampacity (≥ 56.5 A required) — **select 6 AWG THHN copper**

If the panel also had a 5 kW (208 V single-phase is not applicable here — assume 5 kW at 460 V three-phase = approximately 6.3 A) resistance heater, add 125 % × 6.3 = 7.9 A to the total: 56.5 + 7.9 = 64.4 A minimum ampacity, still within 6 AWG Cu range (65 A).

---

## Art 409.110 — required markings

Art 409.110 lists the markings that must appear on the ICP enclosure or a nameplate attached to it. These markings are required for the panel to be installed by an electrical contractor and accepted by an AHJ.

| Marking | Content required | Why it matters |
|---|---|---|
| Manufacturer name, trademark, or other identification | Panel builder identification | Traceability and warranty |
| Voltage, number of phases, and frequency | e.g., "460V / 3Ø / 60 Hz" | Confirms supply compatibility |
| Full-load current (FLC) | The total ampere demand on the supply conductors | Used by the EC to size supply conductors and service OCPD |
| Short-circuit current rating (SCCR) | In amperes RMS symmetrical | Must equal or exceed available fault current at installation |
| Enclosure type | Per NEMA or IEC enclosure classification | Confirms suitability for the environment (indoor, wash-down, etc.) |
| Overcurrent protective device type and rating | If supplied as part of the panel | Coordination documentation |

**The SCCR marking is non-negotiable.** An ICP without a marked SCCR cannot be installed under Art 409.110. The installer must confirm that the panel's marked SCCR is equal to or greater than the available short-circuit current (ASCC) at the point of installation. If the ASCC exceeds the panel SCCR, either the panel must be upgraded or current-limiting fuses must be added upstream to bring the let-through current within the panel's rating.

---

## Art 409.22 — OCPD sizing for the panel supply

The overcurrent protective device for the ICP supply must:

- Not exceed the marked short-circuit current rating (SCCR) of the panel
- Be sized to protect the supply conductors per Art 240
- For panels with motor loads, follow Art 430.62 for feeder OCPD sizing (largest branch-circuit OCPD + sum of other motor FLCs)

For the worked example above (25 HP + 10 HP motors):

Feeder OCPD ≤ largest branch-circuit OCPD + other FLCs = 90 A (25 HP breaker) + 14 A (10 HP FLC) = 104 A

Select a **100 A** OCPD (next standard size at or below 104 A). This must also not exceed the panel's marked SCCR.

---

## Art 409 and UL 508A — the relationship

Art 409 is a **code requirement** — the law that governs how ICPs must be built and marked. UL 508A is a **product standard** — the engineering criteria that define what an ICP must do to be listed and marked with the UL 508A mark.

| | NEC Article 409 | UL 508A |
|---|---|---|
| Type | Legally adopted code (NFPA 70) | Product listing standard (UL) |
| Enforced by | AHJ (Authority Having Jurisdiction) | UL field inspection or third-party listing |
| Scope | Minimum installation and marking requirements | Engineering design criteria for component ratings, wiring, SCCR determination |
| SCCR | Requires marking; does not specify how to calculate | Provides SCCR determination procedures (Supplement SB) |
| Relationship | References listed equipment | A panel listed to UL 508A satisfies Art 409 marking requirements |

In practice: a panel built and listed to UL 508A will meet Art 409 requirements because the listing process verifies the SCCR, markings, and component ratings. A custom panel built without a UL 508A listing must still comply with Art 409; the builder must independently document SCCR and ensure all required markings are present.

Most industrial panel shops build to UL 508A as a matter of standard practice because customers, ECs, and AHJs expect the listing mark. The UL 508A listing mark on the enclosure is de facto evidence of Art 409 compliance.

---

## ICP (Art 409) vs. MCC (Art 430 Part F)

A Motor Control Center (MCC) looks similar to an ICP but is governed by a different part of Article 430.

| Feature | ICP — Art 409 | MCC — Art 430 Part F |
|---|---|---|
| Primary article | Art 409 | Art 430 Part F (430.92–430.98) |
| Listing standard | UL 508A | UL 845 |
| Contents | General power and control components | Motor branch circuits with individual starters in plug-in buckets |
| SCCR marking | Art 409.110 | Art 430.98 |
| Typical use | Machine control panels, PLC panels, custom assemblies | Centralized motor control for multiple motors in a plant |
| Supply conductor sizing | Art 409.20 | Art 430.24 (feeder) + Art 430.62 (OCPD) |

The key practical difference: an MCC is a standardized product with plug-in starter buckets and a defined bus structure. An ICP is a custom-assembled panel. Both require SCCR marking and supply conductor sizing, but the applicable article and listing standard differ.

---

## Art 409 pre-shipment inspection checklist

Before releasing an ICP for shipment, verify the following:

- [ ] Enclosure nameplate is attached and legible
- [ ] Nameplate includes: manufacturer name or mark
- [ ] Nameplate includes: supply voltage, phases, and frequency
- [ ] Nameplate includes: full-load current (FLC) of the panel
- [ ] Nameplate includes: short-circuit current rating (SCCR) in amperes RMS symmetrical
- [ ] Nameplate includes: enclosure type designation (NEMA or IEC)
- [ ] SCCR has been calculated and documented (UL 508A Supplement SB or equivalent)
- [ ] All components used in the SCCR calculation are installed as specified (fuse type and rating, breaker series rating, etc.)
- [ ] Supply conductor size is documented and meets Art 409.20
- [ ] Internal wiring complete: power and control separated per Art 725.136 (Class 2 separation maintained)
- [ ] Wire labels and terminal markings match the drawings shipped with the panel
- [ ] All unused knockouts are closed
- [ ] Door interlock (if specified) is functional
- [ ] Grounding and bonding: equipment grounding bar connected, EGC terminal labeled
- [ ] Drawings revision is current and matches as-built panel

---

## Practical takeaway

Article 409 governs the ICP as an assembly. The three most important compliance points are:

1. **SCCR marking** — required on the enclosure; must be verified against available fault current at installation.
2. **Supply conductor sizing** — Art 409.20 formula (125 % largest motor + 100 % others + 125 % resistance heating).
3. **Markings** — voltage, phases, frequency, FLC, SCCR, and enclosure type must all appear on the nameplate.

UL 508A listing is the standard industry method for satisfying Art 409 requirements. The listing process validates SCCR and required markings, giving the installer and AHJ confidence in the panel design.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/nec-application/article-430-workflow/' | relative_url }}">&larr; Practical Article 430 Workflow</a>
  <a href="{{ '/training/nec-application/' | relative_url }}">↑ NEC for Machines and Panels</a>
  <span></span>
</div>
