---
layout: default
title: "IEC 60079 — Explosive Atmospheres"
description: "IEC 60079 series: marking, area classification, Ex d / Ex i protection methods, installation and inspection — Quick Start, per-part depth, worked IS-loop entity check, common mistakes."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Hazardous Area"
    url: "/standards/hazardous-area/"
  - name: "IEC 60079"
repo_path: "control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/"
related_standards:
  - name: "NEC (Art. 500–505)"
    url: "/standards/us-electrical/nec/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
crosswalk_refs:
  - name: "IEC 60079 ↔ NEC Art. 500–505"
    url: "/tools/crosswalks/iec60079-nec-500-505/"
last_reviewed: "2026-05-06"
---

<div class="page-header">
  <span class="page-header__label">International · Hazardous Area</span>
  <h1>IEC 60079 — Explosive Atmospheres</h1>
</div>

## Quick Start

- **Where IEC 60079 applies vs. NEC Class/Division.** IEC 60079 uses the **Zone** system (Zone 0/1/2 for gas, Zone 20/21/22 for dust). The US has two parallel systems: NEC Articles 500–503 (Class/Division — older), and NEC Articles 504–505 (which import IEC 60079 directly). For greenfield US projects, NEC Article 505 (Zone) is increasingly preferred and accepts IECEx/ATEX-certified equipment.
- **What the marking string actually tells you.** A label like `Ex ia IIB T4 Gb` encodes everything needed for selection: protection method (`ia` = intrinsic safety, two-fault tolerant), gas group (`IIB`, suitable for ethylene, hydrogen sulfide), max surface temperature (`T4` = 135 °C), and Equipment Protection Level (`Gb` = Zone 1). Read the marking before reading the certificate.
- **Why area classification (60079-10-1) drives everything.** Every other decision — equipment selection, cable type, bonding scheme, inspection schedule — flows from the Zone determination. A wrong area drawing means every downstream choice is wrong. This is non-trivial work and typically requires a competent process-safety engineer, not a control engineer working solo.
- **When intrinsic safety is the right choice.** IS is the default for field instrumentation (transmitters, sensors, flow meters, level switches) because it allows live calibration and maintenance in Zone 0/1 without de-energising. Choose Ex d (flameproof) when the equipment must contain internal sparking sources at higher power — motors, large solenoid valves, big terminal boxes.
- **What the certificate says vs. what the nameplate says.** Certificates can be **withdrawn** by the certifying body without recall of equipment in the field. Nameplates persist regardless. Always verify against the **IECEx online certificate database** or the relevant ATEX notified-body record — particularly during initial inspection (60079-14) and on incident investigation.

---

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard family** | IEC 60079 series |
| **Editions in corpus** | 2011 – 2017 (per part) |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Scope** | Electrical equipment and installations in explosive atmospheres |
| **Repository** | `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/` — 6 parts |
| **Status in corpus** | Core parts complete; non-core parts gap-flagged below |

---

## Equipment Marking System

All Ex equipment carries a marking string defined in IEC 60079-0:

```
Ex [protection method(s)] [gas group] T[temp class] [EPL]
```

**Example:** `Ex d IIB T4 Gb`

| Element | Meaning |
|---------|---------|
| `Ex` | Certified for explosive atmospheres |
| `d` | Protection method — flameproof enclosure (one of several; see below) |
| `IIB` | Gas group — ethylene and similar (IIA &lt; IIB &lt; IIC by hazard) |
| `T4` | Max surface temperature 135 °C (T1 highest = 450 °C, T6 lowest = 85 °C) |
| `Gb` | Equipment Protection Level — Zone 1 |

Multiple protection methods may appear in one marking — for example `Ex de IIC T5 Gc` for a flameproof + increased-safety combination.

### EPL → Zone mapping

| EPL (gas) | Zone | Protection level |
|-----------|------|------------------|
| **Ga** | Zone 0 | Highest — safe with two independent faults |
| **Gb** | Zone 1 | High — safe with one fault |
| **Gc** | Zone 2 | Enhanced — safe in normal operation |
| Da / Db / Dc | Zone 20 / 21 / 22 | Equivalent for dust atmospheres |

### Gas groups

| Group | Hazard | Typical gases |
|-------|--------|---------------|
| **IIA** | Lowest | Propane, methane, acetone |
| **IIB** | Intermediate | Ethylene, hydrogen sulfide |
| **IIC** | Highest | Hydrogen, acetylene |

Equipment marked **IIC** is suitable for any gas group (it satisfies the most demanding case). Equipment marked **IIA** is only suitable for IIA gases — using it in IIB or IIC atmospheres is non-compliant.

### Temperature classes

| T-code | Max surface temp | Notes |
|--------|------------------|-------|
| T1 | 450 °C | Very high autoignition gases only |
| T2 | 300 °C | |
| T3 | 200 °C | Kerosene, fuel oil |
| T4 | 135 °C | Most common in process industry |
| T5 | 100 °C | Carbon disulfide (rare) |
| T6 | 85 °C | Diethyl ether |

**Rule.** Select equipment whose T-code maximum surface temperature is **below the autoignition temperature** of the substance at the installation. Best practice keeps a margin of at least **50 °C** below autoignition.

---

## Corpus Coverage

The reference library carries six core parts of the IEC 60079 series — the parts most-consulted by control and process-safety engineers. Other parts of the family are referenced in equipment markings but not held in depth.

| Part | Title | Corpus |
|------|-------|--------|
| **60079-0** | General requirements (marking, EPL, gas groups, T-codes) | ✓ |
| **60079-1** | Flameproof enclosures (Ex d) | ✓ |
| 60079-2 | Pressurization (Ex p) | <span class="badge badge--gap">Not in corpus</span> |
| 60079-7 | Increased safety (Ex e) | <span class="badge badge--gap">Not in corpus</span> |
| **60079-10-1** | Area classification — gas | ✓ |
| 60079-10-2 | Area classification — dust | <span class="badge badge--gap">Planned</span> |
| **60079-11** | Intrinsic safety (Ex i) | ✓ |
| **60079-14** | Installation design and erection | ✓ |
| 60079-15 | Non-sparking (Ex nA) | <span class="badge badge--gap">Not in corpus</span> |
| **60079-17** | Inspection and maintenance | ✓ |
| 60079-18 | Encapsulation (Ex m) | <span class="badge badge--gap">Planned</span> |
| 60079-31 | Dust ignition protection by enclosure (Ex t) | <span class="badge badge--gap">Planned</span> |

**For Ex e and Ex p installations**, refer to the IEC 60079-7 and 60079-2 standards directly — this site does not yet hold detailed application guidance for those protection methods.

---

## Per-Part Depth

### 60079-0 — General Requirements

The general requirements part defines the marking system, Equipment Protection Levels (EPLs), gas groups, temperature classes, and the certification schemes that all other parts inherit. ATEX (EU) and IECEx (international) certification cover most equipment; the schemes are mutually recognised in many jurisdictions, and equipment carrying both marks is common. NEC Article 505 (US Zone system) accepts IECEx/ATEX-certified equipment for Zone installations — verify with the local AHJ.

The **margin rule** is the most-applied piece of this part: pick a T-code whose max surface temperature is below the substance autoignition temperature, with at least a 50 °C margin. For ethylene (autoignition ~425 °C), T2 (300 °C) is the warmest acceptable equipment; cooler classes (T3, T4, T5, T6) are progressively more conservative.

### 60079-10-1 — Area Classification (Gas)

Area classification establishes which Zones exist, where they extend, and what gas group applies. Without it, no other selection decision can be made correctly.

| Zone | Condition | Typical examples |
|------|-----------|------------------|
| **Zone 0** | Explosive atmosphere present continuously or for long periods | Inside storage tanks; vapour space above process liquid |
| **Zone 1** | Explosive atmosphere likely in normal operation | Within ~1.5 m of a Zone 0 opening; pump-seal areas; compressor rooms |
| **Zone 2** | Explosive atmosphere unlikely in normal operation; if present, only briefly | Within ~3 m of a Zone 1 boundary; flanged-joint vicinity; analyser buildings |

**Release grades** — from each release source, an atmosphere may be:
- **Continuous** (drives Zone 0),
- **Primary** (likely periodic — typically Zone 1),
- **Secondary** (unlikely — typically Zone 2).

Multiple release sources can overlap, expanding zones or escalating their severity. **Ventilation grade** modifies the result: poor ventilation can convert a Zone 2 source into Zone 1, or extend Zone boundaries.

The classified-area drawing is the deliverable: Zone extents (plan and elevation), gas group(s), substance autoignition temperature, basis for classification, and revision history. It is required for the initial commissioning inspection (60079-14) and for periodic inspections (60079-17) — losing or failing to maintain it is a common compliance failure.

### 60079-1 — Flameproof Enclosures (Ex d)

Ex d is the workhorse for **higher-power equipment with internal sparking** — motors, large solenoid valves, junction boxes with switching contacts. The principle is fundamentally different from intrinsic safety: Ex d allows internal ignition to occur, then **contains** it. The enclosure withstands the explosion and **quenches** escaping gases through precision-machined flame paths (gap × length) so the gas cools below its autoignition temperature before reaching the outside atmosphere.

The flame path is the joint surface between mating parts of the enclosure. Three rules govern it:

1. **Gap width** — must not exceed the maximum allowed for the gas group. IIC (hydrogen) demands the tightest tolerances; IIA the most generous.
2. **Flame path length** — the minimum length to quench the flame before it reaches the atmosphere.
3. **Surface finish** — flame paths must be machined metal-to-metal. **Never apply paint, thread sealant, anti-seize, or any other coating to flame path surfaces** — this changes the effective gap and invalidates the certification.

All openings in an Ex d enclosure must be sealed using either an **Ex d certified cable gland** (with integral flame path), an **Ex d certified stopping plug** for unused entries, or — in NEC conduit installations — a threaded conduit with a sealing fitting filled with sealing compound. Standard industrial cable glands are not Ex d rated.

**Live work caution.** Ex d covers must not be opened in a hazardous atmosphere while energised. De-energise first, and allow cooling before opening if the equipment generates internal heat.

### 60079-11 — Intrinsic Safety (Ex i)

Intrinsic safety prevents ignition by **limiting the electrical energy** in the hazardous-area circuit below the threshold required to ignite the gas. Unlike Ex d, IS allows live calibration and maintenance — the energy is too low to cause an ignition in the first place. This makes IS the default choice for field instrumentation.

| Level | Zone | Fault tolerance | Typical use |
|-------|------|-----------------|-------------|
| **ia** | Zone 0, 1, 2 | Two-fault — safe under any two component failures | Most process instruments |
| **ib** | Zone 1, 2 | One-fault | Less critical instruments |
| **ic** | Zone 2 only | No fault tolerance — safe in normal operation | Zone 2 only |

The **associated apparatus** in the safe area enforces the energy limits. Two types:

- **Zener (shunt) barrier** — Zener diodes clamp voltage; a fuse limits current; a resistor limits energy. Low cost, widely used. **Requires an intrinsically safe earth (ISE) of ≤1 Ω** to a known clean earth.
- **Galvanic isolator** — transformer or optical coupling provides full electrical isolation between safe and hazardous sides. No ISE required, supports floating field devices, but costs more and consumes more loop power.

**Entity concept.** IS lets you mix certified components from different manufacturers as long as the entity parameters are compatible. The barrier exposes:

- **Uo** — max open-circuit voltage,
- **Io** — max short-circuit current,
- **Po** — max output power,
- **Co** — max external capacitance the barrier can drive safely,
- **Lo** — max external inductance the barrier can drive safely.

The field device exposes the matching internal parameters: **Ui, Ii, Pi, Ci, Li**.

**Compatibility checks:**

```
Uo ≤ Ui      Io ≤ Ii      Po ≤ Pi
Ci + Ccable ≤ Co        Li + Lcable ≤ Lo
```

Cable capacitance (typically a few hundred pF/m) and inductance (typically under 1 µH/m) must be added to the field device's internal values before the comparison.

**FISCO** (Fieldbus Intrinsically Safe Concept) extends this to FOUNDATION Fieldbus and PROFIBUS PA installations — multiple field devices on one IS segment fed by a single FISCO-certified power conditioner, eliminating per-device entity calculation on that segment.

### 60079-14 — Installation Design

A correctly certified piece of equipment installed incorrectly loses its protection. Part -14 governs how Ex equipment is wired, connected, and commissioned.

**Equipment selection check** (perform on every item):

1. EPL matches the Zone (Ga ≥ Zone 0; Gb ≥ Zone 1; Gc ≥ Zone 2).
2. Gas group rating matches or exceeds the substance group (IIC equipment satisfies any gas group).
3. T-code max surface temperature is below the substance autoignition temperature with the 50 °C margin.
4. Certificate is valid (not withdrawn) — verify against the IECEx database or ATEX notified-body record.

**Cable selection.** Armoured cable (SWA/AWA) is typical for general Ex wiring; mineral-insulated cable is used for high-temperature or fire-survival circuits; screened instrumentation cable is used for IS, with the **screen earthed at one point only** (typically the safe-area side) to avoid earth loops.

**Cable segregation.** IS wiring must be physically separated from non-IS wiring — different conduits, different trays, or a metallic barrier. Mixing the two in a multicore cable or a shared tray can inject energy into the IS circuit that exceeds entity-parameter limits, defeating the protection.

**Equipotential bonding.** All metallic structures in the hazardous area connect to a single bonding network — vessels, pipework, steelwork, cable trays, equipment enclosures. Bonding resistance between any two bonded points should be **&lt;10 Ω** (many sites require **&lt;1 Ω** for critical systems). The IS earth (zener-barrier installations) is a dedicated **≤1 Ω** bond to a known clean earth, separate from the general protective earth.

**Initial verification before energising.** Equipment certificates verified, glands and stopping plugs in place, flame paths undamaged (Ex d) or entity parameters within limits (Ex i), bonding continuity verified, classified-area drawing matches installed equipment. A **commissioning certificate** is issued at completion — required by 60079-14.

### 60079-17 — Inspection and Maintenance

Hazardous-area equipment degrades over time — flame paths corrode, cable glands loosen, IS earth resistance drifts, equipment is modified without re-certification. Part -17 defines the inspection regime that keeps an installation compliant between commissioning and decommissioning.

| Grade | Scope | Typical frequency |
|-------|-------|-------------------|
| **Visual** | External condition — damage, corrosion, nameplate legibility, gland tightness | Continuous to monthly |
| **Close** | Visual checks plus covers removed to verify flame paths, IS parameters, internal connections | Annually |
| **Detailed** | Close checks plus full re-verification against current certificate, dimensional checks, entity recalculation | Every 3–5 years; after incidents |

**Competent person** — inspections must be performed by someone with documented knowledge of the protection methods present, the applicable installation standards, the hazardous substances, and practical experience. National schemes (CompEx in the UK, EEHA in Australia, equivalents elsewhere) document the qualification.

Common findings classified as **immediate hazard** that take equipment out of service immediately: non-certified cable gland in use, modified enclosure with extra holes, corroded flame path with gap out of tolerance, withdrawn certificate. Records of every inspection — date, inspector qualification, grade applied, findings, actions, next due date — are required for regulatory audits, insurance reviews, and incident investigation.

---

## Worked Example — IS Loop Entity Check

**Scenario.** A 4–20 mA pressure transmitter on an ethylene tank, classified **Zone 1, gas group IIB**, with the area drawing requiring at least **T3 equipment** (substance autoignition margin). The transmitter is wired through a 100 m armoured screened twisted-pair cable to a zener barrier in the safe-area control room.

**Selected components.**

| Component | Marking | Entity parameters |
|-----------|---------|-------------------|
| Field transmitter | `Ex ia IIB T4 Gb` | Ui = 30 V, Ii = 100 mA, Ci = 15 nF, Li = 50 µH |
| Zener barrier (associated apparatus) | `[Ex ia] IIC` | Uo = 28 V, Io = 93 mA, Co = 83 nF, Lo = 5.7 mH |
| Cable (100 m) | Standard IS-rated screened TP | 200 pF/m, 0.7 µH/m |

**Step 1 — marking compatibility.**
- Field equipment is `IIB` — matches the area's IIB gas group. ✓
- `T4` (135 °C max surface) is colder than the area's `T3` minimum (200 °C max). T4 satisfies T3. ✓
- `Gb` matches Zone 1. ✓

**Step 2 — cable contribution.**
- Ccable = 100 m × 200 pF/m = **20 nF**
- Lcable = 100 m × 0.7 µH/m = **70 µH**

**Step 3 — entity checks.**

| Check | Calculation | Result |
|-------|-------------|--------|
| Uo ≤ Ui | 28 V ≤ 30 V | ✓ |
| Io ≤ Ii | 93 mA ≤ 100 mA | ✓ |
| Ci + Ccable ≤ Co | 15 nF + 20 nF = **35 nF** ≤ 83 nF | ✓ |
| Li + Lcable ≤ Lo | 50 µH + 70 µH = **120 µH** ≤ 5 700 µH | ✓ |

All four entity checks pass. Po ≤ Pi must also be verified from the certificates (typically driven by the Uo×Io product). The barrier–transmitter–cable combination is a compliant IS loop.

**Step 4 — earthing.**
- Zener-barrier IS earth must measure **≤1 Ω** to a known clean earth — verify at commissioning and at every detailed inspection.
- Cable screen earthed **at one point only** — typically the safe-area side, at the barrier earth bus. Earthing both ends creates a current loop that can inject noise or, under fault, exceed the entity limits.

**Step 5 — documentation deliverables.**
- IS loop diagram showing barrier, cable run, field device, entity parameters, and the four compatibility checks.
- Certificate references for both the barrier and the field device (numbers and revisions; verified valid against the IECEx database at commissioning).
- Entry in the equipment register required by 60079-14.

---

## Common Mistakes

1. **Choosing equipment by gas-group letter alphabetically — "IIC must be best, pick that".** IIC equipment satisfies any gas group, but it is more expensive and Ex d / Ex e equipment in IIC has stricter installation requirements. Match the equipment group to the actual hazard. Specifying IIC where IIB suffices wastes budget and complicates installation.
2. **Trusting the nameplate without checking the certificate.** Certificates can be **withdrawn** by the certifying body without recall of installed equipment — the nameplate persists. Verify against the **IECEx online certificate database** or the relevant ATEX notified-body record at commissioning and during detailed inspections (60079-17).
3. **Mixing certified and uncertified components in an IS loop.** The entity-check math fails immediately if any uncertified component touches the loop — there are no entity parameters for an uncertified surge protector or terminal block. The whole loop becomes non-compliant.
4. **Routing IS and non-IS cables in the same multicore cable or shared tray without segregation.** Energy from the non-IS circuit can couple into the IS circuit and exceed the entity-parameter limits, defeating the protection. Per 60079-14, segregate physically — different conduits, different trays, or a grounded metallic barrier.
5. **Using zener barriers with inadequate IS earth (>1 Ω).** Zener barriers depend on a low-impedance path to clear faults. If the IS earth has drifted high (typical cause: corrosion at the bonding lug, undersized bonding conductor, or shared with a noisy supplementary earth), barriers behave unpredictably under fault. If the IS earth cannot be reliably maintained ≤1 Ω, switch to galvanic isolators.
6. **Field-modifying an Ex enclosure (extra cable entries, larger openings, drilled mounting holes) without re-certification.** The certificate covers the equipment **as built**. Any modification — even what seems harmless, like an extra cable gland hole — invalidates the certification. The corpus's `60079-17` inspection table classifies a modified enclosure as an **immediate hazard**: take it out of service, re-certify or replace.

---

## Practical Checklist

#### Area Classification

- [ ] Classified-area drawing current, signed, and matches the actual plant layout.
- [ ] Each release source documented with grade (continuous / primary / secondary) and ventilation assessment.
- [ ] Gas groups and substance autoignition temperatures listed on the drawing per Zone.
- [ ] Drawing accessible to operators, maintenance, and inspectors.

#### Equipment Selection

- [ ] EPL matches the Zone (Ga ≥ Zone 0; Gb ≥ Zone 1; Gc ≥ Zone 2).
- [ ] Gas group rating ≥ substance gas group.
- [ ] T-code max surface temperature < substance autoignition temperature, with ≥ 50 °C margin.
- [ ] Certificate verified valid against the IECEx database / ATEX notified-body record (not just the nameplate).
- [ ] For IS loops: barrier and field device are entity-compatible (all four checks documented).

#### Installation (IEC 60079-14)

- [ ] Cable type appropriate for the protection method and entry (Ex d certified glands; IS cable screen earthed at one point only).
- [ ] IS and non-IS cables physically segregated (different conduits or trays, or grounded barrier).
- [ ] Equipotential bonding continuous; resistance &lt;10 Ω general / ≤1 Ω for IS earth on zener barriers.
- [ ] Flame paths on Ex d enclosures undamaged, unpainted, no thread sealant.
- [ ] Unused cable entries closed with Ex-certified stopping plugs (not standard plugs).
- [ ] Equipment register populated; IS loop documentation filed.
- [ ] Commissioning certificate issued at completion.

#### Periodic Inspection (IEC 60079-17)

- [ ] Inspection grade (visual / close / detailed) appropriate to risk and frequency.
- [ ] Inspector competency documented (CompEx, EEHA, or equivalent national scheme).
- [ ] Defects classified per 60079-17 severity scheme; immediate hazards taken out of service.
- [ ] IS earth resistance re-measured at detailed inspection (≤1 Ω).
- [ ] Records retained: date, inspector, grade, findings, actions, next due date.

---

## Lifecycle Application

| Stage | IEC 60079 activity |
|-------|-------------------|
| [Standards Selection]({{ '/lifecycle/standards-selection/' | relative_url }}) | Decide IEC 60079 (Zone) vs. NEC Art. 500 (Class/Division) for the project; identify substances and confirm gas groups; preliminary area classification feasibility |
| [Detailed Design]({{ '/lifecycle/detailed-design/' | relative_url }}) | Area classification drawing per 60079-10-1; protection-method choice per equipment (Ex d for sparking power devices, Ex i for instruments); IS loop entity calculations; cable and bonding scheme per 60079-14 |
| [Build]({{ '/lifecycle/build/' | relative_url }}) | Equipment register populated; certificates archived; cable glands, stopping plugs, and flame-path surfaces preserved; IS earth and equipotential bonding installed |
| [Installation]({{ '/lifecycle/installation/' | relative_url }}) | 60079-14 installation rules at the site; cable segregation enforced; bonding continuity verified; IS earth measured |
| [Pre-Commissioning]({{ '/lifecycle/pre-commissioning/' | relative_url }}) | Initial verification per 60079-14: certificate validity, gland integrity, flame-path condition, IS entity-check sign-off, classified-area drawing matches installed equipment |
| [Commissioning]({{ '/lifecycle/commissioning/' | relative_url }}) | Commissioning certificate issued; first periodic-inspection schedule defined per 60079-17 (visual / close / detailed) and competent person assigned |

---

## Relationship to NEC

NEC has two parallel approaches to hazardous areas — IEC 60079 maps to one, parallels the other.

| NEC Article | Scope | Relationship to IEC 60079 |
|-------------|-------|---------------------------|
| Art. 500–503 | Class / Division system (older US approach) | Parallel methodology — see the [IEC 60079 ↔ NEC Art. 500–505 crosswalk]({{ '/tools/crosswalks/iec60079-nec-500-505/' | relative_url }}) for equipment-level mapping |
| Art. 504 | Intrinsically safe systems | Aligns with IEC 60079-11; entity concept, IS earth requirement, and cable segregation map directly |
| Art. 505 | Zone classification system | Imports IEC 60079 directly; ATEX/IECEx-certified equipment generally accepted by AHJ |

For a US installation choosing between paths, Art. 505 (Zone) is increasingly preferred for greenfield work; existing facilities often run mixed Art. 500 and Art. 505 sections.

---

## Related Standards

- [NEC]({{ '/standards/us-electrical/nec/' | relative_url }}) — Articles 500–505 cover US hazardous-area requirements
- [IEC 61511]({{ '/standards/functional-safety/iec-61511/' | relative_url }}) — Process-sector functional safety; safety instrumented functions in hazardous areas
- [IEC 60079 ↔ NEC Art. 500–505 crosswalk]({{ '/tools/crosswalks/iec60079-nec-500-505/' | relative_url }})

<a href="{{ '/standards/hazardous-area/' | relative_url }}" class="card__link">&larr; Hazardous area family</a>
