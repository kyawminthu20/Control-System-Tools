---
layout: default
title: "Marine Industry Standards Overlay"
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Marine"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/marine.md"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Marine</span>
  <h1>Marine Industry Standards</h1>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Marine and shipbuilding |
| **Typical systems** | Ship automation, propulsion control, cargo systems |
| **Markets** | International (flag state and class rules) |
| **Special concern** | Classification society rules (ABS, DNV, Lloyd's), vibration, corrosion |

## Standards Path

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical | NEC (for US-flagged vessels) | Complete |
| International electrical | IEC 60204-1 (referenced by class rules) | Complete |
| Risk assessment | ISO 12100 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| Safety functions | ISO 13849-1 or IEC 62061 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| Marine class rules | ABS, DNV-GL, Lloyd's, BV | Not in corpus |
| Marine electrical | IEC 60092 series | Not in corpus |

## Key Overlays

**Classification society requirements:**
- ABS (American Bureau of Shipping), DNV, Lloyd's Register, BV, and others have their own rules
- These class rules typically reference IEC 60204-1 and other IEC standards
- Classification society rules are **not in this corpus**

**Vibration and shock:**
- Marine installations have higher vibration requirements than land-based
- Equipment must be rated for marine vibration profiles (IEC 60068 series or class-specific)

**Corrosion:**
- Salt air, humidity, and occasional spray require higher IP ratings and corrosion-resistant materials

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/marine.md`
