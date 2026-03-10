<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_13849
EDITION: 2023

HIERARCHY:
  clause: "5"
  clause_title: "Safety-Related Parts of Control Systems — MTTFd, DC, CCF"

INDEX_TAGS:
  topics: ["performance_level", "MTTFd", "diagnostic_coverage", "CCF", "srp_cs", "PFHd"]
  systems: ["machinery", "control_system"]
-->

# ISO 13849-1:2023 — Clause 5 — SRP/CS Requirements: MTTFd, DC, CCF

## 0. Why this clause matters

Clause 5 defines the three quantitative parameters — MTTFd, DC, and CCF — that determine the achievable PL within a chosen Category. Category selection (Clause 6) defines the architecture; Clause 5 fills in the numbers that confirm what PL that architecture actually achieves. A designer who picks Category 3 without calculating MTTFd, DC, and CCF has not completed the design — they have only selected a topology.

## 1. MTTFd — Mean Time To Dangerous Failure

MTTFd is the mean time to a dangerous failure per channel. It is a reliability measure for the safety-related components in a single channel of the SRP/CS.

| MTTFd Level | Range | Interpretation |
|------------|-------|----------------|
| Low | < 10 years | Component has low reliability; contributes less to PL |
| Medium | 10–30 years | Moderate reliability; typical for general industrial components |
| High | 30–100 years | High reliability; required for Category 4 and for PLe |

**How to determine MTTFd:**
- Preferred: manufacturer datasheet provides B10d (number of cycles to 10% dangerous failure) → calculate MTTFd = B10d / (0.1 × nop) where nop is annual operating cycles.
- Alternative: ISO 13849-1 Annex C and Annex D tables provide default MTTFd values for common component types when datasheet data is unavailable.
- Aggregation: When multiple components are in series in a channel, MTTFdchannel = 1 / Σ(1/MTTFdi) for each component.

**Critical distinction — MTTFd ≠ MTBF:**
- MTBF (Mean Time Between Failures) counts all failures, including safe failures that do not cause a hazardous situation.
- MTTFd counts only dangerous failures — those that could lead to loss of the safety function.
- A component with a high MTBF may still have a low MTTFd if most of its failure modes are dangerous. Always use MTTFd, not MTBF, in ISO 13849-1 calculations.

## 2. DC — Diagnostic Coverage

Diagnostic Coverage quantifies how effectively the diagnostic measures detect dangerous failures before they cause a hazardous event.

| DC Level | Range | Description |
|---------|-------|-------------|
| None | < 60% | No meaningful diagnostic function |
| Low | 60–90% | Basic monitoring (e.g., cross-monitoring with limited tests) |
| Medium | 90–99% | Substantial monitoring (e.g., EDM relay monitoring, plausibility checks) |
| High | ≥ 99% | Comprehensive monitoring (e.g., dynamic testing at every cycle) |

DC is set by the diagnostic measures implemented in the design — it is not a component property but a system design property. Annex E of ISO 13849-1 provides DC values for common diagnostic measures.

Examples:
- Cross-monitoring of two channels with no test: DC = None
- Monitoring of an output device with electrical feedback (EDM): DC = Medium
- Short-circuit detection on each input at every machine cycle: DC = High

## 3. CCF — Common Cause Failure

CCF is the probability that a single external event simultaneously causes dangerous failures in both channels of a redundant (Category 2, 3, or 4) system, negating the benefit of redundancy.

CCF is controlled by design measures scored using Annex F (see ISO13849_2023__AnnexF__ccf.md for full scoring detail):
- **Mandatory minimum:** 65 points out of 100 for Categories 2, 3, and 4.
- A score below 65 means the architecture does not qualify for the claimed Category — the redundancy is not considered valid.
- Key measures: channel separation, use of diverse technology, environmental protection, competence.

## 4. Combined PL determination

The achieved PL is determined by combining Category (architecture), MTTFd (per channel), and DC (avg). The table below summarizes achievable PL (approximate, from ISO 13849-1 Figure 5):

| Category | MTTFd | DC | Max Achievable PL |
|----------|-------|-----|-------------------|
| B | Low | None | PLa |
| B | Medium | None | PLb |
| 1 | High | None | PLc |
| 2 | Low | Low | PLb |
| 2 | Medium | Medium | PLc |
| 2 | High | Medium | PLd |
| 3 | Low | Low | PLc |
| 3 | Medium | Medium | PLd |
| 3 | High | High | PLd |
| 4 | High | High | PLe |

Note: This table represents achievable upper bounds. Actual PL also depends on meeting CCF requirements for Categories 2–4. If CCF score < 65, the architecture is not valid at that Category and the PL is reduced accordingly.

## 5. PFHd calculation

PFHd (Probability of dangerous Failure per Hour) is the quantitative output used to assign a PL and to compare with IEC 62061 SIL levels.

PFHd is derived from MTTFd, DC, and Category using formulas in ISO 13849-1 Annex K and the SISTEMA software tool (free, published by IFA/TÜV). General relationships:

- Higher MTTFd → lower PFHd → higher achievable PL
- Higher DC → lower effective PFHd (detected failures are not counted as undetected dangerous failures)
- Dual channel (Category 3/4) → PFHd is reduced compared to single channel at same MTTFd

**PL to SIL equivalence (approximate):**

| PL | PFHd Range | Comparable SIL (IEC 62061) |
|----|-----------|---------------------------|
| PLa | ≥ 10⁻⁵ /hr to < 10⁻⁴ /hr | — (no SIL equivalent) |
| PLb | ≥ 3×10⁻⁶ /hr to < 10⁻⁵ /hr | — (no SIL equivalent) |
| PLc | ≥ 10⁻⁶ /hr to < 3×10⁻⁶ /hr | SIL 1 |
| PLd | ≥ 10⁻⁷ /hr to < 10⁻⁶ /hr | SIL 2 |
| PLe | < 10⁻⁷ /hr | SIL 3 |

**Note:** PLa and PLb have no SIL equivalent per IEC 62061. IEC 62061 defines SIL 1 as its lowest level, with a PFHd range of ≥ 10⁻⁶ /hr to < 10⁻⁵ /hr — which only overlaps with PLc and above. Safety functions assessed at PLa or PLb cannot be directly compared to or replaced by a SIL-rated subsystem without re-evaluating the requirements.

This equivalence enables comparison between PL-designed subsystems (ISO 13849-1) and SIL-designed subsystems (IEC 62061) when they are combined in the same machine safety system. The SISTEMA tool exports PFHd values for direct use in IEC 62061 calculations.
