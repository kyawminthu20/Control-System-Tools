<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# VFD Commissioning Workflow

## 0. Purpose

Use this workflow to structure first energization and early functional checks for a VFD-driven motor system.

This workflow complements, but does not replace, the specific OEM startup procedure.

## 1. Electrical verification

Before applying power, confirm:

- incoming supply rating matches the drive
- protective earth and bonding are intact
- branch protection and isolation method are identified
- motor cable terminations are complete and intentional
- no obvious phase-to-phase or phase-to-ground faults are present

## 2. Capture and enter motor data

Record and enter the motor information that the drive expects, such as:

- rated voltage
- rated current
- rated frequency
- rated speed
- rated power

Do not guess through this step. Wrong motor data can produce poor control or immediate trips.

## 3. Safe first power-up

Power the drive under controlled conditions and verify:

- the drive powers normally
- no immediate fault is present
- operator/HMI indications are understood
- the machine is still in a safe non-motion state

## 4. First motion check

Run the motor only under low-risk conditions approved for the machine.

Verify:

- actual rotation direction
- smooth acceleration
- current behavior consistent with the no-load or light-load condition
- no abnormal sound, vibration, or heating

## 5. Functional run and load review

Once basic motion is correct, review:

- normal speed range
- acceleration and deceleration behavior
- braking method if used
- drive and motor temperature trend
- cable-noise or EMC side effects on nearby controls

## 6. Evidence to retain

Keep the commissioning basis:

- motor nameplate data
- key drive parameter snapshot
- protection basis
- rotation verification result
- any tuning or commissioning notes

## Related files

- [VFD Fundamentals](../../training_modules/electrical_machines/vfd_fundamentals.md)
- [VFD Motor Integration Review](./vfd_motor_integration_review.md)
- [Drive Commissioning](../../commissioning_checklists/checklists/drive_commissioning.md)
