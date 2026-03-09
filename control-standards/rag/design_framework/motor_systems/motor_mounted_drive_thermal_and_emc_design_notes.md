<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Motor-Mounted Drive Thermal and EMC Design Notes

## 0. Purpose

Use this note when reviewing whether a drive mounted on or near the motor can survive its thermal and EMC environment.

## 1. Why this matters

Integration changes the problem:

- electronics move closer to motor heat
- field wiring becomes more exposed
- enclosure protection becomes more important
- signal integrity may become harder, especially for servo feedback

## 2. Thermal review

### Industrial VFD on motor

Main concerns:

- enclosure heat rise
- reduced convection
- ambient temperature derating
- contamination affecting cooling surfaces

### Industrial servo on motor

Main concerns:

- dense electronics
- feedback electronics near heat sources
- loop-performance sensitivity at temperature extremes

### EV integrated traction unit

Main concerns:

- high power density
- thermal cycling
- liquid-cooling integration

### Drone propulsion unit

Main concerns:

- airflow-dependent cooling
- limited thermal mass
- high-RPM loss concentration

## 3. EMC review

### Industrial VFD on motor

Advantages:

- shorter motor leads
- reduced long-cable output effects

Challenges:

- field wiring noise
- line-side noise control
- grounding and bonding quality

### Industrial servo on motor

Challenges:

- encoder or resolver signal integrity
- noise coupling into low-level feedback wiring
- safety-signal wiring quality

### EV integrated traction unit

Challenges:

- high-voltage switching noise
- vehicle grounding architecture
- dense inverter-to-motor packaging

### Drone propulsion unit

Challenges:

- compact high-speed switching
- EMI near radios, control electronics, and sensors

## 4. Enclosure and environment

Once the drive leaves the cabinet and goes onto the motor, review:

- ingress protection
- sealing quality
- vibration resistance
- washdown or contamination exposure
- field access for inspection and service

## 5. Review questions

1. Does the electronics temperature stay acceptable across worst-case motor heat and ambient?
2. Is the chosen cooling mechanism reliable in the real installation?
3. Does the wiring plan preserve EMC performance in the field?
4. Is enclosure protection adequate for the actual environment?
5. For servo systems, is feedback integrity protected well enough?

## 6. Practical conclusion

Motor-mounted drives often simplify architecture, but they move thermal and EMC risk into the machine field environment. That shift must be intentional and documented.

## Related files

- [Integrated Motor-Drive Architecture Comparison](./integrated_motor_drive_architecture_comparison.md)
- [Integrated Drive Failure Modes and Tradeoffs](./integrated_drive_failure_modes_and_tradeoffs.md)
