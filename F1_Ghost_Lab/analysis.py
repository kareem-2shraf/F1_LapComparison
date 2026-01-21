def define_sectors(total_distance):
    return {
        "S1": (0, total_distance * 0.33),
        "S2": (total_distance * 0.33, total_distance * 0.66),
        "S3": (total_distance * 0.66, total_distance)
    }


def sector_times(telemetry, sectors):
    times = {}
    for name, (start, end) in sectors.items():
        sector = telemetry[
            (telemetry["Distance"] >= start) &
            (telemetry["Distance"] < end)
        ]
        if len(sector) > 1:
            times[name] = (
                sector["Time"].iloc[-1] -
                sector["Time"].iloc[0]
            ).total_seconds()
        else:
            times[name] = 0.0
    return times