<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023
JURISDICTION: US

NEC_HIERARCHY:
  article: "110"
  article_title: "Requirements for Electrical Installations"

INDEX_TAGS:
  topics: ["listing", "labeling", "installation_instructions"]
  systems: ["industrial_control_panel", "machine"]
  risks: ["shock", "fire", "arc_flash"]
-->

# NEC 2023 — Article 110 — Requirements for Electrical Installations

## 0. Scope and relevance to control panels

Article 110 sets the general requirements for the examination, installation, and use of electrical equipment. For **Industrial Control Panels (ICPs)**, this article is the "gatekeeper" for compliance. It mandates that panels are not only built to standard (like UL 508A) but are installed in a way that ensures safety, accessibility, and environmental resilience.

## 1. Installation & listing requirements (field rules)

* **110.3(B) Installation and Use:** This is the most cited rule in inspections. It requires that listed or labeled equipment shall be installed and used in accordance with any instructions included in the listing or labeling.
* *Application:* If a component inside your panel is listed for use only with specific wire types or torque settings, failing to follow those instructions is an NEC violation.


* **110.14 Electrical Connections:** Focuses on the "weakest link" of any panel: the terminations.
* **Torque (110.14(D)):** Requires that terminal tightening torque be verified using a calibrated tool where a value is indicated on the equipment or in the instructions.


* **110.16 Arc Flash Hazard Warning:** ICPs (other than in dwellings) must be field or factory marked to warn qualified persons of potential arc flash hazards.
* **110.26 Spaces About Electrical Equipment:** Establishes the "Working Space" required for panels likely to be examined or serviced while energized.
* **Depth:** Usually a minimum of **3 feet** (900 mm) from the front of the panel (depending on voltage to ground).
* **Width:** The width of the equipment or **30 inches** (762 mm), whichever is greater.
* **Height:** At least **6.5 feet** (2.0 m).



## 2. Manufacturer instructions & evidence

* **110.3(A) Examination:** Equipment must be evaluated for suitability (listing), mechanical strength, wire-bending space, and electrical insulation.
* **110.21 Marking:** Equipment must bear the manufacturer’s name/trademark and relevant ratings (Voltage, Current, Wattage).
* **Field-Applied Hazard Markings (110.21(B)):** Warning labels must be durable, permanently affixed, and not hand-written (except for variable data).



## 3. Common inspection failures

1. **Improper Torque:** Failure to document that terminals were tightened to the manufacturer's specified inch-pounds using a torque wrench.
2. **Enclosure Integrity (110.12):** Leaving unused openings in enclosures (e.g., empty 1/2" knockouts). These must be closed with listed plugs or plates.
3. **Encroachment on Working Space:** Using the 3-foot clearance in front of the panel as storage for pallets or other equipment.
4. **Mixing Lug Metals:** Using lugs not rated for the specific conductor material (e.g., using copper-only lugs for aluminum wire).

## 4. Control-panel design implications

* **Component Selection:** Designers must ensure every component is **Listed** or **Recognized** for its intended purpose.
* **Environmental Ratings (110.28):** The enclosure NEMA/IP rating must match the environment. A NEMA 1 panel cannot be installed in a location requiring a NEMA 4 (hosedown) rating.
* **Identification of Disconnects (110.22):** Each disconnecting means must be legibly marked to indicate its purpose (e.g., "Main Feed," "Motor 4 Disconnect").

## 5. Decision log

* **2026-01-15:** Decided to emphasize 110.26 (Working Space) as it is the most common friction point between machine designers and facility managers.
* **2026-01-15:** Integrated torque requirements (110.14(D)) due to increased enforcement in the 2023 cycle.

## 6. Change log

* 2026-01-15 — Initial draft created; metadata added.

