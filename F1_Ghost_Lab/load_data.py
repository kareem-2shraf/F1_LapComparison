import fastf1
from config import DRIVER, TRACK, SESSION

# Make sure this folder exists: data/cache
fastf1.Cache.enable_cache("data/cache")


def load_fastest_lap(year):
    session = fastf1.get_session(year, TRACK, SESSION)
    session.load()

    laps = session.laps.pick_drivers(DRIVER)
    lap = laps.pick_fastest()

    telemetry = lap.get_telemetry()
    telemetry = telemetry.reset_index(drop=True)

    return telemetry