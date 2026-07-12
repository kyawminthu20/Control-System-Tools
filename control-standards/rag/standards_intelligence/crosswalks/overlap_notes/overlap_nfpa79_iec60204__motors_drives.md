<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: motors_drives
PRIORITY: HIGH
-->

# Overlap Note — NFPA 79 vs IEC 60204-1 — Motors and Drives

## Decision rules (who wins)

- **US machinery projects** → NFPA 79 is the primary machine-electrical standard
- **International / EU-style machinery projects** → IEC 60204-1 is the primary machine-electrical standard
- **Dual-market machines** → design to the stricter combination and document the deltas

For motor and drive topics, both standards are close in intent but differ in language and emphasis.

## High-overlap topics

- overload protection expectations
- predictable motor control behavior
- isolation for maintenance
- drive integration as part of the machine electrical system

## Important deltas to review

- **NFPA 79** is tightly tied to the NEC environment and US machine practice.
- **IEC 60204-1** places stronger explicit emphasis on equipotential bonding, EMC-sensitive drive integration, and maintenance isolation language.
- **IEC 60204-1** more directly highlights shield bonding and drive-related noise-control concerns.

## Evidence required

- [ ] Motor nameplate data
- [ ] Drive datasheet and installation instructions
- [ ] Machine stop/restart narrative
- [ ] Isolation/disconnect concept
- [ ] Cable and shielding basis where drives are used
- [ ] Market target documented as US, international, or dual-market

## Checklist

### Common review

- [ ] Confirm motor and drive are suitable for the application
- [ ] Confirm overload protection approach
- [ ] Confirm isolation for maintenance
- [ ] Confirm start/stop/restart behavior is intentional

### Dual-market review

- [ ] Check any local isolation expectations for service work
- [ ] Check drive-related EMC measures and motor-cable treatment
- [ ] Check documentation language and verification expectations for the target market

## Cross-links

- [NFPA79_2024__Ch12__motors_and_associated_equipment.md](../../us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md)
- [IEC60204_1_2016A1__Clause14__electric_motors.md](../../international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause14__electric_motors.md)
- [nfpa79_iec60204_overlap.md](../overlap_matrix/nfpa79_iec60204_overlap.md)

## References

- NFPA 79 Chapter 12
- IEC 60204-1 Clause 12

## Changelog

- 2026-03-09 — Initial US vs IEC motors/drives overlap note created
  - Added common overlap topics
  - Added dual-market delta review list
