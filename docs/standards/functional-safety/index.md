---
layout: default
title: "Functional Safety Standards"
description: "ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511 — risk assessment and safety function design standards."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/"
related_standards:
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety Standards Family</span>
  <h1>ISO 12100 · ISO 13849-1 · IEC 62061 · IEC 61508 · IEC 61511</h1>
  <p>Risk assessment and safety function design standards. <span class="badge badge--complete">Phase 3 Complete</span></p>
</div>

## PL vs SIL — Which Path?

The choice between Performance Level (PL) and Safety Integrity Level (SIL) depends on application domain:

| Domain | Approach | Standard | Foundation |
|--------|----------|----------|------------|
| Industrial machinery | **PL** (most common) | ISO 13849-1 | ISO 12100 |
| Industrial machinery (alternative) | **Machinery SIL** | IEC 62061 | IEC 61508 |
| Process industry | **SIL** | IEC 61511 | IEC 61508 |
| Generic E/E/PE safety | **SIL** | IEC 61508 | (foundational) |

**ISO 13849-1 and IEC 62061 can be used together** for complex machinery — ISO 13849-1 for mechanical/pneumatic elements, IEC 62061 for electrical/electronic safety functions.

---

## Standards in This Family

### ISO 12100 — Risk Assessment Foundation

**Status:** <span class="badge badge--complete">Reviewed</span>

Foundation standard for all machinery safety. Required as the first step for CE marking. Provides a systematic process for risk assessment and risk reduction.

- Hazard identification
- Risk estimation and evaluation
- Risk reduction strategy (inherently safe design → safeguarding → information for use)

<a href="{{ '/standards/functional-safety/iso-12100/' | relative_url }}" class="card__link">ISO 12100 page &rarr;</a>

---

### ISO 13849-1 — Performance Level (PL)

**Status:** <span class="badge badge--complete">Reviewed</span>

Safety-related parts of control systems. The PL approach uses architectural categories (B, 1–4) and diagnostic coverage to determine the achievable Performance Level (PLa–PLe).

- Most common approach for industrial machinery
- Uses simplified reliability data (MTTFd, DC, CCF)
- Validated by ISO 13849-2 (validation methods)

<a href="{{ '/standards/functional-safety/iso-13849-1/' | relative_url }}" class="card__link">ISO 13849-1 page &rarr;</a>

---

### IEC 62061 — Machinery SIL

**Status:** <span class="badge badge--complete">Reviewed</span>

Functional safety for safety-related electrical control systems on machinery. Uses SIL (1–3) instead of PL. More aligned with IEC 61508 methodology but scoped to machinery.

- Can be used instead of or alongside ISO 13849-1
- More flexible for complex safety functions
- Required when SIL > 2 not achievable with ISO 13849-1 approach

<a href="{{ '/standards/functional-safety/iec-62061/' | relative_url }}" class="card__link">IEC 62061 page &rarr;</a>

---

### IEC 61508 — Generic Functional Safety

**Status:** <span class="badge badge--complete">Reviewed</span>

The foundation standard for all functional safety. IEC 62061 and IEC 61511 both derive from IEC 61508. Multi-part standard covering E/E/PE safety-related systems across all industries.

- Parts 1–7 cover the full safety lifecycle
- Part 3 covers safety-related software
- Rarely applied directly; usually via IEC 62061 or IEC 61511

<a href="{{ '/standards/functional-safety/iec-61508/' | relative_url }}" class="card__link">IEC 61508 page &rarr;</a>

---

### IEC 61511 — Process Industry SIS

**Status:** <span class="badge badge--complete">Reviewed</span>

Application standard for safety instrumented systems (SIS) in the process industry. Covers the SIS lifecycle from concept through decommissioning.

- Applies to oil and gas, chemicals, power generation, and similar process industries
- SIF (Safety Instrumented Function) design and allocation
- Proof test interval and PFDavg calculation
- Process SIS lifecycle, SIL determination, SIS design, and operation or maintenance pages are present in the reference library

<a href="{{ '/standards/functional-safety/iec-61511/' | relative_url }}" class="card__link">IEC 61511 page &rarr;</a>

---

## Standards Hierarchy Diagram

<div class="mermaid-wrap">
<pre class="mermaid">
graph TD
    ISO12100[ISO 12100<br/>Risk Assessment] --> ISO13849[ISO 13849-1<br/>PL approach]
    ISO12100 --> IEC62061[IEC 62061<br/>Machinery SIL]
    ISO13849 --> IEC60204[IEC 60204-1<br/>Implementation]
    IEC62061 --> IEC61508[IEC 61508<br/>Foundation]
    IEC61511[IEC 61511<br/>Process SIS] --> IEC61508
    IEC61131[IEC 61131-3<br/>PLC Software] --> IEC62061
    IEC61131 --> IEC61508
</pre>
</div>
