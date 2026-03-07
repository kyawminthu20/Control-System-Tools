<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_62061
EDITION: 2021

HIERARCHY:
  clause: "7"
  clause_title: "Subsystem Design — PFHd Calculation"

INDEX_TAGS:
  topics: ["functional_safety", "sil", "srecs", "machinery", "pfhd", "1oo1", "1oo2", "diagnostic_coverage", "failure_rate"]
  systems: ["machinery", "control_system", "safety_plc"]
-->

# IEC 62061:2021 — Clause 7: Subsystem Design — PFHd Calculation

## 0. Why This Clause Matters

Clause 7 is where the quantitative engineering work of IEC 62061 is performed. It provides:
- The architectural options for each subsystem (1oo1, 1oo2, 2oo2).
- The formulas for calculating PFHd for each architecture.
- Requirements for the diagnostic coverage that reduces the dangerous undetected failure rate.

The outputs of Clause 7 are the calculated PFHd values for each subsystem, which are then summed (per Clause 6) to verify the total SRECS PFHd meets the SIL target. Clause 7 is also where the SILCL architectural constraint becomes binding — the subsystem architecture determines the maximum SILCL, which caps the maximum SIL the subsystem can contribute regardless of how low its PFHd calculation is.

---

## 1. Subsystem Architectures

IEC 62061 defines subsystem architectures in terms of voting logic (how many channels must operate correctly for the safety function to be maintained) and Hardware Fault Tolerance (HFT — how many faults can be tolerated before the safety function is lost).

### 1oo1 — Single Channel (One out of One)

**Description:** A single channel performs the safety function. Any dangerous failure in the channel causes loss of the safety function.

**HFT:** 0 — no fault tolerance. A single dangerous failure causes loss of the safety function.

**Reliability characteristics:** The weakest architecture. PFHd equals the dangerous undetected failure rate of the single channel. No redundancy to mask failures.

**When appropriate:** For lower SIL targets (SIL 1) where the component failure rate is low enough that the PFHd requirement is met without redundancy, or where the subsystem relies on very high diagnostic coverage to compensate. Also appropriate where the safety system is regularly tested with short proof test intervals, since the proof test limits the accumulation of undetected faults.

**Example:** A single safety relay monitoring a single-channel emergency stop button. Appropriate for SIL 1 with high-quality components and frequent proof testing.

### 1oo2 — Dual Channel Redundant (One out of Two)

**Description:** Two independent channels, each capable of performing the safety function. The safety function is maintained unless both channels fail in a dangerous mode simultaneously. Any single dangerous failure causes a detected fault condition (discrepancy between channels), which can trigger a safe state.

**HFT:** 1 — one fault can be tolerated without loss of the safety function.

**Reliability characteristics:** Significantly better PFHd than 1oo1 for the same component failure rate because both channels must fail for the safety function to be lost. The probability of both failing independently within the proof test interval is much lower than the probability of either single channel failing.

**When appropriate:** SIL 2 and SIL 3 applications. Standard architecture for light curtains, dual-channel safety relays, and redundant sensor arrangements. Required for higher SILCL ratings.

**Example:** A dual-channel light curtain with OSSD1 and OSSD2 outputs monitored by a safety relay or safety PLC that cross-checks the two channels. Both channels must fail for loss of the safety function.

### 2oo2 — Dual Channel Required (Two out of Two)

**Description:** Both channels must agree and be operational for the safety function to be actuated. If either channel fails, the safety function cannot be triggered. This is used for output devices where spurious trips are costly — it improves availability at the expense of reliability (a failure in either channel prevents the safety action, not just loss of it).

**HFT:** 0 from a safety perspective — a failure in either channel can prevent the safety function from operating when demanded. This architecture is typically used to prevent spurious trips, not to improve safety integrity.

**When appropriate:** Output device arrangements where spurious stops cause significant production loss or secondary hazards (e.g., uncontrolled stops on certain machinery). Used with caution — the SILCL of a 2oo2 architecture is limited. Usually combined with diagnostic measures to detect failures in either channel.

**Note on HFT and SILCL:** The architecture designation (1oo1, 1oo2, 2oo2) maps to HFT, which in turn maps to the SILCL in the table in Annex A. 1oo2 gives HFT 1, which enables higher SILCL. 2oo2 gives HFT 0, like 1oo1.

---

## 2. PFHd for 1oo1 Subsystem

For a single-channel (1oo1) subsystem, all dangerous failures that are not detected by diagnostics accumulate and eventually cause loss of the safety function when it is demanded.

**Simplified PFHd formula for 1oo1:**

PFHd = lambda_DU

where lambda_DU is the dangerous undetected failure rate (per hour).

**Expanding lambda_DU from component data:**

lambda_DU = (1 - DC) x lambda_D

where:
- lambda_D = total dangerous failure rate of the subsystem (per hour)
- DC = diagnostic coverage — the fraction of dangerous failures that are detected by the diagnostic function

**Getting lambda_D from component data:**
- For electronic/solid-state components: use the failure rate from IEC 61508-2 Annex D generic data tables, or from manufacturer reliability data. The dangerous fraction of the total failure rate is typically specified as lambda_D.
- For electromechanical components (switches, contactors): use B10D — the number of operations at which 10% of devices fail dangerously. Convert to lambda_D using the formula: lambda_D = 0.1 / (B10D x T_cycle) where T_cycle is the average operating cycle time per hour.

**Effect of diagnostic coverage:** Higher DC reduces lambda_DU and therefore PFHd. For a 1oo1 subsystem, DC is the only lever available to improve PFHd — there is no redundancy. DC values are bounded:
- DC = 0: no diagnostics, lambda_DU = lambda_D
- DC = 60%: medium diagnostics, lambda_DU = 0.4 x lambda_D
- DC = 90%: good diagnostics, lambda_DU = 0.1 x lambda_D
- DC = 99%: excellent diagnostics, lambda_DU = 0.01 x lambda_D

Even with DC = 99%, the 1oo1 architecture has an architectural SILCL limit imposed by its HFT = 0 — see Annex A.

---

## 3. PFHd for 1oo2 Subsystem

For a dual-channel redundant (1oo2) subsystem, both channels must fail dangerously and the failure must go undetected within the proof test interval for the safety function to be lost.

**Simplified PFHd formula for 1oo2:**

PFHd approximately equals (lambda_DU)^2 x T1

where:
- lambda_DU = dangerous undetected failure rate of each channel (assuming identical channels)
- T1 = proof test interval in hours (the period between functional tests that detect latent faults)

**Why the formula works this way:** The probability that both channels fail independently within the proof test interval is approximately the product of the individual failure probabilities. Since probability of failure over interval T1 approximately equals lambda_DU x T1 for each channel, the joint probability is (lambda_DU x T1)^2. Dividing by T1 to get a rate gives PFHd approximately equals lambda_DU^2 x T1.

**Critical insight on proof test interval:** Because T1 appears directly in the formula, a shorter proof test interval gives a lower PFHd. Halving T1 halves PFHd. This means a 1oo2 architecture with monthly proof testing performs significantly better (lower PFHd) than the same architecture with annual proof testing. The proof test plan is therefore a design parameter, not just a maintenance procedure.

**Diagnostic coverage for 1oo2:** The DC in each channel reduces lambda_DU in each channel, which reduces PFHd quadratically (since lambda_DU appears squared in the formula). High DC on both channels is especially effective for 1oo2 architectures.

**Common cause failures (CCF):** For 1oo2 architectures, common cause failures — failures that defeat both channels simultaneously due to a shared cause (same environmental stress, manufacturing defect, software error) — must be assessed and managed. IEC 62061 and IEC 61508-2 provide scoring schemes for evaluating and claiming credit for CCF avoidance measures (physical separation, diverse technology, diversity in manufacturing supply, periodic proof testing).

---

## 4. Component Failure Rate Data Sources

PFHd calculations require quantitative failure rate data. IEC 62061 does not mandate a single source but requires that the source be documented and its basis justified.

**Primary data sources:**

**Manufacturer datasheets:** The preferred source for certified safety devices. Most manufacturers of safety PLCs, safety relays, light curtains, and safety output devices publish PFH values directly (the PFHd of the complete device in the operating mode intended). When using this data:
- Confirm the published PFH corresponds to the operating mode (high-demand or continuous, not low-demand mode PFDavg).
- Confirm the device is used within its rated operating conditions and within the certified application constraints.
- Note any assumptions on proof test interval that the manufacturer's published PFH depends on.

**IEC 61508-2 Annex D generic failure rate data:** Provides component-level failure rates for common electronic and electromechanical components when device-specific data is not available. These are generic rates based on historical field data. They are conservative and intended to be used when better data is unavailable.

**SISTEMA component library (TÜV Rheinland):** The SISTEMA software tool includes a component database with B10D values and failure rates for many common safety components. The library is maintained and updated. This is the most commonly used free tool for both ISO 13849-1 and IEC 62061 calculations.

**Exida SERH (Safety Equipment Reliability Handbook):** A commercial database of failure rate data for process and machinery safety equipment. More comprehensive than generic IEC 61508-2 data but requires a subscription.

**Field failure data:** Where a device has sufficient operational history, actual field failure rates can be used. Requirements for using field data are defined in IEC 61508-2 and include minimum fleet size and operating hours.

**Data hierarchy for decision making:** Use manufacturer published PFH data as the first choice. Fall back to SISTEMA library B10D data. Use IEC 61508-2 Annex D generic data only when component-specific data is unavailable.

---

## 5. Diagnostic Coverage (DC)

Diagnostic coverage (DC) is the fraction of the dangerous failure rate of a component or subsystem that is covered by automatic diagnostic measures. It is defined as:

DC = lambda_DD / lambda_D

where:
- lambda_DD = dangerous detected failure rate (failures that are dangerous but detected by the diagnostic)
- lambda_D = total dangerous failure rate

**Interpretation:** A DC of 90% means that 90% of dangerous failures are detected by the diagnostic function and will cause a safe state to be initiated (or at least a fault indication). The remaining 10% of dangerous failures are undetected and accumulate until a proof test reveals them.

**Equivalence to ISO 13849-1 DC:** The concept of diagnostic coverage in IEC 62061 is directly equivalent to the DC concept in ISO 13849-1. The same diagnostic measures (e.g., cross-monitoring of redundant channels, output feedback monitoring, test pulses on safety outputs) apply in both standards. The numerical ranges are also comparable:
- DC = 0: no diagnostics
- DC = 60%: low diagnostic coverage
- DC = 90%: medium diagnostic coverage
- DC = 99%: high diagnostic coverage

**How DC is set:** DC is not a property of the component alone — it is a property of the diagnostic measures implemented around the component in the subsystem design. A safety PLC performing cross-channel comparison on two sensor channels achieves high DC. A single sensor with no monitoring achieves DC = 0. The designer selects diagnostic measures to achieve the required DC level.

**DC and SILCL interaction:** Higher DC enables higher achievable SIL for the same architecture type. For a 1oo1 subsystem (HFT = 0), moving from no diagnostics (DC = 0) to high diagnostics (DC = 99%) increases the SILCL from "not allowed" to SIL 3 for Type B subsystems — see Annex A for the full table. DC is therefore both a quantitative parameter (reducing lambda_DU in the PFHd formula) and an architectural qualifier (enabling higher SILCL).

**Systematic vs. random hardware failures:** DC addresses random hardware failures. It does not address systematic failures (failures caused by design errors, software bugs, or incorrect specification). Systematic integrity is handled by the development process requirements in IEC 62061 Clause 5 and the software requirements referenced from IEC 61508-3.
