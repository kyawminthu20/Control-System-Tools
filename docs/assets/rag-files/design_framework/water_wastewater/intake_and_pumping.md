<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Intake and Raw Water Pumping

## 0. Purpose

Control narrative and engineering reference for raw water intake screens, wet wells, and raw water pump stations feeding a water treatment plant. Covers pump start permissives, VFD control, level-based sequencing, and common protection trips.

## 1. System Description

A raw water pump station lifts water from a source (river, reservoir, lake) through a traveling screen or bar screen into a wet well, then pumps it to the treatment plant headworks. Key control elements:

- Traveling screen with motorized drive and differential pressure measurement
- Wet well with level measurement (ultrasonic or submersible pressure transducer)
- 2–4 vertical turbine or centrifugal pumps, typically VFD-driven
- Discharge header with pressure transmitter and check valves
- Suction isolation and discharge isolation valves

## 2. Pump Start Permissive Logic

Before any raw water pump can start, all permissives must be satisfied:

| Permissive | Tag Example | Trip Condition |
|---|---|---|
| Wet well level > Low-Low | LT-101 | < 1.5 m — prevents dry running |
| Suction pressure > minimum | PT-101 | < 15 kPa — suction loss trip |
| VFD ready | VFD-101 Status | Fault present — inhibit start |
| Discharge isolation valve open | ZSO-101 | Valve not confirmed open |
| Motor winding temperature OK | TE-101 | > 120°C — thermal protection |

All permissives are hardwired to the motor control circuit AND mirrored to the PLC for SCADA visibility.

## 3. VFD Speed Control

Raw water pumps use a flow demand signal (from the treatment plant headworks flow meter FT-201) as the primary setpoint. The PLC runs a PID loop:

- **PV:** Headworks flow FT-201 (m³/h)
- **SP:** Target production flow (operator setpoint, typically 60–100% of rated)
- **MV:** VFD speed reference (0–60 Hz)
- **Min speed:** 20 Hz (to prevent sedimentation in suction pipe)
- **Ramp:** 5 Hz/s acceleration, 3 Hz/s deceleration

If flow demand falls below minimum pump flow, the pump steps to the next stage down (multi-pump sequencing) rather than running at minimum speed.

## 4. Multi-Pump Sequencing Logic

Duty/assist/standby sequencing:
1. Lead pump runs to max speed (58 Hz) before assist pump starts
2. Assist pump starts at minimum speed and ramps up
3. If both pumps are at max and flow is still insufficient, operator alarm (no automatic addition beyond 2 pumps without operator action)
4. Standby pump: auto-starts on lead pump fault, lead/lag rotation every 24 hours

## 5. Protection Trips

| Trip | Condition | Action |
|---|---|---|
| Wet well Low-Low | LT-101 < 0.8 m | Stop all pumps immediately |
| Discharge pressure High-High | PT-201 > 700 kPa | Stop pump, alarm — check discharge isolation |
| Motor overcurrent | OL relay | Stop pump, lockout, alarm |
| Traveling screen high dP | PDT-101 > 25 kPa | Alarm — initiate screen wash cycle |
| Loss of suction pressure | PT-101 < 10 kPa | Stop pump, delay 30 s, retry once, then lockout |

## 6. Instrumentation List

| Tag | Instrument Type | Range | Output | Purpose |
|---|---|---|---|---|
| LT-101 | Submersible pressure transducer | 0–5 m | 4-20mA | Wet well level |
| FT-101 | Mag flowmeter | 0–1500 m³/h | 4-20mA + pulse | Raw water flow |
| PT-101 | Gauge pressure transmitter | 0–200 kPa | 4-20mA | Suction pressure |
| PT-201 | Gauge pressure transmitter | 0–1000 kPa | 4-20mA | Discharge header pressure |
| PDT-101 | Differential pressure transmitter | 0–50 kPa | 4-20mA | Screen differential pressure |
| TE-101 | RTD (Pt100) | 0–150°C | 4-wire | Motor winding temperature |
| ZSO-101 | Limit switch | Open/closed | Digital | Discharge valve open feedback |