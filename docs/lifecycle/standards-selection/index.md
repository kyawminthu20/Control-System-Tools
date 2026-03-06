---
layout: default
title: "Lifecycle Stage 2 — Standards Selection"
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "2. Standards Selection"
related_standards:
  - name: "Standards Decision Workflow"
    url: "/crosswalks/standards-decision-workflow/"
  - name: "US Electrical Standards"
    url: "/standards/us-electrical/"
  - name: "International Machinery"
    url: "/standards/machinery/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 02</span>
  <h1>Standards Selection</h1>
</div>

## Standards Influence

The `_standards_map.md` routing document is the primary tool at this stage. See also the [decision workflow crosswalk]({{ '/crosswalks/standards-decision-workflow/' | relative_url }}).

## Routing Logic

```
US market only?
  → NEC + NFPA 79 + UL 508A (if panel listing required)

EU / CE marking?
  → IEC 60204-1 + ISO 12100 + ISO 13849-1 or IEC 62061

Global (US + EU)?
  → NFPA 79 + IEC 60204-1 + ISO 13849-1 (most restrictive from each)

Process industry?
  → IEC 61511 + IEC 61508 (foundation)

Safety functions present?
  → ISO 13849-1 (PL path) OR IEC 62061 (SIL path) — based on risk and complexity
```

## Key Deliverable

**Standards Register:** A formal list of applicable standards for the project, with applicability basis and scope notes for each.

| Standard | Applicable? | Basis | Scope |
|----------|------------|-------|-------|
| NEC 2023 | Yes | US installation | Article 409, 430, 670 |
| NFPA 79 2024 | Yes | Machinery scope | All chapters |
| UL 508A 2022 | Yes | UL listing required | All sections |
| ISO 12100 | Yes | CE marking | Full risk assessment |
| IEC 60204-1 | Yes | EU market | All clauses |

## Next Stage

→ [Risk Assessment]({{ '/lifecycle/risk-assessment/' | relative_url }})
