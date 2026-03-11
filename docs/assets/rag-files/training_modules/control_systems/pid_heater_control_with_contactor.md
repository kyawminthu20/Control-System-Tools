<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: CONTROL_SYSTEMS
MODULE_ID: pid_heater_control_with_contactor
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["heater_control", "contactor", "time_proportioning", "pi_control", "anti_windup", "deadband", "state_machine", "structured_text", "heater_interlocks"]
  systems: ["thermal_loop", "heater", "plc", "contactor"]
-->

# PID Heater Control With Contactor

## 0. Purpose

This note explains a practical heater-control design for a heating-only process with:

- temperature sensor feedback
- a contactor output
- minimum 2-second on time
- minimum 2-second off time

This is the kind of structure that fits a real PLC implementation.

## 1. Control philosophy

Because the final device is a **contactor**, the controller should be split into two parts:

- **Part A - temperature controller**: generates a 0 to 100 percent heat demand
- **Part B - output scheduler**: converts that demand into a legal on/off command

The scheduler must enforce:

- minimum on time
- minimum off time
- safety shutdowns
- anti-short-cycling behavior

That is the correct architecture for a binary heater actuator.

## 2. Why a contactor changes the design

A mechanical contactor is essentially:

- on or off
- limited in switching life
- subject to minimum on-time and off-time constraints
- unsuitable for high-frequency modulation

That means a continuous controller output such as "37.4 percent" should not be sent directly to the contactor as if it were an analog final element.

The usual industrial pattern is:

`temperature error -> PI or slow PID -> 0 to 100 percent heat demand -> time-proportioning block -> contactor on/off command`

This works because the heater and thermal mass average the switched power over time. Even though the contactor is binary, the process temperature responds more smoothly than the raw output pattern.

## 3. Why PI is usually the right starting point

For contactor-heated systems, PI is usually better than aggressive full PID.

Common reasons:

- thermal processes are slow
- temperature signals may be noisy
- derivative action often adds little value
- the final actuator is already coarse

Derivative should usually stay at zero initially and only be added if overshoot remains a real problem after conservative PI tuning.

## 4. Functional block view

```text
Setpoint
   |
   v
[ Error = SP - PV ]
   |
   v
[ PI Controller ]
   |
   v
[ Output Clamp 0..100% ]
   |
   v
[ Time Proportioning / Duty Scheduler ]
   |
   v
[ Min ON / Min OFF Enforcement ]
   |
   v
[ Safety Interlocks ]
   |
   v
[ Contactor Coil ]
   |
   v
[ Heater ]
   |
   v
[ Temperature Sensor ]
   |
   +------------------------ feedback ------------------------+
```

## 5. Time-proportioning window

The PI block can still produce a 0 to 100 percent demand, but that demand should be converted into on-time within a fixed scheduling window.

A typical starting point is:

- control window: 20 to 40 seconds
- minimum on time: 2 seconds
- minimum off time: 2 seconds

Example with a 20-second window:

- 10 percent demand -> 2 seconds on, 18 seconds off
- 25 percent demand -> 5 seconds on, 15 seconds off
- 50 percent demand -> 10 seconds on, 10 seconds off
- 80 percent demand -> 16 seconds on, 4 seconds off

This is much more realistic than trying to switch every 2 seconds just because the contactor can survive a 2-second minimum interval.

## 6. Output conditioning and resolution limits

With a fixed window:

`OnTime = WindowTime x HeatDemandPct / 100`

`OffTime = WindowTime - OnTime`

Then enforce the mechanical limits:

- if `OnTime` is below the minimum on time, treat the demand as zero for that window
- if `OffTime` is below the minimum off time, treat the demand as fully on for that window
- otherwise run the normal duty cycle

With a 20-second window and a 2-second minimum pulse:

- the smallest valid on pulse is 10 percent
- very fine demands such as 1 percent or 5 percent are not representable

Longer windows improve duty resolution:

- 40-second window -> 5 percent minimum pulse
- 60-second window -> about 3.3 percent minimum pulse

The tradeoff is slower effective control action.

## 7. Suggested state machine

A clean implementation can use a small state machine with four states:

- `OFF`: heater is off and the controller is waiting for a valid heating demand
- `HEATING_ON`: contactor is energized for the on portion of the duty window
- `HEATING_OFF_WAIT`: contactor is de-energized while waiting through the off portion of the duty window
- `TRIP`: forced-off state due to a safety or sensor fault

That separation makes the minimum on/off rules much easier to enforce cleanly.

## 8. Main signals

Typical inputs:

- process variable
- setpoint
- auto/manual command
- permissive status
- high-high temperature trip
- sensor-fault status
- contactor feedback, if available

Useful internal variables:

- error
- heat demand percent
- window time
- on time
- off time
- minimum on time
- minimum off time
- integrator state
- state-machine state

Typical outputs:

- contactor command
- sensor-fault alarm
- overtemperature alarm
- no-heat-rise alarm
- contactor mismatch alarm

## 9. Practical PI law

For this application, a simple first-pass law is:

```text
Error = SP - PV
P_term = Kp * Error
I_term = I_term + Ki * Error * dt
HeatDemandPct = clamp(P_term + I_term, 0, 100)
```

Heating-only action should be configured so that:

- PV below SP -> more output
- PV above SP -> less output

## 10. Anti-windup rule for this heater

This application needs anti-windup because:

- the output is clamped between 0 and 100 percent
- the final actuator is coarse on/off hardware
- the plant can spend long periods saturated at full output during warm-up

A practical rule is:

```text
If output >= 100% and error > 0:
    stop integrating

If output <= 0% and error < 0:
    stop integrating
```

More generally, only integrate when the output is not saturated or when the current error would drive the output back toward the valid range.

## 11. Operating modes and deadband

A practical heater controller often works well with two modes:

- **warm-up mode**: force 100 percent heat demand while far below setpoint
- **control mode**: switch to PI behavior as the temperature approaches the target

Example concept:

```text
If PV < SP - WarmupBand:
    HeatDemandPct = 100
Else:
    use PI output
```

For contactor systems, a small deadband near setpoint is often useful to reduce wear and chatter.

Typical behaviors inside the deadband include:

- hold last demand
- freeze the integrator
- allow only very slow correction

Example concept:

```text
If abs(Error) < Deadband:
    freeze integrator adjustment
```

## 12. Sensor validation and safety

Do not trust the temperature input blindly.

Validate for:

- open sensor
- shorted sensor
- out-of-range value
- implausible step change or rate of change

If the sensor is invalid, the safe response is to trip the heater off and force the controller into a faulted state.

The scheduled output must still be overridden by safety logic such as:

- overtemperature trip
- sensor failure
- permissive loss
- overload or protection trip
- welded-contactor detection if feedback is available

For overheating hazards, software shutdown should be backed by an independent hardware protective device rather than relying only on PLC logic.

## 13. Heater and contactor fault detection

Useful commissioning and maintenance alarms include:

- **no heat rise** while commanded on for an extended period
- **command/feedback mismatch** if the contactor has auxiliary status contacts
- **welded contactor indication** if command is off but feedback remains on

Those checks help distinguish tuning problems from hardware failures.

## 14. Structured-text sketch

The following sketch shows the core idea, not a vendor-specific library block:

```pascal
Error := SP - PV;

SensorFault := (PV < PV_MinValid) OR (PV > PV_MaxValid);
OverTempTrip := (PV >= HighHighLimit);

IF NOT Permissive_OK OR SensorFault OR OverTempTrip THEN
    State := TRIP;
END_IF;

CASE State OF

    TRIP:
        ContactorCmd := FALSE;
        HeatDemandPct := 0.0;

        IF Permissive_OK AND NOT SensorFault AND NOT OverTempTrip AND AutoMode THEN
            State := OFF;
        END_IF;

    OFF:
        ContactorCmd := FALSE;

        IF AutoMode AND Permissive_OK THEN
            IF PV < (SP - WarmupBand) THEN
                HeatDemandPct := 100.0;
            ELSE
                P_term := Kp * Error;

                IF NOT ((HeatDemandPct >= 100.0 AND Error > 0.0) OR
                        (HeatDemandPct <= 0.0 AND Error < 0.0)) THEN
                    I_term := I_term + (Ki * Error * dt);
                END_IF;

                HeatDemandPct := P_term + I_term;

                IF HeatDemandPct > 100.0 THEN HeatDemandPct := 100.0; END_IF;
                IF HeatDemandPct < 0.0 THEN HeatDemandPct := 0.0; END_IF;
            END_IF;

            OnTime := WindowTime * HeatDemandPct / 100.0;
            OffTime := WindowTime - OnTime;

            IF OnTime < MinOnTime THEN
                OnTime := T#0s;
                OffTime := WindowTime;
            ELSIF OffTime < MinOffTime THEN
                OnTime := WindowTime;
                OffTime := T#0s;
            END_IF;

            IF OnTime > T#0s THEN
                State := HEATING_ON;
                StateTimer := T#0s;
            END_IF;
        END_IF;

    HEATING_ON:
        ContactorCmd := TRUE;
        StateTimer := StateTimer + dt;

        IF StateTimer >= OnTime THEN
            ContactorCmd := FALSE;
            State := HEATING_OFF_WAIT;
            StateTimer := T#0s;
        END_IF;

    HEATING_OFF_WAIT:
        ContactorCmd := FALSE;
        StateTimer := StateTimer + dt;

        IF StateTimer >= OffTime THEN
            State := OFF;
            StateTimer := T#0s;
        END_IF;

END_CASE;
```

## 15. Commissioning sequence

A practical first commissioning pass is:

1. verify sensor scaling, heater output polarity, contactor action, and protective devices
2. command fixed duty values manually and confirm the real on/off timing
3. start with integral disabled or very weak
4. tune proportional action first
5. add integral slowly until steady-state offset disappears without hunting
6. solve overshoot first by adjusting P, I, warm-up transition, or deadband before reaching for derivative

## 16. Recommended starting values

A reasonable first-cut design is:

- window time: 20 seconds
- minimum on time: 2 seconds
- minimum off time: 2 seconds
- warm-up band: about 5 degrees below setpoint
- deadband: about plus or minus 0.5 degrees
- controller type: PI only
- derivative: zero initially
- PLC execution rate: roughly 250 to 500 milliseconds

These are starting points, not universal rules.

## 17. Engineering takeaways

- A contactor-heated loop is not a normal analog-output PID problem.
- PI plus time-proportioning is usually the right first solution.
- Minimum on/off timing, anti-windup, deadband, and permissives are part of the control design, not afterthoughts.
- Warm-up mode often works better than letting PI handle the entire trip from ambient.
- If tight hold and fine modulation matter, the final element should usually be SSR, SCR, or another modulating power stage instead of a mechanical contactor.

## Related files

- [PID Control Overview](./pid_control_intuitive_foundation.md)
- [PID Control Intuition](./pid_control_intuition.md)
- [Industrial PID Implementation](./industrial_pid_implementation.md)
- [Industrial Control Loop Architectures](./industrial_control_loop_architectures.md)
