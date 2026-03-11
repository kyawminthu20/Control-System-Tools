<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: CONTROL_SYSTEMS
MODULE_ID: industrial_control_loop_architectures
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["pi_vs_pid", "vfd_speed_loop", "servo_loops", "cascade_control", "temperature_control", "level_control", "process_loops"]
  systems: ["vfd", "servo_drive", "process_control", "thermal_loop", "tank", "machine"]
-->

# Industrial Control Loop Architectures

## 0. Purpose

This note explains how PID-related control is arranged in common industrial loop architectures.

Use it to understand:

- why many real loops are PI instead of full PID
- how VFD speed loops are structured
- how servo cascade loops are structured
- how process loops differ from motion loops

## 1. Why many industrial loops are PI instead of full PID

Many real loops are implemented as **PI**, not full PID.

That is especially common when:

- the process is relatively slow
- measurement noise is significant
- derivative action adds little benefit
- steady-state offset removal matters more than fast transient shaping

This is why PI control appears so often in:

- VFD speed loops
- tank level loops
- flow loops
- temperature loops with noisy measurement

Derivative is more common where transient behavior matters sharply and feedback quality is high enough to support it.

## 2. VFD speed-loop structure

Most VFD-based systems use nested loops rather than one single controller block.

A common structure is:

`optional position loop -> speed loop -> current or torque loop -> motor`

The speed loop is often PI:

- proportional action reacts to present speed error
- integral action removes load-related offset

This is common in:

- conveyors
- pumps
- fans
- general machine-speed regulation

In many of these systems, derivative action is unnecessary and can create more trouble than value.

## 3. Servo-drive cascade control

Servo drives usually use cascade control loops.

A common structure is:

`position loop -> velocity loop -> current loop -> inverter -> motor`

Typical roles:

- position loop generates a velocity command
- velocity loop generates a torque-producing command
- current loop controls the inverter and motor current directly

In many servo systems:

- the position loop may use PID or PD-like behavior
- the velocity loop is commonly PI
- the current loop is also commonly PI

The loops also run at different rates. Position updates are usually slower than velocity updates, and current regulation runs fastest of all.

## 4. Process-loop examples

### Temperature control

For a furnace or heated process:

- the plant is the thermal mass
- the actuator is heater power
- the controlled variable is temperature

Typical interpretation of the terms:

- **P** reacts immediately to temperature error
- **I** compensates for steady heat losses
- **D** can reduce overshoot near setpoint

Temperature loops often benefit from integral action because the plant typically needs continuous power just to hold temperature.

### Tank level control

For a tank with an inlet valve or pump:

- the plant is the tank and liquid dynamics
- the actuator is valve position or pump command
- the controlled variable is level

These loops are often PI, not full PID.

Common reasons:

- level changes slowly
- sensors may be noisy
- derivative action often adds noise sensitivity without much benefit

## 5. Architecture comparison

| Loop type | Typical controller choice | Why |
| --- | --- | --- |
| VFD speed loop | `PI` | speed regulation usually needs offset removal more than derivative damping |
| servo position loop | `PID` or `PD-like` | motion transients and tracking error matter strongly |
| servo velocity loop | `PI` | torque-producing command needs stable offset correction |
| servo current loop | `PI` | fast electrical loop with predictable plant behavior |
| temperature loop | `PI` or `PID` | integral matters, derivative may help in some thermal cases |
| tank level loop | `PI` | slow and noisy process, derivative often not worth it |

## 6. Engineering takeaways

- Most industrial loops are PI because offset removal matters more often than derivative shaping.
- Motion systems and process systems use the same PID ideas, but not the same loop structures.
- VFDs and servo drives usually embed PID-related behavior inside nested loops.
- The presence of multiple loops does not remove PID logic; it distributes it across different control layers.
- The best controller type depends on plant speed, feedback quality, and the job of the specific loop.

## Related files

- [PID Control Overview](./pid_control_intuitive_foundation.md)
- [PID Control Intuition](./pid_control_intuition.md)
- [Industrial PID Implementation](./industrial_pid_implementation.md)
- [PID Heater Control With Contactor](./pid_heater_control_with_contactor.md)
- [Servo Drive Fundamentals](../../training_modules/electrical_machines/servo_drive_fundamentals.md)
