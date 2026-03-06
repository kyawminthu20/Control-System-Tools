---
layout: default
title: "Energy Industry Standards Overlay"
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Energy"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/energy.md"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Energy</span>
  <h1>Energy Industry Standards</h1>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Energy — power generation, renewable energy, grid infrastructure |
| **Typical machines** | Turbine controls, generator protection, substation automation |
| **Markets** | US and international |
| **Special concern** | Outdoor installation, process safety, cybersecurity |

## Standards Path

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical | NEC, NFPA 79 | Complete |
| International electrical | IEC 60204-1 | Complete |
| Risk assessment | ISO 12100 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| Process safety | IEC 61511 | Planned — limited <span class="badge badge--verify">TO VERIFY</span> |
| Cybersecurity | IEC 62443 | Routing reference <span class="badge badge--verify">TO VERIFY</span> |
| Grid / substation | NERC CIP, IEC 61850 | Not in corpus |

## Key Overlays

- **Outdoor environments:** Enclosures rated for outdoor exposure; NEMA 3R or 4X / IP65 or higher. Sun loading, thermal management.
- **Process safety:** Many energy systems have SIS requirements — IEC 61511 applies for process safety functions.
- **Cybersecurity:** Modern energy control systems (SCADA, EMS) are targets for cyberattack — IEC 62443 and NERC CIP requirements apply. IEC 62443 is a routing reference in this corpus; NERC CIP is not covered.

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/energy.md`
