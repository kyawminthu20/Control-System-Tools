---
layout: default
title: "Lifecycle — Safety Wiring Practices"
description: "Practical safety wiring reference: 24 VDC rationale, NC contact logic, wire gauge, color coding, termination, and dual-channel input specification."
redirect_from:
  - /verification/safety-wiring/
  - /lifecycle/safety-wiring/index.html
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "Safety Wiring"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle — Safety Wiring</span>
  <h1>Safety Wiring Practices</h1>
  <p>Practical wiring reference for dual-channel safety inputs on industrial machines. Applies at Detailed Design and is verified during Pre-Commissioning.</p>
</div>

## Why This Matters

For a dual-channel safety input, wiring choices directly affect whether the safety function achieves its target PL or SIL. The architecture (Category 3 / 4) only works when:

- both channels are physically separate
- fault detection (short-circuit, wire break, cross-channel) is possible
- terminations are mechanically reliable under machine conditions

---

## 1. Voltage — Use 24 VDC for Safety Control Circuits

Standards do not mandate a specific voltage for safety logic. In practice:

> **99% of modern machine safety circuits use 24 VDC.**

| Voltage | Typical Use | Notes |
|---------|------------|-------|
| **24 VDC** | Machine safety control (industry standard) | SELV — IEC 61140 |
| 48 VDC | Robotics / telecom / battery systems | Safety I/O rarely rated for this |
| 120 VAC | Legacy machinery only | Avoid in new designs |

### Why 24 VDC

| Reason | Explanation |
|--------|------------|
| **SELV** | Safety Extra Low Voltage (IEC 61140) — low shock hazard, safer wiring |
| **Device ecosystem** | E-stops, safety PLCs, light curtains, interlocks all rated 24 VDC |
| **Diagnostics** | Safety PLC test pulses require low-voltage DC signaling |
| **Cross-fault detection** | Short-to-24V and short-to-0V detectable at this level |

**Important:** 24 VDC is the safety *logic* voltage. Motor power remains 208/480 VAC. The safety PLC controls isolation devices (contactors, STO), not the power circuit itself.

---

## 2. Contact Type — NC, Held Closed

For hardwired safety devices (E-stops, gate interlock switches, rope pulls, limit switches in safety functions):

- Use **2 NC (normally closed) channels**
- Both channels **closed in the safe (running) state**
- Opening either channel causes a safety demand (stop)

### Why NC, Not NO

This is the **fail-safe default**:

| Condition | NC behavior | Result |
|-----------|------------|--------|
| Device actuated (E-stop pressed) | Contact opens | Safety demand — correct |
| Wire break | Circuit opens | Safety demand — fail-safe |
| Device fails open | Circuit opens | Safety demand — fail-safe |

A broken wire looks identical to a genuine safety demand. The machine stops. This is the correct fail-safe behavior.

**Exception:** OSSD outputs (optical safety sensors, light curtains) are electronic and sit high in the healthy state — different signaling model, but same fail-safe principle.

---

## 3. Dual-Channel Separation

For Category 3 / 4 or PL d / e designs, the two channels must be kept physically separate all the way back to the safety controller.

```
T0 (test pulse 1) → E-stop NC contact 1 → Safety Input SI0
T1 (test pulse 2) → E-stop NC contact 2 → Safety Input SI1
```

**Never do this:**

```
24V → jumper → both contacts → tied together → one input pair
```

That defeats diagnostics. The safety controller cannot detect:
- short between channels
- short to 24 V
- short to 0 V
- welded contact

### What the Controller Detects

Safety PLC test pulses (typically 1 ms wide, offset between channels) enable detection of:

| Fault | Detection Method |
|-------|-----------------|
| Short between CH1 and CH2 | Different pulse patterns per channel |
| Short to 24 V | Pulse drops not observed |
| Short to 0 V | Input held low regardless of contact state |
| Wire break | Input stays low when contact should be closed |
| Welded contactor | Auxiliary NC feedback stays open after output de-energizes |

---

## 4. Discrepancy Time

Safety controllers allow a short timing difference between Channel 1 and Channel 2 switching.

| Setting | Purpose |
|---------|---------|
| **Discrepancy time** | Maximum allowed delay between CH1 and CH2 state change |
| **Input filter time** | Debounce period per channel |

### Practical Starting Point

| Device Type | Typical Discrepancy Setting |
|-------------|----------------------------|
| Mechanical NC contacts, one actuator | 20–100 ms |
| OSSD dual-channel sensors | Per manufacturer spec (often shorter) |

- Start with **20–100 ms** for mechanical devices, then adjust based on actual hardware behavior
- Do not set it large without justification — it reduces diagnostic sharpness
- Wire length mismatch is not the issue; mechanical contact travel and controller filtering are

---

## 5. Wire Gauge

Current in safety input circuits is typically tiny (a few milliamps for test pulses). Wire size is driven by mechanical robustness, not load current.

| Location | Recommended | Notes |
|----------|------------|-------|
| **Panel wiring** | **18 AWG stranded copper** | Default for machine control |
| Panel, longer runs or harsh env | 16 AWG | Larger terminal compatibility |
| Pre-made cordsets | 20 AWG | Only if manufacturer terminal range supports it |

Reference: NFPA 79, IEC 60204-1 Clause 12 (wire sizing rules for machine control circuits).

---

## 6. Insulation Rating

Even at 24 VDC, use wire with a higher insulation rating.

| Requirement | Recommendation |
|-------------|---------------|
| **Panel wire** | 600 V rated machine-control wire (MTW / TEW) |
| **Field cable** | Rated for routing environment (flex, oil, coolant, tray) |
| **VFD proximity** | Cable rated for VFD-induced noise; route separately from motor leads |

The insulation rating is chosen for panel practice, routing alongside higher-voltage conductors, and mechanical / chemical durability — not just signal voltage.

---

## 7. Color Coding

Follow NFPA 79 / UL 508A machine wiring color conventions consistently.

| Color | Meaning |
|-------|---------|
| **Blue** | Ungrounded DC control conductors (24 VDC safety circuits) |
| **Red** | Ungrounded AC control conductors |
| **Green** or **Green/Yellow** | Protective earth (PE) |
| **Orange** | Conductors that remain energized when main disconnect is off |
| **Orange / Blue stripe** | DC conductors that remain energized when disconnect is off |
| **White / Blue stripe** | Grounded DC return (varies by convention and jurisdiction) |

For 24 VDC safety input loops:
- Use **blue** for the ungrounded 24 VDC safety feed conductors
- Label CH1 and CH2 clearly at both ends
- If the safety circuit remains live with the main disconnect off (e.g., safety bus kept energized), use the appropriate "always energized" color

Do not invent a custom color code on machines maintained by other people.

---

## 8. Termination and Vibration

On machines with vibration, shock, moving cable tracks, hydraulic power units, pumps, or fans — termination quality is part of safety reliability.

| Location | Best Practice |
|----------|--------------|
| **Panel — general** | Spring-clamp terminals or screw terminals with ferrules |
| **Panel — safety I/O** | Follow safety controller manufacturer terminal requirements exactly |
| **Field device connections** | Ferrules where accepted; otherwise per device manufacturer spec |
| **Vibrating structures** | Clamp cable jacket (not just conductors), use strain relief |

**Ferrule guidance:**
- Crimp ferrules on all stranded conductors before insertion into screw or cage-clamp terminals
- Do not insert loose fine-strand wire under a clamp plate unless the terminal is explicitly designed for it
- Spring-clamp terminals (e.g., Phoenix Contact, Weidmuller PUSH IN) are inherently vibration-resistant and maintenance-free

---

## Baseline Dual-Channel Input Specification

Reference specification for a standard hardwired 24 VDC safety input on an industrial machine:

| Parameter | Specification |
|-----------|--------------|
| **Voltage** | 24 VDC |
| **Contact type** | Dual NC, positive-opening safety contacts |
| **Channel separation** | Separate CH1 and CH2 conductors — never paralleled |
| **Wire gauge** | 18 AWG stranded copper (typical default) |
| **Insulation** | 600 V machine-control rated, suitable for environment |
| **Color** | Blue (ungrounded DC control); orange where always-energized |
| **Termination** | Ferrules + spring terminals or torque-controlled screw terminals |
| **Discrepancy time** | 20–100 ms starting point, tuned per device and controller |
| **Input configuration** | Dual-channel equivalent, pulse test, cross-short detection, manual reset |
| **Device certification** | Published PFHd / B10d data; positive-opening NC contacts |

---

## Standards Referenced

| Standard | Topic |
|----------|-------|
| **NFPA 79** | Machine electrical wiring, conductor color coding (US) |
| **IEC 60204-1** | Machine electrical equipment, conductor sizing (international) |
| **IEC 61140** | SELV definition (24 VDC justification) |
| **ISO 13849-1** | Category 3/4 requirements, CCF, DC requirements |
| **IEC 62061** | Dual-channel subsystem architecture, PFHD |

## See Also

- [Safety Architecture — Lifecycle Stage 4]({{ '/lifecycle/safety-architecture/' | relative_url }})
- [Detailed Design — Lifecycle Stage 5]({{ '/lifecycle/detailed-design/' | relative_url }})
- [Scenario 06 — Practical Machine Safety Implementation]({{ '/tools/scenarios/machine-safety-implementation/' | relative_url }})
