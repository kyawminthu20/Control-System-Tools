<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: DERIVED_REFERENCE
CATEGORY: SEMI_FACILITY
STATUS: DRAFT
-->

# Common Control Philosophy for Semiconductor Facility Utility Systems

## Purpose

This note defines a reusable control pattern for semiconductor facility utility systems such as gas skids, chemical delivery skids, UPW modules, exhaust subsystems, and tool utility interfaces.

## Core hierarchy

Use this order when designing logic:

1. shutdown and emergency layers
2. permissives and interlocks
3. operating mode
4. state or sequence logic
5. device commands and loop control

A system should never allow a lower layer to override a higher layer.

## Common modes

Most facility utility systems can use a restrained mode set:

- `OFF`
- `MANUAL_LOCAL`
- `MANUAL_REMOTE`
- `AUTO`
- `MAINTENANCE`
- `FAULT`
- `EMERGENCY_SHUTDOWN`

The exact names can vary, but the behavior should be explicit and documented.

## State-machine pattern

For sequence-driven utility systems, use a state model instead of scattered latch logic. A common pattern is:

- `IDLE`
- `PRECHECK`
- `PURGE_PRE`
- `READY`
- `STARTING`
- `STABILIZE`
- `RUNNING`
- `STOPPING`
- `PURGE_POST`
- `FAULT`

Not every system needs every state, but every transition should have an owner and an exit condition.

## Permissives, interlocks, and trips

## Permissives

Permissives answer: "may the sequence start or continue?"

Examples:

- utility available
- no active shutdown command
- tank level above minimum
- exhaust available
- no active gas or leak alarm

## Interlocks

Interlocks answer: "what unsafe action must be blocked?"

Examples:

- do not open chemical supply without exhaust proof
- do not start pump against a closed discharge path
- do not enable gas flow without cabinet healthy
- do not advance sequence without valve proof or timing confirmation

## Trips

Trips answer: "what condition forces safe state now?"

Examples:

- hazardous gas detection
- chemical leak detection in protected area
- overpressure or vacuum loss beyond safe boundary
- fire alarm or emergency power off input
- exhaust loss where capture is safety-critical

## Safe-state design rules

- Isolation valves default closed unless the safe response requires purge or vent.
- Purge paths and exhaust paths may be forced on during abnormal conditions.
- Pumps, heaters, and blend devices should default to off unless they are part of the mitigation path.
- Safe state must include what happens after power loss, PLC fault, or network loss.

## Manual-mode discipline

Manual mode is useful for maintenance and troubleshooting, but it should not be a loophole around hazard controls.

Keep active in manual:

- shutdown inputs
- critical trips
- hazardous interlocks
- timeouts that prevent equipment damage

Restrict carefully in manual:

- direct actuation of hazardous flow paths
- simultaneous actions that defeat containment or purge intent
- sequence steps that rely on hidden preconditions

## Shutdown ownership

Every system should define which layer owns final shutdown:

- local skid PLC
- facility PLC or SCADA
- hardwired safety system
- fire alarm or emergency system
- tool controller

Ambiguous shutdown ownership creates the worst commissioning failures.

## Required outputs of this philosophy

- mode definition table
- state definition table
- permissive matrix
- interlock matrix
- trip matrix
- cause and effect table
- operator reset policy
