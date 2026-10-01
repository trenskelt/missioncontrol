def greet_astronaut(astronaut): 
    print(f"Hello, {astronaut}!")
greet_astronaut("Sally Ride")

# crew.py
# Name: Trent Skelton
# Date: 10/1/2026
# Lab: Mission Control, Parts 3 and 4 (parameters and arguments)
astronaut_name = input("Welcome astronaut. What is your name? ")
companion_name = input("What is your companion's name? ")
def greet_astronaut(astronaut):
    print(f"Hello, {astronaut}! Welcome to the mission.")
greet_astronaut(astronaut_name) 
greet_astronaut(companion_name) 
greet_astronaut("Mission Specialist Rivera")
def announce_rocket(rocket):
    print(f"Attention all personnel: {rocket} is ready for launch.")
    
def greet_all_astronauts(astronaut1, astronaut2):
    print(f"Hello, {astronaut1} and {astronaut2}! Welcome to the mission.")
greet_all_astronauts(astronaut_name, companion_name)
# PREDICTION 3: I think this call will print the names backwards
greet_all_astronauts(companion_name, astronaut_name)

def mission_assignment(astronaut, role, destination):
    print(f"{astronaut} will serve as {role} on the mission to {destination}.")

mission_assignment("Ada", "Pilot", "Mars")
mission_assignment("Mae", "Commander", "the Moon")
