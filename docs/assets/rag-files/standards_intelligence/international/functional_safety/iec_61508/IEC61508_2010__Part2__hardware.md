<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_61508
EDITION: 2010

HIERARCHY:
  clause: "Part 2"
  clause_title: "Requirements for E/E/PE Safety-Related Systems (Hardware)"

INDEX_TAGS:
  topics: ["functional_safety", "hardware_fault_tolerance", "safe_failure_fraction", "pfdavg", "pfhd", "silcl", "type_a", "type_b"]
  systems: ["all_industries", "control_system", "safety_plc"]
-->

# IEC 61508:2010 — Part 2 — Hardware Requirements

## 0. Why this matters

Part 2 defines how to quantify hardware safety integrity. It establishes the concepts of Hardware Fault Tolerance (HFT), Safe Failure Fraction (SFF), and Type A/B subsystem classification that underpin all modern functional safety hardware analysis.

Specifically:
- The SILCL tables in IEC 62061 Annex A derive directly from Part 2 Table 3 concepts
- SIL assignment in IEC 61511 uses the same HFT and SFF framework
- Safety PLC manufacturer certification documents reference Part 2 to state the maximum SIL the device can be used in
- Understanding Part 2 allows engineers to evaluate why a 1oo2 architecture is required at SIL 3 and why a 1oo1 architecture may be acceptable at SIL 1 or SIL 2 with sufficient SFF

## 1. Hardware fault tolerance (HFT)

**Definition:** The number of faults a subsystem can tolerate while still performing its required safety function.

| HFT | Architecture | Description |
|-----|-------------|-------------|
| HFT 0 | 1oo1 (single channel) | One fault causes loss of safety function |
| HFT 1 | 1oo2 (dual channel) | One fault tolerated; two simultaneous faults cause loss of safety function |
| HFT 2 | 2oo3 (voted triple) | Two simultaneous faults tolerated |

Higher HFT allows a higher SIL claim. At SIL 3, HFT 1 is typically required for Type B subsystems. At SIL 1–2, HFT 0 may be acceptable with sufficient SFF.

HFT addresses **random hardware failures** (component wear-out, random electronic failures). It does not address common-cause failures — those are addressed separately by the beta factor (CCF analysis) and diversity requirements.

## 2. Safe failure fraction (SFF)

**Definition:** The proportion of failures that lead to a safe state or are detected by diagnostics.

```
SFF = (λS + λDD) / (λS + λD)
```

Where:
- λS = rate of safe failures (failures that do not compromise the safety function)
- λDD = rate of dangerous detected failures (dangerous failures caught by diagnostics)
- λD = total dangerous failure rate (λDD + λDU)
- λDU = rate of dangerous undetected failures

**Interpretation:**
- High SFF means most failures are either safe or caught before they defeat the safety function
- A subsystem with SFF = 90% means 10% of all failures are dangerous and undetected
- Higher SFF allows a higher SIL claim at the same HFT

**Diagnostic Coverage (DC)** is a related metric used in IEC 62061 and ISO 13849-1:
```
DC = λDD / λD
```
DC expresses the fraction of dangerous failures that are detected. High DC raises SFF.

## 3. Type A vs Type B subsystems

The classification affects the minimum HFT required for a given SIL.

| Attribute | Type A | Type B |
|-----------|--------|--------|
| Definition | All failure modes of constituent components are well defined and quantifiable | Not all failure modes are known |
| Examples | Simple relays, contactors, pressure switches, solenoid valves | PLCs, microprocessors, complex ASICs, safety relays with internal microprocessors |
| Failure rate data | Available from historical data or standards (e.g., SN 29500, IEC TR 62380) | Often derived from analysis or manufacturer data; not fully characterised |
| SIL claim impact | Can achieve a given SIL at lower HFT | Requires higher HFT or SFF to achieve the same SIL |

**Why it matters:** A Type B subsystem (any PLC-based safety system) cannot claim SIL 3 at HFT 0 regardless of SFF. This is why SIL 3 systems almost always require redundant architectures.

## 4. PFDavg vs PFHd modes

The mode of operation determines which metric applies and how the system is designed and tested.

| Parameter | PFDavg (low-demand mode) | PFHd (high-demand / continuous mode) |
|-----------|--------------------------|---------------------------------------|
| Full name | Probability of Failure on Demand, averaged | Probability of dangerous Failure per Hour |
| Units | Dimensionless probability | Per hour (/hr) |
| When demanded | Rarely — less than once per year | Frequently — at least once per year, or continuously |
| Testing approach | Proof tests at defined intervals (PTI) | Continuous diagnostics, repair on detection |
| Typical domain | Process SIS (IEC 61511) | Machinery safety (IEC 62061) |
| Example safety function | Emergency shutdown of a pressure vessel (demanded only during process upset) | Light curtain stopping a press (demanded every cycle) |

**Key distinction:** In low-demand mode, the safety function sits dormant most of the time. Its reliability is tested periodically. In high-demand mode, the safety function operates frequently, and its failure rate per hour is directly relevant to risk.

Mixing these metrics — applying PFDavg where PFHd is required, or vice versa — is a significant error that can result in underestimating risk by orders of magnitude.

## 5. Random hardware integrity — simplified architectural constraints

The following tables represent the conceptual structure of IEC 61508-2 Table 3. These are simplified representations; the normative source is the standard itself.

**Type A subsystems — Maximum SIL achievable:**

| SFF | HFT 0 | HFT 1 | HFT 2 |
|-----|-------|-------|-------|
| < 60% | SIL 1 | SIL 2 | SIL 3 |
| 60% to < 90% | SIL 2 | SIL 3 | SIL 4 |
| 90% to < 99% | SIL 3 | SIL 4 | SIL 4 |
| ≥ 99% | SIL 3 | SIL 4 | SIL 4 |

**Type B subsystems — Maximum SIL achievable:**

| SFF | HFT 0 | HFT 1 | HFT 2 |
|-----|-------|-------|-------|
| < 60% | Not allowed | SIL 1 | SIL 2 |
| 60% to < 90% | SIL 1 | SIL 2 | SIL 3 |
| 90% to < 99% | SIL 2 | SIL 3 | SIL 4 |
| ≥ 99% | SIL 3 | SIL 4 | SIL 4 |

**Note:** The SILCL tables in IEC 62061 Annex A are the machinery-specific derivation of these concepts, restated in terms of PFHd ranges and IEC 62061 subsystem categories. When working with machinery, use the IEC 62061 Annex A tables directly rather than deriving from Part 2.

## 6. Change log

- 2026-03-06 — Phase 3 corpus creation; Part 2 hardware requirements document established.
