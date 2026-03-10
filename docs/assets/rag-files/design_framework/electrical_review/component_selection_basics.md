<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Component Selection Basics

## 0. Purpose

This note provides a first-pass review framework for common low-complexity components used in simple control, indication, and interface circuits.

## 1. Resistors

Check:

- resistance value
- power rating
- tolerance
- temperature/environment exposure

Typical use:

- current limiting
- pull-up or pull-down biasing
- divider creation

## 2. Capacitors

Check:

- capacitance value
- voltage rating
- polarity if electrolytic
- stored-energy and discharge concern

Typical use:

- filtering
- smoothing
- timing
- suppression

## 3. Diodes

Check:

- polarity
- forward current rating
- reverse-voltage rating
- diode family appropriate to the job

Typical use:

- rectification
- reverse-polarity blocking
- flyback suppression
- indication

## 4. Transistor-type switching devices

Check:

- whether the device is being used as a signal switch or power switch
- drive method
- voltage/current rating
- expected heat dissipation

Practical rule:

- use the simplest device class that safely fits the load and switching behavior

## 5. Review trigger to escalate

Escalate beyond this note if the design depends on:

- detailed bias networks
- switching-loss calculations
- EMC-critical layout
- safety-related output behavior

## Related standards

- [NEC_2023__Art725__class_1_2_3_control_circuits.md](../../standards_intelligence/us/nec/NEC_2023__Art725__class_1_2_3_control_circuits.md)
- [NFPA79_2024__Ch09__control_circuits_and_control_functions.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md)
- [NFPA79_2024__Ch11__control_equipment.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch11__control_equipment.md)
