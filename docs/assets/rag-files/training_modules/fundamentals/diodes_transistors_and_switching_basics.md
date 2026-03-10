<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: FUNDAMENTALS
MODULE_ID: diodes_transistors_and_switching_basics
LEARNING_LEVEL: foundational

INDEX_TAGS:
  topics: ["diodes", "leds", "zeners", "transistors", "mosfets", "igbts", "switching"]
  systems: ["electrical_circuits", "control_interfaces"]
-->

# Diodes, Transistors, and Switching Basics

## 0. Purpose

This module gives a practical introduction to one-way devices and basic semiconductor switching elements.

## 1. Diodes

The simplest diode idea is directional behavior:

- forward direction conducts
- reverse direction blocks

Important practical checks:

- polarity
- forward current rating
- reverse-voltage rating

## 2. Common diode families

- signal diodes
- rectifier diodes
- Schottky diodes
- LEDs
- zener diodes

Each family is optimized for a different electrical job.

## 3. LEDs and zeners

- LEDs are diodes intended to emit light and require current limiting.
- Zeners are used where controlled reverse breakdown is useful as a simple reference or clamp function.

## 4. Transistor basics

Transistors are often introduced first as switches.

Common practical device groups:

- BJT
- MOSFET
- IGBT

The detailed physics differs, but the everyday engineering question is usually:

- what signal turns it on
- what load it must switch
- what voltage and current it must survive

## 5. Switching takeaway

When choosing a switching device, check:

- polarity or orientation
- device type
- load current
- voltage stress
- heat dissipation

## 6. Working caution

These devices are easy to simplify too much.

Use datasheets and application context before treating a transistor as a generic black box.
