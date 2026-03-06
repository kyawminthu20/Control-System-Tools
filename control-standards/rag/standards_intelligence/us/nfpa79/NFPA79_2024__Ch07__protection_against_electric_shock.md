<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "7"
  chapter_title: "Protection Against Electric Shock"

INDEX_TAGS:
  topics: ["electric_shock", "touch_safe"]
-->


## 0. Hazard Model

The standard operates on a dual-risk model for electric shock:

* **Direct Contact:** Touching parts that are normally "live" (e.g., busbars, terminals).
* **Indirect Contact:** Touching conductive parts (like the machine frame) that have become energized due to a fault or insulation failure.
* **Threshold of Concern:** NFPA 79 generally considers voltages above **30V rms (42.4V peak) or 60V DC** to be hazardous in dry conditions, requiring specific protective measures.

## 1. Protective Measures

To mitigate these hazards, the standard mandates a "defense-in-depth" approach:

* **Insulation of Live Parts:** Live conductors must be completely covered with insulation that can only be removed by destruction (e.g., wire jackets).
* **Enclosures (Protection by Barriers):** Parts not otherwise insulated must be placed inside enclosures or behind barriers rated at least **IP2X** (finger-safe) or **IPXXB**.
* **Discharge of Residual Voltage:** Components that store energy (like large capacitors in VFDs) must be discharged to below **60V within 5 seconds** after power is removed, or be marked with a warning label stating the required wait time.

## 2. Control Voltage Considerations

One of the most effective ways to protect operators is the use of **PELV (Protective Extra-Low Voltage)** or **SELV (Safety Extra-Low Voltage)** systems.

* **Voltage Limits:** Using a 24VDC control system significantly reduces shock hazards compared to 120VAC.
* **Isolation:** PELV/SELV circuits must be electrically separated from higher voltage circuits by a safety isolating transformer or an equivalent power supply.
* **Grounding:** In a PELV system, one side of the secondary circuit is connected to the protective bonding circuit to ensure that a fault triggers a fuse rather than energizing the machine frame.

## 3. Panel Layout Implications

Designers must organize the internal layout of the control cabinet to maintain "touch-safety":

* **Finger-Safe Components:** Modern design favors components where terminals are recessed, preventing accidental contact during troubleshooting.
* **Separation of Voltages:** High-voltage power distribution (e.g., 480V) should be physically separated or partitioned from low-voltage control signals (e.g., 24V) to prevent induction and accidental cross-contact.
* **Warning Signs:** Any enclosure that cannot be fully de-energized by the main disconnect (e.g., external interlocking signals) must have a yellow warning label stating: **"WARNING: Hazard of Electric Shock — More than one disconnect switch may be required to de-energize the equipment."**

---

### Would you like me to proceed to **Chapter 8**, which covers the **Protective Bonding Circuit** (Grounding), which is the primary mechanism for clearing faults?