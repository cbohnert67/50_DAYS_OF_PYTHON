"""Create a function called alarm that sets an alarm clock for the
user. The function should ask the user to enter time they want
the alarm to go off. The user should enter the hour and
minute. The function should then print out the time when the
alarm will go off. When its alarm time, the code should let off a
sound. Use the winsound module for sound."""

import winsound
import time

def alarm():
    while True:
        hour = int(input("Enter the hour: "))
        minute = int(input("Enter the minute: "))
        print(f"Alarm set for {hour}:{minute}")
        while True:
            if hour == int(time.strftime("%I")) and minute == int(time.strftime("%M")):
                winsound.Beep(1000, 1000)
                break

alarm()