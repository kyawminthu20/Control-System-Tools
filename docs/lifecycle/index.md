---
layout: default
title: "Engineering Lifecycle"
description: "11-stage control system engineering lifecycle with standards overlay — from concept through maintenance."
breadcrumb:
  - name: "Lifecycle"
repo_path: "control-standards/rag/standards_intelligence/reference_models/"
related_standards:
  - name: "ISO 12100 (Risk Assessment)"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
---

<div class="page-header">
  <span class="page-header__label">Engineering Lifecycle</span>
  <h1>Control System Engineering Lifecycle</h1>
  <p>11 stages from concept through maintenance — with standards overlay at each stage.</p>
</div>

## Lifecycle with Standards Overlay

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    A[Concept] --> B[Standards Selection]
    B --> C[Risk Assessment]
    C --> D[Safety Architecture]
    D --> E[Detailed Design]
    E --> F[Documentation]
    F --> G[Build]
    G --> H[Installation]
    H --> I[Pre-commissioning]
    I --> J[Commissioning]
    J --> K[Maintenance]

    A -.-> A1[ISO 12100]
    B -.-> B1[NFPA 79 / IEC 60204 / IEC 61511]
    C -.-> C1[ISO 12100 / IEC 61511]
    D -.-> D1[ISO 13849 / IEC 62061 / IEC 61511]
    E -.-> E1[UL 508A / NEC / design docs]
    G -.-> G1[IEC 61131-3 / IEC 62443]
    J -.-> J1[FAT / SAT / safety validation]
    K -.-> K1[Proof test / calibration / MOC]
</pre>
</div>

---

## Stage Summary

| # | Stage | Standards | Key Deliverable | PL/SIL Decision |
|---|-------|-----------|-----------------|----------------|
| 1 | [Concept]({{ '/lifecycle/concept/' | relative_url }}) | ISO 12100 | Scope document, boundary definition | — |
| 2 | [Standards Selection]({{ '/lifecycle/standards-selection/' | relative_url }}) | `_standards_map.md` routing | Standards register | — |
| 3 | [Risk Assessment]({{ '/lifecycle/risk-assessment/' | relative_url }}) | ISO 12100, ISO 13849-1, IEC 62061, IEC 61511 | Risk assessment report | PL/SIL decision point |
| 4 | [Safety Architecture]({{ '/lifecycle/safety-architecture/' | relative_url }}) | ISO 13849-1, IEC 62061, IEC 61508 | Safety architecture document | Confirm PL or SIL |
| 5 | [Detailed Design]({{ '/lifecycle/detailed-design/' | relative_url }}) | NFPA 79, UL 508A, IEC 60204-1 | BOM, circuit diagrams, verification plan | — |
| — | [Safety Wiring Practices]({{ '/lifecycle/safety-wiring/' | relative_url }}) | NFPA 79, IEC 60204-1, IEC 61140 | Dual-channel input spec, wire gauge, color, termination | — |
| 6 | [Draft Documentation]({{ '/lifecycle/draft-documentation/' | relative_url }}) | All applicable | Safety manual draft | — |
| 7 | [Build]({{ '/lifecycle/build/' | relative_url }}) | UL 508A, NFPA 79 | Shop traveler, build records | — |
| 8 | [Installation]({{ '/lifecycle/installation/' | relative_url }}) | NEC, NFPA 79 | Installation record | — |
| 9 | [Pre-Commissioning]({{ '/lifecycle/pre-commissioning/' | relative_url }}) | ISO 13849-1 Annex K, IEC 62061 | Pre-comm checklist | — |
| 10 | [Commissioning]({{ '/lifecycle/commissioning/' | relative_url }}) | All applicable | V&V report, FAT/SAT | Final PL/SIL verification |
| 11 | [Maintenance]({{ '/lifecycle/maintenance/' | relative_url }}) | ISO 13849-1 §10, IEC 61511 | Maintenance and proof test plan | — |

---

## Lifecycle Deliverables

<div class="mermaid-wrap">
<pre class="mermaid">
graph TD
    A[Concept] --> A1[System description]
    A --> A2[Boundary definition]

    B[Risk Assessment] --> B1[Hazard list]
    B --> B2[Risk evaluation]
    B --> B3[PLr or SIL target per safety function]

    C[Safety Architecture] --> C1[Safety function register]
    C --> C2[Architecture concept]
    C --> C3[PL or SIL allocation]

    D[Detailed Design] --> D1[Device list]
    D --> D2[Panel BOM]
    D --> D3[I/O list and network architecture]

    E[Commissioning] --> E1[FAT / SAT]
    E --> E2[Validation report]
    E --> E3[Final PL / SIL verification]

    F[Lifecycle Support] --> F1[Proof-test procedures]
    F --> F2[MOC records]
    F --> F3[Revision history]
</pre>
</div>
