---
layout: training-module
title: "BLDC and PMSM Implementation Guide"
description: "Production-grade implementation reference: system architecture, control methods, drive selection, wiring, failure modes, and a full commissioning checklist."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "Motors, Drives, and Motion"
    url: "/fundamentals/motors/"
repo_path: "control-standards/rag/training_modules/electrical_machines/bldc_pmsm_implementation_guide.md"
---

## Purpose

- **When to use this page:** you are about to build, specify, or commission a BLDC or PMSM system and the motor family is already decided.
- **What it helps you decide:** drive stack, control method, wiring archetype, and commissioning gates.
- **What it will not do:** choose the family for you (see [BLDC vs PMSM Comparison]({{ '/fundamentals/motors/bldc-vs-pmsm/' | relative_url }})), replace the drive vendor's manual, or substitute for a machine-specific risk assessment.

### Choose fast

<div class="glance-grid">
  <div class="card">
    <span class="card__label">Choose BLDC when</span>
    <span class="card__title">Cost &amp; simplicity win</span>
    <p class="card__desc">Fans, pumps, drones, power tools, low-cost conveyors. Torque ripple is tolerable; zero-speed torque is not required.</p>
  </div>
  <div class="card">
    <span class="card__label">Choose PMSM when</span>
    <span class="card__title">Precision &amp; efficiency win</span>
    <p class="card__desc">Servo, robotics, CNC, EV traction, semi stages. You need smooth torque, zero-speed holding, or field-weakening range.</p>
  </div>
  <div class="card">
    <span class="card__label">Watch-outs</span>
    <span class="card__title">What usually bites first</span>
    <p class="card__desc">Encoder offset wrong, shield pigtailed, long motor cable without reactor, regen OV, FOC parameters not ID'd.</p>
  </div>
  <div class="card">
    <span class="card__label">Build sequence</span>
    <span class="card__title">Size → spec → wire → tune</span>
    <p class="card__desc">Size motor from load, spec drive to motor, wire per archetype, run parameter ID, then tune current → speed → position.</p>
  </div>
</div>

### Jump to

<div class="glance-grid" role="navigation" aria-label="On this page">
  <a class="card" href="#system-architecture-end-to-end"><span class="card__title">Architecture</span></a>
  <a class="card" href="#control-methods"><span class="card__title">Control</span></a>
  <a class="card" href="#motor-selection-guide"><span class="card__title">Sizing</span></a>
  <a class="card" href="#drive-selection-guide"><span class="card__title">Drive Choice</span></a>
  <a class="card" href="#wiring-and-integration"><span class="card__title">Wiring</span></a>
  <a class="card" href="#implementation-checklist"><span class="card__title">Checklist</span></a>
</div>

---

## Executive overview

**BLDC (Brushless DC Motor)**
- 3-phase permanent-magnet synchronous machine
- **Trapezoidal back-EMF**
- Driven with **6-step (block) commutation**, typically from Hall sensors or sensorless BEMF zero-crossing
- Historically optimized for low BOM cost and simple firmware

**PMSM (Permanent Magnet Synchronous Motor)**
- 3-phase permanent-magnet synchronous machine
- **Sinusoidal back-EMF**
- Driven with **sinusoidal current** via **FOC (Field-Oriented Control)**
- Optimized for smooth torque, precision, and efficiency

### Naming confusion — why it exists

- The motor hardware is often **physically similar** — both have 3-phase stator windings and permanent-magnet rotors
- The distinction lives in: **back-EMF waveform shape**, **stator winding layout** (concentrated vs distributed), and **control strategy**
- Vendors mix the terms freely. A "BLDC" with sinusoidal BEMF + FOC is really a PMSM system. A "PMSM" driven 6-step behaves like a noisy BLDC
- Interior-magnet PMSMs (IPM) have an additional **reluctance torque** component that surface-PM BLDCs cannot exploit

### Why the distinction matters in real systems

- **Torque smoothness** — 6-step produces 14–25% torque ripple; FOC produces <2%
- **Zero-speed torque** — only FOC with proper feedback delivers deterministic torque at standstill
- **Speed range** — IPM-PMSM + FOC field weakening extends constant-power range 3–5× base speed; BLDC 6-step cannot
- **Cost / complexity** — 6-step firmware fits on a $1 MCU; FOC needs a DSP, high-res feedback, and parameter ID
- **Functional safety** — industrial PMSM servo drives carry STO/SS1/SLS per IEC 61800-5-2; low-end BLDC drives typically do not

---

## System architecture (end-to-end)

Both families share the same end-to-end topology. Differences live in the control block and the feedback device.

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    A[Power Source<br/>AC mains or DC bus] --> B[Rectifier / PFC<br/>AC systems only]
    B --> C[DC Link<br/>Capacitor bank]
    C --> D[Inverter<br/>3-phase, 6 switches]
    D --> E[Motor<br/>BLDC or PMSM]
    E --> F[Load<br/>Gearbox, coupling, inertia]

    G[Feedback Device<br/>Hall / Encoder / Resolver] --> H[Controller<br/>MCU / DSP / FPGA]
    E -.rotor position.-> G
    H --> D
    I[Command Input<br/>Analog / fieldbus / step-dir] --> H
</pre></div>

### Block roles

| Block              | Role                                                              |
| ------------------ | ----------------------------------------------------------------- |
| Power source       | Provides energy: battery, DC supply, or AC mains                  |
| Rectifier / PFC    | AC → DC; active PFC for industrial drives, passive for low-cost   |
| DC link            | Buffers ripple, absorbs regen energy, sets inverter input voltage |
| Inverter           | 6-switch 3-phase bridge; modulates phase voltages via PWM         |
| Motor              | Converts electrical power to shaft torque                         |
| Load               | Mechanical coupling, gearbox, and end application                 |
| Feedback device    | Rotor position → required for correct commutation                 |
| Controller         | Runs current, speed, position loops; generates PWM                |
| Command input      | External reference: torque, speed, or position target             |

### Why this, not that — topology-level routing

- **Battery source, no PFC** — mobile and tethered-DC systems (drones, e-bikes, AGVs). Skip rectifier, go straight to DC link.
- **AC mains + passive rectifier** — cost-driven industrial BLDC/VFD. Accept distorted line current.
- **AC mains + active PFC** — any drive that must meet IEC 61000-3-2 / -3-12 (harmonic limits) or operate above ~5 kW in most regions. Required for modern industrial servo drives.

---

## BLDC vs PMSM — deep comparison

| Dimension                | BLDC (6-step)                           | PMSM (FOC)                                                     |
| ------------------------ | --------------------------------------- | -------------------------------------------------------------- |
| Back-EMF shape           | Trapezoidal (flat 120° top)             | Sinusoidal                                                     |
| Stator winding           | Concentrated (tooth-wound)              | Distributed (sinusoidal MMF), sometimes skewed                 |
| Rotor magnets            | Surface-mount (SPM)                     | SPM or interior (IPM) — IPM offers reluctance torque           |
| Ld, Lq relationship      | Ld ≈ Lq                                 | IPM: Ld < Lq → reluctance torque exploitable                   |
| Commutation states       | 6 discrete, per electrical cycle        | Continuous sinusoidal, 3-phase simultaneous                    |
| Required position resolution | 60° electrical (3 Halls sufficient) | <1° electrical (encoder or observer)                           |
| Torque ripple            | 14–25%                                  | <2% with good encoder                                          |
| Cogging torque           | Often higher                            | Lower (by design)                                              |
| Zero-speed torque        | Unreliable without encoder              | Full rated torque, deterministic                               |
| Low-speed smoothness     | Poor (audible commutation)              | Excellent                                                      |
| Speed range extension    | Crude phase advance only                | Field weakening; IPM extends 3–5× base                         |
| MCU requirement          | 8- or 32-bit, 50–100 MHz                | 32-bit DSP or MCU w/ FPU, 150–300 MHz                          |
| Firmware footprint       | 8–20 KB                                 | 60–200 KB (plus autotune, fault logging, fieldbus)             |
| Commissioning effort     | Hours                                   | Days (parameter ID, encoder offset, loop tuning)               |
| Typical applications     | Fans, pumps, drones, power tools        | Servos, robotics, CNC, EV traction, semiconductor stages       |
| Cost (1 kW class system) | Low ($230–650 total)                    | High ($1100–2700 total)                                        |
| Functional safety        | Rare                                    | Industrial servo drives — STO/SS1/SLS per IEC 61800-5-2        |

### The back-EMF is the root cause of every downstream difference

- Feed sine current into a trapezoidal motor → torque ripple from waveform mismatch
- Feed 6-step current into a sinusoidal motor → even worse ripple plus acoustic noise
- The **drive strategy must match the motor's back-EMF shape** — that match determines everything else

---

## Control methods

### BLDC — 6-step (block) commutation

- Controller energizes **two phases** at a time; the third floats
- 6 commutation states per electrical cycle (every 60°)
- Each state uses the floating phase's BEMF (sensorless) or a Hall transition (sensored) to trigger the next commutation

**Commutation table (typical CW):**

| State | Phase U | Phase V | Phase W |
| ----- | ------- | ------- | ------- |
| 1     | +       | −       | off     |
| 2     | +       | off     | −       |
| 3     | off     | +       | −       |
| 4     | −       | +       | off     |
| 5     | −       | off     | +       |
| 6     | off     | −       | +       |

**Hall-based**
- 3 digital Halls spaced 120° electrical
- Direct lookup of the commutation state from the Hall code
- Robust, cheap, self-starting from any rotor angle

**Sensorless (BEMF zero-crossing)**
- Measure floating phase voltage, detect zero-crossing relative to DC bus midpoint
- Delay 30° electrical → commutate
- Works well above ~10% rated speed
- Startup requires open-loop ramp or align-and-go sequence

**When to use 6-step**
- Cost-dominated designs
- Loads tolerant of torque ripple (fans, pumps, propellers)
- Minimal low-speed operation required

**Limitations**
- Audible commutation buzz (especially 10–30% speed)
- No clean torque control during the commutation transition
- No field weakening
- Poor dynamic response vs FOC

### PMSM — sinusoidal control and FOC

**Sinusoidal commutation (scalar, no dq)**
- Three sine references aligned to rotor angle; phase-current magnitude scales with command
- Smoother than 6-step but no decoupling between flux and torque
- Transitional architecture — rarely a final product target

**FOC (Field-Oriented / Vector Control)**
- Measure 2 or 3 phase currents
- **Clarke transform**: abc → αβ (stationary 2-phase)
- **Park transform**: αβ → dq (rotor-aligned)
- Two independent PI loops:
  - **Id loop** — regulates flux-producing current (typically Id = 0 for SPM, Id < 0 for IPM/field weakening)
  - **Iq loop** — regulates torque-producing current (torque ∝ Iq)
- **Inverse Park / inverse Clarke** → phase voltage commands → **SVPWM** → inverter gates

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    A[Phase currents<br/>Ia, Ib, Ic] --> B[Clarke<br/>abc → αβ]
    B --> C[Park<br/>αβ → dq]
    C --> D[Id PI loop]
    C --> E[Iq PI loop]
    F[θ_rotor] --> C
    F --> G[Inverse Park]
    D --> G
    E --> G
    G --> H[Inverse Clarke]
    H --> I[SVPWM]
    I --> J[Inverter]
    J --> K[Motor]
    K -.-> A
    K -.-> F
</pre></div>

**When to use FOC**
- Servo-grade applications (precision motion, torque control)
- Anything requiring full torque at zero speed
- Wide speed range with field weakening
- Low audible noise, low torque ripple required

**Limitations**
- High compute requirement (current loop at 10–20 kHz)
- Demands accurate rotor position — encoder offset error directly reduces torque
- Parameter identification required (Rs, Ls or Ld/Lq, ψ_f)
- Complex commissioning

### Control method — operational routing

- **Default to 6-step only when the load is tolerant and BOM is the constraint.** Fans, pumps, propellers, centrifuges.
- **Step to sinusoidal (scalar)** only as a transitional architecture. In new designs, skip it — go straight to FOC.
- **Go to FOC** as soon as any of the following are true: precise torque control, sub-5% torque ripple, zero-speed torque, field weakening, acoustic noise constraint, closed-loop position.

---

## Mathematical foundation (practical)

The three equations below are enough to size a motor, debug a drive, or explain instability.

### Electrical equation (per phase)

$$V = R i + L \frac{di}{dt} + K_e \omega$$

- **V** — applied phase voltage
- **R** — winding resistance (copper loss: P = I²R)
- **L** — phase inductance (sets current slew rate and ripple)
- **i** — phase current (torque is proportional to this)
- **K_e ω** — back-EMF (rises linearly with speed)

**Engineering meaning:** the drive must overcome resistance, inductance, and back-EMF. At high speed, BEMF approaches DC bus → no voltage headroom left → torque collapses. This is what limits top speed.

### Torque equation

$$T = K_t I$$

- **T** — shaft torque
- **K_t** — torque constant (numerically equal to K_e in SI units)
- **I** — current (Iq in FOC language)

**Engineering meaning:** torque is a current problem, not a voltage problem. Torque limits = current limits = thermal limits. When the user demands "more torque," they are demanding "more current" → more copper loss → more heat.

### Electrical vs mechanical speed

$$\omega_e = p \cdot \omega_m$$

- **ω_e** — electrical angular frequency (what the commutation sees)
- **ω_m** — mechanical shaft speed
- **p** — number of pole pairs

**Engineering meaning:** a 4-pole-pair motor spinning at 3000 RPM mechanically has an electrical frequency of 200 Hz. Commutation timing, current-loop bandwidth, and PWM frequency must all be specified relative to ω_e, not ω_m. A common bug: designers think in RPM, then the current loop runs out of bandwidth at high pole counts.

### Mechanical equation (sizing / dynamics)

$$T - T_{load} = J \frac{d\omega}{dt} + B \omega$$

- **J** — rotor + load inertia
- **B** — viscous friction
- **T_load** — external load torque

**Engineering meaning:** motor torque is spent on accelerating inertia, overcoming friction, and driving the load. Inertia mismatch (load J >> motor J × gear²) is the classic cause of oscillation and gain-limited tuning.

---

## Drive architecture

<div class="mermaid-wrap"><pre class="mermaid">
flowchart TB
    subgraph PowerStage["Power Stage"]
        DC[DC Bus +] --> HS1[High-side U]
        DC --> HS2[High-side V]
        DC --> HS3[High-side W]
        HS1 --> U[Phase U]
        HS2 --> V[Phase V]
        HS3 --> W[Phase W]
        U --> LS1[Low-side U]
        V --> LS2[Low-side V]
        W --> LS3[Low-side W]
        LS1 --> GND[DC Bus −]
        LS2 --> GND
        LS3 --> GND
    end

    subgraph Control["Control"]
        MCU[MCU / DSP] --> GD[Gate Driver ICs]
        GD --> HS1
        GD --> HS2
        GD --> HS3
        GD --> LS1
        GD --> LS2
        GD --> LS3
        CS[Current Sense<br/>Shunts or Hall] --> ADC[ADC]
        ADC --> MCU
        FB[Encoder / Halls / Resolver] --> INT[Feedback Interface] --> MCU
    end

    U -.-> CS
    V -.-> CS
    W -.-> CS
</pre></div>

### Inverter (power stage)

| Device | Voltage class | Switching frequency | Typical use                      |
| ------ | ------------- | ------------------- | -------------------------------- |
| MOSFET | ≤ 200 V       | 20–100 kHz          | Battery, robotics, small servos  |
| SiC FET| 400–1200 V    | 50–200 kHz          | High-efficiency industrial, EV   |
| IGBT   | 600–1700 V    | 4–20 kHz            | Industrial AC mains drives       |
| GaN FET| ≤ 600 V       | 100 kHz–MHz         | Compact, high-power-density      |

**Why this device, not that:**
- Below ~200 V DC: use MOSFETs. IGBTs have too much saturation loss at that voltage.
- 400 V DC link (single-phase mains) and above: choose between IGBT (cheap, slower) and SiC (lower loss, higher switching frequency, ~3–5× part cost).
- GaN is the right call only when size/density is the constraint — otherwise the cost/benefit is weak.

### Gate driver

Role: interfaces the logic-level MCU signals to the gate capacitance of the power switches.

Functions:
- Level shifting for high-side drivers (bootstrap or isolated supply)
- Dead-time insertion to prevent shoot-through
- Gate charge / discharge (determines switching speed and losses)
- Desaturation / overcurrent protection
- Undervoltage lockout (UVLO)
- Miller clamp (prevents false turn-on from dv/dt)

Poor gate driving → shoot-through → instant MOSFET destruction. This is one of the top-three failure modes in DIY BLDC/PMSM drives.

### Controller (MCU / DSP / FPGA)

| Control | MCU class                             | Current loop rate |
| ------- | ------------------------------------- | ----------------- |
| BLDC 6-step | Cortex-M0/M3, ~50 MHz             | 1–10 kHz          |
| BLDC FOC    | Cortex-M4F, 100–200 MHz           | 10 kHz            |
| PMSM FOC    | Cortex-M7, C2000 DSP, 300 MHz     | 10–20 kHz         |
| High-end servo | FPGA + DSP                    | 20–40 kHz         |

### Current sensing

| Topology                  | Pros                                     | Cons                                     |
| ------------------------- | ---------------------------------------- | ---------------------------------------- |
| Single DC-link shunt      | Cheapest, one amplifier                  | Requires per-state reconstruction        |
| Two phase shunts          | Good accuracy, Ic = −(Ia + Ib)           | Two amplifiers, needs ground-referenced  |
| Three phase shunts        | Redundant, best accuracy, fault detect   | Three amplifiers                         |
| Hall-effect current sensor| Isolated, linear over wide range         | More expensive, more board area          |

**Routing:** single DC-link shunt for the tightest cost targets and low-dynamic BLDC; two-phase shunts for most FOC designs; three-phase shunts for safety-rated drives that need phase-fault detection; Hall-effect for high-voltage industrial drives where isolation is required.

### Feedback interface

| Feedback        | Signaling                         | Resolution          |
| --------------- | --------------------------------- | ------------------- |
| Hall sensors    | 3 open-drain or push-pull digital | 60° electrical      |
| Incremental enc.| A/B quadrature + Z                | 1024–10000 PPR      |
| Absolute enc.   | BiSS-C, EnDat, SSI, Nikon         | 17–26 bit           |
| Resolver        | Analog sine/cosine + excitation   | 12–16 bit effective |
| Sensorless      | Back-EMF observation or MRAS/SMO  | Estimated, not direct |

---

## Motor selection guide

### Selection logic

1. **Torque — continuous and peak**
   - Compute required T_continuous at worst-case operating point
   - Compute T_peak from acceleration: T_peak = J·α + T_load
   - Motor rated torque > T_continuous × safety factor (1.2–1.5)
   - Motor peak torque > T_peak

2. **Speed — rated and maximum**
   - Rated speed must match application duty point
   - Maximum speed bounded by mechanical and BEMF limits

3. **Inertia matching**
   - Target load/motor inertia ratio (reflected through gearbox²):
     - 1:1 for ultra-dynamic systems
     - 5:1 typical industrial
     - 10:1 upper limit before tuning difficulty rises sharply

4. **Voltage and current**
   - Motor K_e·ω_max < DC bus voltage × modulation index (≈ 0.9 for SVPWM)
   - Drive rated current ≥ motor peak current

5. **Thermal limits**
   - RMS current over duty cycle drives winding temperature
   - I²t integral must stay below thermal limit
   - Winding thermistor (PTC, PT100, or KTY) required for industrial motors

6. **Environment**
   - IP rating, ambient temperature, vibration, humidity
   - Food-grade, washdown, explosion-proof if applicable

### BLDC selection (hobby / embedded)

Typical parameter set:
- KV rating (RPM/V) — inversely related to K_e
- No-load current
- Max continuous / burst current
- Number of poles (high pole count → high torque density, lower max RPM)
- Weight and can size (e.g. 2208, 5010 — the first 2 digits are stator diameter mm, last 2 are stack height mm)

Examples:
- Drone: 2204–2806 motor, 1400–2600 KV, outrunner
- E-bike hub: 48 V class, high pole count, direct drive
- Power tool: inrunner, 12–24 V, high-speed, gear reduction

### PMSM selection (industrial / servo)

Typical parameter set:
- Rated torque / peak torque
- Rated speed / max speed
- Rated current / peak current
- Torque constant K_t (Nm/A)
- Voltage constant K_e (V/krpm)
- Winding resistance and inductance (Rs, Ld, Lq)
- Rotor inertia
- Cogging torque
- Insulation class (F or H typical)
- Feedback type

Examples by category:
- General servo: 200–750 W, incremental encoder, Class F insulation
- High-precision servo: absolute multi-turn encoder, BiSS-C, skewed rotor
- Direct-drive torque motor: hollow-bore, large diameter, high pole count, cogging-minimized
- Linear PMSM: ironless or iron-core; for semiconductor stages and lithography

### Motor family — application routing

| Application class                      | Preferred family                                            |
| -------------------------------------- | ----------------------------------------------------------- |
| Propulsion (drone, RC, small EV)       | BLDC outrunner, high KV, sensorless                          |
| Light EV hub (e-bike, e-scooter)       | BLDC or PMSM, high pole count, Hall-commutated               |
| Industrial fan / pump                  | BLDC (or induction if mains-direct)                          |
| General-purpose servo (200 W–3 kW)     | PMSM + absolute encoder + FOC                                |
| Precision robotics / cobot joint       | Frameless PMSM, 23+ bit absolute, BiSS-C/Hiperface DSL       |
| CNC spindle                            | IPM-PMSM (field-weakening range), or induction > 30 kW       |
| Semiconductor stage                    | Ironless linear PMSM or torque motor, laser interferometer   |
| Servo press                            | High-torque PMSM servo, absolute encoder + load cell         |

---

## Drive selection guide

### Hobby / low-cost

| Drive                  | Control      | Feedback supported        | Typical cost    | Notes                                |
| ---------------------- | ------------ | ------------------------- | --------------- | ------------------------------------ |
| Drone ESC (BLHeli_S)   | 6-step       | Sensorless                | $5–25           | Single-direction, propeller-tuned    |
| Drone ESC (BLHeli_32)  | 6-step + FOC | Sensorless                | $15–60          | Bidirectional, RPM feedback          |
| VESC (open source)     | FOC          | Hall, encoder, sensorless | $80–250         | E-bikes, skateboards, robotics       |
| ODrive                 | FOC          | Encoder (inc/abs)         | $150–450        | Robotics, precision motion           |
| SimpleFOC shield       | FOC          | Various                   | $40–120         | Educational, Arduino/STM32           |
| MoteusR4               | FOC          | Magnetic absolute         | $300–500        | Robotic joints, cobots               |

### Industrial / servo

| Vendor       | Product family           | Feedback             | Fieldbus                           | Safety          |
| ------------ | ------------------------ | -------------------- | ---------------------------------- | --------------- |
| Elmo         | Gold / Platinum          | Abs, BiSS, EnDat     | EtherCAT, CANopen                  | STO, SS1, SLS   |
| Siemens      | Sinamics S120 / V90      | DRIVE-CLiQ, SSI      | PROFINET, PROFIBUS, EtherCAT       | Full SIL 3      |
| Beckhoff     | AX5000, AX8000           | EnDat, BiSS, Hiperface| EtherCAT                          | TwinSAFE        |
| Kollmorgen   | AKD, AKD2G               | Hiperface DSL, SFD   | EtherCAT, PROFINET, EIP            | STO, SS1        |
| Yaskawa      | Sigma-7                  | Serial absolute      | MECHATROLINK, EtherCAT             | STO, SS1        |
| Rockwell     | Kinetix 5700             | Hiperface DSL        | EtherNet/IP (CIP Motion)           | STO via GuardLogix |
| Mitsubishi   | MR-J5                    | Serial absolute      | CC-Link IE TSN, SSCNET             | STO             |
| Parker       | Aries II, PSD / Compax3  | Resolver, EnDat      | EtherCAT, PROFINET                 | STO             |
| Schneider    | Lexium 32 / 62           | Hiperface, SinCos    | EtherCAT, PROFINET, Sercos III     | STO             |
| Bosch Rexroth| IndraDrive               | Hiperface, EnDat     | Sercos III, EtherCAT               | Full SIL 3      |
| Delta        | ASDA-A3                  | Serial absolute      | EtherCAT, CANopen                  | STO             |
| SEW-Eurodrive| Movidrive                | Hiperface, SinCos    | EtherCAT, PROFINET                 | STO, SS1        |

Selection drivers (industrial):
- **Fieldbus compatibility with PLC ecosystem** — usually the dominant constraint
- **Feedback compatibility with motor** — Hiperface vs BiSS vs EnDat vs DRIVE-CLiQ
- **Functional safety level required** — STO is the modern minimum; SS1/SLS/SBC add cost
- **Autotuning quality and commissioning UX**
- **Regional support, lead time, spares**

---

## Hobby vs industrial comparison

| Factor                  | Hobby BLDC                     | Industrial PMSM                       |
| ----------------------- | ------------------------------ | ------------------------------------- |
| Motor cost (1 kW)       | $30–150                        | $400–900                              |
| Drive cost              | $20–250                        | $600–1500                             |
| Commissioning effort    | Minutes (flash and go)         | Days (param ID, tuning, commissioning)|
| Tuning complexity       | Low (preset profiles)          | High (nested PI loops, notch filters, feedforward) |
| Feedback                | Sensorless or 3-Hall           | Absolute encoder or resolver          |
| Control mode            | 6-step, sometimes FOC          | FOC with field weakening, MTPA        |
| Safety certification    | None                           | STO / SS1 / SLS / SBC per IEC 61800-5-2|
| Fieldbus                | UART, CAN, PWM                 | EtherCAT, PROFINET, EtherNet/IP       |
| Thermal management      | Ambient / airflow              | Motor thermistor + drive thermal model|
| MTBF                    | Hundreds to low thousands hr   | 50,000+ hours                         |
| Diagnostics             | Minimal, sometimes serial log  | Full fault history, oscilloscope, drives-tools |
| Regeneration handling   | Often absent or crude          | Brake chopper + resistor, regen to mains|
| Ingress protection      | Open frame / IP20              | IP54–IP67 standard                    |
| Position accuracy       | 1% of rev (at best)            | < 1 arc-min with absolute encoder     |
| Typical lifecycle       | Prototype / consumer           | 10–20 years in service                |

---

## Cost vs performance tradeoff

### Why FOC costs more

- **Higher-spec MCU / DSP** — current loop at 10–20 kHz, Clarke/Park every cycle
- **Better ADC** — simultaneous-sampling, ≥12-bit, with precise shunt amplifier
- **Higher-resolution feedback** — encoder or resolver instead of 3 Halls
- **Parameter identification routine** — motor self-ID or manual entry of Rs, Ld, Lq, ψ_f
- **Larger firmware** — 60–200 KB vs 8–20 KB for 6-step
- **Commissioning time** — days vs hours, including encoder offset calibration

### When 6-step is enough

- Load tolerates torque ripple (fans, pumps, propellers, centrifuges)
- Operating speed is well above 10% rated (sensorless works clean there)
- Position accuracy is not required
- Acoustic noise is not a product constraint
- BOM cost is the dominant design driver

### Where diminishing returns start

| Investment                              | Marginal gain                                      |
| --------------------------------------- | -------------------------------------------------- |
| 6-step → sensorless FOC                 | Large: smoother, quieter, better efficiency        |
| Sensorless FOC → Hall FOC               | Modest: better startup under load                  |
| Hall FOC → encoder FOC                  | Large: zero-speed torque, precise position         |
| Incremental → absolute encoder          | Large: no homing, safer power cycles               |
| 17-bit → 23-bit absolute encoder        | Small unless sub-arc-min positioning is spec'd     |
| 10 kHz → 20 kHz current loop            | Small unless the motor is very low inductance      |
| Standard FOC → MTPA on IPM              | Modest efficiency gain (3–8%), worth it on EVs     |
| STO only → SS1/SLS/SBC                  | Only justified when hazard analysis requires       |

---

## Measurement and testing

### Why NOT to measure PWM output with RMS meters

A typical handheld RMS multimeter bandwidth is 1–10 kHz. Inverter PWM switches at 8–20 kHz. The result:
- Meter reads the **fundamental component** aliased with unknown spectral leakage
- Motor phase voltage is a high-frequency square-wave-modulated quantity — instantaneous values are either +Vbus or −Vbus, not the "average"
- Phase current reads better than voltage because the motor inductance filters it, but still not reliably on a consumer meter

**What to measure instead:**

### Correct measurement architecture

| Quantity                  | Correct instrument                                     |
| ------------------------- | ------------------------------------------------------ |
| DC bus voltage            | Any DC meter or oscilloscope channel                   |
| DC bus current            | DC current clamp or precision shunt + DAQ              |
| DC input power            | Vbus × Ibus (power analyzer or computed from DAQ)      |
| Phase voltage (waveform)  | Differential oscilloscope probe, isolated              |
| Phase voltage (RMS, true) | Power analyzer with ≥ 100 kHz bandwidth (Yokogawa WT series, HIOKI PW) |
| Phase current (waveform)  | Current probe (Hall-effect or Rogowski), ≥ 100 kHz BW  |
| Phase current (RMS)       | Power analyzer                                         |
| Shaft torque              | In-line torque transducer (HBM, Magtrol, Kistler)      |
| Shaft speed               | Optical tachometer or encoder + frequency counter      |
| Output mechanical power   | T × ω (from measured torque and speed)                 |
| Electrical efficiency     | (Shaft power) / (DC input power)                       |
| Motor temperature         | PT100 on winding, IR camera on housing                 |

### Oscilloscope role

- Observe inverter switching waveforms (dead time, dv/dt)
- Diagnose shoot-through, ringing, ground bounce
- Observe phase current ripple vs PWM frequency
- Capture commutation transients on BLDC 6-step
- Verify encoder A/B/Z alignment and direction

### Data logger / DAQ role

- Long-duration efficiency maps (sweep torque and speed)
- Thermal profiles (winding vs ambient over duty cycle)
- Load-disturbance recovery response
- Control loop tuning: log setpoint, PV, and error at current-loop rate

### Power analyzer role

- Gold standard for efficiency measurement
- Simultaneously measures Vbus, Ibus, phase voltages, phase currents, with synchronous sampling
- Computes true RMS, true power, power factor, THD

---

## Practical implementation scenarios

Scan the 8 scenarios below, jump to the closest match for the detailed stack.

<div class="scenario-grid">
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 1</span>
    <span class="scenario-card__title"><a href="#scenario-1--drone-motor">Drone motor</a></span>
    <div class="scenario-card__start"><strong>Motor:</strong> BLDC outrunner, high KV</div>
    <div class="scenario-card__start"><strong>Drive:</strong> ESC, 6-step sensorless</div>
    <div class="scenario-card__start"><strong>Control:</strong> DShot digital throttle</div>
    <div class="scenario-card__start"><strong>Why it wins:</strong> lightest, cheapest, no feedback needed</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 2</span>
    <span class="scenario-card__title"><a href="#scenario-2--conveyor-system">Conveyor system</a></span>
    <div class="scenario-card__start"><strong>Motor:</strong> Induction or IE4 PMSM</div>
    <div class="scenario-card__start"><strong>Drive:</strong> General-purpose VFD</div>
    <div class="scenario-card__start"><strong>Control:</strong> V/Hz or sensorless vector</div>
    <div class="scenario-card__start"><strong>Why it wins:</strong> continuous duty, serviceable, energy bills</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 3</span>
    <span class="scenario-card__title"><a href="#scenario-3--precision-robotics-cobot-joint">Precision robotics (cobot joint)</a></span>
    <div class="scenario-card__start"><strong>Motor:</strong> Frameless PMSM, low-cogging</div>
    <div class="scenario-card__start"><strong>Drive:</strong> EtherCAT servo, STO minimum</div>
    <div class="scenario-card__start"><strong>Control:</strong> Nested FOC + feedforward</div>
    <div class="scenario-card__start"><strong>Why it wins:</strong> transparent torque, absolute power-up</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 4</span>
    <span class="scenario-card__title"><a href="#scenario-4--low-cost-industrial-automation">Low-cost industrial automation</a></span>
    <div class="scenario-card__start"><strong>Motor:</strong> BLDC with integrated Halls</div>
    <div class="scenario-card__start"><strong>Drive:</strong> Hall-based 6-step / basic FOC</div>
    <div class="scenario-card__start"><strong>Control:</strong> 0–10 V analog or Modbus RTU</div>
    <div class="scenario-card__start"><strong>Why it wins:</strong> robust in dust/vibration, tight budget</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 5</span>
    <span class="scenario-card__title"><a href="#scenario-5--semiconductor-equipment-wafer-handler-stage">Semiconductor stage</a></span>
    <div class="scenario-card__start"><strong>Motor:</strong> Ironless linear or rotary PMSM</div>
    <div class="scenario-card__start"><strong>Drive:</strong> High-end servo (Elmo / ACS / Aerotech)</div>
    <div class="scenario-card__start"><strong>Control:</strong> Jerk-limited FOC + ILC</div>
    <div class="scenario-card__start"><strong>Why it wins:</strong> sub-micron accuracy, cogging-free</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 6</span>
    <span class="scenario-card__title"><a href="#scenario-6--cnc-spindle">CNC spindle</a></span>
    <div class="scenario-card__start"><strong>Motor:</strong> IPM-PMSM or high-speed induction</div>
    <div class="scenario-card__start"><strong>Drive:</strong> Servo w/ field-weakening + HSC</div>
    <div class="scenario-card__start"><strong>Control:</strong> FOC MTPA + field weakening</div>
    <div class="scenario-card__start"><strong>Why it wins:</strong> 3–5× constant-power range, rigid tapping</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 7</span>
    <span class="scenario-card__title"><a href="#scenario-7--e-bike--light-ev-traction">E-bike / light EV</a></span>
    <div class="scenario-card__start"><strong>Motor:</strong> PMSM (IPM perf, SPM low-cost)</div>
    <div class="scenario-card__start"><strong>Drive:</strong> VESC-class FOC with regen</div>
    <div class="scenario-card__start"><strong>Control:</strong> FOC + MTPA + field weakening</div>
    <div class="scenario-card__start"><strong>Why it wins:</strong> range per Wh, hill-start holding torque</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario 8</span>
    <span class="scenario-card__title"><a href="#scenario-8--industrial-servo-press">Industrial servo press</a></span>
    <div class="scenario-card__start"><strong>Motor:</strong> PMSM servo, 5–30 kW</div>
    <div class="scenario-card__start"><strong>Drive:</strong> Servo w/ STO/SS1, gain scheduling</div>
    <div class="scenario-card__start"><strong>Control:</strong> Gain-scheduled PI + force loop</div>
    <div class="scenario-card__start"><strong>Why it wins:</strong> handles orders-of-magnitude load swing safely</div>
  </div>
</div>

### Scenario 1 — Drone motor

- **Motor:** BLDC, outrunner (e.g. 2207, 1700 KV), 14 poles
- **Drive:** ESC, 6-step sensorless (BLHeli_32 or AM32)
- **Feedback:** None (sensorless BEMF)
- **Power:** 4S–6S LiPo, 14.8–22.2 V nominal
- **Control:** Digital throttle from flight controller — DShot (150/300/600/1200 kbit serial) is the common signaling protocol, not PWM
- **Why this choice:**
  - Weight-critical — no encoder or Halls
  - Load (propeller) is dynamic but tolerant of torque ripple
  - Startup at zero speed is not required (props spin up unloaded)
  - Cost per axis < $20

### Scenario 2 — Conveyor system

- **Motor:** Induction (classic) **or** PMSM for IE4/IE5 efficiency
- **Drive:** VFD (general-purpose AC drive)
- **Feedback:** Open-loop V/Hz for induction; sensorless vector or encoder for PMSM
- **Control:** Speed reference from PLC over PROFINET or hardwired 4–20 mA
- **Why this choice:**
  - Continuous duty, moderate speed accuracy
  - Reliability and serviceability dominate
  - Induction has lower BOM; PMSM wins on energy bills over a 10-year horizon
  - A servo-grade PMSM is overkill — no position control needed

### Scenario 3 — Precision robotics (cobot joint)

- **Motor:** PMSM, frameless, high-pole-count, low-cogging
- **Drive:** Servo drive with EtherCAT CoE, STO minimum
- **Feedback:** Absolute multi-turn encoder, 23+ bit, BiSS-C or Hiperface DSL
- **Control:** Nested current → velocity → position with feedforward; optional torque-sensor loop
- **Why this choice:**
  - Transparent torque control for human interaction
  - Absolute position at power-up — no homing
  - Cogging would be felt directly through the (sometimes harmonic) gearbox
  - Safety functions mandated by ISO 10218 / ISO/TS 15066

### Scenario 4 — Low-cost industrial automation

- **Motor:** BLDC with integrated Halls
- **Drive:** Simple controller with Hall-based 6-step or basic FOC
- **Feedback:** 3 Hall sensors
- **Control:** Speed command via 0–10 V analog or Modbus RTU
- **Why this choice:**
  - Application tolerates moderate precision
  - Budget does not justify a servo drive
  - Halls are robust in dusty / vibrating environments
  - Retrofits where a DC-brushed motor was previously used

### Scenario 5 — Semiconductor equipment (wafer handler, stage)

- **Motor:** Linear PMSM (ironless) or rotary high-precision PMSM
- **Drive:** High-end servo (Elmo Gold, ACS, Aerotech) with EtherCAT or SERCOS
- **Feedback:** Linear encoder (1 nm resolution) or laser interferometer
- **Control:** Jerk-limited trajectories, cascaded loops, iterative learning control
- **Why this choice:**
  - Sub-micron positioning accuracy required
  - Ironless motor eliminates cogging (fundamental for lithography-class stages)
  - Must integrate with fab MES over SECS/GEM (via PLC gateway)
  - Cleanroom-compatible (no brushes, sealed bearings, outgassing-rated materials)

### Scenario 6 — CNC spindle

- **Motor:** PMSM IPM for constant-power range, or high-speed induction for spindles > 30 kW
- **Drive:** Servo drive with field-weakening support and HSC (high-speed machining) firmware
- **Feedback:** Absolute encoder for C-axis rigid tapping; pulse encoder for pure speed
- **Control:** FOC with MTPA below base speed, field weakening above
- **Why this choice:**
  - Needs wide constant-power range (often 3–5× base)
  - Rigid tapping requires C-axis position control
  - Surface finish demands low torque ripple

### Scenario 7 — E-bike / light EV traction

- **Motor:** PMSM (IPM for performance models, SPM for low-cost)
- **Drive:** Custom MCU-based or VESC-class FOC
- **Feedback:** Halls + sensorless observer; some premium systems use absolute encoder
- **Control:** FOC with MTPA and field weakening, regen braking
- **Why this choice:**
  - Range per Wh dominates — MTPA and field weakening both contribute
  - Zero-speed holding torque for hill starts
  - Regen braking recovers energy

### Scenario 8 — Industrial servo press

- **Motor:** PMSM servo, 5–30 kW
- **Drive:** Servo drive with gain scheduling and STO/SS1
- **Feedback:** Absolute encoder + load cell + linear scale on press ram
- **Control:** Gain-scheduled PI loops (different gains for travel vs press modes), cascaded with force loop
- **Why this choice:**
  - Deterministic torque control through press engagement
  - Mechanical load changes by orders of magnitude between free travel and press phases
  - Safety-rated stop and guard monitoring mandated

For three fully worked engineering archetypes (fan/pump, precision axis, AGV) with per-scenario tuning and measurement strategy, see the Motor Selection Scenarios module.

---

## Wiring and integration

### Cable-group legend

All wiring diagrams in the BLDC and PMSM modules use the same cable-class convention — shown once here, applied everywhere.

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    P[Power]:::power
    PH[Phase U/V/W]:::phase
    F[Feedback]:::feedback
    S[Safety]:::safety
    B[Fieldbus]:::bus
    SH[Shield / PE]:::shield

    classDef power stroke:#c0392b,stroke-width:2px
    classDef phase stroke:#2c3e50,stroke-width:2px
    classDef feedback stroke:#2980b9,stroke-width:2px
    classDef safety stroke:#e67e22,stroke-width:2px
    classDef bus stroke:#27ae60,stroke-width:2px
    classDef shield stroke:#7f8c8d,stroke-width:1px,stroke-dasharray:3 3
</pre></div>

| Cable group | Typical signals | IEC 60757 conductor color | Termination practice |
|-------------|-----------------|---------------------------|----------------------|
| Power       | DC+ / DC- / battery / L1/L2/L3 | Red (+), Black (−), Brown/Black/Grey for AC | Short low-impedance bond to chassis PE; separate conduit from signal cables |
| Phase       | U, V, W         | Brown (U), Black (V), Grey (W) per IEC 60204-1 | Shielded VFD/servo cable; 360° shield termination at both ends for servo class |
| Feedback    | Hall / encoder / resolver / temp | Twisted-pair differential; shield is separate | Shielded twisted pair; shield terminated at drive end (check drive manual); min 300 mm from power cables |
| Safety      | STO-1, STO-2, SS1, interlocks | Typically violet or orange per panel convention | Dual-channel, cross-monitored; separate terminal blocks from control wiring |
| Fieldbus    | EtherCAT / PROFINET / CAN / EtherNet-IP / PWM-throttle | Per bus standard (EtherCAT: green jacket is common) | Impedance-matched, terminated per bus spec; keep away from motor cables |
| Shield / PE | Drain wire, cable shield, green/yellow PE | Green/yellow (PE); bare or foil for shield | 360° EMC gland preferred; avoid pigtails above ~10 MHz |

Dashed lines in the diagrams indicate shield or optional connections. Solid lines are the primary conductor of the group.

### Power wiring

- **Conductor sizing:** per NEC 430 / IEC 60204-1. For a single continuous-duty motor, NEC 430.22 gives 125 % of motor FLC as the branch-circuit minimum. Multi-motor, intermittent-duty, and drive-fed feeders use different rules (NEC 430.24 / 430.33, IEC 60204-1 §12) — check the applicable clause before sizing.
- **Overcurrent protection:** fuse or breaker sized for inrush, not steady-state
- **Precharge:** required for drives with large DC-link capacitance to limit inrush
- **Line-side contactor:** use for lockout/tagout isolation and for SS1-Cat-0/1 stop where no certified STO is available. On drives with certified STO per IEC 61800-5-2, use STO as the primary stop path — cycling the main contactor on every E-stop stresses the precharge circuit and shortens contactor life.
- **Bond the drive chassis to PE** with a short low-impedance conductor

### Phase wiring (drive → motor)

- Use **shielded VFD / servo cable** (e.g., Lapp ÖLFLEX SERVO, Igus CF280)
- Shield terminated **360° at both ends** — drive end via EMC gland, motor end via connector shell or EMC gland
- **Keep U-V-W cables twisted or parallel** — never split across different conduits
- Respect maximum cable length published by the drive (typically 10–50 m without reactor, up to 100+ m with du/dt filter)
- For long runs, add **output reactor or sine-wave filter** to limit reflected wave voltage at the motor terminals (can otherwise double the rated insulation stress)

### Feedback wiring

- **Shielded twisted-pair** cable, dedicated per signal pair (A/A-, B/B-, Z/Z-, data/data-, clock/clock-)
- **Shield termination varies.** Single-end at the drive is common for classical incremental/analog encoders to avoid ground-loop noise. Digital one-cable interfaces (Hiperface DSL, DRIVE-CLiQ, OCT) and EMC-rated installations typically require 360° termination at both ends. Always follow the drive/motor manual.
- **Separate conduit or tray from power cables** — minimum 300 mm separation, perpendicular crossings only
- Use connector with positive latching (DB-15, M23, M17)
- Twisted-pair impedance-matched to the signaling standard (120 Ω for BiSS, EnDat, RS-485)

### Grounding and bonding

- **Star-point grounding** at the drive enclosure
- **Separate PE conductors** for drive, motor, enclosure, and any control transformer
- **Bonding jumpers** across door hinges, panel seams, subpanel mounts
- **Do not rely on DIN rail contact** for safety bonding — add dedicated bonding strap
- **HF ground vs safety ground** — some drives require both, per manufacturer documentation

### Shielding practice

- 360° shield termination whenever possible (pigtails are lossy above ~10 MHz)
- Keep shield continuous through connectors — do not land shield on a terminal block
- Use **EMC glands** at panel entries
- Inside the panel, route sensitive signals along the panel wall, power cables in the center of the tray

### Wiring archetypes — which pattern applies

#### Archetype A — Battery BLDC (drone / e-bike / AGV / power tool)

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    BAT([Battery pack]):::power
    FUSE[Fuse / main disconnect]:::power
    PRE[Precharge + contactor]:::power
    ESC[BLDC inverter / ESC]
    MOT[BLDC motor]:::phase
    HALL>Hall sensor]:::feedback
    HOST[Throttle / PWM / CAN]:::bus

    BAT -->|DC+ / DC-| FUSE
    FUSE --> PRE
    PRE -->|DC bus| ESC
    ESC -->|U / V / W| MOT
    HALL -.->|5V / GND / HA / HB / HC| ESC
    HOST -.-> ESC

    classDef power stroke:#c0392b,stroke-width:2px
    classDef phase stroke:#2c3e50,stroke-width:2px
    classDef feedback stroke:#2980b9,stroke-width:2px
    classDef bus stroke:#27ae60,stroke-width:2px
</pre></div>

Fits drones, e-bikes, AGVs, power tools, cooling fans. Typical voltage 12–96 VDC battery. Low cost; minimal wiring; no functional safety wiring required at the drive terminals. Chassis bonding still required on the vehicle side.

#### Archetype B — Integrated PMSM servo (cobot joint / wafer stage / single axis)

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    AC([1φ or 3φ AC]):::power
    FIL[EMI filter]:::power
    DRV[Integrated PMSM servo drive]
    MOT[PMSM motor]:::phase
    ENC>Integrated encoder]:::feedback
    TEMP>Motor temp]:::feedback
    STO[Safety I/O]:::safety
    PLC[Motion controller]:::bus
    PE((Machine PE)):::shield

    AC -->|L / N / PE or 3φ| FIL
    FIL -->|DC bus| DRV
    DRV -->|U / V / W + PE| MOT
    MOT -.->|hybrid cable shield| PE
    ENC -.->|OCT / DRIVE-CLiQ / Hiperface DSL| DRV
    TEMP -.->|PTC / Pt1000| DRV
    STO -->|STO-1 / STO-2| DRV
    PLC -->|EtherCAT / PROFINET| DRV
    DRV -.-> PE

    classDef power stroke:#c0392b,stroke-width:2px
    classDef phase stroke:#2c3e50,stroke-width:2px
    classDef feedback stroke:#2980b9,stroke-width:2px
    classDef safety stroke:#e67e22,stroke-width:2px
    classDef bus stroke:#27ae60,stroke-width:2px
    classDef shield stroke:#7f8c8d,stroke-width:1px,stroke-dasharray:3 3
</pre></div>

Fits cobot joints, wafer-stage axes, single-axis industrial servo. Typical voltage 230–480 VAC or 24–72 VDC on compact variants. One-cable hybrid power + feedback is typical (Beckhoff OCT, Siemens DRIVE-CLiQ, SEW Hiperface DSL). STO + fieldbus standard. Cost-per-axis moderate.

#### Archetype C — Shared DC-bus multi-axis PMSM (CNC / press / printing press)

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    AC([3φ 400–480 VAC]):::power
    REC[Rectifier + regen unit]:::power
    BRK[Brake chopper + resistor]:::power
    DC[[DC bus]]:::power
    INV1[Servo inverter axis 1]
    INV2[Servo inverter axis 2]
    INV3[Servo inverter axis N]
    MOT1[PMSM axis 1]:::phase
    MOT2[PMSM axis 2]:::phase
    MOT3[PMSM axis N]:::phase
    ENC1>Encoder 1]:::feedback
    ENC2>Encoder 2]:::feedback
    ENC3>Encoder N]:::feedback
    STO[Safety controller]:::safety
    PLC[CNC / motion controller]:::bus
    PE((Cabinet PE)):::shield

    AC -->|L1 / L2 / L3 / PE| REC
    REC --> DC
    DC -.-> BRK
    DC --> INV1
    DC --> INV2
    DC --> INV3
    INV1 -->|U / V / W + PE| MOT1
    INV2 -->|U / V / W + PE| MOT2
    INV3 -->|U / V / W + PE| MOT3
    ENC1 -.-> INV1
    ENC2 -.-> INV2
    ENC3 -.-> INV3
    STO -->|STO loop| INV1
    STO -->|STO loop| INV2
    STO -->|STO loop| INV3
    PLC -->|EtherCAT trunk| INV1
    PLC --> INV2
    PLC --> INV3
    INV1 -.-> PE
    INV2 -.-> PE
    INV3 -.-> PE
    MOT1 -.-> PE

    classDef power stroke:#c0392b,stroke-width:2px
    classDef phase stroke:#2c3e50,stroke-width:2px
    classDef feedback stroke:#2980b9,stroke-width:2px
    classDef safety stroke:#e67e22,stroke-width:2px
    classDef bus stroke:#27ae60,stroke-width:2px
    classDef shield stroke:#7f8c8d,stroke-width:1px,stroke-dasharray:3 3
</pre></div>

Fits CNC machining centers, servo presses, printing presses, multi-axis pick-and-place. Typical voltage 400–800 VDC bus from 3φ 400/480 VAC mains. Shared DC bus enables regen recovery between axes. Highest integration and cost; daisy-chained fieldbus + shared STO loop + bonded PE star point at the cabinet.

### Common integration mistakes

- Running encoder cable through the same bundle as motor phase cable
- Using unshielded motor cable on drives with fast switching (SiC, GaN)
- Daisy-chaining PE through DIN rails instead of dedicated bonding bus
- Shield pigtailed 100+ mm before termination
- Missing line reactor on long-cable runs
- Mixing 24 V DC I/O return and drive logic return
- Skipping common-mode choke on drive input in weak grid environments

---

## Common failure modes

### Commutation errors

- **Wrong phase order** — motor runs reversed, or oscillates at standstill, or draws surge current
- **Hall misalignment** — commutation fires at wrong electrical angle → reduced torque, high current, overheating
- **Encoder offset not calibrated** — FOC drive cannot establish correct dq frame; max torque unreachable, motor runs hot at moderate load
- **Sensorless BEMF fails at low speed** — stalls under load near zero RPM

### Current spikes

- **Shoot-through** from inadequate dead time → instantaneous MOSFET/IGBT destruction
- **Aggressive gain settings** cause current-loop saturation and oscillation
- **dv/dt-induced false turn-on** at the low-side gate → partial shoot-through
- **DC-link overvoltage during regen** — with an undersized or missing brake chopper/resistor, returning kinetic energy pushes the DC bus above OV threshold and the drive trips on the deceleration event

### Noise and EMI

- **Unshielded motor cable** → radiated emissions fail EN 55011 / FCC Part 15
- **Improper shield termination** → common-mode current on PE → ground loop noise on sensors
- **High switching frequency with long cables** → reflected wave at motor terminals doubles voltage stress → winding insulation breakdown
- **Missing common-mode choke** → drive disturbs nearby analog sensors, 4–20 mA loops

### Instability under load

- **Inertia mismatch** → oscillation at current/speed loop crossover
- **Mechanical resonance** (belt, coupling, gearbox) → excited at specific speeds → gain-limited tuning
- **Backlash in gearbox** → limit-cycle oscillation in position loop
- **Cable capacitance too high** → current loop sees the cable as an extra LC pole

### Overheating

- **Continuous current above rated** — exceeds I²t thermal limit
- **Ambient temperature above spec** — derate per motor thermal curve
- **Poor mounting surface** — motor flange not bolted to heatsink surface
- **Wrong FOC Id command (IPM)** — negative Id only useful above base speed; applying it below base wastes power as heat
- **Stuck brake** — motor fights the brake continuously

### Drive-specific

- DC-link capacitor aging → ripple rises → OC trips → eventual explosion
- Gate driver failure → shoot-through
- Fan failure → thermal derating → nuisance trips
- Firmware bug in field-weakening → runaway at high speed
- Encoder battery flat (absolute multi-turn) → position lost on power cycle

---

## Implementation checklist

<div class="card-grid">
  <div class="card" markdown="1">
<span class="card__label">1 · Motor</span>

- [ ] Torque sized for continuous and peak operation with safety margin (1.2–1.5×)
- [ ] Speed rating above maximum operating point
- [ ] Inertia ratio within tuning-friendly range (target ≤ 5:1 reflected)
- [ ] Voltage constant matched to DC bus (K_e·ω_max < 0.9·Vbus)
- [ ] Insulation class adequate for ambient + duty (F minimum for industrial)
- [ ] IP rating matches environment (IP54 typical industrial, IP67 for washdown)
- [ ] Thermistor / PT100 present and wired
- [ ] Brake (if required) matched to drive's brake output voltage
- [ ] Feedback device matches drive interface (Hall, incremental, absolute, resolver)
  </div>
  <div class="card" markdown="1">
<span class="card__label">2 · Drive</span>

- [ ] Rated current ≥ motor peak current
- [ ] DC bus voltage range matches supply
- [ ] Fieldbus matches PLC (EtherCAT, PROFINET, EtherNet/IP, CANopen)
- [ ] Feedback protocol supported (BiSS-C, EnDat, Hiperface DSL, etc.)
- [ ] Functional safety functions available (STO minimum)
- [ ] Firmware up to date
- [ ] Brake chopper resistor sized for regen energy
- [ ] Heatsink / cooling adequate for duty cycle
  </div>
  <div class="card" markdown="1">
<span class="card__label">3 · Wiring</span>

- [ ] Power cable sized per NEC 430 / IEC 60204-1
- [ ] Motor cable shielded, terminated 360° at both ends
- [ ] Feedback shield terminated per drive manual (single- or double-end)
- [ ] Power and signal wiring physically separated (minimum 300 mm)
- [ ] PE bonded star-point at drive enclosure
- [ ] EMC glands used at panel entries
- [ ] Output reactor / du/dt filter installed for long motor cable runs
- [ ] Connectors latched, strain-relieved, rated for ambient
  </div>
  <div class="card" markdown="1">
<span class="card__label">4 · Control</span>

- [ ] Parameter identification complete (Rs, Ld, Lq, ψ_f for PMSM)
- [ ] Encoder offset calibrated (for FOC)
- [ ] Current loop bandwidth set (typical 1/10 of PWM frequency)
- [ ] Velocity loop bandwidth ≤ 1/4 of current loop
- [ ] Position loop bandwidth ≤ 1/4 of velocity loop
- [ ] Current, velocity, position limits programmed
- [ ] Feedforward terms tuned (velocity, acceleration, friction)
- [ ] Safety parameters configured (STO reaction, SS1 ramp, SLS threshold)
- [ ] Diagnostic logging enabled
  </div>
  <div class="card" markdown="1">
<span class="card__label">5 · Testing</span>

- [ ] No-load spin in both directions, with expected current
- [ ] Current balance across three phases within tolerance
- [ ] Rated load step response — no oscillation, settling within spec
- [ ] Max speed reached without OV or OC trips
- [ ] Regen / braking test — DC bus stays below OV threshold
- [ ] Thermal soak at rated duty for ≥ 30 min — winding and housing temps within spec
- [ ] EMC pre-compliance scan (radiated + conducted) for product designs
- [ ] STO / E-stop response verified (motor torque removed within rated reaction time)
- [ ] Encoder position stable across power cycles (absolute)
- [ ] Fault history reviewed — no unexpected warnings or trips during acceptance test
  </div>
</div>

---

## Appendix — Known industry brands

Reference-only vendor map. Pick based on your PLC/CNC ecosystem, required feedback, and required safety functions — not brand.

| Category | Typical vendors | Fit |
|----------|-----------------|-----|
| Industrial servo (motor + drive) | Siemens (Sinamics / Simotics), Rockwell / Allen-Bradley (Kinetix / MP), Bosch Rexroth (IndraDrive / MS2N), Yaskawa (Sigma-7 / Sigma-X), Mitsubishi (MR-J5), Kollmorgen (AKD2G / AKM), Parker (PSD / Compax), Beckhoff (AX8000 + AM8000), SEW-Eurodrive (Movidrive + CMP), Schneider (Lexium 62 + BMH), Delta (ASDA-A3 + ECMA), Fanuc (αi / βi, CNC-coupled), Omron (1S / G5) | Industrial machines with PLC/CNC, STO/SS1/SLS, fieldbus |
| Compact / integrated servo | Maxon (EC + EPOS / ESCON), Faulhaber, Nanotec, Teknic ClearPath, Oriental Motor (AZ), Applied Motion, Moog | Small axes, lab/medical, integrated motor+drive packages |
| Embedded BLDC / motor-control ICs | TI (DRV832x/835x, InstaSPIN), ST (STSPIN, STM32 MC), onsemi (NCV gate drivers), Infineon (iMOTION, XMC), Toshiba (TB67), NXP (S32K + MCSPTE), MPS (MP65xx), Allegro (A4910, A89301) | Custom boards, OEM products, cost-driven BLDC |
| Hobby / maker drives | BLHeli_S / BLHeli_32 ESCs, VESC (open source), ODrive, Moteus, SimpleFOC, Trinamic / ADI, FLIPSKY | Prototypes, drones, e-skate / e-bike, research |
| Linear / specialty motion | Aerotech, ACS Motion Control, Etel, Tecnotion, Parker Trilogy, Yaskawa Sigma linear | Semiconductor stages, metrology, lithography, direct-drive |

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/motors/bldc-vs-pmsm/' | relative_url }}">&larr; BLDC vs PMSM Comparison</a>
  <a href="{{ '/fundamentals/motors/' | relative_url }}">↑ Motors, Drives, and Motion</a>
  <a href="{{ '/fundamentals/motors/motor-selection-scenarios/' | relative_url }}">Motor Selection Scenarios &rarr;</a>
</div>
