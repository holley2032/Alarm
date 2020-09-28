# Alarm clock in Python
# Includes repeat functionality for consistent reminders.

import datetime
import plyer


class Alarm:
    def __init__(self, time, repeat=False, repeat_interval=None):
        self.time = time
        self.repeat = repeat
        self.repeat_interval = repeat_interval


def alarm_init():
    valid_hour = False
    valid_minute = False
    valid_meridian = False
    valid_repeat = False
    while not valid_hour:
        hour = input("What hour would you like the alarm set to: ")
        try:
            hour = int(hour)
            if hour == 0 or (13 <= hour <= 23):
                valid_hour = True
                valid_meridian = True
            elif 1 <= hour <= 12:
                valid_hour = True
            else:
                print("Please enter a valid hour between 0 and 23.")
        except ValueError:
            print("Please enter a valid hour between 0 and 23")
    while not valid_minute:
        minute = input("What minute would you like the alarm set to: ")
        try:
            minute = int(minute)
            if 0 <= minute <= 59:
                valid_minute = True
            else:
                print("Please enter a valid minute between 0 and 59.")
        except ValueError:
            print("Please enter a valid minute between 0 and 59.")
    while not valid_meridian:
        meridian = input("AM/PM: ")
        if meridian.lower() in ["a", "am"]:
            valid_meridian = True
        elif meridian.lower() in ["p", "pm"]:
            hour += 12
            valid_meridian = True
        else:
            print("Please enter AM or PM.")
    while not valid_repeat:
        repeat = input("How often would you like this alarm to repeat? Please enter a number or 'i' for indefinitely: ")
        if repeat.lower == "i":
            valid_repeat = True
        else:
            try:
                repeat = int(repeat)
                valid_repeat = True
            except ValueError:
                print("Please enter a valid number or 'i'.")


def main():
    pass
