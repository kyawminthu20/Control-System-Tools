---
layout: default
title: "Home"
description: "Navigate industrial automation standards families, lifecycle stages, and repository sources."
---

<div class="hero">
  <span class="section-label">Control System Standards Atlas</span>
  <h1 class="hero__title">Industrial Automation Standards — Navigated</h1>
  <p class="hero__subtitle">
    A personal engineering reference for industrial control system standards: navigate families,
    lifecycle stages, crosswalks, and repository sources without opening PDFs.
  </p>
  <a href="{{ '/standards/' | relative_url }}" class="hero__cta">Explore Standards &rarr;</a>
  <a href="{{ '/verification/lifecycle/' | relative_url }}" class="hero__cta hero__cta--secondary">View Lifecycle &rarr;</a>
</div>

---

## Standards Families

<span class="section-label">Six coverage areas in this corpus</span>

<div class="card-grid">
  <div class="card">
    <span class="card__label">US Electrical</span>
    <span class="card__title">NEC · NFPA 79 · UL 508A</span>
    <p class="card__desc">US-market standards for industrial control panels and machinery electrical design. NEC is legally enforced; UL 508A covers panel listing.</p>
    <div class="card__path">rag/us/</div>
    <a href="{{ '/standards/us-electrical/' | relative_url }}" class="card__link">View family &rarr;</a>
  </div>

  <div class="card">
    <span class="card__label">International Machinery</span>
    <span class="card__title">IEC 60204-1</span>
    <p class="card__desc">Electrical equipment of machines for CE-marked and global machinery. Equivalent scope to NFPA 79 for international markets.</p>
    <div class="card__path">rag/international/machinery/</div>
    <a href="{{ '/standards/machinery/' | relative_url }}" class="card__link">View family &rarr;</a>
  </div>

  <div class="card">
    <span class="card__label">Functional Safety</span>
    <span class="card__title">ISO 12100 · ISO 13849-1 · IEC 62061 · IEC 61508 · IEC 61511</span>
    <p class="card__desc">Risk assessment and safety function design. PL (Performance Level) path via ISO 13849-1; SIL path via IEC 62061 or IEC 61511 for process.</p>
    <div class="card__path">rag/international/functional_safety/</div>
    <a href="{{ '/standards/functional-safety/' | relative_url }}" class="card__link">View family &rarr;</a>
    <span class="badge badge--complete">Complete</span>
  </div>

  <div class="card">
    <span class="card__label">Software &amp; Cybersecurity</span>
    <span class="card__title">IEC 61131-3 · IEC 62443</span>
    <p class="card__desc">PLC programming languages and safety software lifecycle (IEC 61131-3). Industrial cybersecurity series (IEC 62443) for networked control systems.</p>
    <div class="card__path">rag/reference_models/</div>
    <a href="{{ '/design/software-stack/' | relative_url }}" class="card__link">Routing guide &rarr;</a>
    <span class="badge badge--verify">TO VERIFY</span>
  </div>

  <div class="card">
    <span class="card__label">Crosswalks</span>
    <span class="card__title">NFPA 79 ↔ IEC 60204-1 · UL 508A / NEC overlap</span>
    <p class="card__desc">Side-by-side comparison tables mapping clause equivalencies between US and international standards.</p>
    <div class="card__path">rag/crosswalks/overlap_matrix/</div>
    <a href="{{ '/tools/crosswalks/' | relative_url }}" class="card__link">View crosswalks &rarr;</a>
  </div>

  <div class="card">
    <span class="card__label">Reference Models</span>
    <span class="card__title">7-Layer Architecture · Safety Architecture · 15-Standard Stack</span>
    <p class="card__desc">Cross-cutting reference models: machine architecture layers, universal safety architecture, and semiconductor compliance stack.</p>
    <div class="card__path">rag/reference_models/</div>
    <a href="{{ '/design/software-stack/' | relative_url }}" class="card__link">View reference &rarr;</a>
  </div>
</div>

---

## Engineering Lifecycle

<span class="section-label">11 stages — click any stage to see which standards apply</span>

<div class="lifecycle-ribbon">
  <a href="{{ '/verification/lifecycle/concept/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">01</span>
    <span class="lifecycle-stage__name">Concept</span>
    <span class="lifecycle-stage__std">ISO 12100</span>
  </a>
  <a href="{{ '/verification/lifecycle/standards-selection/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">02</span>
    <span class="lifecycle-stage__name">Standards Selection</span>
    <span class="lifecycle-stage__std">_standards_map</span>
  </a>
  <a href="{{ '/verification/risk-assessment/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">03</span>
    <span class="lifecycle-stage__name">Risk Assessment</span>
    <span class="lifecycle-stage__std">ISO 12100 · 61511</span>
  </a>
  <a href="{{ '/verification/safety-architecture/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">04</span>
    <span class="lifecycle-stage__name">Safety Architecture</span>
    <span class="lifecycle-stage__std">13849 · 62061</span>
  </a>
  <a href="{{ '/verification/lifecycle/detailed-design/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">05</span>
    <span class="lifecycle-stage__name">Detailed Design</span>
    <span class="lifecycle-stage__std">NFPA 79 · UL 508A</span>
  </a>
  <a href="{{ '/verification/lifecycle/draft-documentation/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">06</span>
    <span class="lifecycle-stage__name">Documentation</span>
    <span class="lifecycle-stage__std">All applicable</span>
  </a>
  <a href="{{ '/implementation/lifecycle-build/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">07</span>
    <span class="lifecycle-stage__name">Build</span>
    <span class="lifecycle-stage__std">UL 508A · NFPA 79</span>
  </a>
  <a href="{{ '/implementation/lifecycle-installation/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">08</span>
    <span class="lifecycle-stage__name">Installation</span>
    <span class="lifecycle-stage__std">NEC · NFPA 79</span>
  </a>
  <a href="{{ '/implementation/lifecycle-pre-commissioning/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">09</span>
    <span class="lifecycle-stage__name">Pre-Commissioning</span>
    <span class="lifecycle-stage__std">13849 Annex K</span>
  </a>
  <a href="{{ '/implementation/lifecycle-commissioning/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">10</span>
    <span class="lifecycle-stage__name">Commissioning</span>
    <span class="lifecycle-stage__std">FAT / SAT / V&amp;V</span>
  </a>
  <a href="{{ '/verification/maintenance/' | relative_url }}" class="lifecycle-stage">
    <span class="lifecycle-stage__num">11</span>
    <span class="lifecycle-stage__name">Maintenance</span>
    <span class="lifecycle-stage__std">13849 §10</span>
  </a>
</div>

<p style="font-size:0.82rem;color:var(--color-text-muted);">Source: <code>rag/reference_models/standards_atlas_diagrams_reference.md</code> Diagrams 6–7</p>

---

## Standards Relationship Graph

<span class="section-label">How standards reference and depend on each other</span>

{% include standards-graph.html mode="mini" container_id="standards-graph-home" %}

---

## Industry Matrix

<span class="section-label">9 confirmed industry overlays — standards vary by sector</span>

| Industry | US Path | International Path | Safety Method | Special Overlays |
|----------|---------|-------------------|---------------|------------------|
| **Semiconductor** | NEC, NFPA 79, UL 508A | IEC 60204-1, ISO 13849-1 | PL or SIL | SEMI S2/S8/S14 <span class="badge badge--complete">Complete</span> |
| **Food &amp; Beverage** | NEC, NFPA 79, UL 508A | IEC 60204-1 | PL | Washdown, hygienic design |
| **Energy** | NEC, NFPA 79 | IEC 60204-1, IEC 62443 | SIL | Outdoor, process safety, cybersecurity |
| **Petroleum / Oil &amp; Gas** | NEC, NFPA 79 | IEC 61511, IEC 60079 | SIL | Hazardous area <span class="badge badge--complete">Complete</span> |
| **Marine** | NEC | IEC 60204-1 | PL / SIL | Marine class rules |
| **Medical** | NEC, FDA regs | IEC 60204-1, IEC 62304 | SIL | FDA, software lifecycle |
| **Nuclear** | NEC, IEEE | IEC 60204-1 | SIL | Nuclear QA |
| **Offshore** | NEC | IEC 60204-1, IEC 61511 | SIL | Offshore electrical, corrosion |
| **Commercial** | NEC, building codes | IEC 60204-1 | — | Lighter industrial |

<p><a href="{{ '/industries/' | relative_url }}">View full industry pages &rarr;</a></p>

---

## Featured Scenarios

<span class="section-label">Start here — five common engineering situations</span>

<div class="scenario-grid">
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 01</span>
    <span class="scenario-card__title">US Industrial Control Panel</span>
    <p class="scenario-card__start"><strong>Start with:</strong> UL 508A + NEC Article 409 + NFPA 79</p>
    <p style="font-size:0.78rem;color:var(--color-text-muted);">Panel intended for US market, UL listing required. All three standards apply — NEC is the legal baseline, UL 508A governs construction and listing, NFPA 79 applies when machine context exists.</p>
    <a href="{{ '/implementation/scenarios/us-industrial-control-panel/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
  </div>

  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 02</span>
    <span class="scenario-card__title">Global Machine (US + EU)</span>
    <p class="scenario-card__start"><strong>Start with:</strong> NFPA 79 (US) + IEC 60204-1 (EU) + ISO 12100</p>
    <p style="font-size:0.78rem;color:var(--color-text-muted);">Machine sold in both US and EU markets. Design to most restrictive from each. CE marking requires ISO 12100 risk assessment as foundation.</p>
    <a href="{{ '/implementation/scenarios/global-machine/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
  </div>

  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 03</span>
    <span class="scenario-card__title">Process Skid Shutdown System</span>
    <p class="scenario-card__start"><strong>Start with:</strong> IEC 61511 + IEC 61508 (foundation)</p>
    <p style="font-size:0.78rem;color:var(--color-text-muted);">SIS / ESD system for process industry. IEC 61511 is the application standard; IEC 61508 is the foundation lifecycle standard. <span class="badge badge--complete">CORPUS COMPLETE</span></p>
    <a href="{{ '/implementation/scenarios/process-skid/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
  </div>

  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 04</span>
    <span class="scenario-card__title">Networked Safety PLC Architecture</span>
    <p class="scenario-card__start"><strong>Start with:</strong> ISO 13849-1 or IEC 62061 + IEC 62443</p>
    <p style="font-size:0.78rem;color:var(--color-text-muted);">Safety PLC with network connectivity. Safety function design per PL or SIL path; cybersecurity overlay per IEC 62443. <span class="badge badge--verify">TO VERIFY</span></p>
    <a href="{{ '/implementation/scenarios/networked-safety-plc/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
  </div>

  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 05</span>
    <span class="scenario-card__title">Semiconductor Equipment Compliance</span>
    <p class="scenario-card__start"><strong>Start with:</strong> 15-Standard Minimum Compliance Stack</p>
    <p style="font-size:0.78rem;color:var(--color-text-muted);">Complex compliance stack for semiconductor fab equipment. SEMI S2/S8/S14 are now in the local corpus alongside the industry overlay.</p>
    <a href="{{ '/implementation/scenarios/semiconductor-equipment/' | relative_url }}" style="font-size:0.8rem;">Full scenario &rarr;</a>
  </div>
</div>

---

## Repository Explorer

<span class="section-label">Directory layout — source of truth is <code>control-standards/rag/</code></span>

<div class="repo-tree">
<pre>control-standards/rag/standards_intelligence/
├── _index.yaml               ← master index (standards, routing, status)
├── _standards_map.md         ← applicability decision matrix
├── us/
│   ├── nec/                  ← NEC (NFPA 70) 2023
│   ├── nfpa79/               ← NFPA 79 2024 — 20 chapters
│   └── ul_508a/              ← UL 508A 2022 — 11 sections
├── international/
│   ├── machinery/
│   │   └── iec_60204_1/      ← IEC 60204-1:2018 — 15 clauses
│   ├── functional_safety/
│   │   ├── iso_13849_1/      ← ISO 13849-1:2023 [complete]
│   │   ├── iso_12100/        ← ISO 12100:2010 [complete]
│   │   ├── iec_62061/        ← IEC 62061:2021 [complete]
│   │   ├── iec_61508/        ← IEC 61508:2010 [complete]
│   │   └── iec_61511/        ← IEC 61511:2016 [complete]
│   ├── hazardous_area/
│   │   └── iec_60079/        ← IEC 60079 series — 6 parts
│   └── semiconductor/
│       └── semi/             ← SEMI S2/S8/S14 — 3 standards
├── crosswalks/
│   └── overlap_matrix/       ← NFPA79↔IEC60204, UL508A/NEC, decision workflow
├── reference_models/         ← 7-layer arch, safety arch, 15-std stack, diagrams
├── routing/                  ← standards applicability routing
└── scenario/                 ← example engineering packages</pre>
</div>

**Start here based on your project:**
- US panel / machinery: [`us/ul_508a/`]({{ '/standards/us-electrical/ul-508a/' | relative_url }}) · [`us/nfpa79/`]({{ '/standards/us-electrical/nfpa-79/' | relative_url }}) · [`us/nec/`]({{ '/standards/us-electrical/nec/' | relative_url }})
- International machinery: [`international/machinery/iec_60204_1/`]({{ '/standards/machinery/iec-60204-1/' | relative_url }})
- Safety functions: [`international/functional_safety/`]({{ '/standards/functional-safety/' | relative_url }})
- US ↔ International overlap: [`crosswalks/overlap_matrix/`]({{ '/tools/crosswalks/' | relative_url }})
