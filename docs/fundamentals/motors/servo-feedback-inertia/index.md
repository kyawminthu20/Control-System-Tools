---
layout: training-module
title: "Servo Feedback and Inertia Matching"
description: "This module explains two practical servo concepts that strongly affect stability and motion quality: feedback devices and inertia matching."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "Motors, Drives, and Motion"
    url: "/fundamentals/motors/"
repo_path: "control-standards/rag/training_modules/electrical_machines/servo_feedback_and_inertia_matching.md"
redirect_from:
  - /fundamentals/electrical-machines/servo-feedback-inertia/
  - /fundamentals/electrical-machines/servo-feedback-inertia/index.html

---

## Purpose

This module explains two practical servo concepts that strongly affect stability and motion quality:

- feedback devices
- inertia matching

## Why feedback matters

Servo systems depend on feedback for:

- position
- speed
- direction

Common feedback devices:

- incremental encoders
- absolute encoders
- resolvers

Incorrect feedback setup can cause:

- wrong direction
- poor position accuracy
- unstable control
- startup problems

## Inertia matching concept

Servo performance depends partly on the ratio:

`load inertia / motor inertia`

A very large ratio makes the system harder to control and can reduce stability.

Ratios below roughly 10:1 are a common rule-of-thumb target. Treat that as a practical heuristic, not a universal standard.

## Why inertia ratio matters

Poor inertia matching can contribute to:

- oscillation
- sluggish response
- harder tuning
- overshoot
- mechanical stress during aggressive moves

## Practical review questions

1. Is the feedback device correctly matched to the drive and motor?
2. Is the feedback direction correct?
3. Is the mechanical load disproportionately large for the selected motor?
4. Is the tuning problem really a configuration problem?

## Practical takeaway

Many "servo tuning" problems are not just tuning problems. They may be caused by:

- wrong encoder setup
- poor inertia ratio
- backlash
- resonance
- mechanical binding

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/motors/motor-vfd-equations/' | relative_url }}">&larr; Motor and VFD Equations Reference</a>
  <a href="{{ '/fundamentals/motors/' | relative_url }}">↑ Motors, Drives, and Motion</a>
  <span></span>
</div>
