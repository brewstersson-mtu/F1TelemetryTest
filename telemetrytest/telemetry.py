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
