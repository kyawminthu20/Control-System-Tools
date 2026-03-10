<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "3"
  chapter_title: "General Requirements"

INDEX_TAGS:
  topics: ["general_safety", "baseline_requirements"]
-->

In the 2024 edition of **NFPA 79**, Chapter 3 serves as the "General Requirements" baseline. While Chapter 1 and 2 define the playground and the vocabulary, Chapter 3 establishes the core design philosophy that every electrical system on the machine must follow.

---

## 0. Safety Philosophy

The overarching philosophy of NFPA 79 is to **protect persons, property, and the machine itself** from electrical and fire hazards.

* **Baseline Hazard Mitigation:** It assumes that any electrical failure or operator error should result in a "Safe State."
* **Risk-Based Design:** It emphasizes that electrical safety is not just about preventing shocks, but also ensuring that control system failures do not lead to mechanical hazards.
* **Cyber-Safety Integration:** For the first time in recent editions, the philosophy now explicitly includes **cybersecurity** as a factor in maintaining physical safety. If a network breach can cause a machine to bypass a limit switch, it is considered an electrical safety failure.

## 1. General Electrical Requirements

These are the "non-negotiable" rules for any industrial machine:

* **Voltage Limits:** The standard applies to equipment operating at **1000 V AC (RMS)** or **1500 V DC** or less.
* **Operating Environment:** Equipment must be designed to function reliably within the environment it is installed in (addressing temperature, humidity, vibration, and contaminants).
* **Supply Disconnect:** Every machine must have a clearly labeled "Machine Supply Circuit and Disconnecting Means." The 2024 update specifically mandates this exact wording for labels to prevent confusion during Lockout/Tagout (LOTO).

## 2. Design Principles for Machinery

When designing the electrical layout, engineers must adhere to several core principles:

* **Component Listing:** Use "Listed" or "Recognized" components (e.g., UL, CSA) to ensure the individual parts of the system meet minimum safety standards.
* **Accessibility:** Control devices (like E-stops) must be "readily accessible," meaning they can be reached quickly without climbing over equipment or using tools.
* **Surge Protection:** The 2024 edition continues the mandate for **Surge Protective Devices (SPDs)** on machines with safety-related circuits to prevent voltage spikes from causing "nuisance" trips or, worse, "failing-to-on."

## 3. Control-System Interpretation

Chapter 3 bridges the gap between raw power and logic:

* **Control Circuit Integrity:** Control circuits must be designed so that a single ground fault does not cause the machine to start unexpectedly or prevent it from stopping.
* **Start/Stop Priority:** A "Stop" command must always take priority over a "Start" command within the logic and physical wiring.
* **Unified SCCR:** For multi-panel systems, the designer must calculate a unified **Short-Circuit Current Rating (SCCR)** for the entire machine, rather than just labeling individual panels.


For a deeper dive into how NFPA 79 compares to the NEC in practice, this [Guide on NFPA 79 and Control Panels](https://www.youtube.com/watch?v=L4_yNFYLyY4) provides a great visual breakdown of where one standard ends and the other begins.