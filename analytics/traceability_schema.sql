CREATE TABLE IF NOT EXISTS production_cycles (
    cycle_id INTEGER PRIMARY KEY,
    timestamp TEXT NOT NULL,
    weight_kg REAL NOT NULL,
    weight_class INTEGER NOT NULL,
    destination TEXT NOT NULL,
    health_score REAL,
    risk_level TEXT,
    cycle_time_s REAL,
    robot_status TEXT
);

CREATE INDEX IF NOT EXISTS idx_cycles_timestamp
ON production_cycles(timestamp);
