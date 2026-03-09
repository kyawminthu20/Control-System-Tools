<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Industrial vs EV vs Drone Motor-Drive Standards Matrix

## 0. Purpose

Use this note as a standards-routing aid when comparing integrated drive-on-motor architectures across industrial machinery, EV traction, and drone propulsion.

This file is a comparison note, not a canonical standards-intelligence file. Exact product-standard applicability still needs confirmation against the actual product and jurisdiction.

## 1. Core routing idea

These categories should not be treated as one standards problem:

- industrial integrated VFD
- industrial integrated servo
- EV integrated traction unit
- drone or UAV integrated propulsion unit

## 2. Standards-family matrix

| Architecture | Typical standards family to review | Main focus |
| --- | --- | --- |
| Industrial VFD integrated on motor | IEC/UL 61800 family, IEC 60034 family, IEC 60529, IEC 60204-1, NFPA 79 | product safety, EMC, enclosure, machine integration |
| Industrial servo integrated on motor | IEC/UL 61800 family, IEC 60034 family, IEC 60204-1, NFPA 79, drive safety-function review where applicable | product safety, EMC, feedback-driven motion, functional safety if claimed |
| EV integrated traction unit | automotive functional-safety and vehicle power-train frameworks | traction safety, high-voltage isolation, vehicle qualification |
| Drone/UAV integrated propulsion unit | aviation or UAS operational/certification framework plus environmental qualification path | airborne environmental qualification, propulsion reliability |

## 3. Industrial integrated VFD

Typical review themes:

- adjustable-speed power-drive product safety
- EMC of the drive system
- rotating-machine construction/performance basis
- enclosure and ingress protection
- machine-level installation rules

Typical machine contexts:

- conveyors
- pumps
- distributed material handling
- modular process equipment

## 4. Industrial integrated servo

Typical review themes:

- power-drive product safety
- EMC with sensitive feedback wiring
- safety-function claims at the drive level, if any
- machine-level electrical integration

Typical machine contexts:

- compact automation axes
- packaging
- robotics
- distributed precision motion

## 5. EV integrated traction unit

Typical review themes:

- automotive functional-safety process
- electric power-train safety
- high-voltage isolation under vehicle conditions
- cooling and packaging in traction duty

This should not be treated as an ordinary industrial VFD problem.

## 6. Drone/UAV integrated propulsion unit

Typical review themes:

- propulsion reliability
- environmental qualification
- vibration and moisture exposure
- mission or certification context

This should not be treated as an ordinary industrial motor-drive installation problem.

## 7. Design questions to answer

1. Is the product part of industrial machinery, road traction, or airborne propulsion?
2. Is the drive an industrial adjustable-speed product, a vehicle traction inverter, or a propulsion controller?
3. Does the architecture claim safety functions at the drive level?
4. What environmental qualification path is actually required?

## 8. Practical conclusion

Use industrial, automotive, and airborne paths as separate review tracks. Similar packaging does not mean the same standards stack.

## Related files

- [Integrated Motor-Drive Architecture Comparison](./integrated_motor_drive_architecture_comparison.md)
- [Motor-Mounted Drive Thermal and EMC Design Notes](./motor_mounted_drive_thermal_and_emc_design_notes.md)
