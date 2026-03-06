---
layout: default
title: "Lifecycle Stage 4 — Safety Architecture Definition"
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "4. Safety Architecture"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 04</span>
  <h1>Safety Architecture Definition</h1>
  <strong>Confirm PL or SIL — Architecture Document</strong>
</div>

## Standards Influence

| Standard | Role at This Stage |
|----------|-------------------|
| **ISO 13849-1** | Category selection (B, 1–4), MTTFd, DC, CCF parameters |
| **IEC 62061** | Subsystem architecture, PFHD calculation |
| **IEC 61508** | Architectural constraints, hardware fault tolerance (for IEC 62061 path) |
| **IEC 61511** | SIS architecture for process SIS |

## Activities

1. **Define safety functions** — each safety function with PLr or SIL target
2. **Select architecture** — Category (ISO 13849-1) or hardware architecture (IEC 62061)
3. **Select components** — sensors, logic solver, final elements
4. **Calculate achievable PL/SIL** — verify architecture meets PLr or SIL target
5. **Address CCF** — Common Cause Failure score per ISO 13849-1 Annex F or IEC 62061

## Architecture Types (ISO 13849-1 Categories)

| Category | Description | Common Use |
|----------|-------------|-----------|
| B | Basic — single channel | PLa–PLb |
| 1 | Single channel, well-tried components | PLb–PLc |
| 2 | Single channel with monitoring | PLc |
| 3 | Dual channel, no single fault leads to loss | PLd |
| 4 | Dual channel with full diagnostics | PLe |

**Category 3 with high MTTFd components and medium DC typically achieves PLd** — the most common target for industrial machine guarding.

## Key Deliverable

**Safety Architecture Document:**
- Safety function register (finalized)
- Selected architecture category per function
- Component MTTFd / PFHD inputs
- Calculated PL / SIL achievable
- CCF score

## Next Stage

→ [Detailed Design]({{ '/lifecycle/detailed-design/' | relative_url }})
