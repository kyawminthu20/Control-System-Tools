---
layout: default
title: "IEC 62061 — Functional Safety, Machinery SIL"
description: "IEC 62061:2021 — SIL approach for safety-related electrical control systems on machinery."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
  - name: "IEC 62061"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/"
related_standards:
  - name: "ISO 13849-1 (PL alternative)"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 61508 (foundation)"
    url: "/standards/functional-safety/iec-61508/"
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
lifecycle_stage:
  - name: "Safety Architecture"
    slug: "safety-architecture/"
  - name: "Detailed Design"
    slug: "detailed-design/"
review:
  standard: "IEC 62061"
  edition: "2021"
  status: "Reviewed"
  coverage: "Core clauses plus Annex A SILCL tables; worked example included"
  last_reviewed: "April 2026"
---

<div class="page-header">
  <span class="page-header__label">Functional Safety · IEC 62061</span>
  <h1>IEC 62061:2021 — Functional Safety of Machinery (SIL)</h1>
  <span class="badge badge--complete">Phase 3 Complete</span>
</div>

## Quick Start

- IEC 62061 applies the SIL approach to machinery — use it when your SRECS includes a programmable safety controller (safety PLC) or when integrating certified safety devices from multiple suppliers.
- Start with [ISO 12100]({{ '/standards/functional-safety/iso-12100/' | relative_url }}) to identify hazards and determine the required SIL for each safety function — IEC 62061 uses the same S/F/P risk parameters as ISO 12100.
- Decompose the SRECS into three subsystems: input (sensor or initiator) → logic (safety PLC or safety relay) → output (actuator or contactor). Each subsystem has its own PFHd contribution.
- Total SRECS PFHd = sum of subsystem PFHd values. This total must be less than or equal to the SIL target PFHd limit. The additive nature makes budget allocation straightforward.
- Check SILCL (SIL Claim Limit) for every subsystem. A low PFHd calculation does not override the SILCL architectural cap — if your subsystem architecture only supports SILCL 2, you cannot use it in a SIL 3 application regardless of the calculated PFHd.

---

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | IEC 62061 |
| **Edition** | 2021 |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Jurisdiction** | Global; harmonized under EU Machinery Directive and Machinery Regulation 2023/1230 |
| **Scope** | Safety-related electrical control systems (SRECS) on machines — SIL 1 through SIL 3 |
| **Repository** | `rag/international/functional_safety/iec_62061/` |
| **Status in Corpus** | <span class="badge badge--complete">Phase 3 Complete</span> — 4 clause files + index |
| **Derived from** | [IEC 61508]({{ '/standards/functional-safety/iec-61508/' | relative_url }}) — sector-specific application for machinery |

**Purpose:** IEC 62061 provides requirements for the design, integration, and validation of safety-related electrical, electronic, and programmable electronic control systems (SRECS) on machinery. It is derived from IEC 61508 but is scoped specifically to machinery, eliminating the most complex IEC 61508 requirements (SIL 4, full software safety lifecycle for certified subsystems) that do not apply to typical machinery contexts.

---

## SIL Levels and PFHd

IEC 62061 applies to high-demand or continuous-demand mode — the mode where the safety function is demanded frequently. For machinery with safety functions demanded more than once per year, high-demand mode applies and PFHd is the correct metric. Low-demand systems (demanded less than once per year) use PFDavg and are covered by process safety standards such as IEC 61511.

| SIL | PFHd range (per hour) | Total SRECS PFHd must be | Typical machinery application |
|-----|-----------------------|--------------------------|-------------------------------|
| SIL 1 | 10⁻⁶ to less than 10⁻⁵ | Less than 10⁻⁵ /hr | Lower-risk auxiliary safety functions, supplementary interlocks |
| SIL 2 | 10⁻⁷ to less than 10⁻⁶ | Less than 10⁻⁶ /hr | Most industrial machine guarding, safety PLCs protecting operators, robot cell access |
| SIL 3 | 10⁻⁸ to less than 10⁻⁷ | Less than 10⁻⁷ /hr | High-risk applications: heavy press tools, automated guided vehicles, certain collaborative robot systems |

SIL 2 is the most common target for industrial machinery safety functions. It corresponds approximately to PLd in [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) terms. SIL 3 is rarely required for typical industrial machinery and adds significant verification burden.

---

## SRECS Architecture

IEC 62061 decomposes the SRECS into three subsystems. Each subsystem is designed and verified independently. The total SRECS PFHd is the sum of all subsystem PFHd values.

```
[Input Subsystem]          [Logic Subsystem]         [Output Subsystem]
Sensor / Initiator    -->  Safety PLC / Relay   -->  Actuator / Contactor
(e.g., light curtain)      (logic controller)         (e.g., contactor pair)

  PFHd_input          +      PFHd_logic          +     PFHd_output
                       = PFHd_SRECS (must be <= SIL target limit)
```

**PFHd allocation principle:** Allocate the tightest PFHd budget (smallest allowable PFHd) to the logic subsystem, because the logic controller affects every safety function that passes through it. A logic subsystem failure can defeat all safety functions simultaneously. Input and output subsystems share the remaining budget, typically informed by manufacturer published PFH values for certified devices.

**SILCL constraint on architecture:** Every subsystem must have a SILCL at or above the SIL target. The subsystem SILCL is the minimum of the SILCL ratings of all devices in that subsystem. Upgrading a single device with a lower SILCL rating can raise the entire subsystem SILCL.

---

## SIL Determination from Risk Parameters

The SIL target for each safety function is derived from [ISO 12100]({{ '/standards/functional-safety/iso-12100/' | relative_url }}) risk assessment parameters. IEC 62061 uses the same S/F/P parameters as ISO 12100 and ISO 13849-1, but routes them through a table that produces a SIL target rather than a PL target.

| Risk parameter | Value | Meaning |
|----------------|-------|---------|
| **S — Severity** | S1 | Reversible injury |
| | S2 | Irreversible injury or death |
| **F — Frequency/duration of exposure** | F1 | Infrequent or short duration exposure |
| | F2 | Frequent, continuous, or long duration exposure |
| **P — Possibility of avoidance** | P1 | Possible under specific conditions |
| | P2 | Scarcely possible |

IEC 62061 also includes a **K factor** for demand rate — the frequency at which the hazardous situation actually occurs, which is distinct from F (the exposure of persons). The K factor adjusts the SIL determination for very low-frequency demands where the safety function is rarely challenged.

**Approximate SIL outcomes from risk parameters:**
- S1 + F1 + P1 combinations: typically no SIL required or SIL 1
- S2 + F2 + P2: typically SIL 2 or SIL 3
- Most industrial guarding scenarios with operator exposure during production: SIL 2

**Comparison with ISO 13849-1:** Both standards use S/F/P parameters from ISO 12100. ISO 13849-1 produces a required PL; IEC 62061 produces a required SIL. The results are comparable (PLd approximately equals SIL 2) but not interchangeable within the same subsystem calculation.

---

## Subsystem Architectures

The architecture of each subsystem determines its Hardware Fault Tolerance (HFT), which in turn sets the maximum SILCL the subsystem can achieve.

| Architecture | Description | HFT | PFHd improvement vs. 1oo1 | Typical use case |
|--------------|-------------|-----|--------------------------|------------------|
| **1oo1** (single channel) | One channel — any dangerous failure causes loss of safety function | 0 | Baseline | SIL 1 applications, simple interlocks with high-quality components |
| **1oo2** (dual channel redundant) | Two independent channels — both must fail for loss of safety function | 1 | Significant — PFHd proportional to (lambda_DU)^2 x T1 | SIL 2 and SIL 3 — standard for light curtains, dual-channel safety relays, redundant sensor pairs |
| **2oo2** (dual channel required) | Both channels must agree to actuate — a failure in either prevents actuation | 0 | None for safety (reduces spurious trips, not dangerous failures) | Output arrangements where spurious trips are unacceptable; used with caution due to HFT 0 |

**Key insight on 1oo2:** The PFHd for 1oo2 scales with the square of the dangerous undetected failure rate, which means small improvements in component quality or diagnostic coverage produce large improvements in subsystem PFHd. The proof test interval T1 also directly affects PFHd — shorter proof test intervals improve PFHd linearly.

---

## SILCL — Architectural Limits

SILCL (SIL Claim Limit) is the maximum SIL a subsystem can claim, determined by its Hardware Fault Tolerance (HFT) and Safe Failure Fraction (SFF). It is independent of the PFHd calculation.

**SFF definition:** SFF = (safe failure rate + dangerous detected failure rate) / total failure rate. A higher SFF means a greater proportion of failures either produce a safe state or are detected, leaving fewer undetected dangerous failures.

**SILCL table for Type B subsystems** (programmable electronics — the typical case for safety PLCs and certified safety devices):

| HFT | SFF less than 60% | SFF 60% to less than 90% | SFF 90% to less than 99% | SFF 99% or greater |
|-----|-------------------|--------------------------|--------------------------|-------------------|
| **0** (1oo1) | Not allowed | SIL 1 | SIL 2 | SIL 3 |
| **1** (1oo2) | SIL 1 | SIL 2 | SIL 3 | SIL 3 |
| **2** (triple redundant) | SIL 2 | SIL 3 | SIL 3 | SIL 3 |

**How to apply the table:**
1. Determine HFT from the subsystem architecture.
2. Calculate or estimate SFF from component failure rate data and the diagnostic measures implemented.
3. Read the SILCL from the table.
4. If the SILCL is less than the required SIL target, either change the architecture (add redundancy to increase HFT) or improve diagnostics (to increase SFF) — or both.

**Certified device SILCL:** When a safety PLC or safety device carries a certification (e.g., "SIL 2 capable"), that is the manufacturer's published SILCL. The subsystem SILCL is the minimum of all device SILCLs in the subsystem. The weakest device limits the entire subsystem.

---

## Worked Example: Light Curtain on Press

**Scenario:** A mechanical press with a light curtain protecting the point of operation. Risk assessment determines SIL 2 is required (SIL 2 limit: total PFHd must be less than 10⁻⁶ /hr).

**SIL target:** SIL 2, total SRECS PFHd less than 1 × 10⁻⁶ /hr.

**Subsystem decomposition:**

| Subsystem | Device | Architecture | PFHd (from datasheet or calculation) | SILCL |
|-----------|--------|--------------|---------------------------------------|-------|
| Input | Safety light curtain (dual OSSD outputs) | 1oo2 (HFT 1) | 3.0 × 10⁻⁸ /hr | SIL 3 (per manufacturer certification) |
| Logic | Safety PLC (e.g., Pilz PNOZ m B0 or equivalent) | 1oo2 internal | 1.5 × 10⁻⁸ /hr | SIL 3 (per device certification) |
| Output | Two safety contactors in series (dual-channel) | 1oo2 (HFT 1) | 4.0 × 10⁻⁸ /hr | SIL 2 (from B10D and proof test calculation) |

**Total SRECS PFHd calculation:**

PFHd_total = 3.0 × 10⁻⁸ + 1.5 × 10⁻⁸ + 4.0 × 10⁻⁸ = 8.5 × 10⁻⁸ /hr

**SIL 2 verification:**
- PFHd requirement: less than 1.0 × 10⁻⁶ /hr
- Calculated PFHd: 8.5 × 10⁻⁸ /hr
- Result: PASS — 8.5 × 10⁻⁸ is well below 1.0 × 10⁻⁶ /hr. The SRECS meets the SIL 2 PFHd requirement.

**SILCL verification:**
- Required SIL: SIL 2
- Minimum subsystem SILCL: SIL 2 (output subsystem is the limiting element)
- Result: PASS — minimum SILCL equals or exceeds the required SIL 2.

**Conclusion:** The SRECS satisfies both the PFHd numerical requirement and the SILCL architectural requirement for SIL 2. Documentation should include the manufacturer datasheet references for all PFHd values, the proof test interval assumed for the contactor B10D calculation, and the SILCL certification references.

---

## PL vs. SIL — When To Choose This Standard

Both IEC 62061 and [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) are harmonized under the EU Machinery Directive. Both are valid for machinery safety functions. The choice depends on technology, team expertise, and system complexity.

| Aspect | ISO 13849-1 (PL) | IEC 62061 (SIL) — this standard |
|--------|-----------------|----------------------------------|
| **Metric used** | PLa through PLe | SIL 1 through SIL 3 |
| **Equivalent levels** | PLd approximately equals SIL 2; PLe approximately equals SIL 3 | — |
| **Best suited for** | Electromechanical devices, proven safety components, simpler architectures | Programmable SRECS, complex safety PLCs, multi-supplier system integration |
| **Software handling** | Prefers proven components; complex software requires IEC 61508-3 | Full SIL-appropriate software requirements via IEC 61508-3 when needed |
| **Quantitative basis** | Safety category combined with MTTFd and diagnostic coverage | PFHd sum across input, logic, and output subsystems |
| **Architectural metric** | Category (B, 1, 2, 3, 4) | Hardware Fault Tolerance (HFT) + Safe Failure Fraction (SFF) |
| **Proof test interval** | Affects DC calculation for electromechanical | Directly affects 1oo2 PFHd calculation — shorter T1 = lower PFHd |
| **Tools** | SISTEMA (TÜV, free), ISO 13849-1 certified calculators | SISTEMA, structured spreadsheet |
| **Multi-subsystem integration** | Possible but less explicit about PFHd summation | Explicit PFHd summation framework — natural fit for multi-supplier SRECS |
| **Can both be used on one machine?** | Yes — apply each standard to different subsystems with documented boundaries | Yes |

**Decision guidance:**
- Use ISO 13849-1 when the system is primarily electromechanical and the team is familiar with the category-based approach.
- Use IEC 62061 when the system includes a programmable safety controller, the SIL 2 or SIL 3 target requires rigorous quantification, or the design integrates certified safety devices from multiple suppliers.
- Use both when different subsystems have different technology types — document the boundary carefully and sum PFHd values consistently.

---

## Common Mistakes

1. **Using PFHd (high-demand metric) instead of PFDavg for a low-demand safety instrumented system.** IEC 62061 is for high-demand or continuous-demand mode only. If the safety function is demanded less than once per year, it is a low-demand SIS and IEC 61511 with PFDavg is the correct framework. Applying IEC 62061 to a low-demand system produces misleading results.

2. **Ignoring SILCL — achieving a low PFHd does not override the architectural SILCL cap.** A 1oo1 subsystem with SFF = 70% has a SILCL of SIL 1 regardless of how low its failure rate is. Using that subsystem in a SIL 2 application violates the architectural requirements even if the PFHd arithmetic appears to work out.

3. **Summing subsystem SIL levels instead of summing PFHd values.** SIL levels are not additive. PFHd values are additive. The correct procedure is: calculate the PFHd for each subsystem, sum the PFHd values, and verify the total against the SIL target PFHd limit. Do not attempt to combine SIL integers arithmetically.

4. **Using component MTBF (Mean Time Between Failures) instead of PFH or B10D for the PFHd calculation.** MTBF combines safe and dangerous failures and does not distinguish between them. The IEC 62061 calculation requires lambda_D (dangerous failure rate) or, for electromechanical devices, B10D. Using MTBF as a proxy for lambda_D overestimates the reliability of the safety function and produces an incorrect PFHd.

5. **Treating the SIL rating of a certified component as the SIL of the subsystem.** A component rated SIL 2 can contribute to a SIL 2 subsystem — but the subsystem SIL also depends on the full architecture, the combination of all components, the diagnostic coverage implemented, and the application program. A SIL 2 safety PLC used in a poorly designed application program in a 1oo1 architecture with poor diagnostics may not achieve a subsystem SILCL of SIL 2 for the complete design.

6. **Skipping the SRECS validation plan.** IEC 62061 Clause 8 requires a validation plan to be produced and executed before the SRECS is placed in service. Validation is not optional — it demonstrates that the complete SRECS, as installed and integrated, actually performs the specified safety functions under the specified conditions. Stopping at the design verification (PFHd calculation and SILCL check) without validation is non-compliant.

---

## Practical Checklist

Use this checklist for each safety function on a machine using IEC 62061:

- [ ] Safety function specified: initiation event, response action, target SIL, required response time, and proof test interval documented.
- [ ] SIL target derived from [ISO 12100]({{ '/standards/functional-safety/iso-12100/' | relative_url }}) risk assessment using S/F/P parameters and IEC 62061 SIL determination table.
- [ ] SRECS decomposed into input, logic, and output subsystems with documented boundaries.
- [ ] PFHd budget allocated to each subsystem before component selection begins.
- [ ] PFHd for each subsystem calculated from manufacturer datasheet values or from B10D and failure rate data; data sources documented.
- [ ] Total SRECS PFHd calculated as sum of subsystem PFHd values; confirmed to be less than or equal to SIL target PFHd limit.
- [ ] SILCL verified for each subsystem using HFT and SFF; all subsystem SILCLs at or above the required SIL.
- [ ] Common cause failure (CCF) assessment performed for all 1oo2 redundant channel arrangements; CCF avoidance measures documented.
- [ ] Application program for safety PLC developed, reviewed by an independent person, and tested against the safety function specification.
- [ ] SRECS validation plan produced and executed per Clause 8; validation results recorded.

---

## Lifecycle Application

IEC 62061 defines a safety lifecycle that spans from hazard identification through decommissioning. The key activities and the clause that governs them:

| Lifecycle stage | IEC 62061 activity | Governing clause |
|----------------|--------------------|-----------------|
| Hazard identification and risk assessment | Use ISO 12100; establish SIL targets per safety function | Clause 4 (scope); Clause 6.2 (SIL determination) |
| Safety function specification | Document each safety function with initiation event, response, SIL target, response time, proof test interval | Clause 6.2 |
| SRECS architecture | Decompose into subsystems; allocate PFHd budget; verify SILCL for each subsystem | Clause 6.3, Clause 6.4 |
| Subsystem design | Select architectures (1oo1, 1oo2); calculate PFHd from component data; verify DC and SFF | Clause 7 |
| SRECS integration | Integrate subsystems; verify interfaces; check common cause failure avoidance measures | Clause 6.5 |
| Application programming | Develop safety PLC application program per systematic integrity requirements for the target SIL | Clause 5 (systematic integrity); IEC 61508-3 for software |
| Validation | Execute validation plan; confirm SRECS performs each safety function as specified | Clause 8 |
| Operation and maintenance | Execute proof test plan at documented intervals; re-verify PFHd if proof test interval changes | Clause 9 |
| Modification | Re-assess PFHd and SILCL if SRECS is modified; re-execute validation for affected safety functions | Clause 10 |
