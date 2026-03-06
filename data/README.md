# Data
**AI_READ_ACCESS: ALLOWED (context-dependent)**

Optional datasets including PLC exports, network captures, and historian data.

## Contents

### plc_exports/
Exported PLC programs, tag databases, I/O configurations
- Formats: .L5X (Logix), .ACD, CSV tag exports, etc.

### network_captures/
Network traffic captures for troubleshooting
- Formats: .PCAP, .PCAPNG
- Use for EtherNet/IP, EtherCAT, PROFINET analysis

### historian_exports/
Process data exports from historians
- Formats: CSV, Excel
- Use for trending, analysis, troubleshooting

## Usage Notes
- Sanitize data before committing (remove customer-specific info if necessary)
- Large files may be stored externally and linked
- Data here supplements troubleshooting and design work in /rag/
