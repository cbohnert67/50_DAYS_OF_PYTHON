"""Create a function called average_calories that calculates the
average calories intake of a user. The function should ask the user
to input their calories intake for any number of days and once they
hit ‘done’ it should calculate and return the average intake."""

def average_calories():
    calories = []
    while True:
        calorie = input("Enter your calories intake: ")
        if calorie.lower() == 'done':
            break
        if not calorie.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        calories.append(int(calorie))
    return sum(calories) / len(calories)

print(average_calories())