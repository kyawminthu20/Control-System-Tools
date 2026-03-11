<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: NEC_APPLICATION
MODULE_ID: grounding_bonding_control_panels
LEARNING_LEVEL: applied

INDEX_TAGS:
  topics: ["grounding", "bonding", "EGC", "article_250", "control_panels"]
  systems: ["industrial_control_panel", "machine"]
-->

# Grounding and Bonding for Control Panels

## 0. Purpose

This module explains the difference between grounding and bonding, covers the NEC rules that apply to industrial control panels, and identifies the most common mistakes that create shock and fault-clearing hazards.

## 1. Grounding vs. bonding — the core distinction

These two terms are often used interchangeably in the field, but they have different meanings in the NEC:

**Grounding** — connecting the electrical system or equipment to earth (the ground electrode system). Grounding provides a reference voltage and limits the potential difference between equipment and earth during normal operation and lightning events.

**Bonding** — connecting metal parts together so they form a low-impedance fault-current path back to the source. Bonding is what causes the OCPD to trip when a fault occurs. Bonding does not depend on earth — a good bond is a metallic connection back to the transformer or source neutral, not a rod in the ground.

A critical NEC principle: the grounding electrode (ground rod, water pipe, etc.) is **not** the primary fault-current return path. The equipment grounding conductor (EGC) is the fault-current path. The earth is too resistive to reliably trip an OCPD.

## 2. Equipment grounding conductor (EGC)

The EGC is the conductor that provides the low-impedance fault-current path from equipment back to the source. It must be:

- Sized from **Table 250.122** based on the rating of the upstream OCPD — not the load current
- Continuous and have no breaks or removable links
- Connected at both ends: to the equipment enclosure (or ground bus) and to the source neutral/ground point

**Table 250.122 — common EGC sizes:**

| Upstream OCPD rating | Minimum EGC (copper) |
|---------------------|----------------------|
| 15 A | 14 AWG |
| 20 A | 12 AWG |
| 60 A | 10 AWG |
| 100 A | 8 AWG |
| 200 A | 6 AWG |
| 400 A | 3 AWG |
| 600 A | 1 AWG |

Common mistake: sizing the EGC based on load current (like the phase conductor) instead of the OCPD rating. The EGC must carry fault current, which can be much larger than normal load current, but its size is determined by how long the OCPD takes to clear — hence the OCPD rating is the reference.

## 3. Panel enclosure bonding

Every metal part of the control panel enclosure, mounting plate, subpanel, wireway, and connected conduit must be bonded together and to the EGC. Per Art 250.96:

- Metal raceways, cable trays, and enclosures must be bonded to form a continuous fault-current path
- Bonding jumpers must be used where standard connections (locknuts, bushings) are not sufficient for fault current
- Paint and coatings under lug connections must be removed to ensure metal-to-metal contact

## 4. Ground bus vs. neutral bus — why they must be separated

In the **service entrance panel** (main panel), the neutral bus and the ground bus are bonded together at one point — the main bonding jumper. This is the only point where neutral and ground connect.

In every **downstream panel** (subpanel), the neutral bus and the ground bus must be kept **separate**:
- Neutral conductors connect only to the neutral bus
- EGC conductors connect only to the ground bus
- The ground bus is bonded to the panel enclosure

If the neutral and ground are bonded in a subpanel, neutral current returns through the EGC — creating voltage on metal enclosures and violating Art 250.142(B).

## 5. Control panel grounding requirements

For an industrial control panel (ICP under Art 409 / UL 508A):

- The panel must have a dedicated **ground bus or ground lug** bonded to the enclosure
- All individual component enclosures inside the panel must be bonded to the ground bus
- The incoming EGC from the supply connects to the ground bus
- Motor frames must have their own EGC routed with the branch-circuit conductors (Art 250.134)

## 6. VFD grounding notes

VFDs generate high-frequency switching noise that can flow on the EGC. Best practice:

- Use a dedicated EGC routed with the drive supply conductors — do not rely on conduit alone
- Bond the drive chassis to the panel ground bus with a short, low-impedance strap
- For long motor cables, consider a symmetrical shielded cable with the shield bonded at both ends
- High-frequency ground loops can cause nuisance trips and communication errors — consult the drive manufacturer's grounding guidelines alongside NEC minimums

## 7. Common mistakes

| Mistake | Consequence |
|---------|-------------|
| EGC sized by load current, not OCPD | Undersized EGC may not carry fault current long enough for OCPD to trip |
| Neutral and ground bonded in subpanel | Neutral current on metal enclosures; shock hazard |
| Ground bus not bonded to enclosure | Enclosure floats at fault voltage; OCPD may not trip |
| Paint under ground lug | High resistance joint; poor fault-current path |
| No EGC in conduit run to motor | Motor frame not grounded; shock hazard on fault |

## 8. Engineering takeaway

Bonding is about clearing faults, not about referencing voltage to earth. A well-bonded system clears faults quickly because the impedance of the fault-current loop is low enough to drive enough current through the OCPD to trip it. The grounding electrode system is a separate function — primarily for lightning and voltage-reference stability.

Always verify the EGC size from Table 250.122 against the actual upstream OCPD installed on site.

## Related files

- [NEC Code Reading Fundamentals](./nec_code_reading_fundamentals.md)
- [Motor and Panel Code Application](./motor_and_panel_code_application.md)
- [SCCR Workflow for Industrial Control Panels](./sccr_workflow.md)
