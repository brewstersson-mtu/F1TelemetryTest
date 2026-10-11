import fastf1
import matplotlib.pyplot as plt

year = (int(input("Enter year: ")))

race_choice = input("Please enter the race stats you would like to view: ")
race_choice = race_choice.upper()
print(race_choice)

session = fastf1.get_session(year, race_choice, 'Q')
session.load()
print(session.event.OfficialEventName)
print(session.event.EventDate)

driver_one = input("Please enter the first drivers stats you'd like to compare ABBREVIATED: ")
driver_one = driver_one.upper()
driver_two = input("Please enter the second drivers stats you'd like to compare ABBREVIATED: ")
driver_two = driver_two.upper()
print(f"You have chosen {driver_one} and {driver_two} to compare.")
drivers = [driver_one, driver_two]

driver_one_lap = session.laps.pick_driver(driver_one).pick_fastest()
driver_two_lap = session.laps.pick_driver(driver_two).pick_fastest()

driver_one_speed = driver_one_lap['SpeedST']
driver_two_speed = driver_two_lap['SpeedST']

speeds = [driver_one_speed, driver_two_speed]
colors = ['#6CD3BF', '#00A19B']

print(session.event.OfficialEventName)
print("Speed Trap Comparison")
print(f"{driver_one}: {driver_one_speed} km/h")
print(f"{driver_two}: {driver_two_speed} km/h")

if driver_one_speed > driver_two_speed:
    difference = driver_one_speed - driver_two_speed
    print(f"{driver_one} was faster by {difference:1f} km/h!")
elif driver_two_speed > driver_one_speed:
    difference = driver_two_speed - driver_one_speed
    print(f"{driver_two} was faster by {difference:1f} km/h!")
else:
    print("They had the exact same top speed!")

plt.figure(figsize=(6,5))
bars = plt.bar(drivers, speeds, color=colors, width=0.5)

plt.title(session.event.OfficialEventName, fontsize=14, pad=15)
plt.ylabel('Speed (km/h)', fontsize=12)

plt.ylim(min(speeds) - 5, max(speeds) + 5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f"{yval} km/h", ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()