---
layout: default
title: "Semiconductor Industry Standards Overlay"
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Semiconductor"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/semiconductor.md"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Semiconductor</span>
  <h1>Semiconductor Equipment Standards</h1>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Semiconductor fab equipment |
| **Typical machines** | Etch, deposition, CMP, metrology, handlers, implant |
| **Markets** | US, EU, Asia (global installation) |
| **Special concern** | Hazardous process gases, cleanroom EMC, SEMI standards |

## Standards Path

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical | NEC, NFPA 79, UL 508A | Complete |
| International electrical | IEC 60204-1 | Complete |
| Risk assessment | ISO 12100 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| Safety functions | ISO 13849-1 (PLd or PLe typical) | Planned <span class="badge badge--verify">TO VERIFY</span> |
| Semiconductor-specific | SEMI S2, S8, S14 | <span class="badge badge--gap">NOT IN LOCAL CORPUS</span> |
| Cybersecurity | IEC 62443 | Routing reference only <span class="badge badge--verify">TO VERIFY</span> |
| Fab safety | NFPA 318 | Not confirmed in corpus |

## What Changes vs Baseline Machine Design

Per the industry overlay file at `rag/scenario/mini_machine_safety_design_v2/industry_overlays/semiconductor.md`:

- **Chemical compatibility, leak containment, purge logic:** Higher priority than in a standard industrial machine. SEMI standards (S2, S8, S14) govern these requirements — **NOT IN LOCAL CORPUS**.
- **Single-point ground and EMC discipline:** More stringent due to co-existence with sensitive instrumentation and networked tooling. IEC 60204-1 Clause 8 (equipotential bonding) provides partial coverage.
- **Documentation and interlock validation:** Deeper than baseline. Tool integration often requires interface qualification and host handshake records. SEMI semiconductor acceptance artifacts are **NOT IN LOCAL CORPUS**.

## Typical Acceptance Artifacts

- Chemical P&ID with valve lineup and spill sensors <span class="badge badge--verify">TO VERIFY</span>
- Tool interface and interlock cause-and-effect matrix
- EMC bonding layout and cable segregation record
- SEMI compliance checklist or gap register <span class="badge badge--gap">NOT IN LOCAL CORPUS</span>

## Repository Path

- Local: `rag/reference_models/15-Standard Minimum Compliance Stack.md`
- Industry overlay: `rag/scenario/mini_machine_safety_design_v2/industry_overlays/semiconductor.md`

<a href="{{ '/scenarios/semiconductor-equipment/' | relative_url }}" class="card__link">See full semiconductor equipment scenario &rarr;</a>
