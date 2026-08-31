# Dashboard V2

Recommended page structure:

### Overview
Real-time machine state and KPI cards.

### Production
- total cycles
- good parts
- rejects
- throughput
- weight histogram

### Predictive Maintenance
- health score trend
- vibration RMS trend
- temperature trend
- AI confidence
- risk distribution

### Robot
- ready/busy/fault
- pick/place cycle time
- target distribution

### Traceability
Search by cycle ID and display:
weight -> class -> destination -> AI state -> timestamp

### Alarms
Severity:
- INFO
- WARNING
- CRITICAL

Use persistent event IDs and timestamps.
