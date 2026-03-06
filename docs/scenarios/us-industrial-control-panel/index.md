---
layout: default
title: "Scenario 01 — US Industrial Control Panel"
description: "Standards routing for a US-market industrial control panel requiring UL listing: UL 508A, NEC, NFPA 79."
breadcrumb:
  - name: "Scenarios"
    url: "/scenarios/"
  - name: "US Control Panel"
repo_path: "control-standards/rag/standards_intelligence/us/"
related_standards:
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
  - name: "NEC"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
crosswalk_refs:
  - name: "UL 508A / NEC / NFPA 79 Overlap"
    url: "/crosswalks/ul508a-nec-nfpa79/"
---

<div class="page-header">
  <span class="page-header__label">Scenario 01</span>
  <h1>US Industrial Control Panel</h1>
</div>

## Project Summary

| Field | Detail |
|-------|--------|
| **Market** | United States |
| **Application** | Standalone industrial control panel, UL listing required |
| **Machine context** | Panel is part of an industrial machine |
| **Listing requirement** | UL listing required (insurance / AHJ) |

## Starting Standards

| Standard | Role | Status |
|----------|------|--------|
| **UL 508A 2022** | Panel construction and UL listing | Complete in corpus |
| **NEC 2023** | Installation code — legally enforced | Complete in corpus |
| **NFPA 79 2024** | Machine electrical design (if machine context) | Complete in corpus |

## Standards Decision Logic

```
US market panel with UL listing required:
  ├── UL 508A    → panel construction, SCCR calculation, listing requirements
  ├── NEC Art. 409  → installation requirements; requires SCCR label
  ├── NEC Art. 250  → grounding and bonding (legally required)
  └── NFPA 79   → applies if panel is part of a machine
                   (NEC Art. 670 references NFPA 79)
```

## Repository Paths

| Standard | Repository Path |
|----------|----------------|
| UL 508A | `rag/us/ul_508a/` |
| NEC | `rag/us/nec/` |
| NFPA 79 | `rag/us/nfpa79/` |

## Key Engineering Decisions

**1. SCCR**
- Calculate panel SCCR using UL 508A Supplement SB
- NEC Article 409.110 requires SCCR label on the panel
- SCCR must meet or exceed available fault current at installation

**2. Grounding**
- NEC Article 250 baseline (legally required)
- NFPA 79 Chapter 8 for machine-specific bonding
- UL 508A Section 7 for panel bonding workmanship

**3. Wire Sizing**
- UL 508A Section 5 inside the panel
- NEC Article 310 for field conductors

**4. Emergency Stop (if machine context)**
- NFPA 79 Chapter 9 defines E-stop behavior
- For formal PL verification: ISO 13849-1

## Recommended Next Steps

1. [UL 508A panel construction requirements]({{ '/standards/us-electrical/ul-508a/' | relative_url }})
2. [NEC Article 409 and 430]({{ '/standards/us-electrical/nec/' | relative_url }})
3. [NFPA 79 Chapter 9 — control circuits]({{ '/standards/us-electrical/nfpa-79/' | relative_url }})
4. [UL 508A / NEC / NFPA 79 overlap crosswalk]({{ '/crosswalks/ul508a-nec-nfpa79/' | relative_url }})

## Assumptions and Limitations

- This scenario assumes a US-only market panel. For EU or global markets, see [Scenario 02]({{ '/scenarios/global-machine/' | relative_url }}).
- Safety function design (PL/SIL) is not the primary focus of this scenario. If safety functions are required, add ISO 13849-1 and see [Scenario 04]({{ '/scenarios/networked-safety-plc/' | relative_url }}).
- Content is derived from the local RAG corpus. Verify against current published editions of each standard.
