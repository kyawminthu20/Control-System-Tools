<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_62061
EDITION: 2021

HIERARCHY:
  clause: "Annex A"
  clause_title: "SILCL and SIL Capability Tables"

INDEX_TAGS:
  topics: ["functional_safety", "sil", "srecs", "machinery", "silcl", "hft", "sff", "architectural_constraints"]
  systems: ["machinery", "control_system", "safety_plc"]
-->

# IEC 62061:2021 — Annex A: SILCL and SIL Capability Tables

## 0. Why This Annex Matters

Annex A defines the SILCL (SIL Claim Limit) — the maximum SIL a subsystem can claim, regardless of how low its calculated PFHd is. This is the architectural constraint that prevents a designer from claiming high SIL solely by using components with very low failure rates, without also implementing the architectural robustness (redundancy, diagnostics, software quality) that high SIL demands.

The SILCL is a binding cap. If a subsystem has a SILCL of 2, it cannot be used in an application requiring SIL 3, even if the PFHd calculation produces a value in the SIL 3 range. Both criteria — PFHd within the SIL target range AND SILCL at least equal to the SIL target — must be satisfied.

Understanding SILCL is essential because:
- Certified safety devices publish their SILCL (or SIL capability rating). Using a device rated SILCL 2 in a SIL 3 subsystem is not permitted without additional measures.
- The SILCL of a complete subsystem is the minimum of the SILCL of its constituent devices.
- Achieving a low PFHd through careful component selection does not raise the SILCL — only architectural changes (adding redundancy, improving diagnostics, improving software processes) raise the SILCL.

---

## 1. SILCL Definition

SILCL (SIL Claim Limit) is defined as the maximum SIL that a subsystem architecture can support, given:
1. Its Hardware Fault Tolerance (HFT) — the number of faults the architecture can tolerate without losing the safety function.
2. Its Safe Failure Fraction (SFF) — the proportion of all failures that lead to a safe state or are detected.
3. The subsystem type (Type A or Type B) — characterizing how well the failure behavior of the subsystem can be determined.

A subsystem's SILCL is determined before the PFHd calculation. It is a property of the architecture and the component types used, not of the numerical failure rate values.

**Relationship between SILCL and the certified SIL of devices:** When a device manufacturer publishes a SIL capability rating (e.g., "SIL 2 capable" or "SILCL 2"), they have performed the HFT and SFF analysis for that device and determined its SILCL. The machinery builder using the device as a subsystem element must verify that the subsystem SILCL (which depends on all elements together) meets the SIL target.

---

## 2. Hardware Fault Tolerance (HFT)

HFT is the number of faults within the subsystem that can be tolerated while the safety function is maintained. The HFT is determined by the subsystem architecture:

**HFT 0:** A single fault causes loss of the safety function.
- Architecture: 1oo1 (single channel) or 2oo2 (dual channel, both required)
- The subsystem cannot tolerate any dangerous fault while maintaining the safety function.
- 1oo1 example: a single safety relay contact that, if failed, prevents the safety function from responding.
- 2oo2 example: two contactors in series, where a failed-open contactor in either channel prevents actuation of the safety output.

**HFT 1:** A single fault does not cause loss of the safety function.
- Architecture: 1oo2 (dual channel redundant) or 2oo3 (two out of three voting)
- One channel can fail dangerously and the safety function is still maintained by the remaining channel.
- 1oo2 example: dual-channel light curtain with two OSSD outputs — one channel failing dangerous does not prevent the safety function because the other channel still operates.

**HFT 2:** Two simultaneous faults do not cause loss of the safety function.
- Architecture: 1oo3 or equivalent triple redundancy
- Very rarely required for machinery; adds significant complexity and cost.
- Applicable for SIL 3 subsystems in some configurations.

**HFT is an architectural property:** HFT cannot be improved by selecting more reliable components. The only way to improve HFT is to change the architecture (add redundancy).

---

## 3. Safe Failure Fraction (SFF)

SFF is the fraction of the total failure rate that leads to a safe state or is detected (and therefore does not result in an undetected dangerous condition being present in the subsystem):

SFF = (lambda_S + lambda_DD) / (lambda_S + lambda_D)

where:
- lambda_S = safe failure rate (failures that cause the subsystem to go to the safe state — nuisance trips)
- lambda_DD = dangerous detected failure rate (failures that are dangerous but detected by diagnostics)
- lambda_D = total dangerous failure rate (lambda_DD + lambda_DU)

**Interpretation:**
- A high SFF means most failures either go safe or are detected — the undetected dangerous failure mode is a small fraction of all failures.
- A low SFF means a significant proportion of all failures are dangerous and undetected — the subsystem is less architecturally capable of supporting high SIL.

**Relation to diagnostic coverage:** DC = lambda_DD / lambda_D. SFF combines DC with the safe failure rate. A subsystem with many safe failures (safe outputs go safe on fault) naturally has a higher SFF even at modest DC.

**SFF ranges and their significance:**
- SFF less than 60%: most failures are dangerous and undetected. Very restrictive SILCL implications.
- SFF 60% to less than 90%: moderate. Acceptable for SIL 1 or SIL 2 at appropriate HFT.
- SFF 90% to less than 99%: good. Enables SIL 2 at HFT 0 and SIL 3 at HFT 1.
- SFF greater than or equal to 99%: excellent. Enables SIL 3 at HFT 0. Achievable with high-DC diagnostics.

---

## 4. SILCL Table

The following table applies to **Type B subsystems** — subsystems where the failure behavior cannot be fully determined (the typical case for programmable electronics such as safety PLCs, microcontroller-based safety devices, and complex digital safety components).

Type A subsystems are those where all failure modes are well defined, all failure modes in all parts are known, and failure behavior in all environmental conditions can be fully determined. True Type A subsystems are rare in modern machinery safety applications — most safety PLCs and programmable safety devices are Type B.

**SILCL for Type B subsystems:**

| HFT | SFF less than 60% | SFF 60% to less than 90% | SFF 90% to less than 99% | SFF 99% or greater |
|-----|-------------------|--------------------------|--------------------------|-------------------|
| 0 | Not allowed | SIL 1 | SIL 2 | SIL 3 |
| 1 | SIL 1 | SIL 2 | SIL 3 | SIL 3 |
| 2 | SIL 2 | SIL 3 | SIL 3 | SIL 3 |

**Reading the table:**
- A 1oo1 subsystem (HFT 0) with SFF = 95% has a SILCL of SIL 2. It cannot support SIL 3, even if the PFHd calculation produces a value below 10⁻⁷ /hr.
- A 1oo2 subsystem (HFT 1) with SFF = 80% has a SILCL of SIL 2. Improving SFF to 95% raises the SILCL to SIL 3.
- A 1oo1 subsystem (HFT 0) with SFF below 60% cannot be used in any SIL-rated application without redesign.

**Note on Type A subsystems:** For Type A subsystems (simple electromechanical devices where all failure modes are known), the SILCL table is slightly more permissive — HFT 0 with SFF greater than or equal to 60% allows SIL 2 rather than SIL 1. In practice, most designers conservatively apply the Type B table unless they have specific justification for classifying a subsystem as Type A.

**Minimum SILCL from certified devices:** When using a device certified to a given SIL or SILCL, that rating is the manufacturer's published SILCL for that device. The subsystem SILCL is the minimum of all device SILCLs in the subsystem. A subsystem consisting of a SILCL 3 safety PLC, SILCL 2 certified input device, and SILCL 3 certified output device has an overall subsystem SILCL of SIL 2 (limited by the input device). Upgrading the input device to SILCL 3 would raise the subsystem SILCL to SIL 3.

---

## 5. Systematic Integrity

The SILCL determined from the HFT/SFF table is the maximum SILCL from a random hardware failure perspective. The actual achievable SILCL is further bounded by the systematic capability of the subsystem — the ability to prevent and detect systematic failures.

Systematic failures include:
- Software design errors and coding mistakes.
- Incorrect specification or requirements errors.
- Design errors in the safety function logic.
- Environmental sensitivity not addressed in design (temperature extremes, vibration, EMI).
- Human factors in the application programming of the safety PLC.

**Systematic integrity requirements by SIL:**

- **SIL 1:** Basic software engineering practices. Structured design, code review, documented test cases.
- **SIL 2:** More rigorous software development lifecycle. Formal requirements, traceable design, independent verification. For safety PLC application programming: use of certified safety function blocks, documented application program review by a person independent of the author.
- **SIL 3:** Highly rigorous software development. Formal methods or structured analysis required for complex logic. Independent safety assessment by a competent body. Extensive validation testing under worst-case conditions.

**Practical implication:** For most machinery applications using certified safety PLCs:
- The device manufacturer has addressed systematic integrity for the internal software (firmware, operating system) of the safety PLC up to the device's certified SIL.
- The machinery builder is responsible for systematic integrity of the application program loaded into the safety PLC.
- For SIL 2 applications, this means the application program must be developed with a defined process, documented, reviewed by an independent reviewer, and tested against the safety function specification.
- The SILCL of the complete subsystem (hardware plus application software) is bounded by the lower of the hardware SILCL and the systematic capability demonstrated for the application software.

**Assessment and documentation:** Systematic capability cannot be numerically calculated in the same way as PFHd. It is assessed by evaluating the development process, the tools used, the qualifications of the personnel, and the review and testing rigor. For certified safety PLCs, the device certification covers the internal systematic capability — the burden on the machinery builder is primarily the application program and the integration process.
