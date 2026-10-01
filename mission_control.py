# mission_control.py
# Name: Trent Skelton
# Date: 10/1/2026
# Description: Runs two Mission Control launch sequences.

import time


def show_banner():
	print("========================================")
	print("          MISSION CONTROL")
	print("========================================")


def crew_report(commander, pilot, rocket):
	print(f"Commander {commander} and pilot {pilot} are ready to launch {rocket}.")


def launch_countdown(seconds):
	print(f"T-minus {seconds} seconds and counting...")
	for remaining_seconds in range(seconds, 0, -1):
		print(remaining_seconds)
		time.sleep(1)
	print("Liftoff! The rocket has launched into space.")


commander_name = input("Enter the commander's name: ")
pilot_name = input("Enter the pilot's name: ")
rocket_name = input("Enter the rocket's name: ")
countdown_length = int(input("Enter the countdown length in seconds: "))

show_banner()
crew_report(commander_name, pilot_name, rocket_name)
launch_countdown(countdown_length)

show_banner()
crew_report("Mae Jemison", "Neil Armstrong", "Odyssey")
launch_countdown(3)
