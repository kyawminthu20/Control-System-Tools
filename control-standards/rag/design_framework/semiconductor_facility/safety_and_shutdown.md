<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: DERIVED_REFERENCE
CATEGORY: SEMI_FACILITY
-->

# Safety and Shutdown Architecture

## Purpose

This note maps the shutdown layers that commonly appear across semiconductor facility systems.

## Typical shutdown layers

### Layer 1: process or equipment self-protection

- protects the skid, pump, valve train, or analyzer
- examples: dry-run stop, fail-to-open timeout, high motor current

### Layer 2: utility or sequence interlock

- prevents unsafe or invalid operating combinations
- examples: exhaust required, source unavailable, destination not ready

### Layer 3: local hazardous shutdown

- isolates a cabinet, skid, or enclosure on leak, gas detection, or severe process deviation
- usually owned by local logic plus hardwired shutdown paths

### Layer 4: area or facility emergency response

- examples: fire alarm interaction, emergency power off, area gas alarm escalation
- often crosses package boundaries and must have clear ownership

## Core design rules

- safe state must be defined for each hazard scenario, not only for each piece of equipment
- the same input may alarm locally but trip only when a voting, persistence, or zoning rule is met
- hardwired shutdown paths should be documented separately from convenience SCADA alarms
- manual reset rules matter as much as trip rules

## Inputs that frequently participate in shutdown logic

- gas detection
- chemical leak detection
- fire alarm
- EPO or ESD
- exhaust loss
- overpressure or vacuum-loss conditions
- abnormal temperature where materials or chemistry are at risk

## Common output actions

- isolate gas or chemical supply
- stop pump or heater
- maintain or force exhaust
- enable purge
- drop permit-to-run to the tool
- generate local and supervisory alarm

## Documents that should exist

- shutdown hierarchy
- cause and effect matrix
- reset authority table
- proof-test and maintenance note for critical sensors
