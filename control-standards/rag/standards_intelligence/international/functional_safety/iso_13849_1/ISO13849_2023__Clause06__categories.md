<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_13849
EDITION: 2023

HIERARCHY:
  clause: "6"
  clause_title: "Categories — Architecture Requirements"

INDEX_TAGS:
  topics: ["categories", "architecture", "fault_tolerance", "srp_cs", "safety_architecture"]
  systems: ["machinery", "control_system"]
-->

# ISO 13849-1:2023 — Clause 6 — Categories: Architecture Requirements

## 0. Why this clause matters

Category is the architecture decision — it determines how the safety function is structured, how faults are detected (or not), and what level of fault tolerance is provided. Category determines the achievable PL ceiling before any component data is calculated. A safety function cannot achieve PLe with a Category 3 architecture, no matter how reliable the components are. Understanding Categories is understanding what the system can and cannot achieve structurally.

## 1. Category B

**Architecture:** Single channel (1oo1) using basic safety principles.

- No dedicated diagnostic function; no fault detection mechanism.
- The safety function relies on correct component selection and basic design practices.
- Achieves up to **PLb** when well-tried components are used.
- If only basic components (not specifically well-tried), achieves **PLa** at most.

**Design requirements:**
- Use components designed and dimensioned to withstand expected stresses.
- Follow applicable standards for component design (e.g., electromechanical safety components per IEC 60947-5-1).

**Suitable for:** Very low-risk applications where failure of the safety function is unlikely to cause serious harm. Not suitable for regular operator access zones.

## 2. Category 1

**Architecture:** Single channel (1oo1) using well-tried components and well-tried safety principles.

- No diagnostic function; single channel only.
- The improvement over Category B is the component quality specification: well-tried means proven over time in safety applications (e.g., positive-opening contacts in safety relays, proven circuit topologies).
- Achieves up to **PLc**.

**Design requirements:**
- Components must be well-tried (defined in ISO 13849-2 Annex A for electromechanical; other annexes for hydraulic, pneumatic).
- Safety principles must be well-tried (e.g., fail-safe by de-energization).

**Suitable for:** Applications where hazardous exposure is infrequent and faults are unlikely to occur between inspections. Not suitable for high-frequency access or high-severity hazards.

## 3. Category 2

**Architecture:** Single main channel plus a periodic test channel (1oo1 + test function).

- The test channel periodically tests the safety function at a defined frequency.
- If the test detects a fault, a safe state is initiated.
- The test frequency must be ≥ 100× the demand rate for the safety function to ensure faults are detected before the next demand.
- Fault detection is not continuous — a fault between test cycles is not immediately detected.

**Design requirements:**
- The test function itself must be reliable; its MTTFd must be factored into the overall calculation.
- Test output must be monitored — the OTE (output test equipment) failure must be detectable.
- CCF measures must achieve ≥ 65 points (Annex F).

**Achievable PL:** PLb through PLd depending on MTTFd and DC.

**Suitable for:** Applications where a periodic (not continuous) test adequately covers the demand rate. Common in some light guarding and monitoring applications.

## 4. Category 3

**Architecture:** Dual channel (1oo2 with cross-monitoring).

- A single fault in any part of the SRP/CS does not cause loss of the safety function — the second channel maintains the safe state.
- Faults accumulate over time if undetected; the possibility of accumulated faults must be considered.
- When a single fault is detected (at or before next demand), the system must move to a safe state or provide a warning that prevents further machine operation.

**Design requirements:**
- Both channels must be independent — separate wiring, separate power paths where possible.
- Cross-monitoring must be implemented (safety relay with cross-monitoring, or safety PLC cross-fault detection).
- CCF measures must achieve ≥ 65 points (Annex F) — this is critical for Category 3 validity.
- MTTFd calculated per channel; both channels contribute.

**Achievable PL:** PLb through PLd depending on MTTFd and DC.

**Suitable for:** The most common choice for PLd applications — industrial E-stop, guard interlocks, light curtains interfaced to safety relays or safety PLCs.

## 5. Category 4

**Architecture:** Dual channel with high DC (1oo2 with comprehensive diagnostics).

- Single fault is detected before or at the next demand for the safety function.
- The system is designed so that an accumulation of undetected faults cannot cause loss of the safety function — this is the key distinction from Category 3.
- DC ≥ 99% (High) is required.

**Design requirements:**
- High DC must be achieved and verified — all reasonable failure modes must be detected.
- Cross-monitoring must be comprehensive and continuous, not periodic.
- MTTFd must be High (30–100 years per channel).
- CCF measures must achieve ≥ 65 points (Annex F).
- Design analysis must demonstrate that accumulated undetected faults cannot produce a dangerous failure.

**Achievable PL:** PLe only.

**Suitable for:** PLe applications — rare in standard machinery; used in collaborative robotics nearest-person zones, some press guarding, and applications where a Category 3 design cannot achieve sufficient PL.

## 6. Category summary table

| Category | Architecture | Fault Tolerance | DC Required | Achievable PL | Typical Application |
|----------|-------------|-----------------|-------------|---------------|---------------------|
| B | Single channel | None | None | PLa–PLb | Very low risk; auxiliary functions |
| 1 | Single channel (well-tried) | None | None | Up to PLc | Infrequent access; low severity |
| 2 | Single + test function | Detected at next test | Low–Medium | PLb–PLd | Periodic-demand safety functions |
| 3 | Dual channel | Single fault tolerated | Low–High | PLb–PLd | Most industrial guarding; E-stop; light curtains |
| 4 | Dual channel, high DC | Single fault detected before next demand | High (≥99%) | PLe | Highest risk; cobot safety; specialized press guarding |

## 7. Common architecture examples

**Category 3 — Two-channel E-stop with safety relay:**
- Channel 1: NC contact of E-stop → Safety relay input A1
- Channel 2: NC contact of E-stop → Safety relay input A2 (cross-monitoring relay)
- Safety relay monitors both channels and detects cross-faults between channels
- Output contacts: dual-channel NC contacts in series in the power circuit to the drive enable
- MTTFd calculated for E-stop device (from B10d data) and safety relay (from datasheet)
- DC = Medium (cross-monitoring by safety relay detects short across channels)

**Category 4 — Dual-channel safety PLC with cross-monitoring:**
- Input device (e.g., light curtain) provides dual OSSD (Output Signal Switching Device) outputs
- Safety PLC reads both OSSD channels on separate input cards with separate 0V references
- Safety PLC performs cross-fault monitoring at every program scan cycle
- Safety PLC output drives two separate output channels, each monitored by EDM feedback
- DC = High (continuous, scan-cycle-level diagnostic monitoring)
- This architecture is required for PLe and is typical of safety-rated collaborative robot cell guarding
