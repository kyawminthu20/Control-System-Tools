---
layout: default
title: "IEC 60079 — Explosive Atmospheres"
description: "IEC 60079 series: equipment marking, protection methods (Ex d/i/e/p), area classification, installation, and inspection for hazardous areas."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Hazardous Area"
    url: "/standards/hazardous-area/"
  - name: "IEC 60079"
related_standards:
  - name: "NEC (Art. 500–505)"
    url: "/standards/us-electrical/nec/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
last_reviewed: "2026-03-08"
---

<div class="page-header">
  <span class="page-header__label">International · Hazardous Area</span>
  <h1>IEC 60079 — Explosive Atmospheres</h1>
</div>

<span class="badge badge--complete">Phase 10 Complete</span>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | IEC 60079 series |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Scope** | Electrical equipment and installations in explosive atmospheres |
| **Corpus** | 6 parts — general requirements, Ex d, area classification, IS (Ex i), installation, inspection |

---

## Equipment Marking System

All Ex equipment carries a marking string. Example: **`Ex d IIB T4 Gb`**

| Element | Meaning |
|---------|---------|
| `Ex` | Certified for explosive atmospheres |
| `d` | Protection method: flameproof enclosure |
| `IIB` | Gas group: ethylene and similar (IIA < IIB < IIC) |
| `T4` | Max surface temperature: 135°C |
| `Gb` | Equipment Protection Level: Zone 1 |

**EPL → Zone mapping:**

| EPL | Zone | Protection level |
|-----|------|-----------------|
| Ga | Zone 0 | Highest — two independent faults |
| Gb | Zone 1 | High — one fault tolerance |
| Gc | Zone 2 | Enhanced — normal operation |

---

## Zone Classification

Zones are determined per **IEC 60079-10-1** based on release grade and ventilation:

| Zone | Condition |
|------|-----------|
| Zone 0 | Explosive atmosphere continuously present |
| Zone 1 | Explosive atmosphere likely in normal operation |
| Zone 2 | Explosive atmosphere unlikely; brief if present |

A classified area drawing documenting zone extents, gas groups, and T-codes is required.

---

## Protection Methods

| Method | Code | Standard | Zone | Principle |
|--------|------|----------|------|-----------|
| Flameproof enclosure | Ex d | IEC 60079-1 | 1, 2 | Contains internal explosion; quenches escaping gases |
| Intrinsic safety | Ex ia/ib/ic | IEC 60079-11 | 0/1/2 | Limits energy below ignition threshold |
| Increased safety | Ex e | IEC 60079-7 | 1, 2 | Prevents sparks and excess temperature |
| Purged/pressurized | Ex p | IEC 60079-2 | 1, 2 | Maintains positive pressure to exclude atmosphere |
| Encapsulation | Ex m | IEC 60079-18 | 1, 2 | Encapsulates components in compound |
| Non-sparking | Ex nA | IEC 60079-15 | 2 only | Cannot ignite in normal operation |

---

## Intrinsic Safety Quick Reference

IS is the standard approach for process instruments. Key points:

- **Zener barriers** — require IS earth ≤1 Ω; low cost; widely used
- **Galvanic isolators** — no IS earth required; provides isolation; use in floating systems
- **Entity check:** Uo ≤ Ui, Io ≤ Ii, Ci + Ccable ≤ Co, Li + Lcable ≤ Lo

---

## Relationship to NEC

| NEC Article | IEC 60079 Relationship |
|-------------|----------------------|
| Art. 500–503 | Class/Division system — parallel US approach |
| Art. 504 | IS system aligns with IEC 60079-11 |
| Art. 505 | Zone system directly references IEC 60079 equipment certification |

ATEX/IECEx certified equipment is generally accepted in NEC Art. 505 Zone installations — verify with AHJ.

---

## Installation and Inspection Checklist

- [ ] Area classification drawing current and signed
- [ ] Equipment EPL matches zone (Ga→Zone 0, Gb→Zone 1, Gc→Zone 2)
- [ ] Gas group rating ≥ hazardous substance group
- [ ] T-code max surface temp < substance autoignition temp (with margin)
- [ ] Certificate valid — check IECEx/ATEX database, not just nameplate
- [ ] Cable glands Ex-certified and correct type for enclosure and gas group
- [ ] IS earth resistance ≤1 Ω (for zener barrier installations)
- [ ] Entity parameters verified for all IS loops (Ci + Ccable ≤ Co, etc.)
- [ ] Equipotential bonding verified
- [ ] Inspection records current (IEC 60079-17 schedule)

---

<a href="{{ '/standards/hazardous-area/' | relative_url }}" class="card__link">&larr; Hazardous area family</a>
