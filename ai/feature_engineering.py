"""Feature preparation and validation for the edge-health model."""

from __future__ import annotations

import numpy as np

FEATURE_LIMITS = {
    "vibration_rms": (0.0, 10.0),
    "temperature_c": (-40.0, 150.0),
    "current_a": (0.0, 100.0),
    "cycle_time_s": (0.01, 3600.0),
}


def validate_telemetry(
    vibration_rms: float,
    temperature_c: float,
    current_a: float,
    cycle_time_s: float,
) -> None:
    """Reject non-finite or physically impossible telemetry values."""
    values = {
        "vibration_rms": vibration_rms,
        "temperature_c": temperature_c,
        "current_a": current_a,
        "cycle_time_s": cycle_time_s,
    }
    for name, value in values.items():
        numeric = float(value)
        lower, upper = FEATURE_LIMITS[name]
        if not np.isfinite(numeric) or not lower <= numeric <= upper:
            raise ValueError(f"{name} must be between {lower} and {upper}")


def build_features(
    vibration_rms: float,
    temperature_c: float,
    current_a: float,
    cycle_time_s: float,
) -> np.ndarray:
    """Return model features in the same order used during training."""
    validate_telemetry(vibration_rms, temperature_c, current_a, cycle_time_s)
    return np.array(
        [[
            float(vibration_rms),
            float(temperature_c),
            float(current_a),
            float(cycle_time_s),
        ]],
        dtype=float,
    )
