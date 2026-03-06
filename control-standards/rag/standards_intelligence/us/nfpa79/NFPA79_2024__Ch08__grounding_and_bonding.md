<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "8"
  chapter_title: "Grounding and Bonding"

INDEX_TAGS:
  topics: ["grounding", "bonding", "protective_earth"]
-->

## 0. Purpose

The primary purpose of grounding and bonding is **life safety**.

* **Fault Clearing:** To provide a low-impedance path for fault current so that a fuse or circuit breaker trips immediately if a "hot" wire touches the machine frame.
* **Equipotential Bonding:** To ensure all metal parts of a machine are at the same electrical potential, eliminating the risk of "touch potential" (shock) between two different parts of the machine.
* **Lightning/Surge Protection:** To dissipate external electrical surges safely into the earth.

## 1. Protective Bonding Rules

NFPA 79 strictly distinguishes between the "grounded conductor" (usually the neutral) and the "grounding conductor" (the protective earth wire).

* **The PE Terminal:** Every machine must have a single, primary **Protective Earth (PE)** terminal. All internal grounding conductors must terminate here. It must be marked with the ground symbol or the letters "PE."
* **Continuity:** The protective bonding circuit must be continuous. You cannot rely on hinges, sliding tracks, or bearing surfaces for a ground path.
* **Bonding Jumpers:** Moving parts (like a control station on a swinging arm or a cabinet door with mounted pushbuttons) must have a flexible braided copper jumper or wire to ensure a solid ground connection.
* **Color Coding:** Grounding conductors must be **Green** or **Green with one or more Yellow stripes**. Using these colors for any other purpose is a major code violation.

## 2. Noise vs. Safety Grounding

Control engineers often struggle with the "Functional Ground" (FE) versus the "Protective Earth" (PE).

* **Safety First:** You can never sacrifice a safety ground (PE) to solve an electrical noise problem.
* **Functional Ground (FE):** Used for EMI/RFI shielding and signal integrity. FE conductors are often marked **White with a Pink stripe** or just **Pink**.
* **Star Grounding:** To minimize "ground loops" that cause PLC analog signal drift, a "Star Ground" configuration is recommended where all shields return to a single point, but this point *must* still eventually bond to the PE terminal for safety.

## 3. Inspection Failure Modes

During field evaluations (UL/FEB), Chapter 8 is where many machines fail. Common issues include:

* **Painting Over Connections:** Bolting a ground lug to a painted surface. The paint acts as an insulator; the surface must be scraped to bare metal or use "star washers" that bite through the finish.
* **Sizing the Conductor:** Using a ground wire that is too small. The grounding conductor must be sized based on the largest upstream overcurrent device (refer to **Table 8.2.2.3** in NFPA 79).
* **Daisy-Chaining:** Wiring the ground from one motor to the next in a series. If one motor is disconnected for repair, the downstream motors lose their safety ground. Each device should have a direct path back to the sub-panel ground bar.

---

### Would you like me to move on to **Chapter 9**, which covers **Control Circuits and Control Functions** (the logic and safety categories of the machine)?