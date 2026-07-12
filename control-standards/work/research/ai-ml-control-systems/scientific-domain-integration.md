# Scientific Domains and Their Control-System Interfaces

## Core idea

Most control systems act on a scientific process. The controller does not merely
move tags: it changes energy, momentum, mass, charge, chemical composition,
organism state, or environmental exposure. A digital twin can preserve these
causal relationships and give AI models a scientifically meaningful context.

The desired hierarchy is:

```text
governing science and conservation laws
        + validated empirical models
        + synchronized measurements
        + learned residuals or perception
        + uncertainty and operating constraints
        = science-informed digital twin
```

## Domain map

| Science | Real-world state | Typical measurements | Typical manipulated variables | Control/twin examples |
|---|---|---|---|---|
| Mechanics | Position, velocity, stress, vibration, deformation | Encoder, accelerometer, force, strain | Torque, force, motion profile | Motion control, robotics, structural health |
| Fluid dynamics | Flow, pressure, level, velocity field | Flow, pressure, DP, level | Valve position, pump/fan speed | Pipe networks, HVAC, pumping, aerodynamics |
| Thermodynamics and heat transfer | Temperature, phase, energy, heat flux | RTD, thermocouple, IR, calorimetry | Heater power, cooling flow, compression | Furnaces, chillers, batteries, reactors |
| Electromagnetics | Voltage, current, flux, field, charge | CT/PT, Hall sensor, power analyzer | Switching, excitation, converter duty | Motors, drives, power electronics, plasma |
| Chemistry | Concentration, reaction rate, equilibrium, pH, redox | Analyzer, spectroscopy, pH, conductivity | Feed rate, dosing, temperature, pressure | Reactors, water treatment, combustion |
| Electrochemistry | State of charge, potential, ion transport, degradation | Voltage, current, impedance, temperature | Charge/discharge current, cooling | Batteries, fuel cells, electrolysis |
| Biology | Biomass, metabolism, physiological state, population response | Optical, biochemical, image, gas uptake | Nutrients, light, temperature, gas, flow | Bioprocesses, agriculture, medical devices |
| Microbiology | Growth, inhibition, contamination, community state, biofilm | OD, ATP, microscopy, sequencing proxies | Sterilization, nutrients, pH, oxygen | Fermentation, wastewater, clean systems |
| Space/environmental science | Radiation, vacuum, plasma, orbital/solar environment | Dosimeter, vacuum gauge, particle/field sensor | Shielding state, thermal mode, orientation | Spacecraft, vacuum tools, radiation facilities |

## Coupled interfaces matter most

Real systems normally cross scientific boundaries:

- **Thermal-fluid:** heat changes density and viscosity; flow changes heat transfer.
- **Reaction-transport:** mixing and diffusion determine where chemistry occurs.
- **Electro-thermal:** electrical losses produce heat; temperature changes resistance
  and device life.
- **Electrochemical-thermal-mechanical:** battery reactions, heat, swelling, and
  degradation interact.
- **Biochemical:** organisms change chemistry while chemistry changes growth.
- **Microbial-fluid-surface:** transport, attachment, biofilm growth, and cleaning
  interact across different time scales.
- **Radiation-material-electronic:** exposure changes materials and electronics,
  creating accumulated and event-driven effects.

The interface variables—flux, concentration, energy, force, charge, population,
and boundary conditions—must be explicit in the twin. Otherwise separate models
may each look correct while their coupled prediction is wrong.

## Role of AI inside scientific twins

### Learn what is difficult to observe

- CNNs extract state from images, spectra, waveforms, or spatial fields.
- Estimators infer unmeasured state from available instruments.
- PINNs and hybrid models combine governing equations with sparse data.

### Learn what first-principles models omit

- A learned residual can correct a known model within a validated operating region.
- Surrogates can approximate an expensive solver for faster scenario evaluation.
- Data-driven models can represent uncertain kinetics or degradation when the
  limits and provenance are explicit.

### Connect people to the science

- LLMs can retrieve assumptions, equations, operating history, and evidence.
- They can explain which scientific model and sensor evidence support a result.
- They should not invent boundary conditions, material properties, kinetics, or
  biological behavior when those inputs are absent.

## Time- and length-scale problem

A single twin may span:

- Microseconds: power-electronic switching and fast electrical transients
- Milliseconds/seconds: motion, pressure, flow, and basic regulatory control
- Minutes/hours: thermal soaking, reactions, batches, and organism response
- Days/months/years: fouling, corrosion, aging, ecology, and radiation dose

Research must determine which model runs online, which runs asynchronously, and
which only supports design or planning. Not every scientific model belongs in a
PLC scan or even in the live operational loop.

## Model-evidence ledger

Each twin component should eventually record:

- Scientific domain and modeled phenomenon
- Governing equations or causal assumptions
- Boundary and initial conditions
- Material, chemical, or biological parameters and their sources
- Empirical correlations and valid ranges
- Learned components, datasets, and feature definitions
- Calibration state and uncertainty
- Spatial and temporal resolution
- Coupling variables and interface ownership
- Numerical solver and convergence criteria
- Validation experiments and acceptance limits
- Known invalid regimes and fallback behavior

## Research questions

- What scientific state truly determines the controlled outcome?
- Which variables can be sensed directly, and which must be inferred?
- Which conservation laws constrain the model?
- Which interface dominates uncertainty or instability?
- Are biological or chemical dynamics time-varying, adaptive, or population-based?
- What scale separation is valid, and when does it break down?
- Can a reduced-order model retain the behavior required for control?
- How does uncertainty propagate across coupled models?
- Which predictions may influence operation, and which remain research/advisory?
- How will real-world experiments falsify or recalibrate the twin?

