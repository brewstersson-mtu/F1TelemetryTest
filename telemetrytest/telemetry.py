import fastf1

session = fastf1.get_session(2023, 'Monaco', 'Q')
session.load()

print("The fastest speed through the speed trap was: ", session.laps.pick_fastest()['SpeedST'])

lec_lap = session.laps.pick_driver('LEC').pick_fastest()
sai_lap= session.laps.pick_driver('SAI').pick_fastest()

print(f"Leclerc Top Speed: {lec_lap['SpeedST']} km/h")
print(f"Sainz Top Speed: {sai_lap['SpeedST']} km/h")