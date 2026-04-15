---
layout: training-module
title: "PID Heater Control with Contactor"
description: "Practical heater-control design for a PI controller driving a contactor — time-proportioning output scheduling, minimum on/off time enforcement, state machine, and safety interlocks."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Control Systems"
    url: "/fundamentals/control/"
repo_path: "control-standards/rag/training_modules/control_systems/pid_heater_control_with_contactor.md"
related_standards:
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
redirect_from:
  - /training/control-systems/pid-heater-control/
  - /training/control-systems/pid-heater-control/index.html

---

## Purpose

This module explains a practical heater-control design for a heating-only process with temperature sensor feedback, a contactor output, and minimum 2-second on/off timing. This is the kind of structure that fits a real PLC implementation.

## Control philosophy

Because the final device is a **contactor**, the controller should be split into two parts:

- **Part A — temperature controller**: generates a 0 to 100 percent heat demand
- **Part B — output scheduler**: converts that demand into a legal on/off command

The scheduler must enforce:

- minimum on time
- minimum off time
- safety shutdowns
- anti-short-cycling behavior

That is the correct architecture for a binary heater actuator.

## Why a contactor changes the design

A mechanical contactor is essentially:

- on or off
- limited in switching life
- subject to minimum on-time and off-time constraints
- unsuitable for high-frequency modulation

That means a continuous controller output such as "37.4 percent" should not be sent directly to the contactor as if it were an analog final element.

The usual industrial pattern is:

`temperature error → PI controller → 0 to 100% heat demand → time-proportioning block → contactor on/off command`

This works because the heater and thermal mass average the switched power over time.

## Why PI is usually the right starting point

For contactor-heated systems, PI is usually better than aggressive full PID.

Common reasons:

- thermal processes are slow
- temperature signals may be noisy
- derivative action often adds little value
- the final actuator is already coarse

Derivative should usually stay at zero initially and only be added if overshoot remains a real problem after conservative PI tuning.

## Functional block view

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
   +--- feedback ---+
```

## Time-proportioning window

The PI block produces a 0 to 100 percent demand, but that demand should be converted into on-time within a fixed scheduling window.

A typical starting point is:

- control window: 20 to 40 seconds
- minimum on time: 2 seconds
- minimum off time: 2 seconds

Example with a 20-second window:

| Demand | On time | Off time |
|---|---|---|
| 10% | 2 s | 18 s |
| 25% | 5 s | 15 s |
| 50% | 10 s | 10 s |
| 80% | 16 s | 4 s |

## Output conditioning and resolution limits

```
OnTime  = WindowTime × HeatDemandPct / 100
OffTime = WindowTime − OnTime
```

Then enforce mechanical limits:

- if `OnTime` is below the minimum on time, treat the demand as zero for that window
- if `OffTime` is below the minimum off time, treat the demand as fully on for that window
- otherwise run the normal duty cycle

With a 20-second window and a 2-second minimum pulse, the smallest valid on pulse is 10 percent. Longer windows improve duty resolution but slow effective control action.

## Suggested state machine

A clean implementation uses a small state machine with four states:

| State | Description |
|---|---|
| `OFF` | Heater is off; waiting for a valid heating demand |
| `HEATING_ON` | Contactor energized for on portion of the duty window |
| `HEATING_OFF` | Contactor de-energized for off portion; timer counting |
| `FAULT` | High temperature or other safety condition — locked off |

The `FAULT` state requires an explicit acknowledgement reset and cannot be self-cleared by the temperature loop.

## Safety considerations

- Over-temperature protection should be independent of the PI controller — typically a dedicated thermostat or high-temperature cut-out
- The contactor output state should be alarmed if it disagrees with the commanded state
- Minimum off time prevents contactor short-cycling that degrades mechanical life

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/control/control-loop-architectures/' | relative_url }}">&larr; Control Loop Architectures</a>
  <a href="{{ '/fundamentals/control/' | relative_url }}">↑ Control Systems</a>
  <a href="{{ '/fundamentals/control/pid-drone-control/' | relative_url }}">PID in Drone and Motion Control &rarr;</a>
</div>
