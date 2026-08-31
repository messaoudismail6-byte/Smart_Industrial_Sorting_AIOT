# TIA Portal Engineering Package — V4

## Target
Siemens S7-1200 CPU 1214C class controller.

## Suggested program blocks

```text
OB1_Main
 ├── FB10_SafetyPermissives
 ├── FB20_Conveyor
 ├── FB30_Weighing
 ├── FB40_Sorting
 ├── FB50_RobotHandshake
 ├── FB60_ProductionCounter
 ├── FB70_AlarmManager
 └── FB80_AI_Interface
```

## Data blocks

```text
DB100_CellControl
DB200_AI
DB300_Recipes
DB400_Production
DB500_Alarms
DB600_Robot
DB700_Traceability
```

## Recommended engineering principles

- symbolic tags instead of scattered absolute addresses
- reusable FBs
- UDTs for products, alarms and robot handshake
- one source of truth for recipe limits
- diagnostic states for communication faults
- watchdog timers for external devices
- simulation mode for Factory I/O
- no AI-dependent safety interlocks

## Suggested TIA sequence

```text
INIT
 ↓
SAFETY CHECK
 ↓
AUTO READY
 ↓
FEED
 ↓
DETECT
 ↓
WEIGH
 ↓
CLASSIFY
 ↓
ROBOT PICK
 ↓
ROBOT PLACE
 ↓
TRACE
 ↓
COUNTERS/OEE
 ↓
NEXT CYCLE
```
