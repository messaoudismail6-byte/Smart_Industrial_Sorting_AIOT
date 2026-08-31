# Recruiter / Interview Demo

## 5-minute demonstration

### 00:00 — Architecture
Explain PLC, HMI, ESP32, MQTT, Node-RED, AI, Robot and Factory I/O.

### 01:00 — Normal production
Start AUTO mode.
Show:
- product detection
- weight
- classification
- robot pick/place
- counters

### 02:00 — AI
Inject vibration increase.
Show:
- telemetry
- AI health decline
- WARNING
- recommendation

### 03:00 — Fault handling
Set RobotReady = FALSE.
Show that the PLC waits safely for the handshake.

### 04:00 — Overweight
Introduce >5 kg product.
Show automatic REJECT.

### 05:00 — Analytics
Show OEE, reject rate, traceability and AI trend.

## Interview questions to prepare

### Why PLC + AI?
PLC provides deterministic control; AI provides probabilistic prediction.

### Why ESP32?
Low-cost distributed acquisition and rapid prototyping for non-safety telemetry.

### Why MQTT?
Lightweight publish/subscribe architecture for IIoT telemetry.

### Why Factory I/O?
Digital-twin simulation reduces commissioning risk and demonstrates logic before hardware deployment.

### What would you change for production?
Use industrial sensors/gateways, managed networking, TLS/authentication, validated safety, industrial robot interface, OPC UA where appropriate, historian, model monitoring and formal commissioning.
