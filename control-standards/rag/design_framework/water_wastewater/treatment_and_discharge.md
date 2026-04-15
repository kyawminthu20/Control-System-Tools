<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Treatment and Discharge Compliance

## 0. Purpose

Control narrative for biological wastewater treatment (activated sludge and MBR), secondary clarification, effluent disinfection, and discharge permit compliance logic. Covers permit limit trip logic, effluent diversion, and EPA CWA NPDES compliance record-keeping.

## 1. Treatment Train Overview

The standard activated sludge treatment train:

1. **Primary clarification** — gravity settling; removes 50–70% of TSS, 30–40% of BOD. Sludge to digester.
2. **Aeration / biological treatment** — aerobic bacteria consume dissolved organics. DO setpoint 2.0 mg/L. Blower control via dissolved oxygen (DO) PID loop.
3. **Secondary clarification** — bacteria settle as activated sludge. Return activated sludge (RAS) is pumped back to aeration basin. Waste activated sludge (WAS) is sent to thickening/dewatering.
4. **Tertiary filtration** — polishing (sand or membrane) to meet low TSS permit limits.
5. **Disinfection** — UV or chlorination to meet effluent fecal coliform limits.

**MBR (membrane bioreactor)** replaces secondary clarifier + tertiary filtration with submerged membranes in the aeration basin. Permeate is disinfected directly. MBR requires transmembrane pressure (TMP) monitoring and periodic membrane backpulse and chemical clean-in-place (CIP).

## 2. Dissolved Oxygen (DO) Control — Aeration

The aeration blowers supply air to diffusers in the biological basin. DO control loop:

- **PV:** DO analyzer AT-601 (optical or galvanic cell), measured near mid-basin outlet
- **SP:** 2.0 mg/L (typical; adjusted seasonally)
- **MV:** Blower speed (VFD, 0–60 Hz) or inlet vane position
- **Cascade:** Multiple blowers with lead/lag logic; lead blower VFD-modulated, assist blower staged on/off

DO below 1.0 mg/L causes filamentous bulking (poor settleability). DO above 4.0 mg/L is energy waste with no treatment benefit.

## 3. Return and Waste Activated Sludge (RAS/WAS)

- **RAS:** Continuous pump from secondary clarifier underflow to aeration basin inlet. Rate typically 50–100% of influent flow. Controlled manually or by sludge blanket level in clarifier.
- **WAS:** Periodic wasting to maintain mixed liquor suspended solids (MLSS) at target (2,000–4,000 mg/L). SCADA calculates daily WAS volume based on MLSS, SRT (solids retention time), and influent TSS. Operator approves WAS event.

## 4. Effluent Quality Monitoring

Online analyzers monitor the final effluent continuously:

| Parameter | Analyzer | Typical Permit Limit | Action on Exceedance |
|---|---|---|---|
| TSS | Optical turbidity/TSS | 30 mg/L (monthly avg) | Alarm, increase polymer dose |
| pH | pH transmitter | 6.0–9.0 SU | Trip — close effluent valve |
| Dissolved Cl₂ | Amperometric | < 0.1 mg/L (post-dechlorination) | Alarm — check dechlorination |
| DO (effluent) | Optical DO | > 5.0 mg/L (some permits) | Alarm |

Lab grab samples confirm online analyzers weekly. SCADA provides composite sampler trigger signals (time-proportional or flow-proportional).

## 5. Discharge Permit Trip Logic

If any parameter exceeds its permit limit continuously for > 10 minutes:

1. SCADA closes effluent isolation valve XV-601
2. SCADA activates effluent diversion pump — sends flow back to equalization basin (if capacity available) or to emergency storage
3. SCADA generates a regulatory exceedance alarm event — logged with timestamp, parameter, value, duration
4. Operator must acknowledge; if EQ basin is full, operator must contact regulatory agency per permit conditions
5. XV-601 remains closed until manually reset by operator after parameter returns to compliance

This is a SIL 1 function (per IEC 61511): single-channel pH trip with independent alarm on the same sensor, or 2oo3 voting for higher-criticality permits.

## 6. NPDES Compliance Record-Keeping

The SCADA historian must log:
- All effluent analyzer values at 15-minute intervals (minimum)
- All exceedance events with start/stop time and duration
- Composite sampler trigger log (for lab sample chain of custody)
- Blower run hours and sludge wasting events
- Permit limit exceedance notifications sent (for DMR — Discharge Monitoring Report)

Monthly DMR is submitted to the EPA or state primacy agency. SCADA generates the data; permit holder reviews and submits.

## 7. Instrumentation List

| Tag | Type | Range | Output | Purpose |
|---|---|---|---|---|
| AT-601 | Optical DO sensor | 0–20 mg/L | 4-20mA | Aeration basin DO (blower control) |
| AT-602 | Online TSS/turbidity | 0–500 mg/L | 4-20mA | Final effluent TSS |
| AT-603 | pH transmitter | 0–14 pH | 4-20mA | Final effluent pH (trip SIF) |
| AT-604 | Amperometric Cl₂ | 0–2 mg/L | 4-20mA | Residual chlorine (post-dechlor) |
| FT-601 | Mag flowmeter | 0–500 m³/h | 4-20mA + pulse | Final effluent flow (NPDES reporting) |
| XV-601 | Motor-operated valve | Open/close | DO + DI | Effluent isolation (SIF) |
| LT-SC | Sludge blanket detector | 0–5 m | 4-20mA | Secondary clarifier sludge blanket |