<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Filtration and Clarification

## 0. Purpose

Control narrative and engineering reference for gravity filtration, pressure filtration, and sedimentation/clarification in water treatment. Covers the filter run/backwash cycle, turbidity-driven backwash initiation, coagulant dosing integration, and filter-to-waste logic.

## 1. System Description

Water treatment filtration removes suspended solids (floc, particulates, organisms) from clarified water. Common configurations:

- **Rapid gravity filters:** Open concrete beds with sand/anthracite media. Backwashed with air scour + water. Most common in municipal plants.
- **Pressure filters:** Enclosed vessels for smaller systems. Same backwash concept, higher operating pressure.
- **Lamella clarifiers / plate settlers:** Inclined plates or tubes for enhanced sedimentation before filtration.

## 2. Filter Run / Backwash State Machine

A filter cycles through defined states. The PLC state machine manages transitions:

| State | Entry Condition | Exit Condition |
|---|---|---|
| Standby | Manual stop or maintenance | Start command received |
| Filtering | Start command; turbidity OK | dP > setpoint OR time elapsed OR turbidity spike |
| Backwash Initiate | Backwash trigger | Filter effluent valve closed, BW supply open |
| Air Scour | BW supply confirmed | Air scour time complete (typ. 3–5 min) |
| Backwash | Air scour complete | BW flow confirmed, time elapsed (typ. 8–12 min) |
| Rinse | Backwash complete | Filter-to-waste turbidity < 1 NTU |
| Return to Service | Rinse complete | Filter effluent valve opens |

Backwash initiation triggers (any one sufficient):
1. Filter differential pressure > 2.5 m H₂O (head loss accumulation)
2. Filter run time > 24 hours (time-based fallback)
3. Filtered water turbidity > 0.3 NTU (quality-based)

## 3. Turbidity Control Logic

Turbidity is the primary effluent quality indicator in filtration. The control strategy:

**Normal operation:** Turbidity analyzer AT-201 on the filter effluent stream monitors online. Alarm at 0.3 NTU. Trip at 1.0 NTU — filter isolated from clearwell until turbidity clears.

**Backwash trigger on spike:** If AT-201 rises from baseline by > 0.2 NTU in 15 minutes, initiate backwash sequence. Spike indicates media breakthrough or media disturbance.

**Filter-to-waste:** After backwash, effluent is routed to waste (not clearwell) until turbidity drops below 0.2 NTU for 5 consecutive minutes. This prevents backwash water (high TSS) from contaminating the clearwell.

## 4. Coagulant Integration

Upstream coagulant dosing (alum or PAC — see chemical dosing module) directly affects filter performance:

- Under-dosing: Poor floc formation, higher filter loading, shorter runs
- Over-dosing: Excess alum carryover, clearwell pH impact

Jar test results from the lab set the coagulant dose ratio (mg/L per NTU of raw water). The SCADA historian records coagulant dose vs. filtered water turbidity to allow operators to trend and optimize.

## 5. Protection Trips and Alarms

| Tag | Condition | Action |
|---|---|---|
| AT-201 | Filtered turbidity > 1.0 NTU | Close filter effluent valve, alarm, route to waste |
| PDT-201 | Filter head loss > 3.0 m | Alarm — initiate backwash |
| FT-BW | Backwash flow < 80% of setpoint | Alarm — check BW pump/valve |
| LT-BW | Backwash tank Low-Low | Alarm — defer backwash until tank refills |

## 6. Instrumentation List

| Tag | Type | Range | Output | Purpose |
|---|---|---|---|---|
| AT-201 | Nephelometric turbidimeter | 0–10 NTU | 4-20mA | Filter effluent turbidity |
| PDT-201 | Differential pressure transmitter | 0–5 m H₂O | 4-20mA | Filter head loss |
| FT-BW | Mag flowmeter | 0–600 m³/h | 4-20mA | Backwash supply flow |
| LT-BW | Ultrasonic level | 0–5 m | 4-20mA | Backwash tank level |
| AT-RAW | Nephelometric turbidimeter | 0–1000 NTU | 4-20mA | Raw water turbidity (coagulant dose input) |