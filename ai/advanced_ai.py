"""
V4 Advanced Edge AI:
- anomaly score using Isolation Forest
- health degradation trend
- simple RUL estimate from recent health history

This is a portfolio reference. For production, train/calibrate against
real machine-specific failure data and validate the model.
"""
from collections import deque
import numpy as np
from sklearn.ensemble import IsolationForest, RandomForestRegressor

class EdgePredictor:
    def __init__(self):
        self.anomaly = IsolationForest(
            n_estimators=150,
            contamination=0.05,
            random_state=42
        )
        self.rul_model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )
        self.history = deque(maxlen=100)
        self._fit_demo_models()

    def _fit_demo_models(self):
        rng = np.random.default_rng(42)
        X = rng.normal(size=(1500, 4))
        # Demo degradation relationship, not a production failure model.
        y = np.clip(300 - 35*X[:,0] - 8*X[:,1] - 10*X[:,2] - 15*X[:,3], 1, 300)
        self.anomaly.fit(X)
        self.rul_model.fit(X, y)

    def predict(self, vibration, temperature, current, cycle_time):
        x = np.array([[vibration, temperature, current, cycle_time]], dtype=float)
        anomaly_label = int(self.anomaly.predict(x)[0])
        anomaly_score = float(-self.anomaly.score_samples(x)[0])
        anomaly_score = float(np.clip(anomaly_score, 0, 1))

        health = 100 - (
            min(vibration/2.0, 1)*35 +
            min(max(temperature-40, 0)/50, 1)*25 +
            min(max(current-4, 0)/8, 1)*20 +
            min(max(cycle_time-6, 0)/8, 1)*20
        )
        health = float(np.clip(health, 0, 100))
        self.history.append(health)

        # RUL estimate is expressed as normalized operating-hours proxy.
        rul_proxy = float(np.clip(
            300 * (health/100) * (1 - 0.5*anomaly_score), 1, 300
        ))

        return {
            "health_score": round(health, 1),
            "anomaly": anomaly_label == -1,
            "anomaly_score": round(anomaly_score, 3),
            "estimated_rul_hours_proxy": round(rul_proxy, 1),
            "history_points": len(self.history)
        }
