<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: motors_drives
PRIORITY: HIGH
-->

# Overlap Note — Motors and Drives

## Decision rules (who wins)

- **Motor branch-circuit sizing and protection math** → NEC Article 430
- **Internal panel assembly rules for starters, drives, and related wiring** → UL 508A
- **Machine-level motor behavior, restart expectations, and drive integration in machinery** → NFPA 79 Chapter 12

Use all three when the panel is part of a machine.

## Quick routing logic

- If the question is about feeder or branch conductors, short-circuit protection, or overload basis, start with **NEC 430**.
- If the question is about how the drive or starter is incorporated inside a listed panel, start with **UL 508A**.
- If the question is about motor behavior in the machine, restart, direction, interlocking, or safe stopping expectations, start with **NFPA 79**.

## Evidence required

- [ ] Motor nameplate data
- [ ] Drive or starter datasheet
- [ ] Branch protection basis
- [ ] Overload-setting basis
- [ ] Panel schematic or motor branch diagram
- [ ] Machine control narrative for start/stop/restart behavior

## Checklist

### Motor branch review

- [ ] Confirm whether the motor is across-the-line, soft-started, or VFD-driven
- [ ] Confirm conductor-sizing basis
- [ ] Confirm short-circuit/ground-fault protection basis
- [ ] Confirm overload protection basis

### Panel integration review

- [ ] Confirm starter/drive is suitable for the intended panel assembly
- [ ] Confirm heat, routing, and segregation concerns are addressed
- [ ] Confirm any listed-combination or manufacturer-instruction dependency is captured

### Machine behavior review

- [ ] Confirm rotation direction logic where reversal matters
- [ ] Confirm unintended automatic restart is addressed
- [ ] Confirm any safety-related torque-removal approach is reviewed at machine level

## Common mistakes

❌ Treating drive branch protection as only a panel-layout issue  
❌ Treating overload setting as only a machine-controls issue  
❌ Assuming NEC 430 alone resolves machine restart and control-behavior concerns  
❌ Assuming a panel-compliant starter layout automatically satisfies machine behavior requirements

## Cross-links

- [NEC_2023__Art430__motors_motor_circuits_and_controllers.md](../../us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md)
- [NFPA79_2024__Ch12__motors_and_associated_equipment.md](../../us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md)
- [UL508A_2022__motor_controllers_and_drives.md](../../us/ul_508a/UL508A_2022__motor_controllers_and_drives.md)
- [ul508a_nec_nfpa79_overlap.md](../overlap_matrix/ul508a_nec_nfpa79_overlap.md)

## References

- NEC Article 430
- NFPA 79 Chapter 12
- UL 508A motor-controller and drive guidance

## Changelog

- 2026-03-09 — Initial motors and drives overlap note created
  - Added routing rules for NEC 430, UL 508A, and NFPA 79
  - Added evidence checklist and machine/panel review split
