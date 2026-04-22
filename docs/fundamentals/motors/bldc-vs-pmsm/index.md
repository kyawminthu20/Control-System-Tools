---
layout: training-module
title: "BLDC vs PMSM — Motors, Drives, and Scenarios"
description: "Head-to-head engineering comparison of BLDC and PMSM systems, with 10 real-world scenario walkthroughs and a decision matrix."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Motors, Drives, and Motion"
    url: "/fundamentals/motors/"
repo_path: "control-standards/rag/training_modules/electrical_machines/bldc_vs_pmsm_comparison.md"
---

## Purpose

- **Use this page when** you are choosing between BLDC and PMSM (and implicitly, against induction) for a new or retrofit machine.
- **Choose BLDC if** BOM cost dominates, the load tolerates torque ripple, and you do not need torque at zero speed.
- **Choose PMSM if** you need smooth torque, zero-speed holding, field-weakening range, or functional safety (STO/SS1/SLS).

### At a glance

<div class="glance-grid">
  <div class="card">
    <span class="card__label">BLDC wins when</span>
    <span class="card__title">Cost dominates</span>
    <p class="card__desc">Fans, pumps, propellers, power tools, low-end conveyors. Load masks ripple; no encoder required.</p>
  </div>
  <div class="card">
    <span class="card__label">PMSM wins when</span>
    <span class="card__title">Control quality dominates</span>
    <p class="card__desc">Servos, cobots, CNC, EV traction, semi stages. Needs smooth torque, zero-speed hold, or field weakening.</p>
  </div>
  <div class="card">
    <span class="card__label">Induction + VFD</span>
    <span class="card__title">Still the right answer sometimes</span>
    <p class="card__desc">Continuous-duty conveyors, pumps, HVAC fans where robustness and zero-magnet cost beat marginal efficiency gains.</p>
  </div>
  <div class="card">
    <span class="card__label">Health warning</span>
    <span class="card__title">Don't choose by motor name</span>
    <p class="card__desc">Vendors mix the terms. A "BLDC" with sinusoidal BEMF + FOC is really a PMSM system. The back-EMF waveform decides, not the nameplate.</p>
  </div>
</div>

### Jump to

<div class="glance-grid" role="navigation" aria-label="On this page">
  <a class="card" href="#physical-construction--what-actually-differs"><span class="card__title">Construction</span></a>
  <a class="card" href="#control-strategy-comparison"><span class="card__title">Control</span></a>
  <a class="card" href="#feedback--why-it-gates-performance"><span class="card__title">Feedback</span></a>
  <a class="card" href="#decision-matrix-use-this-when-speccing"><span class="card__title">Decision Matrix</span></a>
  <a class="card" href="#scenario-walkthroughs"><span class="card__title">Scenarios</span></a>
</div>

---

## The one-sentence distinction

- **BLDC** = permanent-magnet synchronous motor with **trapezoidal** back-EMF, typically driven with **6-step commutation**.
- **PMSM** = permanent-magnet synchronous motor with **sinusoidal** back-EMF, typically driven with **sinusoidal commutation or FOC**.

In this module, "PMSM" refers to the servo-style sinusoidal/FOC case — the combination that dominates industrial and high-performance designs. A PMSM can be driven 6-step (and some low-cost products do this), but it behaves like a noisy BLDC when you do.

Same family. Different shaping of the flux linkage. Different control strategy. Different drive cost.

The motor nameplate will not always tell you which you have — the **back-EMF waveform** does.

---

## Physical construction — what actually differs

| Feature                 | BLDC                            | PMSM                                             |
| ----------------------- | ------------------------------- | ------------------------------------------------ |
| Magnet placement        | Usually surface-mount (SPM)     | SPM (sinusoidal shaping) or IPM (interior)       |
| Stator winding          | Concentrated (tooth-wound)      | Distributed (sinusoidal MMF)                     |
| Back-EMF shape          | Trapezoidal                     | Sinusoidal                                       |
| Slot/pole ratio         | Optimized for flat-top EMF      | Optimized for sinusoidal EMF                     |
| Cogging torque          | Often higher                    | Lower (by design, often with skew)               |
| Rotor saliency (Ld, Lq) | Ld ≈ Lq (surface magnets)       | Ld ≠ Lq on IPM → reluctance torque available     |
| Typical feedback        | Hall sensors or sensorless BEMF | Encoder, resolver, or high-res sensorless        |

### Why the winding matters

- **Concentrated windings** (BLDC) are cheaper to wind, have shorter end-turns, and fit the flat-top EMF of trapezoidal machines.
- **Distributed windings** (PMSM) spread the MMF smoothly around the air gap → clean sinusoidal flux linkage → low torque ripple under sine current.

### IPM-PMSM adds reluctance torque

Interior-magnet PMSM exploits Ld < Lq:

T = (3/2) · p · [ψ_f · Iq + (Ld − Lq) · Id · Iq]

The second term is **reluctance torque**. It lets the drive inject controlled negative Id to gain torque per amp and to extend the speed range via **field weakening**. BLDCs cannot do this meaningfully.

---

## Back-EMF — the root cause of all control differences

### Trapezoidal (BLDC)

- Flat top over ~120° electrical
- During the flat region, torque is smooth with **DC-like** phase current
- Outside the flat region, torque dips → ripple

### Sinusoidal (PMSM)

- Clean sine, aligned with rotor position
- Constant torque requires the **phase current to be sinusoidal and phase-locked** to the rotor

### Implication

- If you feed **sine current** to a trapezoidal motor → torque ripple (waveform mismatch)
- If you feed **6-step square current** to a sinusoidal motor → large torque ripple, acoustic noise, heating

The drive must match the motor's back-EMF shape. That match is the whole game.

---

## Control strategy comparison

### A. 6-step trapezoidal (classic BLDC)

- 6 commutation states per electrical cycle
- Two phases conducting, one floating, per state
- Position resolution required: **60° electrical** (3 Hall sensors are enough)
- Current regulated as **DC magnitude** during each 120° conduction window

#### Strengths

- Minimal compute (can run on an 8-bit MCU)
- Fast to commission
- Very cheap BOM
- Works well at mid/high speed with light load dynamics

#### Weaknesses

- Torque ripple at commutation transitions (~14% theoretical on an ideal trap motor, worse in practice)
- Audible noise (especially at low speed)
- Poor low-speed smoothness
- No field weakening
- No clean torque control during commutation

### B. Sinusoidal commutation (no FOC)

- Sine references for each phase, open-loop aligned to rotor angle
- Still scalar control, no dq transformation
- Better smoothness than 6-step, worse torque response than FOC
- Transitional strategy — rarely the final architecture on a new design

### C. FOC / vector control (PMSM standard)

- Clarke (abc → αβ) and Park (αβ → dq) transforms project stator currents into a rotor-aligned frame
- Two PI current loops: one on **Id** (flux), one on **Iq** (torque)
- Decouples flux and torque — same math as a separately-excited DC machine
- Requires: high-resolution rotor position, fast ADC sampling, sufficient MCU/DSP bandwidth

#### Strengths

- Smooth torque from zero speed
- Deterministic response
- Field weakening for extended speed range
- MTPA (Maximum Torque Per Ampere) on IPM machines
- High efficiency at partial load

#### Weaknesses

- Complex commissioning (needs motor parameter identification: Rs, Ld, Lq, ψ_f, encoder offset)
- Position accuracy critical — an encoder offset error shows up directly as reduced torque and efficiency
- More expensive hardware (higher-res feedback, better ADC, more MCU)

---

## Drive / inverter architecture

### Shared power stage

Both BLDC and PMSM drives share the same topology:

- 3-phase two-level voltage-source inverter
- 6 switches (MOSFET up to ~100 V / ~150 A, IGBT above)
- DC bus capacitor bank
- Gate drivers with dead time
- Current sensing (1, 2, or 3 shunts, or Hall-effect current sensors, or DC-link shunt with reconstruction)

The **hardware is nearly identical**. The difference is in the controller, feedback quality, and software.

### BLDC drive (trapezoidal)

| Block                   | Typical choice                           |
| ----------------------- | ---------------------------------------- |
| MCU                     | 8- or 32-bit, ~50–100 MHz                |
| Current sense           | Single DC-link shunt, per-step gating    |
| PWM frequency           | 15–30 kHz typical                        |
| Feedback                | 3 Hall sensors (digital)                 |
| Commutation table       | 6-state lookup, indexed by Hall code     |
| Control loop rate       | 1–10 kHz for current (often slower)      |
| Protection              | Overcurrent, DC-bus OV/UV, thermal       |

### PMSM / servo drive (FOC)

| Block                   | Typical choice                                      |
| ----------------------- | --------------------------------------------------- |
| MCU / DSP               | 32-bit DSP or MCU with FPU, 150–300 MHz             |
| Current sense           | 2 or 3 in-line phase shunts or Hall-effect sensors  |
| PWM frequency           | 8–20 kHz (industrial servo), higher on small motors |
| Feedback                | Incremental encoder, absolute encoder, or resolver  |
| Modulation              | Space Vector PWM (SVPWM)                            |
| Control loop rate       | 10–20 kHz current, 1–5 kHz velocity, 0.5–2 kHz pos  |
| Protection              | OC, OV/UV, OT, I²t, position error, STO, SBC        |

### The gap in software

- BLDC drive firmware fits in ~8–20 KB of flash.
- PMSM FOC firmware is typically 60–200 KB plus autotuning routines, parameter identification, fault logging, fieldbus stack (EtherCAT, PROFINET, CANopen, etc.).

### Functional safety

PMSM servo drives routinely carry **STO (Safe Torque Off)**, and often SS1, SS2, SLS, SBC per IEC 61800-5-2. Trapezoidal BLDC drives in lower-cost markets typically do not, unless specifically rated.

---

## Feedback — why it gates performance

| Feedback          | Resolution             | Works for BLDC 6-step | Works for PMSM FOC        |
| ----------------- | ---------------------- | --------------------- | ------------------------- |
| 3 Halls           | 60° electrical         | Yes — native          | Marginal, startup only    |
| Incremental enc.  | typ. 1024–10000 PPR    | Overkill              | Yes (needs index + align) |
| Absolute enc.     | 17–26 bit single-turn  | Overkill              | Yes — preferred           |
| Resolver          | analog, ~12–16 bit     | Overkill              | Yes — rugged              |
| Sensorless (BEMF) | Zero-cross detection   | Yes, mid/high speed   | Poor at low speed         |
| Sensorless (obs.) | Luenberger / SMO / MRAS| —                     | Yes, with startup caveat  |

**Rule of thumb:**

- Want precise torque at zero speed → you need a **real encoder** and **FOC**.
- Want cheap and rugged at moderate speed → Halls + 6-step.
- Want no sensor in the rotor hub → sensorless BEMF (cheap) or observer-based (performance).

---

## Torque ripple — quantified

| Scheme                           | Typical torque ripple       |
| -------------------------------- | --------------------------- |
| Ideal 6-step on trapezoidal      | ~14% (commutation dips)     |
| Real 6-step on trapezoidal       | 15–25%                      |
| 6-step on sinusoidal motor       | 30–50% (mismatched)         |
| Sinusoidal commutation (no FOC)  | 3–8%                        |
| FOC on PMSM with good encoder    | < 2%                        |
| FOC on PMSM with encoder misalign| rises fast — 5–15%          |

Ripple matters any time you are driving a load that sees the ripple mechanically — gearheads, precision stages, camera gimbals, coordinate-table positioners. It does not matter for a fan impeller.

---

## Speed range and field weakening

### BLDC 6-step

- Base speed set by DC bus vs back-EMF
- Crude phase advance can push a small extra RPM window, but there is no clean flux control
- Above base speed → torque drops sharply, efficiency drops

### PMSM FOC (SPM)

- Field weakening via negative Id
- Modest speed range extension (typically 1.5–2× base)
- Torque falls ∝ 1/ω above base speed

### PMSM FOC (IPM)

- Field weakening + reluctance torque
- Wide constant-power range (often 3–5× base speed)
- Used in EV traction, spindle drives

The field-weakening window is the **single biggest reason** to choose PMSM + FOC over trapezoidal BLDC once the application needs a wide speed range from a fixed DC bus.

---

## Efficiency comparison

- At the shaft, both motors have similar peak efficiency (90–95% for industrial sizes).
- Under partial load and at low speed, **FOC-PMSM wins** because copper losses scale with I² and FOC produces the minimum current for a given torque (especially with MTPA on IPM).
- At full load, high speed, and constant operating point, the gap shrinks.
- 6-step trapezoidal pays a perpetual penalty in **switching losses** and **commutation-induced harmonic heating** vs SVPWM.

---

## Cost structure (2026 ballpark, industrial)

| Item                              | BLDC system   | PMSM servo system |
| --------------------------------- | ------------- | ----------------- |
| Motor (1 kW class)                | $150–400      | $400–900          |
| Drive                             | $80–250       | $600–1500         |
| Feedback device                   | Halls in-motor| Encoder: $80–300  |
| Commissioning effort              | hours         | days (first time) |
| BOM complexity                    | low           | high              |
| Spares & support ecosystem        | generic       | vendor-coupled    |

Rule: if a 6-step BLDC covers your spec, the total installed cost is **roughly one-third** of a servo-grade PMSM for the same mechanical output.

---

## Decision matrix (use this when speccing)

Step through these in order. The first row that returns "yes" selects the architecture. Use it as a fast first pass, then drop into the scenario that matches your load for the full reasoning.

| Question                                                          | If yes, choose                |
| ----------------------------------------------------------------- | ----------------------------- |
| Need full torque at zero speed, deterministically?                | PMSM + FOC + encoder          |
| Need wide constant-power range (>2× base speed)?                  | IPM-PMSM + FOC + field weak.  |
| Need torque ripple below ~3%?                                     | PMSM + FOC                    |
| Need absolute position at startup?                                | PMSM + FOC + absolute encoder |
| Need functional safety (STO/SS1/SLS)?                             | PMSM servo drive (certified)  |
| Is load a fluid / fan / quadratic torque, moderate speed range?   | BLDC sensorless / sinusoidal  |
| Is BOM cost the dominant constraint and ripple tolerable?         | BLDC 6-step                   |
| Is it a propeller / light inertia high-speed load?                | BLDC sensorless 6-step        |
| Is the machine a conveyor / pump / continuous process?            | Induction + VFD (reconsider)  |

---

## Scenario walkthroughs

Scan the 10 scenario cards, then jump to the detail section that matches your load.

<div class="scenario-grid">
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario A</span>
    <span class="scenario-card__title"><a href="#scenario-a--hvac-ec-fan--pump-variable-torque">HVAC EC fan / pump</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> BLDC</div>
    <div class="scenario-card__start"><strong>Why:</strong> fluid load masks ripple; no position need; lowest BOM</div>
    <div class="scenario-card__start"><strong>When PMSM wins:</strong> IE5 / low-noise mandates</div>
    <div class="scenario-card__start"><strong>Stack:</strong> sensorless BEMF or 3-Hall 6-step / sine</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario B</span>
    <span class="scenario-card__title"><a href="#scenario-b--e-bike--light-ev-traction">E-bike / light EV</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> PMSM (IPM)</div>
    <div class="scenario-card__start"><strong>Why:</strong> field weakening + MTPA give wide speed + best Wh/km</div>
    <div class="scenario-card__start"><strong>When BLDC wins:</strong> rock-bottom cost floor on low-end bikes</div>
    <div class="scenario-card__start"><strong>Stack:</strong> FOC + Halls + sensorless observer fusion</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario C</span>
    <span class="scenario-card__title"><a href="#scenario-c--industrial-servo-press">Industrial servo press</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> PMSM servo</div>
    <div class="scenario-card__start"><strong>Why:</strong> only stack that holds full torque at zero speed deterministically</div>
    <div class="scenario-card__start"><strong>When BLDC wins:</strong> not for this duty</div>
    <div class="scenario-card__start"><strong>Stack:</strong> FOC + absolute encoder + gain-scheduled nested loops + STO/SS1</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario D</span>
    <span class="scenario-card__title"><a href="#scenario-d--conveyor--roller-line-continuous-duty">Conveyor / roller line</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> Induction + VFD first; BLDC / PMSM as alternatives</div>
    <div class="scenario-card__start"><strong>Why:</strong> rugged, no magnets, mature VFD ecosystem, no feedback needed</div>
    <div class="scenario-card__start"><strong>When PMSM wins:</strong> IE4/IE5 mandates or regen payback on inclines</div>
    <div class="scenario-card__start"><strong>Stack:</strong> V/f or sensorless vector; scalar / light-vector FOC for PMSM</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario E</span>
    <span class="scenario-card__title"><a href="#scenario-e--drone--multirotor-propulsion">Drone / multirotor</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> BLDC</div>
    <div class="scenario-card__start"><strong>Why:</strong> propeller inertia absorbs ripple; ESC is lightest and cheapest</div>
    <div class="scenario-card__start"><strong>When PMSM wins:</strong> rare — cinematography gimbals, heavy-lift industrial drones</div>
    <div class="scenario-card__start"><strong>Stack:</strong> sensorless BEMF 6-step or FOC-lite ESC</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario F</span>
    <span class="scenario-card__title"><a href="#scenario-f--cnc-spindle-520-kw">CNC spindle (5–20 kW)</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> PMSM IPM</div>
    <div class="scenario-card__start"><strong>Why:</strong> field-weakening + reluctance torque give constant-power window without oversizing</div>
    <div class="scenario-card__start"><strong>When BLDC wins:</strong> not for this duty</div>
    <div class="scenario-card__start"><strong>Stack:</strong> FOC + MTPA + field weakening + high-res encoder for C-axis</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario G</span>
    <span class="scenario-card__title"><a href="#scenario-g--robot-joint-collaborative-robot">Robot joint (cobot)</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> PMSM</div>
    <div class="scenario-card__start"><strong>Why:</strong> cog-free torque transparency required for safe human-contact force control</div>
    <div class="scenario-card__start"><strong>When BLDC wins:</strong> not for cobot joints — ripple breaks force estimation</div>
    <div class="scenario-card__start"><strong>Stack:</strong> FOC + dual absolute encoder + strain-gauge torque sensor + EtherCAT</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario H</span>
    <span class="scenario-card__title"><a href="#scenario-h--semiconductor-wafer-handler--lithography-stage">Semi wafer handler / stage</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> PMSM (ironless or linear)</div>
    <div class="scenario-card__start"><strong>Why:</strong> ironless topology + FOC hit the positioning noise floor lithography needs</div>
    <div class="scenario-card__start"><strong>When BLDC wins:</strong> not at this accuracy class</div>
    <div class="scenario-card__start"><strong>Stack:</strong> FOC + laser interferometer or sub-nm encoder + jerk-limited trajectory</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario I</span>
    <span class="scenario-card__title"><a href="#scenario-i--battery-powered-power-tool-drill-impact">Power tool (drill / impact)</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> BLDC (migrating to light FOC on premium lines)</div>
    <div class="scenario-card__start"><strong>Why:</strong> compact, cheap, sensorless, drop-proof</div>
    <div class="scenario-card__start"><strong>When PMSM/FOC wins:</strong> premium tools where low-speed feel, regen, and efficiency justify the MCU cost</div>
    <div class="scenario-card__start"><strong>Stack:</strong> sensorless BEMF 6-step or light FOC with observer</div>
  </div>
  <div class="scenario-card">
    <span class="scenario-card__num">Scenario J</span>
    <span class="scenario-card__title"><a href="#scenario-j--retrofit-replacement-field-upgrade">Retrofit / field upgrade</a></span>
    <div class="scenario-card__start"><strong>Winner:</strong> Keep BLDC motor; upgrade drive to Hall-interpolated sinusoidal</div>
    <div class="scenario-card__start"><strong>Why:</strong> no mechanical change allowed; interpolated sine gives ~5–8 dB quieter</div>
    <div class="scenario-card__start"><strong>When full PMSM/FOC wins:</strong> if the envelope opens and an encoder can be added</div>
    <div class="scenario-card__start"><strong>Stack:</strong> mid-range BLDC drive, sine-mode firmware, existing Hall harness</div>
  </div>
</div>

Each scenario identifies the winning choice and the reasoning. These are drawn from real application patterns.

### Scenario A — HVAC EC fan / pump (variable torque)

- Load profile: quadratic torque vs speed, slow setpoint changes
- Ripple tolerance: high (fluid absorbs it)
- Position control: not needed
- Speed range: 20–100%

**Winner: BLDC with sensorless 6-step or sinusoidal.**
Reason: cheap, robust, no encoder, and the load tolerates torque ripple. This is the ECM motor category powering most modern HVAC equipment.

**Summary — Scenario A:** Family: **BLDC**. Why it wins: fluid load masks ripple, no position need, lowest BOM. When PMSM would win instead: stringent low-noise or efficiency mandates (e.g., premium residential HVAC, IE5 regulatory pressure). Control/feedback: sensorless BEMF or 3 Halls, 6-step or sinusoidal commutation. Drive class: low-cost single-chip ECM controller or integrated fan drive. Wiring: 3 phase leads + optional Hall harness; DC bus from rectified mains.

### Scenario B — E-bike / light EV traction

- Torque at zero speed: yes, for hill holding
- Speed range: wide, needs field weakening
- Efficiency on battery: critical
- Feedback: Halls plus sensorless observer

**Winner: PMSM with FOC (often IPM).**
Reason: field weakening extends top speed, MTPA extends range per Wh. BLDC 6-step is still seen on low-end e-bikes but is obsolete for serious designs.

**Summary — Scenario B:** Family: **PMSM (IPM preferred)**. Why it wins: field weakening + MTPA give wide constant-power range and best Wh/km. When BLDC would win instead: strict cost floor on sub-$500 bikes where range and top speed are unregulated. Control/feedback: FOC with Halls + observer fusion (startup-safe, sensorless at speed). Drive class: integrated e-mobility controller (30–80 V class, 20–80 A). Wiring: 3 phase leads + Hall harness + battery + throttle/CAN.

### Scenario C — Industrial servo press

- Torque at zero speed: mandatory (press hold)
- Position accuracy: tight
- Load is highly nonlinear (press engagement vs travel)
- Gain scheduling needed between press and travel modes

**Winner: PMSM servo + high-res encoder + FOC.**
Reason: there is no other option that can hold torque at zero speed, deliver deterministic current response, and support nested loops with gain scheduling. This is the standard architecture for industrial servo press applications.

**Summary — Scenario C:** Family: **PMSM servo**. Why it wins: only topology that holds full torque at zero speed deterministically and supports gain-scheduled nested loops. When BLDC would win instead: never for this duty — a trap motor cannot hold press force without severe heating. Control/feedback: FOC + high-res absolute encoder (or resolver), nested position/velocity/current loops. Drive class: industrial servo drive with STO/SS1, fieldbus (EtherCAT/PROFINET). Wiring: motor power cable (U/V/W + PE + shield), separate feedback cable, 24 V STO channel. For the full wiring pattern, see [Archetype B or Archetype C]({{ '/fundamentals/motors/bldc-pmsm-implementation/#wiring-archetypes--which-pattern-applies' | relative_url }}) in the Implementation Guide, depending on whether this is a single-axis press or a multi-axis servo line.

### Scenario D — Conveyor / roller line (continuous duty)

- Torque smoothness: moderate
- Position: rarely, only indexers
- Cost per drive: critical across many axes
- Robustness: maximum

**Winner: Induction + VFD (usually). BLDC second. PMSM only if you need regeneration.**
Reason: induction is actually the right answer here. If magnetic motors are desired (magnet-price tolerant), IE4/IE5 PMSM with scalar or light-vector control is increasingly chosen for efficiency reasons on new lines.

**Summary — Scenario D:** Family: **Induction first; BLDC as PM fallback; PMSM for efficiency-driven new builds**. Why induction wins: ruggedness, zero-magnet cost, mature VFD ecosystem, no feedback device needed. When PMSM would win instead: efficiency-regulated markets (IE4/IE5 mandates), or when regenerative braking on inclined conveyors pays back the drive cost. Control/feedback: V/f or sensorless vector (induction); scalar or light-vector FOC (PMSM). Drive class: general-purpose VFD. Wiring: motor cable, no feedback on induction; encoder or EnDat for PMSM variants.

### Scenario E — Drone / multirotor propulsion

- Torque ripple: tolerated by propeller dynamics
- Startup: fast spin-up from zero
- Weight: critical
- Cost: critical
- Position: irrelevant

**Winner: BLDC, sensorless 6-step (ESC).**
Reason: this is the textbook BLDC use case. PMSM FOC adds no useful benefit and costs weight and compute.

**Summary — Scenario E:** Family: **BLDC**. Why it wins: propeller inertia absorbs ripple; ESC is lightest, cheapest, highest power density. When PMSM would win instead: very rare — high-end cinematography gimbals or heavy-lift industrial drones where acoustic signature matters. Control/feedback: sensorless BEMF 6-step (modern ESCs may run FOC-lite). Drive class: electronic speed controller (ESC). Wiring: 3 phase leads, battery, PWM or DShot signal input. Wiring follows [Archetype A — Battery BLDC]({{ '/fundamentals/motors/bldc-pmsm-implementation/#archetype-a--battery-bldc-drone--e-bike--agv--power-tool' | relative_url }}).

### Scenario F — CNC spindle (5–20 kW)

- Constant power over wide speed range
- Smooth torque at low speed for rigid tapping
- Position for C-axis machining

**Winner: PMSM IPM + FOC with field weakening**, or induction + vector if peak speed is extreme.
Reason: IPM gives the constant-power window without oversizing the motor. A trap BLDC cannot do this.

**Summary — Scenario F:** Family: **PMSM IPM** (induction + vector only if top speed exceeds what IPM field weakening can reach). Why it wins: constant-power window from field weakening + reluctance torque, smooth low-speed torque for rigid tapping. When BLDC would win instead: never — trap BLDC has no usable constant-power region. Control/feedback: FOC + high-res encoder (for C-axis, absolute or incremental with index). Drive class: spindle-grade servo drive with field weakening and C-axis mode. Wiring: motor power + encoder + brake + coolant/thermal sense.

### Scenario G — Robot joint (collaborative robot)

- Torque transparency (low cogging, low ripple)
- Absolute position
- Back-drivability
- Torque sensing accuracy

**Winner: PMSM + FOC + high-res absolute encoder + torque sensor.**
Reason: the ripple and cogging characteristics of a BLDC are immediately felt through the gearbox. Cobots and direct-drive joints essentially mandate sinusoidal motors with FOC.

**Summary — Scenario G:** Family: **PMSM**. Why it wins: cog-free torque transparency required for safe human-collaborative force control. When BLDC would win instead: never for cobot joints — ripple breaks force estimation and back-drivability. Control/feedback: FOC + high-res absolute encoder (often dual encoder: motor + output) + strain-gauge torque sensor. Drive class: integrated joint drive (often inside the joint housing) with EtherCAT. Wiring: hollow-shaft cable routing, combined power + feedback + torque-sensor harness.

### Scenario H — Semiconductor wafer handler / lithography stage

- Nanometer-class positioning (on linear, air-bearing stages)
- Jerk-limited, ultra-smooth motion
- Thermal stability

**Winner: PMSM (often ironless / linear PMSM) + FOC + laser interferometer or high-end encoder.**
Reason: cogging-free ironless PMSM + FOC is the only topology that hits the positioning noise floor the process requires.

**Summary — Scenario H:** Family: **PMSM (ironless or linear PMSM)**. Why it wins: ironless topology eliminates cogging entirely; FOC delivers the noise floor lithography needs. When BLDC would win instead: never — trap BLDC cannot approach the required noise floor. Control/feedback: FOC + laser interferometer or sub-nm-class optical encoder; jerk-limited trajectory. Drive class: precision-motion servo drive (often custom, with thermal modelling). Wiring: shielded linear-motor cable, interferometer fiber or optical-encoder cable, water cooling lines.

### Scenario I — Battery-powered power tool (drill, impact)

- Compactness
- Instant torque
- Variable trigger speed
- Sensorless preferred (drop-proof, wire-count)

**Winner: BLDC with sensorless 6-step or light FOC.**
Reason: low cost, robust. Modern high-end tools (Milwaukee M18 FUEL, DeWalt FlexVolt) actually run light FOC for better low-speed feel and regen braking, which is a sign that the industry crosses over to FOC even in cost-sensitive products when MCU cost drops.

**Summary — Scenario I:** Family: **BLDC** (with migration to light FOC on premium lines). Why it wins: compact, cheap, sensorless — drop-proof mechanics. When PMSM/FOC would win instead: premium tools where low-speed feel, regen braking, and battery efficiency justify the extra MCU cost. Control/feedback: sensorless BEMF 6-step, or light FOC with observer. Drive class: integrated tool controller on the trigger PCB. Wiring: 3 phase leads, battery pack connector, trigger + Hall-on-trigger position.

### Scenario J — Retrofit replacement (field upgrade)

- Existing motor is a BLDC with Halls only
- New requirement: lower acoustic noise and smoother startup
- Mechanical change: not allowed

**Winner: Keep the motor, upgrade the drive to sinusoidal commutation using Hall interpolation.**
Reason: you cannot run clean FOC on 60° Halls alone, but interpolated sinusoidal commutation between Hall edges is a proven intermediate step that buys ~5–8 dB of noise reduction without touching the motor. This is a realistic field fix.

**Summary — Scenario J:** Family: **BLDC motor retained; drive upgraded to sinusoidal (Hall-interpolated)**. Why it wins: no mechanical change allowed, noise is the target — Hall interpolation gets most of the acoustic benefit. When full PMSM+FOC would win instead: if the mechanical envelope ever opens up and an encoder can be fitted, FOC beats Hall-interpolated sine. Control/feedback: sinusoidal commutation with Hall edge interpolation (time-based angle estimator between Hall transitions). Drive class: mid-range BLDC drive with sine-mode firmware. Wiring: unchanged — same 3 phase leads + existing Hall harness.

*For deep engineering walkthroughs of three archetype scenarios (fan/pump, precision axis, AGV) with per-scenario drive selection, wiring, tuning, and measurement detail, see the [Motor Selection Scenarios]({{ '/fundamentals/motors/motor-selection-scenarios/' | relative_url }}) module.*

---

## Common field failure modes (BLDC vs PMSM-specific)

### BLDC-specific

- Hall sensor alignment drift → commutation wrong → high current, low torque, overheating
- Wrong phase order at install → runs backwards, stalls, or oscillates
- Sensorless BEMF startup fails under load → back-drive or forced alignment needed
- Commutation transient noise coupling into nearby analog sensors

### PMSM-specific

- Encoder offset not calibrated (or lost after replacement) → wrong dq alignment → motor runs hot, max torque unreachable
- Encoder cable noise → position jitter → current jitter → acoustic whine
- Parameter ID wrong (Ld/Lq swapped on IPM) → instability near base speed
- DC-link **overvoltage** during hard regen → with an undersized or missing brake chopper/resistor, returning kinetic energy pushes the bus above OV threshold and the drive trips on the deceleration event

### Shared

- DC bus capacitor aging → ripple rises → overcurrent trips
- Gate driver shoot-through on dv/dt events → MOSFET destruction
- Motor thermistor open-circuit mistaken for cold motor → thermal runaway

---

## What the user should take away

- BLDC and PMSM are the same family; the control strategy and the back-EMF shape define the split.
- Most of the cost, complexity, and capability live in the **drive**, not the motor.
- When the mechanical spec says "servo" — deterministic torque at zero speed, tight position accuracy, or functional safety — **PMSM + FOC + proper feedback** is almost always the right architecture.
- For fans, pumps, propellers, and simple continuous-motion loads, **BLDC 6-step** (or sensorless sinusoidal) is still hard to beat on cost and robustness.
- The middle ground — appliance motors, e-bikes, cordless tools — is **migrating to FOC** as MCU cost drops. The distinction is blurring at the low end; it remains sharp at the industrial-servo end.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/motors/pmsm-reference/' | relative_url }}">&larr; PMSM Motor Reference</a>
  <a href="{{ '/fundamentals/motors/' | relative_url }}">↑ Motors, Drives, and Motion</a>
  <a href="{{ '/fundamentals/motors/bldc-pmsm-implementation/' | relative_url }}">BLDC/PMSM Implementation Guide &rarr;</a>
</div>
