---
layout: default
title: "IEC 60079 ↔ NEC Art. 500/505 Crosswalk"
description: "Zone vs. Division: how IEC 60079 hazardous-area classification aligns with NEC Article 500 (Division) and Article 505 (Zone) for US installations."
breadcrumb:
  - name: "Crosswalks"
    url: "/crosswalks/"
  - name: "IEC 60079 ↔ NEC 500/505"
related_standards:
  - name: "IEC 60079"
    url: "/standards/hazardous-area/iec-60079/"
  - name: "NEC (Art. 500–505)"
    url: "/standards/us-electrical/nec/"
---

<div class="page-header">
  <span class="page-header__label">Crosswalk</span>
  <h1>IEC 60079 ↔ NEC Art. 500/505</h1>
  <p>Zone vs. Division classification for hazardous areas — how international IEC 60079 practice aligns with the US Division system (Art. 500) and the US Zone system (Art. 505).</p>
</div>

## Purpose

IEC 60079 defines the **Zone classification system** used internationally under IECEx and ATEX certification schemes. NEC Article 500 defines the traditional **Division classification system** long used in North America. NEC Article 505, added to bring US practice into alignment with IEC, introduced the Zone system into US installations — enabling IECEx/ATEX-certified equipment to be used legally in US hazardous areas without re-certification.

Both Art. 500 (Division) and Art. 505 (Zone) are legally valid in the US. The engineer of record or the Authority Having Jurisdiction (AHJ) selects which system governs a given installation. Mixing both systems within a single classified area is generally not permitted without explicit AHJ approval.

**Strategy:** For new US projects involving IECEx/ATEX-certified equipment, Art. 505 (Zone) typically provides a cleaner path. For existing US plants already classified under Division, maintaining Division consistency is usually preferred.

---

## Classification System Comparison

### Gas and Vapor (IEC 60079-10-1 vs. NEC)

| Zone (IEC / Art. 505) | Division (Art. 500) | Description |
|-----------------------|---------------------|-------------|
| Zone 0 | — (no Division 0) | Explosive atmosphere present continuously or for long periods — inside tanks, vessels, pipes |
| Zone 1 | Division 1 | Likely to occur during normal operation |
| Zone 2 | Division 2 | Not likely in normal operation; only under abnormal or fault conditions |

**Key relationship:** Division 1 encompasses both Zone 0 and Zone 1 — it is the broader category. Division 2 is roughly equivalent to Zone 2. Because Division 1 includes the continuously-hazardous Zone 0 condition, equipment rated only for Zone 1 is **not** automatically acceptable for a Division 1 area without further verification.

### Dust (IEC 60079-10-2 vs. NEC Class II)

| Zone (IEC) | NEC Approximate Equivalent | Description |
|------------|---------------------------|-------------|
| Zone 20 | Class II, Division 1 (continuously present) | Combustible dust cloud present continuously or frequently |
| Zone 21 | Class II, Division 1 | Likely to occur during normal operation |
| Zone 22 | Class II, Division 2 | Unlikely under normal operation; fault conditions only |

NEC Class III (ignitable fibers/flyings) has no direct Zone equivalent in IEC 60079 — fibers are addressed separately and are not classified into the Zone 20/21/22 system.

---

## Equipment Classification Comparison

### IEC 60079 / ATEX / IECEx Equipment Protection Levels (EPL)

| EPL (Gas) | EPL (Dust) | Applicable Zone | Protection Concept |
|-----------|------------|-----------------|-------------------|
| Ga | Da | Zone 0 / Zone 20 | Very high protection — two independent means of protection |
| Gb | Db | Zone 1 / Zone 21 | High protection — suitable for normal operation |
| Gc | Dc | Zone 2 / Zone 22 | Enhanced protection — suitable for fault-condition-only zones |

### NEC Class / Group / Division System

NEC classifies hazardous locations by:
- **Class:** Class I (flammable gases/vapors), Class II (combustible dusts), Class III (ignitable fibers)
- **Division:** Division 1 (likely present) or Division 2 (unlikely under normal operation)
- **Group:** Subclassification by gas or dust properties (A, B, C, D for Class I; E, F, G for Class II)

### Gas Group Comparison

| IEC Gas Group | NEC Group | Representative Gases |
|---------------|-----------|---------------------|
| IIC | A + B | Hydrogen (Group B), acetylene (Group A) |
| IIB | C | Ethylene |
| IIA | D | Propane, methane, butane |

IEC IIC is the most stringent group (lowest MESG / highest MIC ratio). NEC splits IIC into two groups (A and B), making the NEC system slightly more granular at the high end. An IIC-rated product covers NEC Groups A, B, C, and D.

---

## Equipment Marking Comparison

**IEC / ATEX example marking:**

```
Ex d IIB T4 Gb
```

| Component | Meaning |
|-----------|---------|
| `Ex` | Certified for explosive atmosphere use |
| `d` | Protection type: Flameproof (contains internal explosion) |
| `IIB` | Gas group IIB (ethylene and less severe) |
| `T4` | Temperature class — max surface temp 135°C |
| `Gb` | Equipment Protection Level — Zone 1 gas application |

**NEC Division example marking:**

```
CL I, Div 1, Grp C, T4
```

| Component | Meaning |
|-----------|---------|
| `CL I` | Class I — flammable gas or vapor |
| `Div 1` | Division 1 — likely present under normal operation |
| `Grp C` | Group C — ethylene (equivalent to IEC IIB) |
| `T4` | Temperature class — max surface temp 135°C |

The T-code numbering system is shared between IEC and NEC, making temperature class the most directly portable element between the two marking systems.

---

## Temperature Classification

| T-Code | Max Surface Temperature | Notes |
|--------|------------------------|-------|
| T1 | 450°C | — |
| T2 | 300°C | — |
| T3 | 200°C | — |
| T4 | 135°C | Common for hydrogen sulfide, most hydrocarbons |
| T5 | 100°C | — |
| T6 | 85°C | Carbon disulfide |

Equipment must be selected with a T-code that stays **below the auto-ignition temperature** of the specific flammable substance present. When the auto-ignition temperature is not precisely known, use the most conservative (lowest) applicable T-code.

---

## Protection Types: IEC 60079 vs. NEC Equivalents

| IEC Protection Type | IEC Code | NEC Equivalent | Description |
|--------------------|----------|----------------|-------------|
| Flameproof | Ex d | Explosionproof (XP) | Enclosure contains internal ignition; joints allow pressure relief without propagation |
| Intrinsic Safety | Ex ia / Ex ib | IS — NEC Art. 504 | Limits electrical energy below ignition threshold under fault conditions |
| Increased Safety | Ex e | — (no NEC equivalent) | Eliminates potential ignition sources; avoids sparking by design |
| Pressurized | Ex p | Purged/Pressurized — NEC Art. 500, Type X/Y/Z | Dilutes or purges enclosure atmosphere; maintains positive pressure |
| Non-sparking | Ex nA | — (no direct NEC equivalent) | Zone 2 / Division 2 only; contacts that do not spark under normal operation |
| Encapsulation | Ex m | — (no direct NEC equivalent) | Potted/encapsulated to exclude atmosphere |

**Note on Ex ia vs. Ex ib:** Ex ia (two-fault safe) is approved for Zone 0; Ex ib (one-fault safe) is approved for Zone 1. NEC Art. 504 does not make this distinction explicitly — US IS installations should confirm EPL compatibility when using IECEx-marked IS equipment.

---

## Installation Rules

**IEC Zone installations** are governed by:
- IEC 60079-14 — Electrical installations design, selection, and erection
- IEC 60079-17 — Inspection and maintenance of electrical installations

**US Zone installations (Art. 505):** NEC Article 505 governs Zone 0, 1, and 2 gas/vapor areas in the US. It specifically permits IECEx/ATEX-marked equipment and references IEC 60079-14 for installation practices.

**US Division installations (Art. 500–503):** NEC Articles 500–503 govern Class I/II/III Division 1 and 2 areas under the traditional system. Art. 504 covers IS circuits in both Zone and Division installations.

**Intrinsic safety segregation:** IEC 60079-14 requires physical separation of IS circuits from non-IS circuits in conduit, cable trays, and junction boxes. NEC Art. 504 has comparable requirements for IS wiring segregation in US installations. This is one area where both systems converge on the same physical installation practice.

---

## Selecting Zone vs. Division for a US Project

```text
Using ATEX/IECEx certified equipment from overseas?
  YES → Use NEC Art. 505 (Zone) — accepts IECEx/ATEX marking directly
  NO  → Either Division (Art. 500) or Zone (Art. 505) is acceptable

Existing plant already classified under Division?
  YES → Likely stay with Division to maintain consistency
        unless AHJ agrees to a managed mixed approach

New greenfield design with international equipment and IS field devices?
  YES → Zone (Art. 505 + Art. 504) is typically cleaner and avoids
        dual-marking or re-certification costs

AHJ primarily familiar with Division marking (common in US)?
  YES → Division approach reduces inspection friction
        and avoids misinterpretation of Zone markings
```

Neither system is inherently safer than the other — the hazardous-area boundary, physical segregation quality, and equipment maintenance regime matter more than which classification language is used.

---

## Corpus Status

| Topic | Standards | Corpus Status |
|-------|-----------|---------------|
| Zone classification (gas/vapor) | IEC 60079-10-1 | <span class="badge badge--complete">Complete</span> |
| Flameproof enclosures | IEC 60079-1 | <span class="badge badge--complete">Complete</span> |
| Intrinsic safety | IEC 60079-11 | <span class="badge badge--complete">Complete</span> |
| Installation — Zone system | IEC 60079-14 | <span class="badge badge--complete">Complete</span> |
| Inspection and maintenance | IEC 60079-17 | <span class="badge badge--complete">Complete</span> |
| US Division system | NEC Art. 500, 501, 502, 503, 504, 505 | <span class="badge badge--complete">Complete</span> |
| NEC Zone system | NEC Art. 505 (2023 ed.) | <span class="badge badge--complete">Complete</span> |
| Area classification (dust) | IEC 60079-10-2 | <span class="badge badge--verify">Not in corpus</span> |

---

## Practical Tip

For new US projects involving equipment carrying IECEx or ATEX markings, NEC Article 505 is the correct adoption path — it accepts IECEx/ATEX equipment certification directly, eliminating the need for separate UL-listed Division markings. For traditional US Division equipment (UL-listed, NEC-marked), Article 500 remains fully correct and widely understood by US inspectors and AHJs.

Both systems require the same physical installation discipline: proper conduit seals, IS circuit segregation, equipment maintenance intervals per IEC 60079-17 or NFPA equivalent, and documentation of the area classification drawing. The classification language differs; the underlying safety goal is identical.

<a href="{{ '/crosswalks/' | relative_url }}" class="card__link">&larr; All Crosswalks</a>
