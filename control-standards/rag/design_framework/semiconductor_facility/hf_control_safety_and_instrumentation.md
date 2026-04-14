<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: DERIVED_REFERENCE
CATEGORY: SEMI_FACILITY
STATUS: DRAFT
-->

# Hydrofluoric Acid (HF) — Control, Safety, and Instrumentation

## Purpose

This note turns HF handling into an engineering-reference pattern for semiconductor facility work.

It is intended for facility-side liquid chemical systems such as:

- bulk storage and day tanks
- transfer skids
- wet bench supply
- local distribution panels
- leak-detection and shutdown interfaces

This file is not a substitute for chemical-specific SDS review, project risk assessment, or qualified material-selection work.

## Why HF changes the design

HF is not just "another acid" from a controls perspective.

It changes design priorities in five ways:

1. material compatibility becomes a first-pass gating decision
2. leak response must isolate the chemical path quickly and clearly
3. instrumentation choices narrow because wetted parts and maintenance exposure matter
4. shutdown ownership must be explicit across skid, facility, and area safety layers
5. maintenance burden rises because hidden attack, drift, and seal degradation matter more

## Typical facility boundary

For this reference, the HF system boundary usually includes:

- source storage or day tank
- transfer pump or metering skid
- piping and valve path to point of use
- secondary containment and leak-detection zones
- utility or exhaust dependencies where fumes or enclosure capture matter
- drain or waste segregation interfaces

It usually excludes:

- detailed wet-process chemistry recipes
- medical treatment guidance
- tool-internal process design beyond the facility handoff

## Hazard profile

| Dimension | Practical engineering meaning |
| --- | --- |
| Primary people hazard | severe exposure consequence means leak handling and maintenance exposure need priority |
| Primary hardware hazard | attacks glass, silica-containing materials, and some otherwise familiar instrument or tubing choices |
| Containment concern | small leaks can become high-consequence events because damage may progress before obvious external failure |
| Monitoring concern | both liquid release and vapor or fume exposure may matter depending on storage, transfer, and enclosure design |
| Design consequence | containment, compatible materials, and defined shutdown action take priority over convenience instrumentation |

## Material compatibility rules

The main rule is to never discuss HF compatibility without conditions.

Final selection depends on:

- concentration
- temperature
- pressure
- purity grade
- contamination requirements
- vendor qualification

### Working guidance

- Fluoropolymer and qualified non-metallic flow paths are often preferred for direct HF liquid service.
- Glass, quartz, and silica-containing components should be treated as incompatible for direct HF contact.
- Metallic wetted parts should be treated as exceptions that require project-specific justification, not as the default starting point.
- Seal, diaphragm, liner, tubing, and sensor-body materials must be reviewed together; the weakest wettable part controls the decision.

### Compatibility view by component

| Component area | Preferred direction | Treat as suspect or avoid by default | What to verify |
| --- | --- | --- | --- |
| Main liquid path | qualified fluoropolymer or otherwise HF-suitable non-metallic flow path | glass, quartz, unqualified mixed-material assemblies | concentration, temperature, purity, pressure, permeation, cleaning method |
| Valve wetted trim | HF-qualified non-metallic wetted path or lined design where appropriate | generic utility valves or unknown seat materials | seat and diaphragm material, cycle life, fail position |
| Pressure sensing boundary | compatible diaphragm or seal arrangement with verified wetted path | bare generic metallic wetted elements | chemical attack, dead volume, cleanability, replacement burden |
| Flowmeter wetted path | technology whose full wetted set is qualified for actual HF service | meter chosen by accuracy alone | liner, electrode, tube, gasket, zero stability, flushability |
| Level measurement | non-contact or isolated arrangement where practical | intrusive probes with uncertain compatibility | foam, vapor, tank geometry, overfill independence |
| Gaskets and seals | explicitly qualified seal family for actual solution and temperature | convenient stock elastomer with no HF review | swelling, permeability, maintenance interval, contamination impact |

## Instrumentation implications

HF should be treated as a media-driven instrument-selection problem, not a generic liquid-service problem.

### Level

- Prefer non-contact tank measurement where geometry and vapor conditions allow it.
- Keep overfill protection separate from the convenience level signal.
- Verify sensor location against splash, fumes, washdown, and maintenance access.

### Flow

- Choose only technologies whose entire wetted path is compatible with the actual HF service.
- Lined electromagnetic and some other chemically resistant approaches may fit, but compatibility review matters more than preferred technology labels.
- Low-flow detection may be as important as normal flow measurement because blockage and pump-protection logic often drive the control response.

### Pressure

- Treat the pressure boundary as a compatibility item first and an accuracy item second.
- Use arrangements that keep the sensing element protected from direct attack where possible.
- Do not assume a general-purpose process transmitter is acceptable just because the range fits.

### Leak detection

- Leak detection must be designed as part of the containment strategy, not added afterward.
- Use compatible area leak-detection methods qualified for the actual HF solution and containment geometry.
- Sensor placement at low points, tank bases, pump skids, and transfer zones usually matters more than adding more operator alarms.

### Vapor or area detection

- If the installation can generate HF fumes or vapor exposure in enclosed or exhausted areas, area monitoring may be part of the safety layer.
- Detector placement should follow the actual ventilation and enclosure behavior, not a generic room rule.

### Temperature

- Temperature is a compatibility input, not just a process trend.
- Elevated temperature may change corrosion behavior, sensor suitability, seal life, and alarm limits.

## Control philosophy for HF service

### Pre-start permissives

Typical permissives include:

- source available
- destination ready
- no active leak condition in the governed zone
- required containment or drain path in service
- required exhaust or enclosure status healthy where capture is part of the hazard control
- valve lineup confirmed
- minimum tank level or suction condition healthy
- pump healthy and not in fault

### Interlocks

Interlocks should block actions that are unsafe or invalid, such as:

- starting transfer against a closed downstream path
- opening an HF path when the destination is not ready
- transferring with an active leak condition in the relevant containment zone
- bypassing required ventilation or enclosure proofs where the design depends on them
- routing into an incompatible destination or drain path

### Trips and hazardous shutdown actions

Typical trip or shutdown inputs include:

- confirmed leak detection in a protected zone
- severe overfill or independent high-high condition
- emergency shutdown command
- fire-alarm or area emergency escalation where project logic requires it
- severe process deviation that threatens containment

Typical output actions include:

- stop transfer pump
- close supply or isolation valves
- drop permit to the downstream user if required
- maintain alarms and annunciation
- keep mitigation utilities active if they are part of the defined safe state

### Manual-mode discipline

Manual mode should not defeat:

- leak-based shutdown paths
- emergency shutdown commands
- required ventilation or enclosure proofs
- hard stop logic that protects containment

## Safe-state and shutdown ownership

HF systems need shutdown ownership defined at more than one layer.

| Layer | Typical owner | Example responsibility |
| --- | --- | --- |
| Equipment self-protection | local skid logic | dry-run stop, valve timeout, pump fault response |
| Sequence interlock | local skid or facility utility PLC | block transfer when destination not ready or path not proven |
| Local hazardous shutdown | safety PLC, dedicated safety path, or clearly defined local hazardous logic | isolate supply and stop pump on confirmed leak |
| Area or facility emergency response | facility emergency system or area shutdown logic | fire-alarm interaction, area isolation, evacuation-related escalation |

The main rule is that the downstream tool, the local skid, and the facility system cannot all "sort of" own final shutdown. One layer must be explicitly primary for each scenario.

## Safety-function candidates

HF leak isolation is often a candidate safety function, but the required integrity target is project-specific.

Use the local corpus to structure the function, not to claim a final target.

| Scenario | Initiator | Logic owner | Final element | Safe response | Integrity note |
| --- | --- | --- | --- | --- | --- |
| Leak in skid or containment zone | compatible leak-detection input | local hazardous shutdown layer | isolation valve plus pump stop | isolate source and stop transfer | `TO VERIFY` under project risk method |
| High-high tank level or overfill | independent overfill device | local protection or safety layer | pump stop and source isolation | prevent overflow or routed release | `TO VERIFY` |
| Required exhaust loss where capture is safety-critical | exhaust proof input | local or area shutdown layer | transfer inhibit or isolation | block or stop chemical movement | `TO VERIFY` |

For lifecycle structure, route to IEC 61511 concepts for process safety work and keep detailed SIL determination tied to the actual project risk process.

## Failure modes and maintenance burden

| Failure mode | Likely cause | Operational effect | Engineering response |
| --- | --- | --- | --- |
| Hidden material attack | wrong wetted material or bad condition assumptions | delayed leak, rupture, contamination, or unplanned outage | review full wetted path, not only pipe material |
| Seal degradation | chemical exposure, heat, aging, cleaning cycle burden | seepage, valve unreliability, pump leakage | qualify seal family and define replacement interval |
| Pressure-signal drift | diaphragm attack, trapped residues, damaged seals | bad permissives, false stability, poor pump protection | use protected sensing arrangement and calibration discipline |
| Flow-measurement instability | incompatible internals, coating, bubbles, low-flow edge case | nuisance alarms or missed flow-loss condition | verify meter fit for actual service and operating window |
| Leak-sensor blind spot | poor placement, residue, containment geometry | release not detected quickly enough | zone the containment and place sensors deliberately |
| Maintenance exposure risk | intrusive calibration or replacement in hazardous location | elevated personnel risk and longer outages | prefer low-exposure service methods and clear isolation procedure |

## Facility interaction risks

HF should not be treated as an isolated skid topic.

Check at least these interaction questions:

- Does the drain path stay segregated from incompatible wastes?
- Does the skid depend on shared exhaust or enclosure capture that other systems can disturb?
- Can a routing error connect HF service to materials selected for another acid or solvent family?
- Are maintenance activities likely to expose nearby instrument cables, detector housings, or enclosure materials to fumes or splash?
- Is the tool-handshake logic clear about what happens when facility HF is isolated mid-process?

## Representative signal set

Example signal stems for one HF transfer package:

- `HF_TK_LVL`
- `HF_TK_LSHH`
- `HF_PMP_RUN_CMD`
- `HF_PMP_RUN_FB`
- `HF_FLOW`
- `HF_LEAK_ZONE_1`
- `HF_ISO_VLV_CMD`
- `HF_ISO_VLV_CLS_FB`
- `HF_EXH_PROOF`
- `HF_TRANSFER_PERMIT`

These are placeholders for architecture discussion, not a required site naming standard.

## Related files

- [Bulk Chemical Distribution and Wet Process Systems](./bulk_chemical_distribution.md)
- [Semiconductor Facility Instrument Selection Principles](./instrumentation_selection.md)
- [Safety and Shutdown Architecture](./safety_and_shutdown.md)
- [Common Control Philosophy for Semiconductor Facility Utility Systems](./common_control_philosophy.md)

## Related standards routes

- [SEMI S2 — Equipment Safety](../../standards_intelligence/international/semiconductor/semi/SEMI_S2__equipment_safety.md)
- [SEMI S14 — Fire Risk Assessment](../../standards_intelligence/international/semiconductor/semi/SEMI_S14__fire_risk_assessment.md)
- [IEC 61511 — Framework](../../standards_intelligence/international/functional_safety/iec_61511/IEC61511_2016__Part1__framework.md)
- [IEC 61511 — SIS Design](../../standards_intelligence/international/functional_safety/iec_61511/IEC61511_2016__Clause10__sis_design.md)

## Scope caution

This note is intentionally conservative.

It is meant to help the reader ask the right design questions:

- what can HF attack here
- what should shut down on leak or loss of containment proof
- which signals are permissives versus trips
- who owns final shutdown

Final chemical selection, enclosure design, code overlay, and integrity assignment still require project-specific verification.
