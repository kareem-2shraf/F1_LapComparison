import numpy as np


def normalize_distance(telemetry):
    max_distance = telemetry["Distance"].max()
    telemetry["DistanceNorm"] = np.linspace(
        0, max_distance, len(telemetry)
    )
    return telemetry