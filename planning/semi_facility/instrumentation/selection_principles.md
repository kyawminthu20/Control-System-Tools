<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_INSTRUMENT_SELECTION
-->

# Semiconductor Facility Instrument Selection Principles

## Purpose

This note defines the decision logic for selecting instruments in semiconductor facility service.

The main rule is that semiconductor facilities do not choose instruments by variable alone. Selection depends on media, purity risk, safety role, maintenance burden, and integration method at the same time.

## Primary selection dimensions

### 1. Process media and contamination risk

- UPW and high-purity liquids demand low extractables, low leachables, and clean assembly discipline.
- Corrosive chemicals demand wetted-material compatibility before accuracy or convenience.
- Hazardous gases demand leak integrity, clean metallurgy, and safe enclosure design.
- Cleanroom HVAC signals often prioritize stability, drift performance, and calibration traceability.

### 2. Control criticality

Use one or more of these roles for every instrument:

- `SAFETY_TRIP`: initiates isolation, shutdown, or emergency response
- `PERMISSIVE`: blocks start until a safe precondition is met
- `CONTROL`: feeds a loop or sequence decision
- `QUALITY`: confirms process media quality such as UPW resistivity or TOC
- `MONITORING`: informs operators or maintenance without directly changing control

Higher criticality means tighter requirements for proof, diagnostics, testing, and ownership.

### 3. Installation environment

- Chemical areas may require splash resistance, washdown tolerance, and non-metallic wetted parts.
- Gas cabinets and exhausted enclosures require compact form factors, high leak integrity, and maintainability without widening the hazard zone.
- Mechanical rooms favor serviceability and robust diagnostics.
- Cleanroom-adjacent areas may need better particulate control and tighter installation discipline.

### 4. Integration method

- Hardwired discrete signals remain appropriate for simple safety proofs and permissives.
- Analog signals remain common for continuous utilities and legacy facility systems.
- Digital protocols add diagnostics and configuration depth but increase lifecycle and cybersecurity obligations.
- Safety functions should not be assigned to convenience networking without a defined architecture and validation method.

## Media-driven selection rules

## UPW and high-purity liquid service

- Favor materials and assemblies proven for high-purity liquid service.
- Watch metallic contribution, ionic contribution, TOC contribution, surface finish, and dead-leg risk.
- Treat calibration fluid, sample tubing, and maintenance procedure as part of the measurement system.
- Prefer instruments whose process connections and internal geometry support clean draining and flushing.

## Corrosive liquid chemical service

- Start with compatibility of wetted parts, diaphragm materials, seals, tubing, and sensor bodies.
- Expect backup shutdown means for level, leak, and overfill conditions.
- Treat temperature as a major selection variable because compatibility can shift with concentration and heat.
- Avoid instruments that require intrusive maintenance in high-exposure areas unless that burden is justified.

## Hazardous and specialty gas service

- Treat pressure boundary integrity and purgeability as first-class requirements.
- Choose components that fit the intended gas distribution architecture and cleanliness class.
- Verify response time, proof method, and fail-safe behavior for pressure switches, transducers, and gas detectors.
- Confirm whether the signal is for control only or also participates in a shutdown path.

## Exhaust, abatement, and vacuum service

- Expect dirty service, condensation risk, corrosion, and deposition.
- Favor sensing methods with clear maintenance access and known fouling behavior.
- Differential pressure points and sample systems need contamination-control planning, not just instrument selection.
- Do not treat fan running status alone as equivalent to exhaust performance proof.

## Cleanroom HVAC and room-pressure service

- Stability, drift, and calibration discipline often matter more than wide measurement range.
- Differential pressure devices should be selected with realistic door-opening disturbances in mind.
- Room cascade strategy should be documented before final sensor placement.
- Particle and environmental monitors need clear ownership between facility operations and process engineering.

## Common selection mistakes

- Selecting by vendor familiarity instead of service compatibility.
- Using one generic pressure transmitter spec across UPW, chemical, gas, and vacuum service.
- Treating an analyzer as complete without defining sample conditioning and maintenance method.
- Overloading one signal with control, alarm, and trip duties without clarifying proof and integrity requirements.
- Choosing digital integration for convenience without lifecycle support for addressing, cybersecurity, and spares.

## Documentation minimum for every selected instrument

- process service
- media and concentration range
- normal operating range
- alarm and trip role
- wetted materials
- pressure and temperature limits
- power and signal interface
- calibration method
- failure indication method
- maintenance access notes

## Source anchors

- [SEMI F57](../sources/public_source_register.md)
- [SEMI F61](../sources/public_source_register.md)
- [SEMI F63](../sources/public_source_register.md)
- [SEMI F75](../sources/public_source_register.md)
- [ISA-5.1](../sources/public_source_register.md)
