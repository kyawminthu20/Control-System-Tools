---
layout: training-module
title: "Motor Selection Scenarios — Fan/Pump, Precision Axis, AGV"
description: "Three engineering-grade motor selection archetypes with per-scenario drive, wiring, control, tuning, measurement, and failure-mode detail. Covers a clearly BLDC-favored case, a clearly PMSM-favored case, and an ambiguous tradeoff case."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "Motors, Drives, and Motion"
    url: "/fundamentals/motors/"
repo_path: "control-standards/rag/training_modules/electrical_machines/bldc_pmsm_scenarios.md"
review:
  standard: "Motor and drive engineering practice — vendor documentation governs application"
  edition: "n/a — practice module"
  status: "Review pending"
  coverage: "Training module: Motor Selection Scenarios — Fan/Pump, Precision Axis, AGV — educational treatment; sizing and application decisions follow vendor data and the governing standards."
  last_reviewed: "July 2026"
---

## Purpose

This module presents three engineering-grade motor-selection archetypes with full per-scenario detail. The BLDC vs PMSM Comparison module answers "which family, at a glance" across 10 short scenarios; this module answers "now engineer it" across three canonical archetypes. Each scenario walks through system context, constraints, engineering analysis, recommended solution, architecture diagram, drive selection, wiring, tuning, measurement strategy, failure modes, and cost — so a reader can move from family-choice to buildable architecture. The three archetypes are: a clearly BLDC-favored case (fan/pump), a clearly PMSM-favored case (precision axis / wafer stage), and an ambiguous case (AGV traction) where the decision flips based on cost vs performance priorities.

---

## Framing

The three scenarios are deliberately *archetypes*, not a long list of short examples. A scenario-per-product-class list (drill, blender, dishwasher, elevator, etc.) is useful for a quick "which family" pass, but it does not teach system engineering. This module instead picks three canonical cases that span the decision surface — one clearly BLDC, one clearly PMSM, one ambiguous — and walks each one end-to-end: system definition, mechanical characteristics, control strategy, drive selection, wiring, tuning, measurement strategy, failure modes, and cost structure.

Each scenario follows the same four-step engineering template: **constraints → analysis → decision → justification**. The unified per-scenario flow is conceptual framing first (what the system looks like and what it demands), then the engineering deep-dive (how you actually build and commission it). The goal is to move a reader from family selection to buildable architecture in one pass.

---

## Scenario 1 — BLDC-favored: high-speed cooling fan / pump system

### System context and requirements

**Function:** continuous airflow or fluid circulation.
**Control:** speed only (no position requirement).
**Load:** low inertia, mostly constant torque.
**Environment:** cost-sensitive, high volume.
**Voltage:** 24–48 VDC.
**Feedback:** optional, prefer none.

| Requirement        | Priority     |
| ------------------ | ------------ |
| Low cost           | High         |
| Reliability        | High         |
| Efficiency         | Medium       |
| Smooth torque      | Low          |
| Precision control  | Not required |
| Startup under load | Moderate     |

### Engineering analysis and recommended solution

**Control needs.** No position control. No tight speed regulation needed. Acceptable to have some torque ripple.

**Mechanical behavior.** Load is forgiving. No resonance sensitivity. No low-speed holding requirement.

**Electrical considerations.** Sensorless startup acceptable. Simple commutation sufficient.

**Recommended solution: BLDC Motor + 6-step commutation (sensorless or Hall).**

### Architecture

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    BAT([24–48 V DC]):::power
    FUSE[Fuse]:::power
    ESC[BLDC ESC]
    MOT[BLDC motor]:::phase
    FAN[Fan / pump]
    HALL>Hall sensor 5-wire]:::feedback
    HOST[PWM / analog / CAN]:::bus

    BAT -->|DC+ / DC-| FUSE
    FUSE -->|DC bus| ESC
    ESC -->|U / V / W| MOT
    MOT --> FAN
    HALL -.->|5V / GND / HA / HB / HC| ESC
    HOST -.->|optional| ESC

    classDef power stroke:#c0392b,stroke-width:2px
    classDef phase stroke:#2c3e50,stroke-width:2px
    classDef feedback stroke:#2980b9,stroke-width:2px
    classDef bus stroke:#27ae60,stroke-width:2px
</pre></div>

*Cable-class color legend: see the [Cable-group legend]({{ '/fundamentals/motors/bldc-pmsm-implementation/#cable-group-legend' | relative_url }}) in the Implementation Guide. Solid lines are primary conductors; dashed lines are shields, feedback, or optional connections.*

### Why BLDC wins and why PMSM is not justified

**Advantages of BLDC here:**

- Lowest cost (motor + driver).
- Minimal wiring (no encoder).
- Simple control (6-step).
- High efficiency for this duty.
- Proven in millions of systems.

**Why PMSM is not justified:**

- FOC adds cost (MCU, current sensing, tuning effort).
- Encoder unnecessary.
- Smoothness not required.
- No benefit in system-level performance.

### System definition

| Parameter   | Typical range         |
| ----------- | --------------------- |
| Voltage     | 12–48 VDC             |
| Power       | 10 W – 1 kW           |
| Speed       | 1,000 – 20,000 RPM    |
| Torque      | Low, mostly constant  |
| Duty cycle  | Continuous            |
| Environment | Consumer / industrial |

### Mechanical characteristics

- Low inertia load.
- Aerodynamic or fluid load → torque ∝ speed².
- No position requirement.
- No reversal (or rare).

The load is **self-stabilizing**: speed excursions produce restoring aerodynamic/hydraulic load changes that damp the system. Load inertia smooths the 6-step torque ripple. High-speed operation further reduces ripple impact. The combination is why 6-step commutation — which on a precision axis would be unusable — is perfectly adequate here.

### Control strategy — sensorless 6-step with optional Hall

**Primary: sensorless 6-step.**

- Back-EMF zero-crossing detection.
- 120° conduction.
- Fixed commutation table.

**Optional: Hall-based.** Used for:

- Startup reliability (sensorless can struggle at zero speed).
- Low-speed operation (below the BEMF detection floor).

This matches the standard practical split between trapezoidal BLDC control and sinusoidal/FOC PMSM control: TI documents trapezoidal back-EMF and direct-current-style commutation for BLDC versus sinusoidal excitation for PMSM, while noting the power hardware can overlap. Reference: [TI: Sensorless Trapezoidal Control of BLDC Motors](https://www.ti.com/lit/pdf/sprabq7). TI's BLDC application notes describe Hall-based and sensorless trapezoidal control as standard low-complexity approaches for this class of application. Reference: [TI: Trapezoidal Control of BLDC Motors Using Hall Effect Sensors](https://www.ti.com/lit/an/sprabz4/sprabz4.pdf).

### Drive selection

| Type                     | Example            |
| ------------------------ | ------------------ |
| ESC                      | Hobbywing          |
| Integrated controller IC | Texas Instruments  |
| Smart driver modules     | STMicroelectronics |

Typical drive build:

- Low-voltage DC input.
- 3-phase MOSFET inverter.
- Simple MCU or dedicated motor-control IC.
- One or a limited number of current sensing channels.
- Commutation table instead of a full servo stack.

What it usually does **not** include: position loop, encoder interface, heavy filtering/resonance tools, industrial network integration.

### Wiring

| Signal          | Notes                             |
| --------------- | --------------------------------- |
| DC+ / DC-       | Main supply                       |
| U / V / W       | Motor phases                      |
| Hall (optional) | 3 signals + 5 V + GND             |
| Communications  | Optional PWM / analog / CAN / UART |
| Safety          | Usually basic power cut or enable |

**Why wiring is simple:**

- Sensorless systems eliminate the feedback cable entirely.
- Hall wiring is much lighter than encoder or resolver wiring.
- No STO loop in most low-cost systems.
- No dedicated industrial fieldbus required.

### Tuning / setup

Minimal:

- Commutation timing advance.
- Startup ramp.
- Current limit.

Not required:

- Velocity loop tuning.
- Position loop.

Commissioning reduces to: confirm rotation direction, verify startup and current limit, optionally adjust timing advance. No full axis tuning sequence.

### Measurement strategy

**Use NR-X data logger for:**

- DC voltage.
- DC current.

**Use oscilloscope for:**

- Verifying back-EMF waveform.
- Checking commutation timing.
- Hall signal timing observation.

One current probe plus DC bus logging is typically enough to characterize the drive.

### Failure modes

| Symptom             | Cause                        |
| ------------------- | ---------------------------- |
| No startup          | Sensorless detection failure |
| Noise / vibration   | Poor commutation timing      |
| Overheating         | Airflow blockage             |
| Stall current spike | Load jam                     |

### Cost structure

| Component | Cost level |
| --------- | ---------- |
| Motor     | Low        |
| Driver    | Very low   |
| Sensors   | Optional   |

### Final engineering verdict

> BLDC wins because **system physics reduces the need for control sophistication**. The fluid or aerodynamic load is self-damping, there is no position requirement, and a smooth commanded torque is not needed — so the cheapest commutation scheme (6-step, sensorless) is the right engineering answer, not a compromise.

### Real-world examples

- HVAC fans.
- PC cooling fans.
- Water pumps.
- Automotive auxiliary pumps.
- Circulation pumps and blowers.
- High-volume cost-sensitive products.

---

## Scenario 2 — PMSM-favored: precision robotic axis / wafer stage

### System context and requirements

**Function:** precise positioning and motion.
**Load:** variable, dynamic.
**Requirement:** smooth motion, zero backlash effect.
**Environment:** semiconductor / robotics.
**Voltage:** 200–480 VAC servo system.
**Feedback:** mandatory (encoder).

| Requirement         | Priority |
| ------------------- | -------- |
| Position accuracy   | Critical |
| Smooth motion       | Critical |
| Low-speed stability | Critical |
| Dynamic response    | High     |
| Repeatability       | Critical |
| Noise / vibration   | Very low |

### Engineering analysis and recommended solution

**Control needs.** Full closed-loop stack:

- Current loop.
- Velocity loop.
- Position loop.

**Mechanical sensitivity.** High sensitivity to vibration. Torque ripple directly affects performance.

**Electrical behavior.** Requires accurate rotor position. Requires sinusoidal current control.

**Recommended solution: PMSM + encoder + FOC servo drive.**

### Architecture

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
AC --> Servo_Drive --> PMSM --> Precision_Load
Encoder --> Servo_Drive
PLC --> Servo_Drive
</pre></div>

### Why PMSM wins and why BLDC is not suitable

**Advantages of PMSM here:**

- Smooth sinusoidal torque.
- Full torque at low and zero speed.
- Precise position control.
- Fast dynamic response.
- Minimal torque ripple.

**Why BLDC is not suitable:**

- 6-step → torque ripple → vibration.
- Poor low-speed control.
- Sensorless not viable at zero speed.
- Hall resolution too coarse for micron-level positioning.

### System definition

| Parameter  | Typical range          |
| ---------- | ---------------------- |
| Voltage    | 200–480 VAC            |
| Power      | 100 W – 10 kW          |
| Speed      | 0 – 3,000 RPM          |
| Torque     | Dynamic, bidirectional |
| Accuracy   | Micron-level           |
| Duty cycle | Dynamic                |

### Mechanical characteristics

- High stiffness required.
- Low backlash.
- Sensitive to vibration.
- Load changes rapidly.

The system is **control-dominated**, not load-dominated: the mechanics do not forgive a noisy commanded torque, so the controller has to enforce the behavior the machine needs.

### Control strategy — full servo stack with FOC

**Full servo stack.**

- Current loop at ~kHz bandwidth.
- Velocity loop.
- Position loop.

**FOC implementation.**

- dq transformation (Clarke + Park).
- Torque control via Iq.
- Flux control via Id.
- Sinusoidal excitation at the motor terminals.

Microchip's encoder-based PMSM FOC note ties high-precision speed control directly to encoder-based FOC, and the Hall/encoder FOC guidance notes that fine position information from encoders or resolvers is used when higher performance is required. References: [Microchip: Sensored (Encoder-Based) FOC of Three-Phase PMSM](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ApplicationNotes/ApplicationNotes/Sensored-Encoder-Based%29-Field-Oriented-Control-of-Three-Phase-Permanent-Magnet-Synchronous-DS00002757A.pdf); [Microchip: SF FOC PMSM Using Hall and Encoder](https://ww1.microchip.com/downloads/aemdocuments/documents/fpga/ProductDocuments/UserGuides/sf_foc_pmsm_using_hall_and_encoder_ug.pdf).

### Drive selection

| Tier             | Example                         |
| ---------------- | ------------------------------- |
| Industrial servo | Siemens, Yaskawa                |
| Compact servo    | Elmo Motion Control, Kollmorgen |
| EtherCAT         | Beckhoff                        |

Typical drive build:

- Full 3-phase inverter.
- Multiple current sensors.
- Fast control processor (DSP class).
- Current + speed + position loops in firmware.
- Encoder / resolver interface.
- Filters, gain tuning, often notch filters for resonance.
- Networked motion-control integration.

Beckhoff's AX5000/AX8000 documentation reflects this industrial servo architecture, including dedicated motor power and feedback cable systems and options like One Cable Technology on some platforms. Reference: [Beckhoff AX5000 System Manual](https://download.beckhoff.com/download/document/motion/ax5000_system_manual_hw2_en.pdf).

### Wiring

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    AC([3φ 200–480 VAC]):::power
    FIL[EMI filter + disconnect]:::power
    DRV[Servo drive]
    BRK[Brake resistor]:::power
    MOT[PMSM motor]:::phase
    ENC>Encoder / resolver]:::feedback
    STO[Safety relay]:::safety
    PLC[Motion controller]:::bus
    PE((Cabinet PE)):::shield

    AC -->|L1 / L2 / L3 / PE| FIL
    FIL -->|DC bus| DRV
    DRV -.->|brake chopper| BRK
    DRV -->|U / V / W + PE| MOT
    MOT -.->|motor cable shield| PE
    ENC -.->|A± / B± / Z± or EnDat/BiSS-C| DRV
    ENC -.->|shield| PE
    STO -->|STO-1 / STO-2 24V| DRV
    PLC -->|EtherCAT / PROFINET| DRV
    DRV -.-> PE

    classDef power stroke:#c0392b,stroke-width:2px
    classDef phase stroke:#2c3e50,stroke-width:2px
    classDef feedback stroke:#2980b9,stroke-width:2px
    classDef safety stroke:#e67e22,stroke-width:2px
    classDef bus stroke:#27ae60,stroke-width:2px
    classDef shield stroke:#7f8c8d,stroke-width:1px,stroke-dasharray:3 3
</pre></div>

| Signal   | Notes                                           |
| -------- | ----------------------------------------------- |
| AC input | Drive supply                                    |
| U / V / W | Motor phases                                   |
| Encoder  | Differential pairs, shielded                    |
| STO      | Safety (Safe Torque Off), often with SS1/SLS    |
| Fieldbus | EtherCAT / PROFINET / EtherNet/IP / CANopen     |
| Aux      | Brake, temperature sensor, enable/reset I/O     |

**Why wiring is more complex:**

- Encoder/resolver wiring is mandatory or strongly preferred.
- Shield quality and routing matter far more than on a BLDC fan.
- Safety wiring is usually required.
- Network wiring is part of the axis architecture, not optional.
- Brake and thermal sensor wiring are common.

Beckhoff explicitly recommends shielded preassembled power and feedback cables and warns that incorrect shielding leads to EMC interference. Reference: [Beckhoff: Connection of motors with preassembled cables](https://infosys.beckhoff.com/content/1033/al3800_handbuch/1867989387.html).

### Tuning / setup

Typical commissioning sequence:

1. Motor ID / motor file / motor constants.
2. Feedback configuration.
3. Commutation alignment.
4. Current loop validation.
5. Velocity loop tuning.
6. Position loop tuning.
7. Notch filter for resonance.
8. Load validation.
9. Safety validation.

This is a fundamentally different setup burden from a simple BLDC fan drive.

### Measurement strategy

**NR-X data logger:**

- DC bus power.
- Torque.
- Speed.

**Oscilloscope:**

- Current waveform (sinusoidal quality).
- PWM quality.
- Noise / switching artifacts.
- Encoder signals.

You typically need cleaner synchronized measurements, encoder observation, high-voltage differential probes for inverter output, and current probes with enough bandwidth — plus good correlation between the data logger and the scope.

Tektronix recommends high-voltage differential probes and AC/DC current probes for inverter and motor-drive measurements because of floating nodes and common-mode voltage. Reference: [Tektronix: Making Measurements on 3-Phase Motor Drives with an Oscilloscope](https://www.tek.com/en/documents/primer/making-measurements-on-3-phase-motor-drives-with-an-oscilloscope).

### Failure modes

| Symptom        | Cause                     |
| -------------- | ------------------------- |
| Oscillation    | Velocity loop instability |
| Squeal         | Resonance                 |
| Current spikes | Poor commutation          |
| Position error | Encoder issue             |

### Cost structure

| Component   | Cost   |
| ----------- | ------ |
| Motor       | High   |
| Drive       | High   |
| Encoder     | Medium |
| Integration | High   |

### Final engineering verdict

> PMSM wins because **control authority is required to overcome system sensitivity**. The mechanics do not damp what the controller gets wrong — smoothness, zero-speed torque, and micron-level repeatability have to be produced by sinusoidal FOC on top of a high-resolution feedback device. Every part of the drive architecture (fast current loop, encoder interface, STO, network) follows from that single requirement.

### Real-world examples

- Semiconductor wafer stages.
- Robotic arms.
- CNC axes.
- Pick-and-place machines.
- Semiconductor equipment motion modules.

---

## Scenario 3 — Ambiguous: AGV / mobile robot drive wheel

### System context and requirements

**Function:** traction drive.
**Load:** variable (payload changes).
**Speed:** low to medium.
**Voltage:** 24–72 VDC.
**Environment:** warehouse / factory.
**Budget:** variable depending on product tier.

| Requirement       | Priority    |
| ----------------- | ----------- |
| Efficiency        | High        |
| Smooth motion     | Medium–High |
| Cost              | Medium–High |
| Low-speed control | Important   |
| Robustness        | High        |

### Engineering trade space

**Option A — BLDC (Hall / sensorless).**

- *Pros:* lower cost, simpler electronics, less wiring, easier manufacturing.
- *Cons:* torque ripple, weaker low-speed control, less precise velocity regulation.

**Option B — PMSM + FOC + encoder.**

- *Pros:* smooth motion (better for navigation), better low-speed torque, precise speed control, better energy efficiency under variable load.
- *Cons:* higher cost (encoder + drive), more complex tuning, more wiring.

### Decision matrix

| Factor                       | BLDC wins | PMSM wins |
| ---------------------------- | --------- | --------- |
| Cost-sensitive product       | Yes       |           |
| Premium product              |           | Yes       |
| Smooth navigation needed     |           | Yes       |
| Basic mobility only          | Yes       |           |
| Low-speed precision critical |           | Yes       |
| Minimal wiring               | Yes       |           |
| Energy optimization          |           | Yes       |

### Recommendation logic

**Choose BLDC if:**

- Cost is the dominant constraint.
- System tolerates ripple.
- Navigation is coarse.
- High-volume production.

**Choose PMSM if:**

- Smooth motion matters (customer experience).
- Low-speed control is critical.
- Payload varies significantly.
- Energy efficiency is a selling point.

### System definition

| Parameter | Typical range                |
| --------- | ---------------------------- |
| Voltage   | 24–72 VDC                    |
| Power     | 200 W – 5 kW                 |
| Speed     | 0 – 3 m/s                    |
| Torque    | Variable (payload dependent) |
| Duty      | Stop/start frequent          |

### Mechanical characteristics

- Variable inertia (payload changes).
- Frequent acceleration/deceleration.
- Low-speed operation critical.
- Sometimes uneven terrain.

### Two competing architectures

#### Option A — BLDC (cost-optimized)

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    BAT([24–72 V battery]):::power
    CONT[Main contactor + precharge]:::power
    DRV[BLDC traction driver]
    MOT[BLDC motor]:::phase
    WHL[Drive wheel]
    HALL>Hall sensor]:::feedback
    HOST[Throttle / CAN]:::bus

    BAT -->|DC+ / DC-| CONT
    CONT -->|DC bus| DRV
    DRV -->|U / V / W| MOT
    MOT --> WHL
    HALL -.-> DRV
    HOST -.-> DRV

    classDef power stroke:#c0392b,stroke-width:2px
    classDef phase stroke:#2c3e50,stroke-width:2px
    classDef feedback stroke:#2980b9,stroke-width:2px
    classDef bus stroke:#27ae60,stroke-width:2px
</pre></div>

*Characteristics.* Hall-based commutation, 6-step or basic FOC, moderate control.

*Drive.* Lower-cost 24–72 V controller, Hall-based commutation or basic FOC, moderate current sensing, limited motion intelligence in the drive.

*Wiring.*

| Wiring group  | BLDC AGV version                         |
| ------------- | ---------------------------------------- |
| Battery input | DC+ / DC-                                |
| Motor power   | U / V / W                                |
| Feedback      | Hall signals only, or none if sensorless |
| Control       | Throttle / analog / CAN / UART           |
| Safety        | Basic interlock / contactor              |

*Pros.* Fewer conductors, cheaper motor cable set, easier field replacement, lower BOM.
*Cons.* Weaker low-speed smoothness, less precise velocity control, less refined traction behavior.

#### Option B — PMSM (performance-optimized)

<div class="mermaid-wrap"><pre class="mermaid">
flowchart LR
    BAT([24–72 V battery]):::power
    CONT[Main contactor + precharge]:::power
    DRV[FOC traction drive]
    MOT[PMSM motor]:::phase
    WHL[Drive wheel]
    ENC>Encoder]:::feedback
    PLC[Motion controller]:::bus
    PE((Chassis bond)):::shield

    BAT -->|DC+ / DC-| CONT
    CONT -->|DC bus| DRV
    DRV -->|U / V / W + PE| MOT
    MOT -.-> PE
    ENC -.->|A± / B± / Z±| DRV
    ENC -.-> PE
    PLC -->|CAN / EtherCAT| DRV

    classDef power stroke:#c0392b,stroke-width:2px
    classDef phase stroke:#2c3e50,stroke-width:2px
    classDef feedback stroke:#2980b9,stroke-width:2px
    classDef bus stroke:#27ae60,stroke-width:2px
    classDef shield stroke:#7f8c8d,stroke-width:1px,stroke-dasharray:3 3
</pre></div>

*Characteristics.* FOC control, encoder feedback, full torque control.

*Drive.* FOC traction controller or servo-class drive, encoder feedback, better torque control, better current regulation, often better regen and low-speed handling.

*Wiring.*

| Wiring group   | PMSM AGV version                                                     |
| -------------- | -------------------------------------------------------------------- |
| Battery input  | DC+ / DC-                                                            |
| Motor power    | U / V / W                                                            |
| Feedback       | Encoder cable, or high-quality Hall plus stronger control electronics |
| Communications | CANopen / EtherCAT / industrial network in premium systems           |
| Safety         | Contactor, STO or controlled torque disable depending on platform    |

*Pros.* Smoother starts, better crawl-speed control, better closed-loop traction, better behavior under variable payload.
*Cons.* More wires, higher feedback cost, more sensitivity to routing and noise, more commissioning effort.

Microchip's PMSM FOC references and Hall/encoder guidance reflect this jump in control sophistication: finer position information and sinusoidal control support better synchronized waveforms and better slow-speed behavior. Reference: [Microchip: SF FOC PMSM Using Hall and Encoder](https://ww1.microchip.com/downloads/aemdocuments/documents/fpga/ProductDocuments/UserGuides/sf_foc_pmsm_using_hall_and_encoder_ug.pdf).

### Detailed tradeoffs

**Control.**

| Feature    | BLDC     | PMSM   |
| ---------- | -------- | ------ |
| Startup    | Simple   | Robust |
| Low-speed  | Weak     | Strong |
| Smoothness | Moderate | High   |

**Efficiency.**

| Condition      | Winner  |
| -------------- | ------- |
| Constant speed | Similar |
| Variable load  | PMSM    |
| Stop/start     | PMSM    |

**Cost.**

| Component | BLDC      | PMSM    |
| --------- | --------- | ------- |
| Motor     | Low       | Medium  |
| Driver    | Low       | High    |
| Feedback  | None/Hall | Encoder |
| Total     | Low       | High    |

### Real engineering trade-flip

| Condition change         | Decision flip |
| ------------------------ | ------------- |
| Add encoder requirement  | PMSM          |
| Reduce budget            | BLDC          |
| Require silent operation | PMSM          |
| Coarse navigation only   | BLDC          |
| Energy optimization      | PMSM          |

### Tuning differences

**BLDC.** Minimal tuning. Fixed commutation.

**PMSM.** Full loop tuning required. Gain scheduling may be needed across payload ranges.

### Measurement strategy

**Same for both:**

- DC bus power.
- Torque (if available).
- Speed.

**Additional for PMSM:**

- Current waveform quality.
- Stability under load.

### Failure modes

**BLDC.**

- Poor low-speed control.
- Jerky motion.
- Stall at startup.

**PMSM.**

- Tuning instability.
- Encoder noise.
- Higher integration complexity.

### Cost vs experience tradeoff

| Product type        | Recommendation |
| ------------------- | -------------- |
| Low-cost AGV        | BLDC           |
| Premium AGV        | PMSM           |
| Research / robotics | PMSM           |

### Final engineering verdict

> This scenario is a **business decision disguised as an engineering problem**. The motor physics does not decide — product positioning does. A low-cost platform reaches for BLDC + Hall + basic FOC and lives with the ripple; a premium platform reaches for PMSM + encoder + full FOC and pays for the smoother customer experience. The engineering job is to make the cost-vs-performance tradeoff visible and defensible, not to pick a "best" motor in the abstract.

### Real-world examples

- Warehouse AGVs (cost-optimized → BLDC; premium → PMSM).
- Autonomous mobile robots (AMRs).
- Research robotics platforms.
- Variable-payload traction drives.

---

## Cross-scenario summary

*Visual reference: see the [Cable-group legend]({{ '/fundamentals/motors/bldc-pmsm-implementation/#cable-group-legend' | relative_url }}) and the [three wiring archetypes]({{ '/fundamentals/motors/bldc-pmsm-implementation/#wiring-archetypes--which-pattern-applies' | relative_url }}) in the Implementation Guide — the comparison tables below abstract what the diagrams there show visually.*

### Drive comparison across the three archetypes

| Feature                  | BLDC fan/pump drive       | PMSM precision servo drive                        | BLDC AGV drive          | PMSM AGV drive                 |
| ------------------------ | ------------------------- | ------------------------------------------------- | ----------------------- | ------------------------------ |
| Commutation              | 6-step / sensorless       | Sinusoidal / FOC                                  | Hall / basic FOC        | FOC                            |
| Position loop            | No                        | Yes                                               | Usually no              | Sometimes external or embedded |
| Speed loop               | Simple                    | Advanced                                          | Moderate                | Strong                         |
| Current loop             | Simple/basic              | Fast/high-performance                             | Moderate                | Strong                         |
| Feedback interface       | Hall / none               | Encoder / resolver                                | Hall / encoder optional | Encoder preferred              |
| Tuning depth             | Low                       | High                                              | Medium                  | Medium–high                    |
| EMI sensitivity          | Lower overall complexity  | Higher due to feedback and high-performance loops | Medium                  | Higher                         |
| Typical controller class | ESC / embedded controller | Industrial servo amplifier                        | Traction controller     | FOC traction/servo controller  |

### Wiring comparison across the three archetypes

| Feature                              | BLDC fan/pump | PMSM precision axis          | AGV BLDC version | AGV PMSM version           |
| ------------------------------------ | ------------- | ---------------------------- | ---------------- | -------------------------- |
| Main supply                          | DC bus        | AC or DC bus                 | DC battery       | DC battery                 |
| Motor phases                         | U/V/W         | U/V/W                        | U/V/W            | U/V/W                      |
| Feedback required                    | None or Hall  | Encoder/resolver             | Hall or none     | Encoder or advanced Hall   |
| Feedback cable shielding sensitivity | Low–medium    | High                         | Medium           | High                       |
| Safety wiring                        | Minimal       | STO / common industrial safety | Basic interlock  | Higher-end safety possible |
| Fieldbus / network                   | Optional      | Common                       | Optional         | Common in premium systems  |
| Brake wiring                         | Usually no    | Often yes                    | Usually no       | Maybe                      |
| Temp sensor wiring                   | Optional      | Common                       | Optional         | Common in better systems   |

### Measurement implications

The wiring and drive choice changes **how you debug** the system.

**Simpler BLDC system.** You can often get away with:

- DC bus logging.
- One current probe.
- Hall timing observation.

**PMSM / servo system.** You usually need:

- Cleaner synchronized measurements.
- Encoder observation.
- Differential probes for inverter output (floating nodes, common-mode voltage).
- Current probes with enough bandwidth.
- Better correlation between data logger and scope.

Tektronix recommends high-voltage differential probes and AC/DC current probes for inverter and motor-drive measurements because of floating nodes and common-mode voltage. Reference: [Tektronix: Making Measurements on 3-Phase Motor Drives with an Oscilloscope](https://www.tek.com/en/documents/primer/making-measurements-on-3-phase-motor-drives-with-an-oscilloscope).

**Cross-scenario rule:** avoid RMS measurement on PWM outputs in both families — use bandwidth-adequate probes and averaged DC-bus metrics instead.

### Engineering takeaway

```text
BLDC       → physics handles stability
PMSM       → controller enforces behavior
Ambiguous  → economics decides architecture
```

**Scenario 1 — BLDC-favored (fan/pump).** Simple ESC / BLDC inverter. DC input + U/V/W + maybe Hall. Low cost, low wiring count, low commissioning burden. System physics (fluid/aerodynamic damping, no position requirement) absorbs what the controller is too simple to fix.

**Scenario 2 — PMSM-favored (precision axis).** Servo / FOC inverter. Power + U/V/W + encoder/resolver + safety + network. Precision requires feedback, tuning, and cleaner control. The mechanics are unforgiving; the controller has to do the work.

**Scenario 3 — ambiguous (AGV traction).** Drive and wiring flip with product tier. Lower-cost AGV → BLDC / Hall / basic FOC. Premium AGV → PMSM / encoder / full FOC. The decision is not a motor decision; it is a product-strategy decision.

**Pattern worth remembering.**

```text
No precision required → BLDC
High precision required → PMSM
Uncertain → depends on cost vs performance priorities
```

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/motors/bldc-pmsm-implementation/' | relative_url }}">&larr; BLDC/PMSM Implementation Guide</a>
  <a href="{{ '/fundamentals/motors/' | relative_url }}">↑ Motors, Drives, and Motion</a>
  <a href="{{ '/fundamentals/motors/servo-drive-fundamentals/' | relative_url }}">Servo Drive Fundamentals &rarr;</a>
</div>
