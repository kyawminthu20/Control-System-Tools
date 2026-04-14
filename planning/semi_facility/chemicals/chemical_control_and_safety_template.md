<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_CHEMICAL_TEMPLATE
-->

# Chemical Control And Safety Template

## Purpose

Use this template to build one chemical-specific engineering page that ties hazards, materials, instrumentation, controls, and shutdown behavior together.

This template is for draft planning notes. It is not a compliance claim and it must not contain copied standards text.

## Metadata starter

```text
<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_CHEMICAL_NOTE
-->
```

## Title pattern

`<Chemical or Class Name> — Control, Safety, and Instrumentation`

Examples:

- `Hydrofluoric Acid (HF) — Control, Safety, and Instrumentation`
- `Pyrophoric Gas Cabinets — Control, Safety, and Shutdown Pattern`

## Recommended section layout

## 1. Scope and boundary

- Where the media appears in the facility
- What is in scope: storage, day tank, cabinet, transfer skid, point-of-use, drain, exhaust dependency
- What is intentionally out of scope

## 2. Engineering class

- corrosive acid
- toxic gas
- pyrophoric gas
- flammable solvent
- oxidizer
- cryogenic liquid
- slurry or abrasive liquid

State why the class matters to controls and hardware.

## 3. Hazard profile

Capture only paraphrased engineering-relevant facts:

- primary people hazard
- primary equipment or containment hazard
- reaction or incompatibility concern
- vapor, ignition, asphyxiation, or contamination concern

## 4. Typical process use in a semiconductor facility

- wet bench
- blend skid
- gas cabinet
- VMB
- cleaning module
- CMP area
- utility distribution

## 5. Material compatibility

Record the conditions behind every compatibility statement.

Suggested table:

| Item | Candidate material | Fit | Conditions or cautions |
| --- | --- | --- | --- |
| Piping or tubing | `<material>` | preferred / conditional / avoid | concentration, temperature, contamination, pressure, aging |
| Valve body and seat | `<material>` | preferred / conditional / avoid | note wetting and actuator environment |
| Sensor wetted parts | `<material>` | preferred / conditional / avoid | include diaphragm, liner, electrode, or seal comments |
| Seal or gasket | `<material>` | preferred / conditional / avoid | include replacement burden and failure mode |

## 6. Instrumentation implications

Capture what the media does to measurement choices.

Suggested subsections:

- flow
- pressure
- level
- temperature
- gas or leak detection
- analytical measurement if relevant

For each one, note:

- preferred technologies
- technologies to avoid
- likely failure modes
- mounting or placement concerns

## 7. Control philosophy

Tie the media back to the repository control pattern.

Suggested subsections:

- modes used
- pre-start permissives
- interlocks that block unsafe action
- trips that force safe state
- degraded operation rules

## 8. Safe-state and shutdown ownership

State who owns the final action:

- local skid PLC
- facility PLC
- safety PLC
- hardwired safety
- tool controller

Do not leave shutdown ownership ambiguous.

## 9. SIF or safety-function candidates

Use this section to map:

- initiating condition
- sensing element
- logic owner
- final element
- safe response

Important rule:

- Do not assign SIL, PL, or compliance claims unless the supporting method is available and verified.
- If the repo only supports routing, mark the integrity target as `TO VERIFY`.

Suggested table:

| Scenario | Initiator | Logic owner | Final element | Response | Integrity note |
| --- | --- | --- | --- | --- | --- |
| `<example>` | `<sensor or condition>` | `<system>` | `<valve/pump/etc.>` | `<safe state>` | `TO VERIFY` unless formally supported |

## 10. Failure modes and maintenance burden

Document realistic field behavior:

- corrosion or chemical attack
- coating or fouling
- plugging
- diaphragm damage
- seal degradation
- false trips or hidden failures

Suggested table:

| Failure mode | Cause | Operational effect | Detection method | Mitigation |
| --- | --- | --- | --- | --- |

## 11. Facility interaction risks

Capture system-to-system concerns such as:

- incompatible chemical adjacency
- shared exhaust dependency
- drain segregation
- reaction by mixed waste or misrouting
- room or enclosure ventilation dependency

## 12. Tagging, alarms, and visual package

Include only representative patterns:

- example tag stems
- high / medium / advisory alarm classes
- candidate visuals to add later: architecture, state model, cause and effect, interaction map

## 13. Sources and verification gaps

List:

- local derived standards anchors
- public manufacturer or detector sources
- public SDS or hazard-summary sources
- unresolved claims marked `TO VERIFY`

## Definition of done for one page

- chemical behavior is tied to control implications, not just chemistry facts
- compatibility statements include conditions or cautions
- interlocks and trips are separated clearly
- shutdown ownership is explicit
- unsupported integrity claims remain marked `TO VERIFY`
- likely promotion target is identified
