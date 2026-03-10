<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_61511
EDITION: 2016

HIERARCHY:
  clause: "16"
  clause_title: "Operation and Maintenance"

INDEX_TAGS:
  topics: ["proof_testing", "functional_testing", "maintenance", "modification", "change_control", "operational_readiness", "bypass_management"]
  systems: ["process_industry", "sis", "safety_instrumented_system"]
-->

# IEC 61511:2016 — Clause 16 — Operation, Maintenance, and Modification

## 0. Why this matters

The safety lifecycle does not end at commissioning. The SIS must maintain its integrity throughout the plant's operational life. Proof testing is the primary mechanism — it detects dangerous undetected (DU) failures that would otherwise accumulate and degrade the SIF's PFDavg. Without proof testing, the actual PFDavg increases over time until the SIL requirement is no longer met.

Modification management is equally critical: any change to the SIS — hardware, software, or operating conditions — can affect the SIL of one or more SIFs and must be managed through a formal change control process.

## 1. Proof testing — the core operation and maintenance requirement

Proof testing is a functional test of a SIF that reveals dangerous undetected failures not detected by the SIS diagnostics. The proof test interval (TI) is the time between successive proof tests. The TI is established during design and documented in the SRS.

**Why proof testing is mandatory:** DU failures accumulate over time. A valve that is stuck-open due to internal corrosion will not be detected by the SIS diagnostics. The proof test — full stroke of the valve to its safe position — reveals this failure. If the failure is detected and repaired before the next demand, the PFDavg remains within the design basis. If the valve is never tested, the probability of failure on demand grows toward 1.0.

### Proof test interval and PFDavg

The design PFDavg calculation assumes a specific TI. If the actual proof test interval exceeds the design TI, the actual PFDavg is higher than calculated, potentially breaching the SIL requirement.

**Example:** A SIF designed for PFDavg = 0.01 (SIL 2) with λDU = 2 × 10⁻⁵ /hr in a 1oo1 sensor:

- Design TI = 1 year (8,760 hours): PFDavg = 2 × 10⁻⁵ × 8,760 / 2 = 0.088 → SIL 1 only
- Design TI = 6 months (4,380 hours): PFDavg = 2 × 10⁻⁵ × 4,380 / 2 = 0.044 → SIL 1 only
- Conclusion: This sensor requires redundancy (1oo2) or a shorter TI or a lower λDU sensor to achieve SIL 2 from sensors alone

**Tracking proof test intervals:** Overdue proof tests are a compliance violation. The plant must track proof test due dates and escalate overdue tests through a formal process.

### Proof test coverage

Not all proof tests are 100% coverage. A functional test that does not reach the full safe state does not detect all DU failures. The proof test coverage (PTC) describes the fraction of DU failures that the proof test detects.

**PFDavg corrected for partial coverage:**

**PFDavg = (1 - PTC) × λDU × TI/2 + PTC × λDU × TI/2** (simplification)

A partial stroke test (PST) of a valve has PTC typically 0.5–0.7. A full stroke test has PTC approaching 1.0. If PST is used as the primary proof test method, the PFDavg improvement is less than a full stroke test, and the TI must be shorter to compensate.

## 2. Proof test procedures

Each SIF must have a documented proof test procedure. The procedure specifies:

| Element | Content |
|---------|---------|
| Test objective | Which failures the test is designed to detect |
| Preconditions | Process state required for testing; bypass status; operator notification |
| Test steps | Step-by-step instructions for each subsystem |
| Expected results | What correct operation looks like for each step |
| Failure criteria | What constitutes a failed proof test |
| Corrective action | What to do if the test fails |
| Records | What is recorded and where |
| Test coverage | What fraction of DU failures this test detects |
| Estimated duration | Time required to complete the test |
| Required competency | Who is authorized to conduct the test |

Proof test procedures must be kept current and reviewed when the SIF design or operating conditions change.

## 3. SIS bypass management

During proof testing, a SIF is taken out of service. The bypass procedure must ensure the process is protected during the bypass period.

**Bypass management requirements:**
- Bypass approval by a responsible person before bypass is implemented
- Alternative protection must be in place during the bypass (operator watch, reduced throughput, compensating controls)
- Time limit on the bypass — bypasses must not remain active beyond the period required for the test or maintenance
- Bypass record maintained — who approved, when implemented, when removed
- Automatic bypass timers on the logic solver (where available) — trip the SIS back in if bypass is not removed within the defined window

**Common bypass failure modes:**
- Bypass left in place after maintenance — operator forgets to reinstate the SIF
- Multiple SIFs bypassed simultaneously — removing multiple layers of protection
- Bypass implemented without alternative protection — the hazardous event occurs during an unprotected period

## 4. Functional safety audit

IEC 61511 requires periodic audits of the functional safety management system. The audit confirms:
- Proof tests are being performed at the required intervals
- Proof test records are complete and accurate
- SIS modifications are being managed through change control
- Competency of persons performing safety lifecycle activities is maintained
- The SRS remains current and reflects the as-built and as-operated SIS

## 5. Modification management

Any change to the SIS must be managed through a formal modification (Management of Change, MOC) process. Changes that affect a SIF include:

| Change type | Examples |
|-------------|---------|
| Hardware changes | Replacing a sensor with a different model; installing a valve in a new location |
| Software changes | Modifying logic solver application code; changing setpoints |
| Process changes | Changing operating conditions (temperature, pressure, flow rate) that affect sensor selection or failure rates |
| Proof test procedure changes | Changing the test method or interval |
| Operating procedure changes | Changes that affect operator IPL credit in LOPA |

### Modification process

For each proposed change:
1. **Impact assessment:** Identify which SIFs are affected; determine whether the SIL of the affected SIFs could be compromised
2. **Risk assessment update:** If LOPA assumptions change (initiating frequencies, IPL credits), re-run the LOPA for affected scenarios
3. **SRS update:** Update the SRS to reflect the change
4. **PFDavg recalculation:** Recalculate PFDavg for affected SIFs with the new design
5. **Verification and validation:** Verify the modified design against the updated SRS; functional test the modified SIF
6. **Documentation update:** Update all affected records — SRS, P&ID, logic diagram, proof test procedure
7. **Authorization:** Obtain required approvals before implementing the change; for SIL 2+, this typically requires a functional safety review

**Temporary changes:** Temporary modifications (e.g., a bypass or setpoint change for a turnaround) must be subject to the same MOC process as permanent changes and must be reversed within the defined period.

## 6. Decommissioning

When a SIS or SIF is permanently removed from service, the decommissioning activities must confirm:
- The hazardous event that the SIF was protecting against is no longer possible (process change eliminates the hazard), OR
- Alternative protection measures are permanently in place to provide equivalent risk reduction
- All documentation reflects the removal of the SIF from the safety case
- The logic solver application is updated to remove the decommissioned SIF

Partial decommissioning (removing one SIF from a multi-SIF SIS) must be assessed for impact on the remaining SIFs.

## 7. Competency requirements

All persons performing functional safety lifecycle activities must be competent for those activities. Competency includes:
- Knowledge of IEC 61511 requirements
- Knowledge of the specific process and its hazards
- Experience with the SIS technology being used
- Authorization to perform the specific activity (e.g., logic solver modification)

Competency must be documented — training records, qualifications, and experience logs for all persons performing safety lifecycle activities.

## 8. Change log

- 2026-03-07 — Phase 3 corpus creation; Clause 16 operation and maintenance document established.
