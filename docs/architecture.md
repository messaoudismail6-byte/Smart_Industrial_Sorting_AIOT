# System architecture

```mermaid
flowchart LR
  S[Product / Factory I/O] --> P[Presence Sensor]
  P --> PLC[S7-1200 PLC]
  ESP[ESP32 Sensors] --> MQTT[MQTT Broker]
  MQTT --> NR[Node-RED]
  NR --> AI[Edge AI Prediction API]
  AI --> NR
  NR --> HMI[Dashboard / HMI]
  PLC --> ROB[6-Axis Robot]
  ROB --> A[Bin A]
  ROB --> B[Bin B]
  ROB --> C[Bin C]
  PLC --> VFD[VFD + Conveyor]
  PLC <--> FIO[Factory I/O]
```

## Control philosophy

The PLC controls the deterministic sequence. ESP32 and Node-RED provide telemetry and IIoT services. AI produces advisory health/risk information. The robot executes validated pick-and-place commands. Factory I/O provides a digital twin for simulation.
