import time

def launch_countdown():
    print("Liftoff!")

launch_countdown()


# launch_control.py
# launch_control.py
# Name: Trent Skelton
# Date: 10/1/2026
# Lab: Mission Control, Part 2 (functions without parameters)


import time # gives us time.sleep() so we can pause the program
def launch_countdown():
    print("T-minus 5 seconds and counting...")
    for i in range(5, 0, -1):
        print(i)
    time.sleep(1) # pause for 1 second between numbers
    print("Liftoff! The rocket has launched into space.")
launch_countdown()

# On Monday NASA launches Rocket 1
print("MONDAY: Rocket 1")
launch_countdown()
# On Thursday NASA launches Rocket 2
print("THURSDAY: Rocket 2")
launch_countdown()


def mission_briefing(rocket_name):
    print(f"Mission briefing for {rocket_name}:")
    print("Objective: Deploy satellite into orbit.")
    print("Launch window: 10:00 AM - 2:00 PM.")
    print("Weather conditions: Clear skies.")
    print("All systems normal.")
mission_briefing("Rocket 1")