from dataclasses import dataclass

@dataclass
class OEE:
    availability: float
    performance: float
    quality: float
    oee: float

def calculate_oee(
    planned_time_s: float,
    downtime_s: float,
    ideal_cycle_s: float,
    total_count: int,
    reject_count: int,
) -> OEE:
    run_time = max(0.0, planned_time_s - downtime_s)
    availability = run_time / planned_time_s if planned_time_s else 0.0

    ideal_run_time = ideal_cycle_s * total_count
    performance = ideal_run_time / run_time if run_time else 0.0
    performance = min(max(performance, 0.0), 1.0)

    good = max(0, total_count - reject_count)
    quality = good / total_count if total_count else 0.0

    oee = availability * performance * quality
    return OEE(availability, performance, quality, oee)

if __name__ == "__main__":
    result = calculate_oee(3600, 300, 7, 400, 12)
    print(result)
