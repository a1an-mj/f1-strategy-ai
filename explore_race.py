import os 
import fastf1

os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Monaco", "R")
session.load(telemetry=False, weather=False)

laps = session.laps

print(laps.shape)
print(laps.columns)
print(laps.head())

lec_laps = laps[laps["Driver"] == "LEC"]
print(lec_laps[["LapNumber", "Compound", "TyreLife", "LapTime"]])