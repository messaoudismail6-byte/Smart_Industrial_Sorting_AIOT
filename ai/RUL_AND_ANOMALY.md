# Advanced AI — Anomaly Detection + RUL

## Anomaly Detection

Isolation Forest identifies telemetry combinations that deviate from the learned healthy operating distribution.

Features:
- vibration RMS
- temperature
- motor current
- cycle time

Output:
- anomaly boolean
- anomaly score
- health score

## Remaining Useful Life (RUL)

The V4 architecture adds an RUL estimation interface.

**Important:** the included RUL value is a portfolio demonstration/proxy, not a certified maintenance prediction. A real RUL model should be trained on machine-specific run-to-failure or degradation data.

Recommended production pipeline:

```text
Historian
  ↓
Feature engineering
  ↓
Healthy baseline
  ↓
Anomaly detection
  ↓
Degradation trend
  ↓
RUL model
  ↓
Maintenance work order
```
