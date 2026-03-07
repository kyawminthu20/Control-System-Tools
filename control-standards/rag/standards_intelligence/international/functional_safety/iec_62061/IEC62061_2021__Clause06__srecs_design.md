<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_62061
EDITION: 2021

HIERARCHY:
  clause: "6"
  clause_title: "SRECS Design — SIL Determination and Allocation"

INDEX_TAGS:
  topics: ["functional_safety", "sil", "srecs", "machinery", "pfhd", "sil_determination", "risk_parameters"]
  systems: ["machinery", "control_system", "safety_plc"]
-->

# IEC 62061:2021 — Clause 6: SRECS Design — SIL Determination and Allocation

## 0. Why This Clause Matters

Clause 6 defines the top-level design process for the SRECS (Safety-Related Electrical Control System). It establishes how to:
1. Specify safety functions in a form suitable for quantitative verification.
2. Determine the required SIL for each safety function from the risk parameters established during risk assessment.
3. Decompose the SRECS into subsystems, each with an allocated PFHd budget.

This clause is where the bridge from risk assessment (ISO 12100) to engineering design is built. The output of Clause 6 — a list of safety functions with SIL targets and a decomposed subsystem architecture with PFHd allocations — is the input to Clause 7 subsystem design. If Clause 6 is not done rigorously, the subsystem design in Clause 7 cannot be correctly verified.

---

## 1. Safety Function Specification

Each safety function must be specified before any SIL determination or subsystem design is performed. IEC 62061 requires each safety function specification to document:

**Required attributes for each safety function:**

- **Initiation event (or demand):** What triggers the need for the safety function? Examples: guard door opened, emergency stop actuated, light curtain beam broken, pressure exceeds set point.

- **Response action:** What does the SRECS do in response? Examples: de-energize the main drive contactor, engage the brake, stop the robot motion in the current axis.

- **Target SIL:** Derived from the risk assessment. This is the design target that must be achieved by the complete SRECS for this safety function.

- **Required response time:** How quickly must the safety function respond after the demand? This is a functional requirement that affects architecture selection, not directly the SIL calculation, but it can constrain which subsystem architectures are feasible.

- **Proof test interval:** How frequently will the SRECS be tested under real or simulated demand conditions to detect latent faults? This directly affects the PFHd calculation for 1oo2 architectures.

**Same requirement as ISO 13849-1:** The requirement to document each safety function with a structured specification is the same approach required by ISO 13849-1 Clause 4. If a machine uses both standards for different subsystems, the safety function specification format is compatible — both require the same fundamental information.

**Documentation standard:** The safety function specification is a controlled document. It must be maintained and kept consistent with the SRECS design. Changes to either the machine hazard profile or the SRECS design that affect the specification require a documented review.

---

## 2. SIL Determination from Risk Parameters

IEC 62061 uses the same S/F/P risk parameters as ISO 12100 and ISO 13849-1, but applies them through a different quantitative route to arrive at a SIL rather than a PL.

**Risk parameters (same definitions as ISO 12100):**

- **S — Severity of injury:** S1 = reversible injury; S2 = irreversible injury or death.
- **F — Frequency/duration of exposure:** F1 = infrequent or short duration; F2 = frequent, continuous, or long duration.
- **P — Possibility of avoidance:** P1 = possible under specific conditions; P2 = scarcely possible.

**K-factor (demand rate):** IEC 62061 adds a K parameter that accounts for the frequency at which the hazardous situation occurs (the demand rate on the safety function). This is distinct from the F parameter, which captures the exposure of persons to the hazard. The K-factor adjusts the SIL determination to account for systems where the safety function is demanded very rarely (which reduces the risk contribution) versus systems with continuous or frequent demands.

**SIL determination table approach:**

IEC 62061 provides a table (in the informative annexes and in the normative risk assessment clause) that maps the combination of S, F, P, and K to a required SIL. The table produces one of four outcomes: SIL 1, SIL 2, SIL 3, or "no safety requirement" (the risk is low enough that a dedicated safety function is not required).

**Approximate SIL ranges for machinery:**

- **SIL 1:** Lower-risk situations. Minor injury possible, infrequent exposure, reasonable avoidance possibility.
- **SIL 2:** Medium-risk situations. Most industrial machinery guarding falls here — irreversible injury possible, frequent exposure during operation, limited avoidance ability. SIL 2 is the most common target for safety functions on industrial machines. It corresponds approximately to PLd in ISO 13849-1 terms.
- **SIL 3:** High-risk situations. Irreversible injury or death, continuous exposure, avoidance essentially impossible. Rarely required for typical industrial machinery but applicable to some heavy machinery, press systems, and automated guided vehicles in high-traffic areas.

**Important note on comparison with ISO 13849-1:** When both standards are used on different subsystems of the same machine, the SIL and PL targets should be cross-checked for consistency using the equivalence table in ISO/TR 62061-1. SIL 2 corresponds approximately to PLd, but the equivalence is approximate and should not be used to claim that a PLd-verified subsystem automatically meets SIL 2 requirements — the specific requirements of each standard still apply to that subsystem.

---

## 3. SIL Levels and PFHd Limits

IEC 62061 uses PFHd (Probability of dangerous Failure per Hour) in high-demand or continuous-demand mode as the quantitative measure of safety integrity. The standard is applicable to machinery where the safety function is demanded frequently enough to be classified as high-demand mode (demand rate greater than once per year is the IEC 61508 criterion for high-demand mode).

For low-demand systems (demand rate less than once per year), PFDavg (average Probability of Failure on Demand) is the appropriate metric and IEC 61511 (process safety) is the more appropriate standard. IEC 62061 is not intended for low-demand SIS applications.

| SIL | PFHd range (high-demand / continuous mode) | Design interpretation |
|-----|------------------------------------------|-----------------------|
| SIL 1 | greater than or equal to 10⁻⁶ /hr and less than 10⁻⁵ /hr | Total SRECS PFHd must be less than 10⁻⁵ /hr |
| SIL 2 | greater than or equal to 10⁻⁷ /hr and less than 10⁻⁶ /hr | Total SRECS PFHd must be less than 10⁻⁶ /hr |
| SIL 3 | greater than or equal to 10⁻⁸ /hr and less than 10⁻⁷ /hr | Total SRECS PFHd must be less than 10⁻⁷ /hr |

**Reading the table:** SIL 2 means the SRECS as a whole (all subsystems combined) must have a PFHd that falls within the SIL 2 range — that is, less than 10⁻⁶ per hour. The lower the PFHd, the better the safety integrity. A total SRECS PFHd of 3 × 10⁻⁷ /hr satisfies SIL 2 because it is below the SIL 2 upper limit of 10⁻⁶ /hr.

---

## 4. SRECS Decomposition

IEC 62061 requires the SRECS to be decomposed into subsystems for the purpose of PFHd calculation and SIL verification. The standard defines a three-tier architecture that maps naturally to the physical elements of a safety control system:

**Standard three-subsystem decomposition:**

```
Input Device (Sensor / Initiator)
        |
        v
Logic Controller (Safety PLC / Safety Relay)
        |
        v
Output Device (Actuator / Contactor / Drive)
```

**Each subsystem:**
- Is designed and verified independently.
- Has its own calculated PFHd.
- Has its own SILCL (SIL Claim Limit — see Annex A) that caps the maximum SIL the subsystem can contribute.
- May itself be further decomposed into elements (components) for the PFHd calculation.

**Total SRECS PFHd = sum of subsystem PFHd values:**

PFHd_SRECS = PFHd_input + PFHd_logic + PFHd_output

This additive property is one of the most important features of the IEC 62061 approach. It means:
- If any subsystem has a very high PFHd (poor reliability), it will dominate the total and may prevent the SRECS from meeting the SIL target.
- The total must be less than or equal to the SIL target PFHd limit.
- Budget can be allocated unevenly across subsystems — a subsystem with a very low PFHd (highly reliable) leaves more budget for other subsystems.

**Example for SIL 2 target (total PFHd must be less than 10⁻⁶ /hr):**

If the input subsystem contributes PFHd = 3 × 10⁻⁷ /hr, the logic subsystem contributes PFHd = 2 × 10⁻⁷ /hr, and the output subsystem contributes PFHd = 4 × 10⁻⁷ /hr, then:
Total = 9 × 10⁻⁷ /hr — this is less than 10⁻⁶ /hr, so the SIL 2 requirement is satisfied.

---

## 5. SIL Allocation

SIL allocation is the process of distributing the total PFHd budget across subsystems before detailed design begins. This is a design decision, not a calculation — it defines the targets that each subsystem designer must meet.

**Allocation principles:**

**Logic subsystem typically receives the tightest allocation (lowest PFHd budget):** The logic controller affects every safety function that passes through it. A failure in the logic subsystem affects all the safety functions implemented in that SRECS, not just one. For this reason, designers typically specify a safety PLC with a certified PFH value that is well below the total budget, leaving more room for the input and output subsystems.

**Input and output subsystems share the remaining budget:** The remaining PFHd budget (total SIL limit minus logic PFHd) is split between input and output subsystems. The split is typically informed by the available hardware:
- Certified safety light curtains and safety interlock switches have published PFH values from the manufacturer.
- Safety output devices (contactors, drives with safe torque off) also have published PFH values.
- The designer selects devices that individually fall within the allocated budget for that subsystem.

**Allocation is not final until all subsystems are designed:** The initial allocation is a planning tool. As actual component PFHd values are obtained from datasheets and subsystem architectures are finalized, the actual PFHd values replace the allocated values. The final check verifies that the sum of actual PFHd values meets the SIL target.

**SILCL constraint:** The SIL allocation must also respect the SILCL of each subsystem. Even if a subsystem achieves a very low PFHd (satisfying the numerical requirement for SIL 3, for example), if its architecture only supports SILCL 2, it cannot be used in a SIL 3 application. The SILCL is an architectural cap that is independent of the PFHd calculation. See the Annex A file for the SILCL table and determination method.
