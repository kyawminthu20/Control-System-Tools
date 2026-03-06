---
layout: default
title: "Lifecycle Stage 3 — Risk Assessment"
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "3. Risk Assessment"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 03</span>
  <h1>Risk Assessment</h1>
  <strong>PL/SIL Decision Point</strong>
</div>

## Standards Influence

| Standard | Role at This Stage |
|----------|-------------------|
| **ISO 12100** | Risk assessment methodology; required for CE marking |
| **ISO 13849-1** | Provides PLr table (risk graph) for each safety function |
| **IEC 62061** | Provides SILCL determination for machinery SIL path |
| **IEC 61511** | HAZOP and LOPA methodology for process SIS |

## Activities

1. **Identify hazards** — systematic list per ISO 12100 Annex B
2. **Estimate risk** — severity of harm (S), frequency of exposure (F), probability of avoidance (P)
3. **Evaluate risk** — is risk tolerable with no safety function? If not:
4. **Determine PLr or SIL** — required risk reduction for each safety function
5. **Document** — risk assessment report with all inputs and conclusions

## PL/SIL Decision

This stage is where the PL or SIL target is set for each safety function:

| Method | Input | Output | Standard |
|--------|-------|--------|----------|
| Risk graph | S, F, P | PLr | ISO 13849-1 |
| SILCL determination | Severity, frequency, probability | SILCL | IEC 62061 |
| LOPA | Demand rate, consequence, IPL credits | SIL | IEC 61511 |

## Key Deliverable

**Risk Assessment Report** containing:
- Hazard identification list
- Risk estimation for each hazard
- Required risk reduction (PLr or SIL) per safety function
- Safety function register (preliminary)

## Next Stage

→ [Safety Architecture]({{ '/lifecycle/safety-architecture/' | relative_url }})
