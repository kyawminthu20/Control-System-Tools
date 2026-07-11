---
layout: default
title: "Lifecycle Stage 12 — Management of Change"
description: "Structured re-entry into the safety lifecycle for any modification to a safety function, component, or program — the most commonly failed audit point."
redirect_from:
  - /verification/management-of-change/
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "12. Management of Change"
related_standards:
  - name: "IEC 61511-1"
    url: "/standards/functional-safety/iec-61511/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 12</span>
  <h1>Management of Change</h1>
  <p>Any modification to a safety function restarts the lifecycle at the appropriate stage — there is no such thing as a minor change.</p>
</div>

## 1. Purpose

MOC is the mechanism by which any modification — to hardware, software, process parameters, safety functions, or documentation — is formally assessed, approved, and re-verified before implementation. It is arguably the most commonly failed audit point in operating facilities. IEC 61511-1 §17, ISO 13849-1 §10.2, IEC 62061 §6.9.

The fundamental rule: **Changes restart the lifecycle at the appropriate stage.** There is no such thing as a "minor" change to a safety function.

## 2. When MOC Is Required

| Change Type | MOC Required? | Re-entry Stage |
|-------------|--------------|----------------|
| Component replacement (same part number, same specs) | No — document only | Stage 11 (record the replacement) |
| Component replacement (different part number or specs) | Yes | Stage 4 (re-verify PL/SIL) |
| Software/application program change (safety functions) | Yes | Stage 4.5 → Stage 10 (re-test) |
| Process parameter change (demand rate, response time) | Yes | Stage 3 (re-assess risk) |
| Safety function scope change | Yes | Stage 3 → full forward |
| Guard or device relocation | Yes | Stage 3 or 4 (assess impact) |
| Control system hardware modification | Yes | Stage 4 |
| Operating mode addition | Yes | Stage 3 |
| Safety manual update only | No — document only | Stage 11 (update records) |
| Replacement-in-kind (verified equivalent) | Simplified MOC | Stage 11 (document equivalence) |

## 3. Entry Criteria

Any of the following triggers MOC:

- Proposed change to a component, circuit, program, or parameter that is part of or affects a safety function
- Periodic proof test reveals a component has reached end of rated life and must be replaced with a different part
- Customer or process change that alters demand rate, consequence severity, or required response time
- Regulatory or standards change that invalidates the original design basis

## 4. The MOC Procedure

The MOC procedure has four steps:

1. **Change Request** — document the proposed change, originator, scope, and reason
2. **Impact Assessment** — identify which safety functions are affected, which lifecycle stages are re-entered, what re-verification is needed
3. **Approval** — review by responsible engineer, sign-off before any physical or software change
4. **Implementation + Re-verification** — execute the change, re-verify at the appropriate stage, update documentation

### MOC Record Template

| Field | Content |
|-------|---------|
| MOC ID | |
| Date initiated | |
| Originator | |
| Description of change | |
| Reason for change | |
| Safety functions affected (SF ID) | |
| Hazards potentially introduced or changed | |
| Lifecycle stage(s) to re-enter | |
| Required re-verification activities | |
| Interim compensating measures (if applicable) | |
| Approved by | |
| Date approved | |
| Implementation date | |
| Re-verification complete (Y/N) | |
| Documents updated | |
| Closed by | |
| Date closed | |

## 5. Impact Assessment Guidance

For each affected safety function, answer:

- Does this change affect the input, logic, or output subsystem?
- Does the calculated PL/SIL still hold after the change?
- Does the response time requirement still be met?
- Have the diagnostic coverage or CCF score changed?
- Is the proof test procedure still valid after the change?
- Does the safety manual need to be updated?

## 6. Re-entry Points by Change Type

| Change Category | Stages to Re-enter |
|----------------|-------------------|
| Risk profile change (new hazard, process change) | Stage 3 → 3.5 → 4 → 5 → 7 → 9 → 10 |
| Architecture change (hardware, category) | Stage 4 → 5 → 7 → 9 → 10 |
| Software/application logic change | Stage 4.5 → 7 (software) → 10 |
| Component replacement (non-equivalent) | Stage 4 → 5 → 7 → 9 → 10 |
| Documentation change only | Stage 6 |
| Maintenance procedure change | Stage 11 |

## 7. Key Deliverables

| # | Deliverable |
|---|------------|
| 1 | MOC request form with impact assessment |
| 2 | Approval record |
| 3 | Re-verification records for each re-entered lifecycle stage |
| 4 | Updated as-built drawings, BOM, or program backup |
| 5 | Updated safety manual (if affected) |
| 6 | Updated proof test procedure (if affected) |
| 7 | Closed MOC record with all signatures |

## 8. Exit Criteria

An MOC is closed when:

- All required re-verification activities are complete
- All affected documentation is updated
- The change has been signed off by the responsible engineer
- The updated safety function has been functionally tested on the physical system (if applicable)

## 9. Common Mistakes

- Treating component replacement as "not a change" without equivalence verification
- Not updating the safety manual after a change
- Not re-running the proof test after a hardware change
- Allowing verbal approval instead of written MOC records
- Starting the change before the MOC is approved (changes implemented without authorization)
- Assuming software changes are "minor" — any change to safety function logic requires re-test
- Closing the MOC without verifying that all downstream documents are updated

## 10. Relationship to Adjacent Stages

MOC loops back from Stage 12 to any earlier stage depending on the nature of the change. It is the only backward-looking stage in the lifecycle. Once re-verification is complete, MOC closes and Stage 11 (Maintenance) continues.

```
Ongoing Operations ◄══════════ Stage 12: Management of Change
                                (loops back to any prior stage)
```

Previous stage: [Stage 11 — Maintenance and Lifecycle Support](/lifecycle/maintenance/) | Up: [Lifecycle Overview](/lifecycle/)

## 11. Templates and Tools

| Tool / Template | Purpose |
|----------------|---------|
| MOC Request Form | Initiates the MOC, captures change description and scope |
| Impact Assessment Checklist | Guides assessment of which safety functions and stages are affected |
| Equivalence Verification Form | Documents replacement-in-kind justification |
| SISTEMA / SILver | Re-run PL/SIL calculations after hardware changes |
| MOC Register | Running log of all MOC records for the machine |
