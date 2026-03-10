<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: NEC_APPLICATION
MODULE_ID: motor_and_panel_code_application
LEARNING_LEVEL: applied

INDEX_TAGS:
  topics: ["article_routing", "motors", "panels", "control_circuits", "grounding"]
  systems: ["industrial_control_panel", "machine"]
-->

# Motor and Panel Code Application

## 0. Purpose

This module gives a quick routing guide for common industrial-control questions that span more than one NEC article.

## 1. Use Article 430 when the question is motor-specific

Typical triggers:

- motor branch-circuit conductors
- overload protection
- short-circuit and ground-fault protection
- VFD supply conductors and disconnecting means

Primary anchor:

- [NEC_2023__Art430__motors_motor_circuits_and_controllers.md](../../standards_intelligence/us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md)

## 2. Use Article 409 when the question is about the panel as an assembly

Typical triggers:

- industrial control panel marking
- SCCR marking
- panel identification and assembly context

Primary anchor:

- [NEC_2023__Art409__industrial_control_panels.md](../../standards_intelligence/us/nec/NEC_2023__Art409__industrial_control_panels.md)

## 3. Use Article 725 when the question is about remote or limited-energy control wiring

Typical triggers:

- Class 1, 2, or 3 control circuits
- control-circuit separation
- low-energy remote-control wiring logic

Primary anchor:

- [NEC_2023__Art725__class_1_2_3_control_circuits.md](../../standards_intelligence/us/nec/NEC_2023__Art725__class_1_2_3_control_circuits.md)

## 4. Use Article 250 when the question is about grounding and bonding

Typical triggers:

- equipment grounding conductors
- bonding jumpers
- effective fault-current path

Primary anchor:

- [NEC_2023__Art250__grounding_and_bonding.md](../../standards_intelligence/us/nec/NEC_2023__Art250__grounding_and_bonding.md)

## 5. Use Articles 240 and 310 together when the question is conductor protection

Typical triggers:

- conductor ampacity
- overcurrent device coordination
- ambient and bundling effects
- small-conductor protection

Primary anchors:

- [NEC_2023__Art240__overcurrent_protection.md](../../standards_intelligence/us/nec/NEC_2023__Art240__overcurrent_protection.md)
- [NEC_2023__Art310__conductors_for_general_wiring.md](../../standards_intelligence/us/nec/NEC_2023__Art310__conductors_for_general_wiring.md)

## 6. Practical takeaway

Most industrial questions do not live in one article only.

The usual pattern is:

- find the primary article for the equipment type
- then check the linked articles for grounding, conductors, and overcurrent protection

## Related standards

- [NFPA79_2024__Ch11__control_equipment.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch11__control_equipment.md)
- [NFPA79_2024__Ch12__motors_and_associated_equipment.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md)
- [UL508A_OVERVIEW.md](../../standards_intelligence/us/ul_508a/UL508A_OVERVIEW.md)
