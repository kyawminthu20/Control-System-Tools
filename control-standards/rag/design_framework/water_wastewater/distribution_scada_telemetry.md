<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Distribution SCADA and Telemetry

## 0. Purpose

Control and communications architecture for municipal water distribution systems: SCADA server, RTUs at remote pump stations and reservoirs, historian, HMI, and cybersecurity zone design per IEC 62443.

## 1. System Architecture

A typical distribution SCADA system has four layers:

| Layer | Components | Protocol |
|---|---|---|
| Field | Sensors, actuators, local control panels | 4-20mA, Modbus RTU, hardwired |
| Site control | PLCs / RTUs at each pump station, reservoir | Modbus TCP or EtherNet/IP (local LAN) |
| SCADA | Central SCADA server, historian, HMI | OPC-UA, Modbus TCP, DNP3 (to remote RTUs) |
| Enterprise | Billing, reporting, lab LIMS | REST API via DMZ, manual export |

Remote sites (booster stations, elevated storage tanks, pressure zones) connect to the SCADA server via dedicated radio, cellular, or fiber WAN. DNP3 is common for RTU-to-SCADA because it supports unsolicited reporting and handles communication gaps gracefully.

## 2. IEC 62443 Security Zone Design

Water distribution SCADA is critical infrastructure. Apply IEC 62443 zone and conduit model:

| Zone | Assets | Security Level |
|---|---|---|
| Zone 0 — Field | Sensors, actuators, valve positioners | SL 1 |
| Zone 1 — Control | PLCs, RTUs, local HMIs | SL 2 |
| Zone 2 — Supervisory | SCADA server, historian, engineering workstation | SL 2 |
| Zone 3 — Enterprise | IT network, billing systems | SL 1 |

Conduit rules:
- Zone 0 → Zone 1: Hardwired or dedicated serial; no IP at Zone 0
- Zone 1 → Zone 2: Firewall with whitelist rules; no direct internet access
- Zone 2 → Zone 3: DMZ with unidirectional data diode for historian export; no inbound from Zone 3 to Zone 2
- Remote access: VPN gateway in Zone 2 DMZ; MFA required; session logging

## 3. Remote Site Telemetry

Each remote site (booster pump station, elevated storage tank, pressure reducing valve vault) runs an RTU or small PLC with:

- Local control capability (runs on last known setpoints if comms fail)
- Heartbeat register updated every 30 seconds
- Unsolicited reporting of alarm states (DNP3 or MQTT to SCADA)
- Local data logging (circular buffer, 7-day minimum) in case of comms outage

SCADA polls each RTU every 10 seconds for analog values; alarm events are unsolicited (reported immediately on state change).

## 4. Communication Failure Fallback

If a remote site stops communicating:

1. **0–60 seconds:** SCADA continues to display last-known values (stale data indicator shown on HMI)
2. **60 seconds:** SCADA generates "Communication Loss" alarm for that site
3. **5 minutes:** SCADA changes site status to "Offline — Local Control Active"
4. **At site:** RTU falls back to local control mode — maintains last setpoints, runs on local timers and local alarms
5. **Recovery:** On comms restoration, RTU syncs time, uploads buffered log, transitions back to remote SCADA control

## 5. Historian and Regulatory Logging

The historian must retain:
- All analog values at 1-minute resolution, minimum 2 years
- All alarm events with timestamp, value, operator acknowledgment — minimum 5 years (EPA Surface Water Treatment Rule)
- Turbidity and Cl₂ residual data with 4-hour rolling average (reportable to state primacy agency)
- System startup/shutdown events

Historian export to the state primacy reporting portal: monthly CSV export, manually triggered or automated via DMZ API.

## 6. Instrumentation List (Distribution)

| Tag | Type | Range | Output | Purpose |
|---|---|---|---|---|
| PT-DIST | Gauge pressure transmitter | 0–1000 kPa | 4-20mA | Distribution zone pressure |
| FT-DIST | Mag flowmeter | 0–2000 m³/h | 4-20mA + pulse | Zone metering |
| LT-TANK | Ultrasonic or float | 0–15 m | 4-20mA | Elevated storage tank level |
| AT-DIST | Amperometric Cl₂ | 0–2 mg/L | 4-20mA | Distribution residual (regulatory) |
| ZSO/ZSC | Limit switches | Open/closed | Digital | PRV and isolation valve position |