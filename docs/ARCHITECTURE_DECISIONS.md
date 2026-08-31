# Architecture Decision Records

## ADR-001 — PLC remains authoritative
**Decision:** AI never directly controls safety-critical outputs.

**Reason:** deterministic control, diagnosability and safety separation.

## ADR-002 — MQTT for telemetry
**Decision:** ESP32 publishes telemetry through MQTT.

**Reason:** decoupling, lightweight transport and easy integration with Node-RED.

## ADR-003 — Edge AI
**Decision:** prediction service runs locally.

**Reason:** low latency, operation without cloud dependency and data minimization.

## ADR-004 — Factory I/O digital twin
**Decision:** simulation is part of the engineering workflow.

**Reason:** supports logic validation, demonstration and fault injection.

## ADR-005 — Recipe-driven classification
**Decision:** weight limits are data, not hard-coded process logic.

**Reason:** easier product changeover and maintainability.
