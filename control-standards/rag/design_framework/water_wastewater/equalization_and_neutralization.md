<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Equalization and Neutralization

## 0. Purpose

Control narrative for industrial wastewater equalization basins and pH neutralization systems. Equalization dampens flow and concentration variations before downstream treatment. Neutralization brings pH within range for biological treatment or direct discharge.

## 1. Equalization Basin Control

The equalization (EQ) basin receives variable-flow, variable-quality industrial wastewater from the facility. Its job is to hold the flow and blend it, then release a steady, consistent flow to downstream treatment.

**Level-based control states:**

| State | Level Range | Action |
|---|---|---|
| Receiving | Any | Influent enters freely (gravity or pumped) |
| Normal Pumping | 40–80% | Transfer pump runs at constant rate setpoint |
| High Level | 80–90% | Alarm, increase transfer pump rate to max |
| High-High Level | > 90% | Alarm, close influent valve if controllable (spill prevention) |
| Low Level | 20–40% | Transfer pump at minimum rate |
| Low-Low Level | < 10% | Stop transfer pump, alarm |

**Mixer control:** Submersible mixers run continuously while basin has > 20% level to prevent solids settlement. Mixers stop below 10% level (suction air entrainment risk).

## 2. pH Neutralization System

Industrial wastewater pH can vary widely (acid wash rinses at pH 2, caustic cleaning at pH 12). Neutralization uses a cascade of 2–3 agitated tanks with reagent dosing at each stage:

**Stage 1 — Coarse neutralization:** Large dose of NaOH (caustic) or H₂SO₄ (sulfuric acid) based on pH analyzer AT-501 at the tank inlet. Setpoint: bring pH to 5–9 range.

**Stage 2 — Fine neutralization:** Small trim dose based on AT-502 at the second tank. Setpoint: 6.5–8.5 (discharge permit range).

**pH PID loop considerations:**
- pH is a nonlinear variable (logarithmic scale) — PID requires gain scheduling or a linearized model
- Residence time in neutralization tank creates dead time — integral windup protection essential
- Sample AT near the outlet, not the inlet to the tank
- Minimum reagent pump flow to prevent crystallization in lines during low-demand periods

**Reagent safety interlocks:**
- Secondary containment high-level float switch — locks out all reagent pumps
- Reagent tank Low-Low level — stops corresponding pump, alarm
- Dosing confirmation flow switch on each reagent line — alarm on no-flow within 30 seconds of pump start

## 3. Effluent pH Monitoring and Discharge Hold

After neutralization, AT-503 (final effluent pH) is the regulatory monitoring point. If pH is outside 6.0–9.0:

1. Close effluent valve to the sewer or receiving water
2. Alarm and page operator
3. Divert to EQ basin for re-treatment
4. Operator must acknowledge and manually reset effluent valve

This is typically a SIL 1 safety instrumented function (SIF) per IEC 61511. The pH trip must have separate safety logic from the process control PID loop.

## 4. Instrumentation List

| Tag | Type | Range | Output | Purpose |
|---|---|---|---|---|
| LT-501 | Submersible pressure transducer | 0–5 m | 4-20mA | EQ basin level |
| AT-501 | pH transmitter (glass electrode) | 0–14 pH | 4-20mA | EQ basin inlet pH |
| AT-502 | pH transmitter | 0–14 pH | 4-20mA | Neutralization stage 2 pH |
| AT-503 | pH transmitter | 0–14 pH | 4-20mA | Final effluent pH (SIF input) |
| FT-501 | Mag flowmeter | 0–200 m³/h | 4-20mA | Transfer pump flow |
| FT-REAGENT | Variable area flowmeter | 0–20 L/min | Local / switch | Reagent dose flow confirmation |
| XV-EFFLUENT | Motor-operated valve | Open/close | DO + DI | Effluent isolation (SIF) |