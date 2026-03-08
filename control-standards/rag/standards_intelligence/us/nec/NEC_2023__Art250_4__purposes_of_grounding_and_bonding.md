<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "250"
  section: "250.4"
  article_title: "Grounding and Bonding"
  section_title: "General Requirements for Grounding and Bonding"

INDEX_TAGS:
  topics: ["grounding", "bonding", "system_grounding", "equipment_grounding", "overvoltage", "effective_ground_fault_path", "grounding_electrode_conductor"]
  systems: ["industrial_control_panel", "machine"]
  risks: ["shock", "fire", "overvoltage", "lightning"]
-->



# NEC 2023 — Article 250.4 — Purposes of Grounding and Bonding

## 0. Why this section matters

Section 250.4 is the **purposes** section — it explains the *why* behind every grounding and bonding requirement in Article 250. Before selecting wire sizes, installing electrodes, or routing EGCs, engineers must understand the two distinct goals this section establishes. Confusing them is the root cause of most grounding/bonding design errors.

---

## 1. The core distinction: grounding vs. bonding

| Term | Definition | Purpose |
|------|-----------|---------|
| **Grounding** | Connection to the earth | Overvoltage protection — limits voltage on conductors and metal parts due to lightning, surges, and induction |
| **Bonding** | Low-impedance connection back to the source | Fault clearing — provides the path for fault current to operate the overcurrent device |

> **Key concept:** Grounding does not clear faults. Bonding clears faults. The earth is *not* an effective fault-clearing path — it is too high-impedance to operate a breaker reliably. The fault-clearing path runs back to the source through bonding conductors, not through the earth.

---

## 2. Grounded systems — 250.4(A)

### 250.4(A)(1) — Electrical system grounding

The **winding** (the current source — transformer secondary, generator winding) shall be connected to the earth to:

- Limit voltage imposed by **lightning**
- Limit voltage imposed by **line surges**
- Limit voltage imposed by **unintentional contact with higher-voltage lines**
- Stabilize the system voltage during normal operation

**Mechanism:** A lightning strike or utility disturbance can induce very high voltages on conductors. Connecting the winding to earth provides a discharge path for that high-frequency energy before it builds to the point of damaging conductor insulation or equipment.

**Note on limits:** System grounding *reduces* the risk of overvoltage damage; it does not eliminate it. A direct lightning strike to the service entrance exceeds the protection this method can provide.

### 250.4(A)(2) — Equipment grounding

Metal parts of electrical equipment that are not intended to carry current (enclosures, conduit, cable trays, motor frames) shall be connected to the earth to:

- Reduce voltage to ground on metal parts
- Limit touch potential from induced energy during nearby lightning events
- Prevent side-flash — arcing from energized metal parts to conductive building structure or persons

**Mechanism:** A nearby lightning strike induces high-frequency energy into all metal in the area via electromagnetic induction. If enclosures and conduit are not connected to earth, induced charge has nowhere to dissipate and may arc to building steel or personnel.

### 250.4(A)(3) — Bonding of electrical equipment

Non–current-carrying metal parts shall be bonded together so they are at the same potential and connected to the source of the electrical system at one point.

### 250.4(A)(4) — Bonding of electrically conductive materials

Metal water piping, structural steel, and other electrically conductive materials likely to become energized shall be bonded to prevent potential differences between systems.

### 250.4(A)(5) — Effective ground-fault current path

The wiring system shall provide a **low-impedance circuit** that facilitates operation of the overcurrent device in the event of a line-to-ground fault. This is the bonding requirement — not grounding. The path runs from the fault point back to the source through the equipment grounding conductors and bonding jumpers, not through the earth.

---

## 3. Ungrounded systems — 250.4(B)

Ungrounded systems (delta systems, isolated power) still require:

- Equipment grounding of metal enclosures (250.4(B)(1))
- Bonding of equipment (250.4(B)(2))
- An effective ground-fault current path (250.4(B)(3))

**Key difference:** The system winding is not connected to the earth. The first ground fault does not trip the overcurrent device (no return path). This is an advantage in some process industries (first fault does not cause shutdown) but requires ground-fault monitoring to detect the fault before a second fault creates a phase-to-phase fault.

---

## 4. Grounding electrode conductor (GEC) — installation notes

The GEC is the conductor that connects the system to the grounding electrode (rod, plate, concrete-encased electrode, water pipe).

**Installation requirements directly tied to 250.4 purposes:**

- **Keep it as short as practical** — GEC length adds inductive reactance. At the high frequency of lightning (~1 MHz), inductive reactance impedes current flow. A longer GEC means less effective discharge.
- **Avoid unnecessary bends and loops** — Bends and coils create inductance (skin effect, counter-EMF). The GEC should run as straight as possible.
- **Skin effect context:** Lightning current travels on the outside surface of the conductor (skin effect at high frequency). Conductor cross-section has less relevance; routing geometry matters more. This is why NEC caps GEC size at 6 AWG copper to a ground rod — the path to earth matters more than conductor mass.

---

## 5. Common engineering errors related to 250.4

| Error | Why it matters |
|-------|---------------|
| Relying on ground rods to clear faults | Earth path impedance is too high to reliably operate overcurrent devices. Bonding to source, not earth, clears faults (250.4(A)(5)). |
| Omitting EGC to eliminate "ground loops" | Signal noise isolation never justifies removing a safety EGC. Isolated ground circuits still require an EGC bonded to the source. |
| Running GEC through conduit with tight bends | Reduces lightning-discharge effectiveness due to increased inductive reactance. |
| Treating grounding and bonding as the same thing | Grounding = earth connection for overvoltage. Bonding = fault-current path to source. Distinct purposes, distinct hardware requirements. |
| Grounding to earth at multiple points on a circuit | Can create ground loops (noise) and does not improve fault clearing. Single-point grounding at the source is the NEC model. |

---

## 6. Relationship to rest of Article 250

| Topic | Section |
|-------|---------|
| Grounding electrode system requirements | 250.50 – 250.68 |
| GEC sizing | 250.66 |
| EGC sizing (fault path) | 250.122, Table 250.122 |
| Equipment bonding jumpers | 250.102 |
| Bonding of enclosures / doors | 250.97, 250.102 |
| Isolated ground (signal circuits) | 250.146(D) |

---

## 7. Change log

* 2026-03-08 — Initial draft; synthesized from NEC 250.4 code text and Mike Holt 2020 Bonding and Grounding instructional content. No verbatim NEC text.
