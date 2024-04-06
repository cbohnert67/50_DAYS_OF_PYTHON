"""Write a function called age_in_minutes that tells a user how
old they are in minutes. Your code should ask the user to
enter their year of birth, and it should return their age in
minutes (by subtracting their year of birth to the current year).
Here are things to look out for:
a. The user can only input a 4-digit year of birth. For
example, 1930 is a valid year. However, entering any
number longer or less than 4 digits long should render
input invalid. Notify the user to input a four digits
number.
b. If a user enters a year before 1900, your code should
tell the user that input is invalid. If the user enters the
year after the current year, the code should tell the user,
to input a valid year.
The code should run until the user inputs a valid year.
Your function should return the user's age in minutes. For
example, if someone enters 1930, as their year of birth your
function should return:
You are 48,355,200 minutes old."""

from datetime import datetime

def age_in_minutes():
    while True:
        try:
            year_of_birth = int(input("Enter your year of birth: "))
            if len(str(year_of_birth)) != 4:
                print("Invalid input. Please enter a four-digit number.")
                continue
            if year_of_birth < 1900:
                print("Invalid input. Please enter a valid year.")
                continue
            if year_of_birth > datetime.now().year:
                print("Invalid input. Please enter a valid year.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")
    age_in_minutes = (datetime.now().year - year_of_birth) * 525600
    return f"You are {age_in_minutes:,} minutes old."

print(age_in_minutes())