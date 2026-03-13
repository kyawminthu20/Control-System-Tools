---
layout: training-module
title: "PID in Drone and Motion Control"
description: "How PID stabilizes a quadcopter — nested rate, attitude, altitude, and position loops, motor mixing, sensor feedback, and why a drone is a strong teaching example for cascade PID."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Control Systems"
    url: "/training/control-systems/"
repo_path: "control-standards/rag/training_modules/control_systems/pid_drone_control.md"
---

## Purpose

This module explains how PID control stabilizes and guides a multirotor drone, especially a quadcopter. Use it to understand nested loop structures and how PID principles from industrial systems translate to fast motion-control applications.

## Why drone control is a useful PID example

A quadcopter is an **inherently unstable system**. Without active control, it flips, drifts, or falls almost immediately.

That makes it a strong teaching example for PID because:

- the plant is fast
- the system is unstable without feedback
- the controller must react continuously
- nested loops are easy to see conceptually
- actuator changes map directly into motion and torque

In most drones, stability is achieved through **fast cascade feedback loops** running inside the flight controller at hundreds or thousands of updates per second.

## What the flight controller must regulate

A drone must regulate several variables at the same time:

| Controlled state | Meaning |
| --- | --- |
| Roll | left-right tilt |
| Pitch | forward-back tilt |
| Yaw | rotation around the vertical axis |
| Altitude | vertical position |
| Vertical speed | climb or descent rate |
| Horizontal velocity | speed over ground |
| Position | horizontal location |

The most critical inner stabilization loops are roll, pitch, and yaw. Altitude and position control sit on top of those inner loops.

## Sensor feedback sources

A flight controller depends heavily on an **IMU (Inertial Measurement Unit)**:

| Sensor | Main use |
| --- | --- |
| Gyroscope | angular velocity |
| Accelerometer | acceleration and gravity reference |
| Magnetometer | heading reference |
| Barometer | altitude estimate |
| GPS | position and ground velocity |
| Range sensor or lidar | low-altitude height control on some systems |

The **gyroscope is usually the most critical stabilization sensor** because the inner rate loop depends on accurate angular-rate measurement.

## Control loop hierarchy

Flight controllers use **nested loops** rather than one single PID block:

```text
Position Loop
        ↓
Velocity Loop
        ↓
Angle / Attitude Loop
        ↓
Angular Rate Loop
        ↓
Motor Mix
        ↓
ESC / Motor / Propeller
```

Not every drone uses every layer. A racing drone may focus mainly on rate control. A camera drone usually uses the full stack.

## The most important inner loop: angular rate control

The **angular rate loop** is the core stabilization loop.

- desired roll rate = pilot command or outer-loop output
- measured roll rate = gyroscope reading
- error = desired rate − measured rate

The PID controller turns that error into a corrective torque demand. This loop is the reason the drone feels locked-in rather than loose or unstable.

## Angle or attitude loop

Above the rate loop, many drones use an **angle loop**:

- the angle loop controls desired orientation
- the rate loop controls how fast the drone rotates to achieve that orientation

Example cascade:

`attitude error → desired angular rate → rate PID → motor command`

## Motor mixing

Loop outputs (roll demand, pitch demand, yaw demand, thrust demand) must be distributed across 4 or more motors.

Motor mixing converts these demands into individual motor speed commands. Each motor contributes differently to each axis depending on its position and direction of rotation.

## Tuning considerations in fast motion control

Drone tuning differs from slow industrial process loops in several ways:

- **Derivative filtering is critical** — gyro signals contain high-frequency noise
- **Sample time matters enormously** — rate loops running at lower bandwidth feel sluggish
- **Anti-windup is still needed** — motor saturation during aggressive maneuvers can cause integral windup
- **Gain stability margins are tight** — an aggressive rate loop gain may cause oscillation at motor resonance frequencies

## Connection to industrial motion control

The same nested-loop structure appears in industrial servo systems:

`position loop → velocity loop → current loop → inverter → motor`

The drone example makes the cascade concept concrete before applying it to servo drive commissioning.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/control-systems/pid-heater-control/' | relative_url }}">&larr; PID Heater Control</a>
  <a href="{{ '/training/control-systems/' | relative_url }}">↑ Control Systems</a>
  <span></span>
</div>
