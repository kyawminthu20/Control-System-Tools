<!-- GENERATED EXAMPLE — demonstrates the format produced by the cst toolkit from the example I/O list. Adapt to your project and review before use. -->

# Loop Test Sheet — PT-401

| Project | Example Skid | Loop / drawing | _______ |
|---|---|---|---|
| Description | Discharge pressure | I/O type / signal | AI / 4-20mA |
| Device | pressure transmitter | Address | 0/3/0 |
| Location | skid east | Cabinet | CP-01 |

## Pre-checks

- [ ] Wiring per schedule (wire numbers, terminals, tightness)
- [ ] Shield landed at panel end only (analog)
- [ ] Instrument datasheet range matches configuration

## Function test

| Step | Stimulus | Expected | As-found | As-left | Pass |
|---|---|---|---|---|---|
| 1 | Inject 4.0 mA at field device terminals | HMI/PLC reads 0 % of range |  |  | ☐ |
| 2 | Inject 8.0 mA at field device terminals | HMI/PLC reads 25 % of range |  |  | ☐ |
| 3 | Inject 12.0 mA at field device terminals | HMI/PLC reads 50 % of range |  |  | ☐ |
| 4 | Inject 16.0 mA at field device terminals | HMI/PLC reads 75 % of range |  |  | ☐ |
| 5 | Inject 20.0 mA at field device terminals | HMI/PLC reads 100 % of range |  |  | ☐ |

## Sign-off

| Role | Name | Signature | Date |
|---|---|---|---|
| Technician |  |  |  |
| Witness |  |  |  |

Notes: 0-10 bar
