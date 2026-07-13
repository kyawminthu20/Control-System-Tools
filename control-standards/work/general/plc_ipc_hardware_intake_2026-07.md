# PLC and IPC Product Families: Siemens, Allen-Bradley, and Beckhoff

**Portfolio status: July 11, 2026.**

The vendors divide their hardware differently:

* **Siemens:** dedicated PLCs, software PLCs, virtual PLCs, and separate SIMATIC IPC families.
* **Allen-Bradley:** dedicated Logix controllers, one hybrid Logix/Windows controller, and separate ASEM industrial computers.
* **Beckhoff:** PC-based control. A CX Embedded PC or C/CP Industrial PC becomes the PLC when TwinCAT runtime is installed.

---

# 1. Overall product-family map

| Application class      | Siemens                                           | Allen-Bradley                                                        | Beckhoff                                                        |
| ---------------------- | ------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------- |
| Logic relay            | LOGO!                                             | Micro810                                                             | BC/BX controller                                                |
| Small PLC              | S7-1200 / S7-1200 G2                              | Micro820, Micro850                                                   | CX7000, CX8000, CX8100                                          |
| Medium machine PLC     | S7-1200 G2, ET 200SP CPU                          | Micro870, CompactLogix 5380                                          | CX8200, CX9240, CX5100                                          |
| High-performance PLC   | S7-1500                                           | CompactLogix 5380/5390                                               | CX5200, CX5300, CX5600                                          |
| Large plant controller | S7-1500                                           | ControlLogix 5580/5590                                               | CX20x2, CX20x3, C60xx/C66xx IPC                                 |
| Integrated safety      | F-CPU / TF-CPU                                    | GuardLogix / Compact GuardLogix                                      | TwinSAFE with TwinCAT controller                                |
| Advanced motion        | S7-1500T/TF, Drive Controller                     | CompactLogix/ControlLogix with Kinetix                               | CX/C-series with TwinCAT Motion                                 |
| Redundant control      | S7-1500 R/H                                       | ControlLogix redundancy                                              | TwinCAT redundancy architecture                                 |
| PLC plus Windows       | S7-1500S on SIMATIC IPC; ET 200SP Open Controller | CompactLogix 5480                                                    | CX or C-series IPC with TwinCAT                                 |
| Virtual PLC            | S7-1500V                                          | No direct production equivalent in the main Logix hardware portfolio | TwinCAT runtime on virtualized/supported computing architecture |
| Box IPC                | SIMATIC Box PC                                    | ASEM 6300B                                                           | C60xx, C65xx, C69xx, C66xx                                      |
| Panel IPC              | SIMATIC Panel PC                                  | ASEM 6300P/6300PA                                                    | CP2xxx–CP7xxx                                                   |
| Rack IPC               | SIMATIC Rack PC                                   | VersaVirtual/industrial server architecture                          | C5xxx, C6670                                                    |

---

# 2. Siemens controller families

```text
SIMATIC Controllers
│
├── Logic modules
│   └── LOGO!
│
├── Basic Controllers
│   ├── S7-1200
│   └── S7-1200 G2
│
├── Advanced Controllers
│   └── S7-1500
│       ├── Standard CPU
│       ├── F-CPU
│       ├── T-CPU
│       ├── TF-CPU
│       └── R/H CPU
│
├── Distributed Controllers
│   ├── ET 200SP CPU
│   ├── ET 200SP Open Controller
│   └── ET 200pro CPU
│
├── Drive Controllers
│   ├── CPU 1504D TF
│   └── CPU 1507D TF
│
├── Software Controllers
│   └── S7-1500S
│
└── Virtual Controllers
    └── S7-1500V
```

Siemens officially positions S7-1200 G2 as its compact basic-controller platform and S7-1500 as its advanced controller. The portfolio also includes distributed, software-based, redundant, drive-integrated, and virtual controller forms. ([Siemens][1])

## 2.1 Siemens PLC families

| Family                       | Hardware form                                         | Typical application                                                      | Main engineering environment   |
| ---------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------ |
| **LOGO!**                    | Compact logic module                                  | Small pumps, lighting, building systems, simple machines                 | LOGO! Soft Comfort             |
| **S7-1200**                  | Compact DIN-rail PLC                                  | Small standalone machines                                                | TIA Portal                     |
| **S7-1200 G2**               | Newer compact DIN-rail PLC                            | Compact machines with improved communication, motion, and safety options | TIA Portal                     |
| **S7-1500**                  | Modular cabinet PLC                                   | Medium and large machines, production lines and process skids            | TIA Portal                     |
| **S7-1500 F**                | Fail-safe S7-1500                                     | Integrated standard and safety control                                   | TIA Portal Safety              |
| **S7-1500 T**                | Technology CPU                                        | Advanced synchronized motion and kinematics                              | TIA Portal                     |
| **S7-1500 TF**               | Technology plus fail-safe CPU                         | Motion-intensive machinery with integrated safety                        | TIA Portal Safety              |
| **S7-1500 R/H**              | Redundant CPU pair                                    | High-availability process and infrastructure systems                     | TIA Portal                     |
| **ET 200SP CPU**             | CPU integrated into distributed I/O station           | Distributed machines and limited cabinet space                           | TIA Portal                     |
| **ET 200pro CPU**            | IP65/67 machine-mounted controller                    | Conveyors and decentralized control outside a cabinet                    | TIA Portal                     |
| **ET 200SP Open Controller** | PC-based controller plus local I/O                    | PLC, Windows application and visualization in one device                 | TIA Portal plus PC software    |
| **SIMATIC Drive Controller** | S7-1500 TF CPU plus integrated SINAMICS drive control | High-performance servo and coordinated-motion machines                   | TIA Portal/Startdrive          |
| **S7-1500S**                 | Software controller on an IPC                         | Real-time PLC plus Windows or high-level applications                    | TIA Portal                     |
| **S7-1500V**                 | Virtual PLC                                           | Centrally managed, software-defined automation                           | TIA Portal and Industrial Edge |

S7-1500 R/H uses synchronized controllers for high availability. The ET 200SP and ET 200pro controller families place processing near the distributed I/O. The Drive Controller combines a fail-safe technology CPU with SINAMICS drive control. ([Siemens][2])

### Siemens suffix meanings

| Suffix   | Meaning                                              |
| -------- | ---------------------------------------------------- |
| **F**    | Fail-safe                                            |
| **T**    | Technology CPU with advanced motion                  |
| **TF**   | Technology and fail-safe                             |
| **R**    | Redundant system                                     |
| **H**    | High-availability redundant system                   |
| **S**    | Software controller                                  |
| **V**    | Virtual PLC                                          |
| **D TF** | Drive-integrated technology and fail-safe controller |

## 2.2 Older Siemens controllers

| Family          | Status/role                                                          |
| --------------- | -------------------------------------------------------------------- |
| **S7-300**      | Large installed base; migration path is generally S7-1500            |
| **S7-400**      | Large process and high-availability installed base                   |
| **ET 200S CPU** | Older distributed-controller generation                              |
| **WinAC**       | Older PC-based control generation, replaced conceptually by S7-1500S |

Siemens states that the S7-300/ET 200M family remains available until 2033, but S7-1500 and ET 200MP are the normal modernization direction. ([Siemens][3])

---

# 3. Siemens IPC families

```text
SIMATIC Industrial Computing
│
├── Box PCs
├── Panel PCs
├── Rack PCs
├── Industrial monitors
├── Mobile engineering devices
└── Industrial IoT gateways
```

Siemens organizes its IPC portfolio primarily by physical form: **box, panel and rack PCs**. ([Siemens][4])

## 3.1 SIMATIC Box PCs

A Box PC has no integrated operator display. It is installed in a cabinet, behind a panel or near the machine.

| Product group               | Representative families/models      | Typical use                                        |
| --------------------------- | ----------------------------------- | -------------------------------------------------- |
| IoT gateway                 | **SIMATIC IOT2050**                 | Protocol gateway, data collection, edge processing |
| Entry-level compact         | **IPC BX-21A, IPC227G, IPC327G**    | HMI runtime, gateway, monitoring                   |
| Midrange                    | **BX-32A, BX-35A, BX-39A, IPC527G** | HMI, machine control, data logging                 |
| Performance                 | **BX-53B, BX-54A, BX-56A, IPC627E** | Vision, control, analytics                         |
| High-performance expandable | **BX-59A**                          | Machine vision, GPU/AI, complex PC-based control   |

Siemens currently lists the IOT2050, BX-series systems and IPC227G through IPC627E product classes in its Box PC portfolio. ([Siemens][5])

## 3.2 SIMATIC Panel PCs

A Panel PC combines the computer and display into one device.

| Family/model   | General position                     |
| -------------- | ------------------------------------ |
| **IPC277G**    | Compact fanless panel PC             |
| **IPC377G**    | Entry/midrange industrial panel PC   |
| **IPC PX-32A** | Current compact-performance platform |
| **IPC PX-39A** | Higher-performance panel platform    |
| **IPC677E**    | Expandable high-performance panel PC |

The current Panel PC portfolio includes IPC277G, IPC377G, PX-32A, PX-39A and IPC677E, with panel-mounted and selected fully protected configurations. ([Siemens][6])

## 3.3 SIMATIC Rack PCs

| Class                 | Current families/models                      | Purpose                                                      |
| --------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| **Client class**      | RC-543B, RC-545A                             | SCADA clients, monitoring and basic PC applications          |
| **Workstation class** | RW-543B, RW-545A, IPC647E, IPC847E, IPC1047E | Engineering, vision, simulation, large SCADA                 |
| **Server class**      | RS-545A, RS-828A                             | Virtualization, redundant storage, high-compute applications |

Siemens separates its rack systems into client, workstation and server classes. ([Siemens][7])

## 3.4 Siemens IPC versus Siemens PLC

```text
Dedicated S7 PLC
    ├── Deterministic CPU
    ├── No general-purpose Windows workload
    └── Best for conventional machine/process control

SIMATIC IPC + S7-1500S
    ├── Real-time software PLC
    ├── Windows applications
    ├── HMI, vision or data processing
    └── PLC remains protected from Windows restart/failure

SIMATIC IPC + S7-1500V
    ├── Virtual PLC deployment
    ├── Centralized lifecycle management
    └── Software-defined automation
```

S7-1500S provides S7-1500 functionality on an industrial PC and is designed to continue control during an operating-system restart or failure. S7-1500V is hardware-independent and deployed through Siemens Industrial Edge. ([Siemens][8])

---

# 4. Allen-Bradley controller families

```text
Allen-Bradley Controllers
│
├── Micro Control
│   └── Micro800
│
├── Compact Control
│   ├── CompactLogix 5380
│   ├── Compact GuardLogix 5380
│   ├── CompactLogix 5480
│   └── CompactLogix 5390
│
└── Chassis-based Control
    ├── ControlLogix 5580
    ├── GuardLogix 5580
    └── ControlLogix 5590
```

## 4.1 Micro800 family

| Controller   | Relative position                                   | Typical use                                    |
| ------------ | --------------------------------------------------- | ---------------------------------------------- |
| **Micro810** | Smallest logic controller                           | Relays, timers, small standalone equipment     |
| **Micro820** | Small networked controller                          | Building utilities, pumps, remote equipment    |
| **Micro850** | Expandable micro PLC                                | Small machines and skids                       |
| **Micro870** | Highest-capacity Micro800                           | Larger standalone machines and distributed I/O |
| **Micro830** | Older member; affected catalog numbers discontinued | Older standalone machine applications          |

Rockwell currently promotes Micro810, Micro820, Micro850 and Micro870 starter architectures. Rockwell identifies Micro830 LC30 catalog numbers as discontinued and recommends migration toward Micro820 or newer Micro850 controllers. ([Rockwell Automation][9])

### Important Micro800 distinction

Micro800 uses:

```text
Connected Components Workbench
or FactoryTalk Design Workbench
```

It does **not** use the same Studio 5000 project format as CompactLogix and ControlLogix. Therefore, Micro800 is not simply a smaller Logix 5000 controller.

---

# 5. CompactLogix families

## 5.1 CompactLogix 5380

| Variant                           | Function                                                    |
| --------------------------------- | ----------------------------------------------------------- |
| **CompactLogix 5380**             | Standard machine and skid controller                        |
| **Compact GuardLogix 5380 SIL 2** | Integrated safety, SIL 2 class                              |
| **Compact GuardLogix 5380 SIL 3** | Higher-integrity integrated safety                          |
| **CompactLogix process variants** | Process-focused firmware/features and PlantPAx-oriented use |

The 5380 family uses Compact 5000 I/O locally and supports integrated networking, motion and safety depending on the controller model. ([Rockwell Automation][10])

## 5.2 CompactLogix 5480

The 5480 is unusual because it includes two distinct operating environments:

```text
CompactLogix 5480
│
├── Logix real-time control engine
│   ├── Ladder
│   ├── Structured Text
│   ├── Motion
│   └── EtherNet/IP control
│
└── Windows 10 IoT Enterprise
    ├── HMI
    ├── Analytics
    ├── Custom applications
    └── Third-party software
```

The Windows commercial operating system runs in parallel with, and independently from, the Logix control engine. ([Rockwell Automation][11])

## 5.3 CompactLogix 5390

CompactLogix 5390 is the next compact-controller generation. Rockwell describes it as a high-performance, reduced-footprint controller using local PointMax I/O. However, it is **announced for availability in the fourth quarter of calendar year 2026**, so it is not yet a normal shipping replacement for 5380 as of July 11, 2026. ([Rockwell Automation][12])

---

# 6. ControlLogix families

## 6.1 ControlLogix 5590

ControlLogix 5590 is the newest chassis-based family.

| Configuration | Application                                           |
| ------------- | ----------------------------------------------------- |
| Standard      | Discrete, motion, process and multidiscipline control |
| Safety        | Integrated safety applications                        |
| Redundant     | High-availability systems                             |
| Logix SIS     | Process safety-instrumented-system applications       |

Rockwell states that the 5590 is configurable for standard, safety, redundancy and Logix SIS applications. The chassis architecture permits combinations of controllers, network modules and I/O interfaces. ([Rockwell Automation][13])

## 6.2 ControlLogix 5580 and GuardLogix 5580

| Family                                                  | Purpose                                          |
| ------------------------------------------------------- | ------------------------------------------------ |
| **ControlLogix 5580**                                   | Large machine, plant, process and motion control |
| **GuardLogix 5580**                                     | Standard plus integrated safety                  |
| **ControlLogix 5580 Process**                           | Process-control-focused platform                 |
| **ControlLogix 5580 Redundant**                         | High-availability controller pair                |
| **Extreme-temperature and conformally coated variants** | Harsh industrial environments                    |
| **No Stored Energy variants**                           | Specialized controlled-energy applications       |

The 5580 remains an important current platform even after the introduction of the 5590. ([Rockwell Automation][14])

## 6.3 Older Logix families

| Family                     | Position                                                     |
| -------------------------- | ------------------------------------------------------------ |
| **ControlLogix 5570**      | Previous chassis-based generation                            |
| **CompactLogix 5370**      | Previous compact generation; migration commonly targets 5380 |
| **CompactLogix 1768/1769** | Older CompactLogix platforms                                 |
| **SLC 500**                | Legacy modular PLC                                           |
| **PLC-5**                  | Legacy large controller                                      |
| **MicroLogix**             | Legacy small PLC family                                      |

Rockwell notes that some CompactLogix 5370 controllers are discontinued and directs users toward CompactLogix 5380. ([Rockwell Automation][15])

---

# 7. Allen-Bradley IPC families

```text
Allen-Bradley / ASEM Industrial Computing
│
├── 6300B Box PCs
├── 6300P Panel PCs
├── 6300PA On-Machine PCs
├── 6300T Thin Clients
├── 6181X Hazardous-location PCs
├── 6300M Panel Monitors
├── 6300MA On-Machine Monitors
└── VersaVirtual Appliance
```

Rockwell positions these products around FactoryTalk software, ThinManager, visualization, IIoT gateways, data logging and industrial computing. ([Rockwell Automation][16])

## 7.1 ASEM 6300B Box PCs

| Subfamily/example    | Position                                          |
| -------------------- | ------------------------------------------------- |
| **6300B Atom class** | Entry HMI, gateway and data logging               |
| **6300B-JB1**        | Compact box PC                                    |
| **6300B-EW1**        | Configurable general industrial box PC            |
| **6300B-SB0**        | Book-mount box PC                                 |
| **6300B-SW0/TW0**    | Wall-mount higher-performance PC                  |
| **6300B-SW2**        | Current performance-class box PC with ECC options |

## 7.2 ASEM 6300P Panel PCs

| Family        | Position                                |
| ------------- | --------------------------------------- |
| **6300P-EW1** | Cost-effective panel PC                 |
| **6300P-SW0** | Higher-performance low-profile panel PC |
| **6300P-SW2** | Current performance-class panel PC      |
| **6300PA**    | On-machine IP-rated panel PC            |

## 7.3 Thin clients and monitors

| Product    | Function                                            |
| ---------- | --------------------------------------------------- |
| **6300T**  | ThinManager-ready box thin client                   |
| **6300M**  | Panel-mounted industrial monitor                    |
| **6300MA** | Machine-mounted industrial monitor                  |
| **6181X**  | Display and non-display PCs for hazardous locations |

The 6300T is not normally a full local HMI server. It is a terminal that receives centrally managed applications through ThinManager or related remote-display architecture. The 6300M and 6300MA are monitors rather than computers. ([Rockwell Automation][17])

## 7.4 VersaVirtual

VersaVirtual is an industrialized, preconfigured virtualization appliance rather than a PLC. It is used to consolidate multiple industrial software workloads onto managed compute, networking and storage infrastructure. ([Rockwell Automation][17])

---

# 8. Beckhoff controller philosophy

Beckhoff does not draw a hard line between a PLC and an IPC.

```text
Beckhoff hardware
        +
TwinCAT real-time runtime
        =
PLC / motion controller / CNC / robot controller
```

The main control hardware classes are:

```text
Beckhoff Controllers
│
├── BC/BX Bus Terminal Controllers
├── CX Embedded PCs
├── C-series Industrial PCs
└── CP-series Panel PCs
```

Beckhoff explicitly describes the CX range as combining Industrial PC and hardware-PLC characteristics, from small Arm controllers to multi-core Xeon systems. ([Beckhoff Automation][18])

---

# 9. Beckhoff BC and BX controllers

| Family     | Position                                   | Typical use                                                   |
| ---------- | ------------------------------------------ | ------------------------------------------------------------- |
| **BCxxxx** | Bus coupler with integrated PLC capability | Small decentralized fieldbus controller                       |
| **BXxxxx** | More memory and interfaces than BC         | Larger decentralized controller or intelligent fieldbus slave |

These controllers combine local Bus Terminals with an integrated control runtime. BX controllers are positioned between BC controllers and CX Embedded PCs. ([Beckhoff Automation][19])

They remain relevant for installed systems, but new TwinCAT 3 projects more commonly use CX-series hardware.

---

# 10. Beckhoff CX Embedded PC families

```text
CX Embedded PCs
│
├── Compact / entry
│   ├── CX7000
│   ├── CX8000
│   ├── CX8100
│   └── CX8200
│
├── General compact
│   ├── CX9020
│   └── CX9240
│
├── Midrange x86
│   ├── CX5100
│   ├── CX5200
│   ├── CX5300
│   └── CX5600
│
└── High performance
    ├── CX20x3
    └── CX20x2
```

## 10.1 CX family comparison

| Family     | Processor class                      | Relative position                       | Typical application                                        |
| ---------- | ------------------------------------ | --------------------------------------- | ---------------------------------------------------------- |
| **CX7000** | Compact Arm-based class              | Low-cost TwinCAT 3 controller           | Small machines and local automation                        |
| **CX8000** | Compact fieldbus-specific controller | Entry decentralized controller          | Local fieldbus and I/O control                             |
| **CX8100** | Improved compact controller          | Small machine controller                | Distributed machines                                       |
| **CX8200** | Arm Cortex-A53 class                 | Modern compact controller               | Machine, building and utility control                      |
| **CX9020** | Arm Cortex-A8                        | Established compact Ethernet controller | General machine control                                    |
| **CX9240** | Modern Arm Cortex-A53                | Newer universal compact controller      | General automation                                         |
| **CX5100** | Intel Atom multicore                 | Midrange fanless controller             | PLC, HMI and modest motion                                 |
| **CX5200** | More efficient modular x86           | Midrange modular control                | Machine and motion applications                            |
| **CX5300** | Higher-performance Atom x6           | Upper midrange                          | More demanding PLC/HMI/motion                              |
| **CX5600** | AMD Ryzen two-core                   | High-performance compact controller     | Fast machinery and data-heavy applications                 |
| **CX20x3** | AMD Ryzen two/four-core              | High-performance modular CX             | Large PLC and motion systems                               |
| **CX20x2** | Intel Xeon D, up to 12 cores         | Highest CX performance class            | Large motion, CNC, visualization and multi-runtime control |

These are the current CX families listed by Beckhoff. The CX20xx class occupies the top of the DIN-rail embedded-controller range. ([Beckhoff Automation][18])

## 10.2 CX hardware flow

```text
CX CPU
  │
  ├── Directly attached EtherCAT or Bus Terminals
  │
  ├── Ethernet/EtherCAT networks
  │
  ├── Optional fieldbus/interface modules
  │
  └── TwinCAT runtime
       ├── PLC
       ├── Motion
       ├── CNC
       ├── Robotics
       ├── Safety communication
       └── HMI/data applications
```

The ability to attach I/O directly to the right side of the CX eliminates a separate coupler for local I/O and creates a compact DIN-rail controller. ([Beckhoff Automation][18])

---

# 11. Beckhoff C-series Industrial PCs

```text
Beckhoff Industrial PCs
│
├── C60xx ultra-compact
├── C65xx fanless built-in
├── C69xx compact
├── C70xx machine-mounted IP65
├── C5xxx 19-inch rack
├── C66xx expandable cabinet PCs
└── C6670 industrial server
```

## 11.1 C-series comparison

| Family    | Physical design                       | Typical use                                          |
| --------- | ------------------------------------- | ---------------------------------------------------- |
| **C60xx** | Ultra-compact cabinet PC              | PLC, motion, vision, IoT and machine control         |
| **C65xx** | Fanless built-in PC                   | Installation behind a panel or console               |
| **C69xx** | Compact aluminum cabinet PC           | General scalable machine control                     |
| **C70xx** | Ultra-compact IP65 machine-mounted PC | Cabinet-free local computing                         |
| **C5xxx** | 19-inch rack PC                       | Plant engineering, SCADA and high-compute workloads  |
| **C66xx** | ATX-based expandable cabinet PC       | PCI/PCIe cards, vision and specialized hardware      |
| **C6670** | Industrial server                     | High-performance server and virtualization workloads |

Beckhoff’s current IPC overview identifies the C60xx, C65xx, C69xx, C70xx, C5xxx, C66xx and C6670 classes. ([Beckhoff Automation][20])

## 11.2 C60xx internal performance groups

| Group     | Relative role                                                    |
| --------- | ---------------------------------------------------------------- |
| **C601x** | Atom-class compact control and IoT                               |
| **C602x** | Fanless midrange Atom/Core U class                               |
| **C603x** | High-performance Core class                                      |
| **C604x** | Highest-performance compact class, including GPU-capable options |

The C60xx series ranges from small IoT and automation systems to high-performance control and graphics applications. ([Beckhoff Automation][21])

---

# 12. Beckhoff Panel PC families

| Family              | Display/control design              | Position                                 |
| ------------------- | ----------------------------------- | ---------------------------------------- |
| **CP2xxx**          | Built-in multi-touch                | Current machine panel PCs                |
| **CP3xxx**          | IP65 multi-touch                    | Machine-mounted panel PCs                |
| **CP4xxx**          | New-generation built-in multi-touch | Newer panel platform                     |
| **CP5xxx**          | New-generation IP65 multi-touch     | Newer machine-mounted platform           |
| **CP6xxx**          | Built-in single-touch               | Established resistive-touch platform     |
| **CP7xxx**          | IP65 single-touch                   | Machine-mounted resistive-touch platform |
| **CPX27xx/CPX37xx** | Hazardous-area panel PCs            | Zone 2/22 applications                   |

Beckhoff currently lists CP2xxx/CP3xxx multi-touch, CP4xxx/CP5xxx next-generation multi-touch, CP6xxx/CP7xxx single-touch and CPX hazardous-area families. ([Beckhoff Automation][22])

---

# 13. Direct PLC-family comparison

| System size                    | Siemens                              | Allen-Bradley                                      | Beckhoff                              |
| ------------------------------ | ------------------------------------ | -------------------------------------------------- | ------------------------------------- |
| Very small                     | LOGO!                                | Micro810                                           | BC/BX or CX7000                       |
| Small networked machine        | S7-1200 G2                           | Micro820/Micro850                                  | CX8200/CX9240                         |
| Medium machine                 | S7-1500 compact CPU or ET 200SP CPU  | CompactLogix 5380                                  | CX5100/CX5200                         |
| Complex machine                | S7-1500                              | CompactLogix 5380/5390                             | CX5300/CX5600                         |
| Large multidiscipline system   | S7-1500 high-performance CPU         | ControlLogix 5590                                  | CX20x3/CX20x2 or C60xx                |
| High-performance motion        | S7-1500T/TF or Drive Controller      | CompactLogix/ControlLogix plus Kinetix             | CX20xx/C60xx plus TwinCAT Motion      |
| Integrated PLC and PC workload | S7-1500S or ET 200SP Open Controller | CompactLogix 5480                                  | CX or C-series IPC                    |
| Virtualized controller         | S7-1500V                             | Primarily conventional Logix hardware architecture | TwinCAT PC-based runtime architecture |

---

# 14. Direct IPC-family comparison

| Form factor                 | Siemens                                   | Allen-Bradley                   | Beckhoff                       |
| --------------------------- | ----------------------------------------- | ------------------------------- | ------------------------------ |
| IoT gateway                 | IOT2050                                   | 6300B entry configurations      | C601x or CX compact controller |
| Compact box PC              | BX-21A, IPC227G/327G                      | 6300B-JB1, Atom-class 6300B     | C60xx                          |
| General box PC              | BX-32A through BX-56A                     | 6300B-EW1/SW0/SW2               | C69xx                          |
| Expandable box PC           | BX-59A, IPC627E                           | Higher-end 6300B configurations | C66xx                          |
| Integrated-display PC       | IPC277G/377G/PX/677E                      | 6300P                           | CP2xxx/CP4xxx/CP6xxx           |
| Machine-mounted IP-rated PC | SIMATIC PRO Panel PC variants             | 6300PA                          | CP3xxx/CP5xxx/CP7xxx or C70xx  |
| Hazardous-location PC       | Selected certified SIMATIC configurations | 6181X                           | CPX27xx/CPX37xx                |
| Rack PC/server              | RC/RW/RS and IPC647E–1047E                | VersaVirtual architecture       | C5xxx/C6670                    |

---

# 15. Product-selection flow chart

```text
START
  │
  ├── Is only simple Boolean/timer control required?
  │       │
  │       ├── Siemens: LOGO!
  │       ├── Allen-Bradley: Micro810
  │       └── Beckhoff: BC/BX or CX7000
  │
  ├── Is it a small standalone networked machine?
  │       │
  │       ├── Siemens: S7-1200 G2
  │       ├── Allen-Bradley: Micro850/Micro870
  │       └── Beckhoff: CX8200/CX9240
  │
  ├── Is integrated motion or machine safety required?
  │       │
  │       ├── Siemens: S7-1500 F/T/TF
  │       ├── Allen-Bradley: Compact GuardLogix 5380
  │       └── Beckhoff: CX5200+ with TwinCAT Motion/TwinSAFE
  │
  ├── Is it a large multidiscipline or plant-wide system?
  │       │
  │       ├── Siemens: S7-1500 or S7-1500 R/H
  │       ├── Allen-Bradley: ControlLogix 5590
  │       └── Beckhoff: CX20xx or high-performance C-series IPC
  │
  ├── Must Windows applications run beside real-time control?
  │       │
  │       ├── Siemens: S7-1500S on SIMATIC IPC
  │       │             or ET 200SP Open Controller
  │       ├── Allen-Bradley: CompactLogix 5480
  │       └── Beckhoff: CX/C/CP hardware with TwinCAT
  │
  └── Is virtualization or centralized software-defined control required?
          │
          ├── Siemens: S7-1500V
          ├── Allen-Bradley: controller plus separate virtualization infrastructure
          └── Beckhoff: TwinCAT PC-based/virtualized architecture
```

---

# 16. The most important architectural difference

## Siemens

```text
Dedicated PLC platform
      +
Separate industrial PC platform
      +
Software/virtual PLC options connecting the two
```

Siemens provides the clearest separation between traditional hardware PLC, industrial PC, software PLC and virtual PLC.

## Allen-Bradley

```text
Dedicated Logix controller
      +
EtherNet/IP modular architecture
      +
Separate FactoryTalk/ASEM computer platform
```

The exception is CompactLogix 5480, which places a Windows computer and independent Logix control engine in the same device.

## Beckhoff

```text
Industrial computer
      +
Real-time TwinCAT runtime
      =
Controller
```

For Beckhoff, the CPU form factor and performance change, but the fundamental PC-based control philosophy remains consistent from compact CX controllers to large C-series Industrial PCs.

[1]: https://www.siemens.com/en-us/products/simatic/controller-configurator/ "SIMATIC Controller Selection Guide | Find the Right PLC"
[2]: https://www.siemens.com/en-us/products/simatic/s7-1500-rh-cpus/ "SIMATIC S7-1500 R/H CPUs - High Availability"
[3]: https://www.siemens.com/en-us/products/simatic/s7-300/ "SIMATIC S7-300"
[4]: https://www.siemens.com/en-us/products/simatic-industrial-computing/ "SIMATIC Industrial Computing | Siemens"
[5]: https://www.siemens.com/en-us/products/simatic-industrial-computing/box-pc/ "SIMATIC Box PC"
[6]: https://www.siemens.com/en-us/products/simatic-industrial-computing/panel-pc/ "SIMATIC Panel PC"
[7]: https://www.siemens.com/en-us/products/simatic-industrial-computing/rack-pc/ "SIMATIC Rack PC"
[8]: https://www.siemens.com/en-us/products/simatic/s7-1500s-controller/ "SIMATIC S7-1500 Software Controller"
[9]: https://www.rockwellautomation.com/en-us/capabilities/industrial-automation-control/micro-control.html "Micro Control Systems | Rockwell Automation | US"
[10]: https://www.rockwellautomation.com/en-us/products/hardware/programmable-controllers/compactlogix-5380-controllers.html "CompactLogix 5380 Controllers Allen‑Bradley"
[11]: https://www.rockwellautomation.com/en-us/products/hardware/programmable-controllers.html "PLC/PAC Controllers Allen‑Bradley"
[12]: https://literature.rockwellautomation.com/idc/groups/literature/documents/pp/5390-pp001_-en-p.pdf "CompactLogix 5390 Controller"
[13]: https://www.rockwellautomation.com/en-us/support/documentation/technical/programmable-controllers/controllogix-and-guardlogix-control-systems/controllogix-5590.html "ControlLogix 5590 Controller Technical Resources"
[14]: https://www.rockwellautomation.com/en-us/products/hardware/programmable-controllers/1756controllogix5580.html "ControlLogix 5580 Controllers Allen‑Bradley"
[15]: https://www.rockwellautomation.com/en-us/products/hardware/programmable-controllers/compactlogix-5370-controllers.html "CompactLogix 5370 Controllers Allen‑Bradley"
[16]: https://www.rockwellautomation.com/en-us/products/hardware/industrial-computers-monitors.html "Industrial Computers and Monitors | Rockwell Automation | US"
[17]: https://www.rockwellautomation.com/en-us/products/hardware/industrial-computers-monitors.html "Industrial Computers and Monitors Allen‑Bradley"
[18]: https://www.beckhoff.com/en-us/products/ipc/embedded-pcs/ "Embedded PCs - Modular DIN rail industrial PCs | Beckhoff USA"
[19]: https://www.beckhoff.com/en-us/products/i-o/bus-terminals/ "Bus Terminals - The modular fieldbus system for automation"
[20]: https://www.beckhoff.com/en-us/products/ipc/pcs/ "Industrial PCs | Beckhoff USA"
[21]: https://www.beckhoff.com/en-us/products/ipc/pcs/c60xx-ultra-compact-industrial-pcs/ "C60xx | Ultra-compact Industrial PCs"
[22]: https://www.beckhoff.com/en-us/products/ipc/panel-pcs/ "Panel PCs"


# PLC and IPC Official Reference Library

I created a structured Excel reference index with direct official links for:

* **Siemens:** LOGO!, S7-1200, S7-1200 G2, S7-1500, safety, motion, redundancy, ET 200, software controllers and SIMATIC IPCs.
* **Allen-Bradley / Rockwell:** Micro800, CompactLogix, Compact GuardLogix, ControlLogix, GuardLogix, I/O, Logix programming manuals and ASEM industrial computers.
* **Beckhoff:** TwinCAT programming, libraries, EtherCAT, CX Embedded PCs, EtherCAT terminals, C-series IPCs and CP-series Panel PCs.

The workbook contains four worksheets:

1. **Start Here** — official master portals and model-number lookup process.
2. **Siemens**
3. **Allen-Bradley**
4. **Beckhoff**

Each reference includes the product family, document type, official document title, publication/manual number, coverage, direct URL and design notes.

Exact terminal diagrams usually depend on the complete order number or catalog number. The workbook therefore includes Siemens SiePortal and its TIA controller documentation index, Rockwell’s family documentation hubs and Literature Library, and Beckhoff’s InfoSys and Download Finder. ([Siemens SiePortal][1])

(Workbook relocated to `planning/PLC_IPC_Official_Reference_Links.xlsx`.)

[1]: https://sieportal.siemens.com/en-ww/home "Home - Siemens SiePortal"


