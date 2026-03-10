<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_13849
EDITION: 2023

HIERARCHY:
  clause: "Annex F"
  clause_title: "Common Cause Failure Scoring"

INDEX_TAGS:
  topics: ["CCF", "common_cause_failure", "categories", "redundancy", "annex_F"]
  systems: ["machinery", "control_system", "srp_cs"]
-->

# ISO 13849-1:2023 — Annex F — Common Cause Failure Scoring

## 0. Why this annex matters

CCF scoring is mandatory for Categories 2, 3, and 4. A CCF score below 65 points invalidates the Category claim — the redundancy in the architecture is not considered adequate against common cause events, and the design cannot be credited as meeting that Category. This is one of the most frequently overlooked requirements in ISO 13849-1 designs. Engineers implement dual-channel hardware and obtain safety relay cross-monitoring, then fail to document CCF scoring and unknowingly invalidate their Category 3 claim.

## 1. What CCF addresses

Common Cause Failure is a single event, condition, or shared vulnerability that simultaneously causes dangerous failures in both channels of a redundant system — negating the benefit of that redundancy.

Common CCF scenarios that Annex F is designed to prevent:

| CCF Scenario | Description |
|-------------|-------------|
| **EMI / electrical transient** | A voltage spike or electromagnetic pulse simultaneously damages both channel input circuits |
| **Shared power supply failure** | Both channels powered from the same supply — a supply failure takes out both channels together |
| **Environmental stress** | Temperature extreme, humidity, or vibration beyond component rating simultaneously degrades both channels |
| **Same component batch** | Both channels use components from the same manufacturing batch with a latent defect; both fail at approximately the same time |
| **Software / firmware** | Same firmware version with a systematic error runs on both channels (particularly relevant to programmable devices) |
| **Installation error** | Wiring error or commissioning mistake affects both channels simultaneously |

Without CCF countermeasures, a dual-channel design may provide no more protection than a single-channel design against these failure modes.

## 2. Key measures and point values

Annex F allocates points across approximately seven categories of measures. The total available is 100 points; 65 is the minimum passing score. Key measures:

**Note:** The actual Annex F table distributes points across approximately 7 categories with sub-measures. The exact point allocation should be confirmed from the normative table in ISO 13849-1:2023, Annex F, Table F.1. The values below are illustrative approximations for practical use; practitioners should use the SISTEMA software or official Annex F worksheet to perform the formal score.

| Measure | Max Points | Description |
|---------|-----------|-------------|
| **Separation / segregation of channels** | 15 | Physical separation of channel wiring, components, and circuits. Different cable trays, conduits, or routing paths for the two channels. |
| **Diversity (different technology or design)** | 20 | Using different technology for corresponding elements in each channel (e.g., electromechanical relay in one channel, solid-state in the other; or different manufacturers' E-stop devices). |
| **Design / application / experience** | 5 | Use of proven design methods and component selection based on documented application experience; avoidance of known failure-prone topologies. |
| **Assessment and monitoring** | 5 | Regular inspection, testing, and monitoring of the safety system to detect degradation before it accumulates to a CCF condition. |
| **Training / competence** | 5 | Personnel involved in design, installation, and maintenance are competent; documented training records. |
| **Environmental resistance** | Up to 35 (distributed across sub-measures) | Components on both channels are rated and tested to the same environmental standards (e.g., EN 60068 temperature, humidity, vibration tests) and protected from the common environment that could cause simultaneous failure. |
| **Protection against overvoltage / overcurrent** | (part of environmental) | Both channels have independent overvoltage and overcurrent protection; not sharing a single fuse or SPD. |

## 3. Typical path to 65 points

A practical example of how a Category 3 design achieves the minimum 65 points:

| Measure Applied | Points Claimed |
|----------------|---------------|
| Channels routed in separate cable ducts / conduits; no shared tray | 15 |
| Different E-stop device manufacturers on each channel (or electromechanical + OSSD technology) | 20 |
| Annual safety function validation inspection with documented checklist | 5 |
| Design and commissioning by personnel with documented safety competence | 5 |
| Both channels rated to IEC 60068-2 for temperature range; independent 24 VDC supplies with separate fusing | 15 |
| CCF analysis documented in the Technical File | 5 |
| **Total** | **65** |

This represents the minimum viable CCF design. Additional measures — additional separation, further diversity, environmental qualification — push the score higher and provide more margin.

## 4. Common pitfalls

**Same cable duct for both channels:**
The most frequent CCF failure. Running both channel wires in the same cable tray or conduit exposes them to the same mechanical damage, same electrical interference, and same installation mistakes. Loses the 15 separation points — immediately reduces maximum achievable score to 85, making 65 harder but still possible with strong diversity and environmental measures. Best practice: always route channels in separate ducts.

**Same component batch / supplier for both channels:**
Using the same component (same part number, same manufacturer, same batch) for corresponding elements in Channel 1 and Channel 2 sacrifices diversity points. Latent batch defects affect both channels equally. Solution: specify diversity by using different manufacturers or different technologies for symmetric channel elements.

**Shared power supply for both channels:**
Powering both channels from the same 24 VDC supply (e.g., one PSU feeding both input circuits and both output circuits) creates a single point of failure that bypasses all channel redundancy. A supply failure, surge, or wiring error takes down both channels simultaneously. Solution: separate PSUs or at minimum separate fusing with separate distribution points for each channel.

**Not documenting CCF:**
Having implemented the measures above but not producing a completed Annex F score sheet means the measures cannot be verified during audit or CE marking review. The Technical File must contain the completed CCF scoring documentation. Without it, the Category claim cannot be substantiated regardless of what is actually in the design.

**Over-relying on the safety relay:**
A safety relay with cross-monitoring does not by itself satisfy CCF. The relay monitors for cross-channel faults in the wiring, but CCF measures must address the input device, wiring routing, supply, and environmental exposure — all of which are outside the relay itself.
