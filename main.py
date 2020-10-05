# Alarm clock in Python
# Includes repeat functionality for consistent reminders.

import datetime
import time
from plyer import notification
import threading


class Alarm:
    def __init__(self, time, repeat=False, repeat_interval=None):
        self.time = time
        self.repeat = repeat
        self.repeat_interval = repeat_interval


def message():
    title = "Alarm"
    text = "Your alarm has occurred."
    notification.notify(title=title, message=text)


def alarm_input():  # Repeat less code here.
    valid_hour = False
    valid_minute = False
    valid_meridian = False
    valid_repeat = False
    valid_repeat_int = False
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
        repeat = input("How often would you like this alarm to repeat? ")
        if repeat.lower == "i":
            valid_repeat = True
        else:
            try:
                repeat = int(repeat)
                valid_repeat = True
                if repeat == 0:
                    repeat_int = 0
                    valid_repeat_int = True
            except ValueError:
                print("Please enter a valid number or 'i'.")
    while not valid_repeat_int:
        repeat_int = input("What interval of time would you like between alarms? ")
        try:
            repeat_int = int(repeat_int)
            valid_repeat_int = True
        except ValueError:
            print("Please enter a valid number.")
    return hour, minute, repeat, repeat_int


def alarm_init(hour, minute, repeat, repeat_int):
    now = datetime.datetime.now()
    today = True
    if hour < now.hour:
        today = False
    if hour == now.hour:
        if minute <= now.minute:
            today = False
    day = now.day
    if not today:
        day += 1
    try:
        alarm = datetime.datetime(now.year, now.month, day, hour = hour, minute = minute)
    except ValueError:
        day = 1
        month = now.month + 1
        try:
            alarm = datetime.datetime(now.year, month, day, hour = hour, minute = minute)
        except ValueError:
            month = 1
            year = now.year + 1
            alarm = datetime.datetime(year, month, day, hour=hour, minute=minute)
    timeleft = alarm - now
    timer = threading.Timer(timeleft.total_seconds(), message)
    timer.start()
    time.sleep(timeleft.total_seconds())
    while repeat > 0 or repeat == "i":
        timeleft = datetime.timedelta(minutes=repeat_int)
        timer = threading.Timer(timeleft.total_seconds(), message)
        timer.start()
        time.sleep(timeleft.total_seconds())
        if repeat != "i":
            repeat -= 1


def main():
    (hour, minute, repeat, repeat_int) = alarm_input()
    alarm_init(hour, minute, repeat, repeat_int)


main()
