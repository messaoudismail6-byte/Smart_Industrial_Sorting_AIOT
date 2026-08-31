import numpy as np

def build_features(
    vibration_rms: float,
    temperature_c: float,
    current_a: float,
    cycle_time_s: float,
):
    # Keep feature order identical to training.
    return np.array([[
        float(vibration_rms),
        float(temperature_c),
        float(current_a),
        float(cycle_time_s),
    ]])
