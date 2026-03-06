---
layout: default
title: "International Machinery Standards"
description: "IEC 60204-1 and related international machinery standards for CE marking and global machine design."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "International Machinery"
repo_path: "control-standards/rag/standards_intelligence/international/machinery/"
related_standards:
  - name: "NFPA 79 (US equivalent)"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "ISO 12100 (Risk assessment)"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1 (Safety functions)"
    url: "/standards/functional-safety/iso-13849-1/"
crosswalk_refs:
  - name: "NFPA 79 ↔ IEC 60204-1 Crosswalk"
    url: "/crosswalks/nfpa79-iec60204/"
---

<div class="page-header">
  <span class="page-header__label">International Machinery Standards Family</span>
  <h1>IEC 60204-1 and International Machinery Standards</h1>
  <p>Standards for electrical equipment of machines intended for CE marking or global markets.</p>
</div>

## Standards in This Family

| Standard | Edition | Scope | Status |
|----------|---------|-------|--------|
| [IEC 60204-1]({{ '/standards/machinery/iec-60204-1/' | relative_url }}) | 2018 | Electrical equipment of machines | Complete |
| ISO 12100 | 2010 | Risk assessment foundation | See [Functional Safety]({{ '/standards/functional-safety/' | relative_url }}) |
| ISO 13849-1 | 2023 | Safety-related control systems (PL) | See [Functional Safety]({{ '/standards/functional-safety/' | relative_url }}) |
| IEC 62061 | 2021 | Safety-related control systems (SIL) | See [Functional Safety]({{ '/standards/functional-safety/' | relative_url }}) |

---

## CE Marking Foundation

For EU/CE-marked machinery, the minimum starting set is:

1. **ISO 12100** — Risk assessment (required as foundation)
2. **IEC 60204-1** — Electrical equipment requirements
3. **ISO 13849-1** or **IEC 62061** — If safety functions are present

**Machinery Directive (2006/42/EC)** requires this foundation. ISO 12100 is harmonized under the directive as a Type A standard.

---

## IEC 60204-1 vs NFPA 79

IEC 60204-1 and NFPA 79 are broadly equivalent in technical scope but differ in structure and some requirements:

| Aspect | IEC 60204-1 | NFPA 79 |
|--------|-------------|---------|
| Market | Global / EU | United States |
| Voltage reference | 1000 V AC / 1500 V DC | 600 V |
| Neutral conductor | Explicit N treatment | Less explicit |
| Documentation | Clause 17 (detailed) | Chapter 19 |
| Colors | Yellow-green PE required | Green or bare allowed |

<a href="{{ '/crosswalks/nfpa79-iec60204/' | relative_url }}" class="card__link">View full NFPA 79 ↔ IEC 60204-1 crosswalk &rarr;</a>
