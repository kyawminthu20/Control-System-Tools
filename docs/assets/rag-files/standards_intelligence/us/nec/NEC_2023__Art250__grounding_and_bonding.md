<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "250"
  article_title: "Grounding and Bonding"

INDEX_TAGS:
  topics: ["grounding", "bonding", "protective_earth"]
  systems: ["industrial_control_panel"]
-->



# NEC 2023 — Article 250 — Grounding and Bonding

## 0. Purpose for control panels

Article 250 provides the requirements for grounding and bonding to ensure electrical systems are safe. For control panels, the primary goals are:

1. **Safety:** Limiting the voltage imposed by lightning, line surges, or unintentional contact with higher-voltage lines.
2. **Fault Clearing:** Establishing an effective ground-fault current path to trigger overcurrent devices (breakers/fuses).

## 1. Equipment Grounding Conductors (EGC)

* **Sizing (250.122):** The EGC must be sized based on the rating of the overcurrent device protecting the circuit.
* *Critical Table:* **Table 250.122** provides the minimum size for copper or aluminum EGCs.
* *Example:* A panel fed by a 100A breaker requires a minimum 8 AWG copper EGC.


* **Identification (250.119):** EGCs must be bare, covered, or insulated. If insulated, the outer finish must be **green** or **green with one or more yellow stripes**.

## 2. Bonding of enclosures and doors

* **Effective Path (250.4):** All non-current-carrying conductive materials (enclosure, subpanel, conduits) must be bonded together to form a low-impedance circuit back to the source.
* **Bonding Jumpers (250.102):** Panels with hinged doors containing electrical components (pushbuttons, HMIs, pilot lights) **must** have a flexible bonding jumper connecting the door to the main enclosure. Relying on hinges is generally not sufficient for an effective fault path.
* **Paint and Coatings (250.12):** Non-conductive coatings (paint, lacquer, enamel) on threads, contact points, and tapping locations must be removed to ensure a metal-to-metal connection, or specialized "star" washers must be used.

## 3. Noise vs. Safety Grounding

* **Isolated Ground (250.146(D)):** Often used for sensitive PLC or communication equipment to reduce "noise." However, an isolated ground receptacle/circuit must still have an EGC that terminates at the system grounding terminal.
* **The "Ground Loop" Fallacy:** Designers must never omit the safety EGC to solve data noise issues. Safety (fault path) always supersedes signal integrity in NEC compliance.

## 4. Inspection failure patterns

1. **Undersized EGC:** Using a "default" 14 AWG ground wire for a high-amperage feed.
2. **Failure to Bond Subpanel:** Mounting a backplane on painted studs without removing paint or using grounding hardware, preventing a low-impedance path for components mounted on DIN rail.
3. **Hinged Doors:** Forgetting the bonding jumper for doors equipped with 120V or 480V pilot devices.
4. **Improper Termination:** Terminating more than one grounding conductor in a single lug not specifically rated for multiple wires.

## 5. Change log

* 2026-01-15 — Initial draft created; emphasized Table 250.122 and door bonding requirements.

