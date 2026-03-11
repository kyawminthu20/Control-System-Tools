<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: CONTROL_SYSTEMS
MODULE_ID: industrial_pid_implementation
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["pid", "plc_pid", "sp_pv_cv", "bias", "feedforward", "sample_time", "rockwell_pide", "siemens_pid_compact", "anti_windup"]
  systems: ["plc", "control_loop", "process_control", "machine"]
-->

# Industrial PID Implementation

## 0. Purpose

This note explains how PID appears in real industrial control systems rather than in a purely textbook form.

Use it to understand:

- the extra blocks around the controller
- common PLC loop terms such as SP, PV, and CV
- Rockwell `PIDE` and Siemens `PID_Compact` conventions
- why bias, limits, filters, and sample time matter in practice

## 1. Real loop architecture

The simplest loop picture is:

`setpoint -> controller -> actuator -> plant -> sensor -> feedback`

Industrial implementations usually add more than the core P, I, and D branches.

Common additions are:

- feedforward
- output limits
- anti-windup handling
- measurement filtering
- explicit sample time
- deadband or error tolerance
- manual/auto transfer logic

A more realistic industrial picture is:

`setpoint -> PID controller + feedforward -> actuator -> plant -> sensor conditioning -> feedback`

That extra structure matters because many field problems come from limits, noise, scaling, or timing rather than from the basic PID law alone.

## 2. Common PLC loop terms

Industrial control platforms often name the main loop signals like this:

- **SP**: setpoint
- **PV**: process variable
- **CV**: control variable or controller output

In practical terms:

- SP is what you want
- PV is what you measured
- CV is what the controller sends to the actuator

The controller output is often thought of as:

`CV = bias + proportional action + integral action + derivative action`

The exact internal form varies by vendor, units, and configuration.

## 3. Quick parameter reference

| Item | Practical meaning |
| --- | --- |
| `Kp` | proportional strength |
| `Ki` or `Ti` | integral behavior |
| `Kd` or `Td` | derivative behavior |
| `Bias` | base actuator output at steady operating point |
| output limits | clamp the controller to what the actuator can actually do |
| deadband | ignore or soften very small errors |
| PV filter | smooth noisy measurements |
| sample time / cycle | define how often the digital controller updates |

## 4. Rockwell Logix practical implementation

On Rockwell Logix platforms, engineers commonly work with the `PIDE` instruction.

Typical loop signals include:

- setpoint
- process variable
- control variable

Common parameters include:

- proportional gain
- integral gain
- derivative gain
- bias
- output high and low limits
- deadband
- process-variable filtering

### Why bias matters

Bias represents the base actuator effort needed to hold a normal operating point.

Examples:

- hover thrust in a vertical system
- base torque in a loaded motor system
- normal valve opening for a steady flow condition

If bias is not handled explicitly, the integral term often has to build that value on its own.

## 5. Siemens practical implementation

Siemens platforms commonly expose PID loops through `PID_Compact` style blocks.

These controllers usually express tuning with:

- `Kp`
- `Ti`
- `Td`
- cycle or sample time
- output limits

Many engineers think about the relationships like this:

- `Ki` scales with `Kp / Ti`
- `Kd` scales with `Kp x Td`

The exact implementation depends on the block form and time-base conventions, so vendor documentation should be checked before converting values directly between platforms.

## 6. Bias and feedforward

Bias provides the steady-state actuator value that a plant may need before the loop starts making small corrections.

Feedforward is different. It adds a predicted actuator contribution based on known operating conditions rather than waiting for error to build first.

In practical terms:

- **bias** helps hold the operating point
- **feedforward** helps the loop react faster to expected load or command changes

## 7. Output limits and anti-windup

Real actuators have limits such as:

- valve travel from 0 to 100 percent
- motor speed command limits
- heater power limits

If the controller output hits those limits while integral action keeps accumulating, windup can occur.

That is why industrial PID blocks often include:

- output clamps
- anti-windup logic
- bumpless transfer handling

The controller math is never the whole design. The actuator limits are part of the control design too.

## 8. Measurement filtering and sample time

Derivative action amplifies fast signal changes, so noisy feedback can make the derivative path react to measurement noise instead of true process behavior.

That is why many industrial loops use:

- PV filtering
- derivative filtering
- PI-only structures when measurement quality is poor

Industrial PID is also always discrete in a PLC, drive, or digital controller. That means the loop behavior depends on the configured sample or cycle time.

A loop that is tuned at one update rate may behave differently if the execution timing changes significantly.

## 9. Engineering takeaways

- Industrial PID always includes more than just the P, I, and D branches.
- `SP`, `PV`, and `CV` are the most common field terms for command, measurement, and output.
- Bias is important whenever the plant needs a nonzero holding effort.
- Output limits, anti-windup, filtering, and sample time are core design concerns, not optional cleanup items.
- Rockwell and Siemens express the same basic ideas with different naming and parameter conventions.

## Related files

- [PID Control Overview](./pid_control_intuitive_foundation.md)
- [PID Control Intuition](./pid_control_intuition.md)
- [Industrial Control Loop Architectures](./industrial_control_loop_architectures.md)
- [PID Heater Control With Contactor](./pid_heater_control_with_contactor.md)
