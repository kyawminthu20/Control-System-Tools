<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NFPA
STANDARD_ID: NFPA_79
EDITION: 2024

NFPA_HIERARCHY:
  chapter: "10"
  chapter_title: "Operator Interface and Control Devices"

INDEX_TAGS:
  topics: ["operator_interface", "pushbuttons", "hmi"]
-->


## 0. Purpose

The purpose of Chapter 10 is to standardize the physical characteristics and functional behavior of operator interfaces. By mandating specific colors and locations, the standard reduces the likelihood of "human error," such as an operator accidentally pressing a "Cycle Start" button when they intended to hit a "Stop" button.

## 1. Control Device Requirements

This section defines the "visual language" of the machine. NFPA 79 is very specific about color-coding for pushbuttons and indicator lights:

### Pushbutton Color Logic

| Color | Meaning | Typical Use |
| --- | --- | --- |
| **RED** | Emergency / Stop | Emergency Stop, Power Off. |
| **YELLOW** | Abnormal | Return to safe state, intervention required. |
| **GREEN** | Normal / Start | Cycle start, power on. |
| **BLUE** | Mandatory | Reset functions. |
| **BLACK/WHITE/GRAY** | No specific meaning | Jogging, auxiliary functions. |

### Device Construction

* **Durability:** Devices must be suitable for the environment (e.g., oil-tight for CNC machines, wash-down rated for food processing).
* **Legend Plates:** Every control device must be clearly labeled with its function (e.g., "PUMP START"). Symbols can be used but should follow international standards (ISO/IEC).
* **Positive Action:** Emergency stop buttons must be of the "direct opening action" type, ensuring that the internal contacts are mechanically forced apart when the button is pressed.

## 2. Ergonomics and Safety

The physical layout of the interface is just as important as the wiring behind it.

* **Prevention of Accidental Operation:** Buttons that initiate hazardous motion (like a "Start" button) must be guarded, shrouded, or recessed to prevent them from being bumped by an elbow or a passing cart.
* **E-Stop Accessibility:** As mentioned in previous chapters, the E-Stop must be "readily accessible" and located at every operator station and any other location where a hazard might be initiated.
* **Foot Switches:** If used, they must be protected (e.g., with a cowl or hood) to prevent accidental activation by falling objects or accidental stepping.
* **HMI (Touchscreen) Limits:** While HMIs are allowed, they cannot be the *sole* means of Emergency Stopping. A physical, hard-wired E-stop button is always required. Furthermore, critical safety functions should not rely solely on touchscreen "buttons" that might lag or become unresponsive.

