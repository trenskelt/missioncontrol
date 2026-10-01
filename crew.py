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