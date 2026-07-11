<!-- TEMPLATE — electrical drawing review checklist for machine/panel
     schematic packages. Adapt to your governing standards and project
     conventions; this is a reviewer's aid, not a compliance determination. -->

# Electrical Drawing Review Checklist

| Project |  | Drawing set / rev |  |
|---|---|---|---|
| Reviewer |  | Date |  |

## Power Distribution

- [ ] Supply voltage/phases/frequency match the design basis
- [ ] Disconnect type, rating, and lockability shown and correct
- [ ] SCCR stated and consistent with the documented available fault current
- [ ] Overcurrent protection: every conductor protected; ratings vs conductor sizes traceable
- [ ] Conductor sizes shown with basis (ampacity + voltage drop where long runs)
- [ ] Motor branch circuits: FLC basis, conductor, OCPD, and overload each shown

## Grounding / Earthing

- [ ] PE/ground bus shown; conductor sizes per governing standard
- [ ] No daisy-chained protective conductors
- [ ] Shield grounding convention stated (which end, where landed)
- [ ] Separately derived sources bonded correctly (CPT, PSU)

## Control Circuits

- [ ] Control voltage source and protection shown
- [ ] Wire colors match the stated convention (and the destination market)
- [ ] Interposing relays where field devices exceed output ratings
- [ ] Fuse/breaker every control circuit; ratings coordinate with wire size

## Safety Circuits

- [ ] Safety functions match the SRS (device, channel count, reset behavior)
- [ ] Safety-rated devices identified as such (not standard relays drawn as safety)
- [ ] Stop categories annotated where relevant
- [ ] E-stop chain coverage matches the machine zones

## Documentation Quality

- [ ] Every device on the drawings appears in the BOM (and vice versa)
- [ ] Wire numbers unique and match the wire schedule
- [ ] Terminal numbers match the terminal schedule
- [ ] Title block: project, drawing number, revision, date complete
- [ ] Revision cloud/triangles match the stated revision

## Findings

| # | Sheet | Finding | Severity | Response |
|---|---|---|---|---|
| 1 |  |  |  |  |
