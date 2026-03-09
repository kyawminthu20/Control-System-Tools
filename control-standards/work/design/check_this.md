<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: SOURCE_NOTE
PURPOSE: Motor engineering interview questions — source material for training module expansion.
         Content has been partially promoted into training_modules/electrical_machines/.
         Retained here as reference for future training module work.
-->

# Motor Engineering Interview Questions (Source Note)

## What this file is

Work note containing motor engineering Q&A organized by difficulty level.
Covers torque/power relationships, motor selection, drives, and controls topics
relevant to industrial automation, robotics, and power electronics roles.

Content from this file informed the motor comparison and fundamentals files
already promoted into `training_modules/electrical_machines/`.

Use as a seed for future training module expansion, not as a promoted RAG file.

---

# Motor Engineering Interview Questions (with Answers)

## 1. Fundamental Motor Questions

### Question 1

**What is the difference between torque and power in a motor?**

**Answer**

Torque is the rotational force produced by the motor.

Power represents how fast that torque is applied.

Relationship:

[
P = T \times \omega
]

Where:

- (P) = mechanical power
- (T) = torque
- (\omega) = angular velocity

Another common equation:

[
P(kW) = \frac{T(Nm) \times RPM}{9550}
]

---

### Question 2

**What is synchronous speed of an AC motor?**

**Answer**

Synchronous speed is the speed of the rotating magnetic field in the stator.

[
N_s = \frac{120 \times f}{P}
]

Where:

- (N_s) = synchronous speed (RPM)
- (f) = electrical frequency
- (P) = number of poles

Example:

60 Hz motor with 4 poles:

[
N_s = 1800 \ RPM
]

---

### Question 3

**What is slip in an induction motor?**

**Answer**

Slip is the difference between synchronous speed and rotor speed.

[
s = \frac{N_s - N_r}{N_s}
]

Where:

- (N_s) = synchronous speed
- (N_r) = rotor speed

Slip is required for torque production.

Typical slip:

- 1–3% at full load.

---

## 2. Motor Types

### Question 4

**What is the difference between an induction motor and a synchronous motor?**

| Induction Motor       | Synchronous Motor           |
| --------------------- | --------------------------- |
| Rotor current induced | Rotor magnetic field locked |
| Slip required         | No slip                     |
| Simpler               | More complex                |
| Very common           | Specialized applications    |

Induction motors dominate industrial applications.

---

### Question 5

**What is the difference between BLDC and PMSM motors?**

| BLDC                      | PMSM                     |
| ------------------------- | ------------------------ |
| Trapezoidal back EMF      | Sinusoidal back EMF      |
| Six-step commutation      | Field-oriented control   |
| Often simpler controllers | Used in servo/EV systems |

Physically very similar.

The difference is mainly **control strategy**.

---

### Question 6

**What is a servo motor?**

A servo motor is not a unique motor type.

It is a **closed-loop motion control system** consisting of:

- motor
- encoder/resolver
- servo drive
- feedback control loops

Control loops:

```
Position loop
Velocity loop
Current loop
```

---

## 3. Motor Control

### Question 7

**How does a VFD control motor speed?**

A VFD changes the frequency applied to the motor.

Speed equation:

[
N_s = \frac{120f}{P}
]

Reducing frequency reduces speed.

The VFD maintains **V/Hz ratio** to maintain motor flux.

---

### Question 8

**What are the main control methods for VFDs?**

1. **V/Hz control**
   - simple
   - pumps/fans

2. **Vector control**
   - better torque control

3. **Sensorless vector**
   - no encoder required

4. **Field-oriented control**
   - used in servo drives

---

### Question 9

**What is field-oriented control (FOC)?**

FOC controls motor torque by controlling magnetic field orientation.

The stator current is transformed into:

```
d-axis current
q-axis current
```

- d-axis controls magnetic flux
- q-axis controls torque

Used in:

- servo motors
- EV motors
- robotics

---

## 4. Motor Applications

### Question 10

**Why are induction motors common in industry?**

Reasons:

- rugged
- inexpensive
- reliable
- simple construction
- low maintenance

Applications:

- pumps
- conveyors
- compressors
- fans

---

### Question 11

**Why are servo motors used in robotics?**

Servo systems provide:

- precise position control
- high acceleration
- fast response
- closed-loop feedback

Applications:

- robotic joints
- CNC machines
- semiconductor equipment

---

### Question 12

**Why do drones use BLDC motors?**

Advantages:

- high power density
- lightweight
- efficient
- high RPM capability

Often **outrunner BLDC motors**.

---

## 5. Drive and Electrical Questions

### Question 13

**Why is motor cable length important for VFD systems?**

Long cables cause:

- reflected wave voltage spikes
- insulation stress
- motor overheating

Mitigation methods:

- dv/dt filters
- output reactors
- sine filters

---

### Question 14

**Why is motor shielding important in VFD systems?**

VFDs generate high-frequency switching noise.

Shielded cables help reduce:

- EMI
- ground current noise
- encoder interference

---

### Question 15

**What happens if V/Hz ratio is too low?**

Motor flux decreases.

Effects:

- reduced torque
- poor acceleration
- unstable operation

---

### Question 16

**What happens if V/Hz ratio is too high?**

Magnetic saturation occurs.

Results:

- overheating
- excessive current
- possible motor damage

---

## 6. Practical Troubleshooting Questions

### Question 17

**Motor overheats but current is normal. What could be wrong?**

Possible causes:

- cooling fan failure
- blocked ventilation
- high ambient temperature
- mechanical friction
- bearing damage

---

### Question 18

**Motor vibrates excessively. Possible reasons?**

- shaft misalignment
- bearing wear
- rotor imbalance
- loose mounting
- coupling issues

---

### Question 19

**VFD trips on overcurrent during acceleration. Causes?**

Possible reasons:

- acceleration ramp too short
- mechanical load too heavy
- motor parameter mismatch
- faulty motor
- incorrect drive tuning

---

### Question 20

**Motor runs but produces no torque. Why?**

Possible reasons:

- phase loss
- broken rotor bars
- incorrect drive configuration
- mechanical disconnect

---

# Advanced Interview Questions (Senior Engineers)

### Question 21

**What is motor inertia matching in servo systems?**

Servo performance depends on ratio:

```
Load inertia / Motor inertia
```

Typical recommended ratio:

```
< 10:1
```

Too large ratio causes instability.

---

### Question 22

**What causes regenerative voltage in VFD systems?**

When the motor acts as a generator:

Examples:

- deceleration
- lowering loads
- high inertia stopping

Energy flows back to DC bus.

Solutions:

- braking resistor
- regenerative drive

---

### Question 23

**What is motor power factor?**

Power factor:

[
PF = \frac{Real Power}{Apparent Power}
]

Low power factor increases current demand.

Induction motors often have PF:

```
0.8 – 0.9
```

---

# High-Level System Architecture Question

### Question 24

**Explain the architecture of a motor drive system**

Typical architecture:

```
AC Power
   ↓
Rectifier
   ↓
DC Bus
   ↓
Inverter
   ↓
Motor
```

Control system:

```
Controller
   ↓
PWM control
   ↓
Motor phases
```

---

# Key Interview Tip

Interviewers are usually checking whether you understand:

1. **Physics**
2. **Control methods**
3. **Practical troubleshooting**
4. **Application selection**

Not just formulas.

---

---

# Part 2 — Motors, Drives, and Motion Control

# 1. Motor Fundamentals Interview Questions

## Question 1

**What is the difference between torque and power in a motor?**

**Answer**

Torque is rotational force produced by the motor.

Power is the rate at which torque is applied.

Mechanical power equation:

P = T × ω

Where
P = power
T = torque
ω = angular velocity

Engineering form:

P(kW) = (Torque × RPM) / 9550

---

## Question 2

**What determines the speed of an AC motor?**

Speed depends on:

- supply frequency
- number of motor poles

Synchronous speed:

Ns = (120 × f) / P

Where
f = frequency
P = number of poles

Example
60 Hz, 4-pole motor:

Ns = 1800 RPM

---

## Question 3

**What is slip in an induction motor?**

Slip is the difference between synchronous speed and rotor speed.

s = (Ns − Nr) / Ns

Where
Ns = synchronous speed
Nr = rotor speed

Slip enables torque generation.

Typical slip:

1–3% at full load.

---

## Question 4

**What is motor efficiency?**

Efficiency measures how much electrical power becomes mechanical output.

η = Output Power / Input Power

Loss sources:

- copper loss
- core loss
- mechanical loss
- stray losses

---

## Question 5

**What causes starting current in induction motors?**

At startup:

- rotor speed = 0
- slip = 100%

This produces large current.

Typical starting current:

5–7 × rated current.

---

# 2. Motor Types Interview Questions

## Question 6

**What are the main types of industrial motors?**

Common types:

- induction motors
- synchronous motors
- brushed DC motors
- BLDC motors
- PMSM motors
- stepper motors

---

## Question 7

**Difference between induction and synchronous motors**

Induction Motor

- rotor current induced
- slip required
- most common industrial motor

Synchronous Motor

- rotor rotates exactly at synchronous speed
- no slip
- used in specialized systems

---

## Question 8

**What is a BLDC motor?**

Brushless DC motor.

Characteristics:

- permanent magnet rotor
- electronic commutation
- high efficiency
- high power density

Applications:

- drones
- EV systems
- robotics
- portable machines

---

## Question 9

**What is a PMSM motor?**

Permanent Magnet Synchronous Motor.

Features:

- sinusoidal back EMF
- typically controlled by FOC
- high torque density

Used in:

- servo systems
- EV traction motors
- robotics

---

## Question 10

**What is a stepper motor?**

A motor that moves in discrete steps.

Advantages:

- simple position control
- no feedback required

Limitations:

- lower torque at high speed
- risk of losing steps.

---

# 3. VFD Interview Questions

## Question 11

**What is a VFD?**

A Variable Frequency Drive controls motor speed by adjusting frequency.

Main functions:

- soft start
- speed control
- energy savings
- process optimization

---

## Question 12

**How does a VFD work?**

Architecture:

AC supply
→ Rectifier
→ DC bus
→ Inverter
→ Motor

The inverter produces variable frequency output using PWM.

---

## Question 13

**What is V/Hz control?**

V/Hz control maintains constant voltage-to-frequency ratio.

Purpose:

Maintain magnetic flux.

Used for:

- pumps
- fans
- conveyors

---

## Question 14

**What is vector control?**

Vector control separates torque and flux components.

Benefits:

- better torque response
- better low-speed control.

---

## Question 15

**What causes regenerative voltage in VFD systems?**

When the motor becomes a generator.

Examples:

- rapid deceleration
- lowering loads
- high inertia stopping

Solutions:

- braking resistor
- regenerative unit.

---

# 4. Servo System Interview Questions

## Question 16

**What is a servo system?**

A closed-loop motion control system consisting of:

- motor
- encoder/resolver
- servo drive
- control loops.

---

## Question 17

**What are the control loops in servo drives?**

Typical loop hierarchy:

Current loop
Velocity loop
Position loop

Current loop is fastest.

---

## Question 18

**What is field-oriented control?**

FOC transforms motor current into two components:

d-axis current
q-axis current

d-axis controls magnetic flux.

q-axis controls torque.

Used in:

- servo drives
- EV motors
- robotics.

---

## Question 19

**Why are encoders used in servo systems?**

Encoders provide feedback for:

- position
- speed
- direction

Types:

- incremental
- absolute
- resolver.

---

## Question 20

**What is inertia matching in servo systems?**

Servo stability depends on ratio:

Load inertia / motor inertia

Typical recommended ratio:

< 10:1

Higher ratios reduce stability.

---

# 5. Motor Electrical Design Questions

## Question 21

**Why is motor cable shielding important with VFDs?**

VFD switching creates high-frequency noise.

Shielding reduces:

- EMI
- ground currents
- signal interference.

---

## Question 22

**Why do long motor cables cause problems with VFDs?**

Problems:

- reflected wave voltage spikes
- insulation stress
- motor heating.

Solutions:

- dv/dt filters
- output reactors
- sine filters.

---

## Question 23

**What determines motor conductor size?**

Factors:

- motor current
- conductor temperature rating
- installation method
- voltage drop
- protection coordination.

---

## Question 24

**Why are motor breakers sized differently from normal circuits?**

Motors have high starting current.

Protection must allow:

- starting current
- short-circuit protection.

Overload protection is usually separate.

---

# 6. Industrial Troubleshooting Questions

## Question 25

**Motor overheats but current is normal. Why?**

Possible causes:

- blocked ventilation
- high ambient temperature
- bearing friction
- cooling fan failure.

---

## Question 26

**Motor vibrates excessively. Causes?**

Possible causes:

- misalignment
- rotor imbalance
- worn bearings
- loose mounting.

---

## Question 27

**Motor trips VFD on overcurrent. Why?**

Possible causes:

- acceleration ramp too fast
- heavy load
- incorrect motor parameters
- mechanical binding.

---

## Question 28

**Motor produces noise at low speed with VFD. Why?**

Possible reasons:

- PWM switching noise
- motor resonance
- poor tuning.

---

# 7. Advanced Engineering Questions

## Question 29

**What is motor torque curve?**

Torque vs speed relationship.

Important regions:

- starting torque
- pull-up torque
- breakdown torque.

---

## Question 30

**What is field weakening in motor control?**

Above base speed:

Voltage limit reached.

Motor flux is reduced.

Allows higher speed but lower torque.

Used in:

- EV motors
- servo systems.

---

# 8. Architecture Questions

## Question 31

**What is the difference between centralized and decentralized drives?**

Centralized

Drive in control cabinet.

Decentralized

Drive mounted near motor.

Advantages:

- shorter cables
- modular installation.

---

## Question 32

**What is an integrated motor drive?**

Motor and drive built into one assembly.

Advantages:

- compact design
- simplified wiring.

Challenges:

- thermal management
- maintenance.

---

# 9. Application Questions

## Question 33

**Why do pumps and fans use VFDs?**

Because:

Power ∝ speed³

Small speed reduction saves large energy.

---

## Question 34

**Why do robotics systems use servo motors?**

Because they provide:

- precise position control
- fast acceleration
- closed-loop feedback.

---

## Question 35

**Why do drones use BLDC motors?**

Advantages:

- high RPM capability
- lightweight
- high power density.

---

# 10. Senior Engineering Questions

## Question 36

**What limits motor torque?**

Limits include:

- current limit
- magnetic saturation
- thermal limits.

---

## Question 37

**Why are permanent magnet motors efficient?**

Reasons:

- no rotor copper loss
- strong magnetic field
- high power density.

---

## Question 38

**What is motor power factor?**

PF = real power / apparent power

Induction motors often:

0.8–0.9

---

## Question 39

**Why do motors need grounding?**

Grounding ensures:

- fault protection
- shock safety
- noise control.

---

## Question 40

**What are the main motor losses?**

Loss types:

- stator copper loss
- rotor copper loss
- core loss
- mechanical loss.

---

# Key Interview Strategy

Interviewers are evaluating three things:

1. **Conceptual understanding**
2. **Real-world troubleshooting**
3. **System-level thinking**

Not just formulas.

---

<!-- end of source note -->
