"""In this challenge, copy the text below and save it as a CSV file.
Save it in the same folder as your Python file. Save it as
python.csv.
Write a function called just_digits that reads the text from the
CSV file and returns only digit elements from the file. Your
function should return 1991, 2, 200, 3, 2008 as a list of
strings."""

import csv

def just_digits():
    with open("python.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        result = []
        for row in reader:
            result += [item for item in row[0].split(' ') if item.isdigit()]
        return result

print(just_digits())  # ['1991', '2', '200', '3', '2008']

