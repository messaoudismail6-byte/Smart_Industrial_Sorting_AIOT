# S7-1200 Tag / DB specification

Use these as the engineering specification for the TIA Portal project.

## DB100 `DB_CellControl`

### Inputs
- `ProductPresent` : BOOL
- `WeighingDone` : BOOL
- `Weight_kg` : REAL
- `RobotReady` : BOOL
- `RobotAtPick` : BOOL
- `RobotAtBin` : BOOL
- `VFD_Ready` : BOOL
- `EStop_OK` : BOOL
- `StartPB` : BOOL
- `StopPB` : BOOL
- `ResetPB` : BOOL

### Outputs
- `ConveyorRun` : BOOL
- `ConveyorSpeedPct` : REAL
- `RobotPickRequest` : BOOL
- `RobotBinA` : BOOL
- `RobotBinB` : BOOL
- `RobotBinC` : BOOL
- `RejectRequest` : BOOL
- `CycleComplete` : BOOL
- `AlarmActive` : BOOL

### Classification
- `WeightClass` : INT
  - 1 = < 1 kg
  - 2 = 1–3 kg
  - 3 = 3–5 kg
  - 4 = > 5 kg / reject

## AI data

`DB200 DB_AI`

- `Vibration_RMS` REAL
- `Temperature_C` REAL
- `MotorCurrent_A` REAL
- `CycleTime_s` REAL
- `HealthScore` REAL
- `RiskLevel` INT
- `PredictionValid` BOOL
