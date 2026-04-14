<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: SEMICONDUCTOR_FACILITY
MODULE_ID: hf_handling_basics
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["hf", "hydrofluoric_acid", "chemical_handling", "shutdowns", "materials", "interlocks", "semiconductor_facility"]
  systems: ["bulk_chemical_distribution", "wet_bench_supply", "facility_controls", "chemical_skid"]
-->

# HF Handling In Semiconductor Facilities

## 0. Purpose

This module explains why hydrofluoric acid changes the design of a semiconductor-facility chemical system.

Use it to learn:

- why HF is treated differently from a generic liquid utility
- how materials, sensing, and shutdown logic change when HF is present
- which questions a controls or facility engineer should ask before reviewing a skid, tank, or wet-bench feed

Do not use this module as the final compliance authority. Use it as the learning layer, then route design decisions back to the semiconductor-facility reference notes and standards layer.

## 1. The short mental model

HF changes the job in four ways at once:

| Design area | What changes |
| --- | --- |
| Materials | familiar glass, quartz, and other casual material choices become unacceptable in direct service |
| Containment | even a small leak becomes high-consequence, so leak detection and isolation matter early |
| Instrumentation | the wrong diaphragm, seal, liner, or probe can fail before the logic ever gets a chance to help |
| Shutdown behavior | the system needs a clear response for leak, overfill, routing error, or lost utility proof |

If you remember only one line, remember this:

HF is not mainly a "pump and piping" problem. It is a materials-plus-shutdown problem that happens to include a pump and piping.

## 2. Generic liquid skid versus HF skid

An engineer used to water, CIP, or mild chemical service can miss the real difference.

| Question | Generic liquid skid | HF skid mindset |
| --- | --- | --- |
| What matters first | flow, pressure, capacity | compatibility, containment, then flow and pressure |
| What breaks first | often obvious mechanical fault | may be hidden attack in seals, sensors, or wettable internals |
| What alarms matter most | process deviation alarms | leak, overfill, isolation failure, and containment-related alarms |
| What must be explicit | pump sequence | safe state, shutdown ownership, and maintenance exposure |

## 3. Where HF usually appears in the facility path

A simplified facility-side path is:

`source tank -> day tank -> transfer pump or skid -> valve path -> point of use -> segregated drain or waste path`

At each step, the engineer should ask a different question:

| Segment | Main question |
| --- | --- |
| source or day tank | is storage measured and protected without creating an exposure or compatibility problem |
| transfer pump or skid | what stops flow immediately if leak or bad lineup is detected |
| valve path | are all wetted parts actually suitable for the real concentration and temperature |
| point of use | who owns the final permit and shutdown if the facility side trips |
| drain or waste path | can this route mix with incompatible waste or backflow into the wrong destination |

## 4. The five engineering questions that should always come first

### 4.1 What can HF attack here

Do not stop at pipe material.

Check:

- valve seats
- diaphragms
- seals and gaskets
- sensor liners
- sample tubing
- sight glasses or level accessories

The hidden weak part is often not the main pipe.

### 4.2 What proves the path is safe before transfer starts

Typical pre-start proof includes:

- source available
- destination ready
- no active leak condition
- correct valve lineup
- required exhaust or enclosure proof where the design depends on it
- minimum level or suction condition healthy

This is the difference between a permissive and a hope.

### 4.3 What trips the system immediately

Typical high-consequence trip inputs include:

- leak detection in the governed zone
- independent overfill condition
- emergency shutdown command
- severe loss of containment-related utility proof

Typical outputs are:

- stop the pump
- close isolation valves
- drop transfer permit
- alarm the area and the supervisory layer

### 4.4 Who owns final shutdown

This question matters more than people expect.

Possible owners include:

- local skid logic
- a safety PLC or dedicated shutdown layer
- facility emergency logic
- the process tool controller

If ownership is vague, commissioning problems follow.

### 4.5 What fails slowly before it fails obviously

HF systems often develop problems through:

- seal degradation
- diaphragm damage
- hidden attack in a wetted insert
- drift in a pressure or flow signal
- leak detection that does not actually cover the lowest release point

That is why maintenance strategy is part of the design, not just a handoff after startup.

## 5. How to separate signals in your head

Many review mistakes happen because all signals get treated as the same kind of thing.

Use this split:

| Signal type | Question it answers | Example in HF service |
| --- | --- | --- |
| `PERMISSIVE` | may I start or continue | no active leak, destination ready, correct lineup |
| `INTERLOCK` | what unsafe action must be blocked | do not start against a closed path |
| `TRIP` | what forces safe state now | confirmed leak, overfill, emergency command |
| `ALARM` | what must the operator notice | flow deviation, maintenance warning, signal fault |

This separation makes the logic readable and easier to test.

## 6. Common wrong assumptions

- "It is just another acid."  
  HF usually deserves a stricter compatibility review and a clearer shutdown story.

- "The pipe is compatible, so the system is compatible."  
  The weak point is often a seal, diaphragm, liner, or accessory.

- "One level transmitter is enough."  
  Normal level indication and independent overfill protection should not be mentally merged.

- "If SCADA alarms it, the system is protected."  
  An operator alarm is not the same as an automatic isolation action.

- "Manual mode lets maintenance do anything."  
  Hazardous shutdown paths still need to stay in force.

## 7. A simple abnormal scenario

### Scenario

A leak is detected under the transfer skid during HF movement.

### Good response pattern

1. Leak input changes state.
2. Hazardous shutdown layer identifies the event as a trip, not just an alarm.
3. Pump stops.
4. Isolation valve closes.
5. Transfer permit drops to the downstream user if needed.
6. Area and supervisory alarms remain active until the reset rules are satisfied.

### What this teaches

The key design question is not just "can we detect a leak?"  
It is "what exact action chain happens next, and who owns it?"

## 8. What to review on a real drawing or skid package

When you review a real HF package, scan for these first:

- all wetted materials explicitly called out
- separate normal level and overfill protection
- leak-detection zones and placement
- fail position of isolation valves
- pump stop logic
- exhaust or enclosure dependency if fumes matter
- shutdown ownership between skid, facility, and tool
- maintenance method for sensors and seals

## 9. What this module should connect to next

Read the reference layer after this module if you need the applied engineering view:

- [HF Reference Note](../../design_framework/semiconductor_facility/hf_control_safety_and_instrumentation.md)
- [Bulk Chemical Distribution and Wet Process Systems](../../design_framework/semiconductor_facility/bulk_chemical_distribution.md)
- [Safety and Shutdown Architecture](../../design_framework/semiconductor_facility/safety_and_shutdown.md)
- [Semiconductor Facility Instrument Selection Principles](../../design_framework/semiconductor_facility/instrumentation_selection.md)

Use the standards layer when the question becomes compliance or lifecycle structure:

- [SEMI S2 — Equipment Safety](../../standards_intelligence/international/semiconductor/semi/SEMI_S2__equipment_safety.md)
- [SEMI S14 — Fire Risk Assessment](../../standards_intelligence/international/semiconductor/semi/SEMI_S14__fire_risk_assessment.md)
- [IEC 61511 — Framework](../../standards_intelligence/international/functional_safety/iec_61511/IEC61511_2016__Part1__framework.md)

## 10. Engineering takeaway

HF training is valuable because it forces the reader to think in the right order:

1. compatibility
2. containment
3. permissives and interlocks
4. hazardous shutdown
5. maintenance exposure and failure modes

That order is more useful than memorizing one preferred valve or one preferred sensor.
