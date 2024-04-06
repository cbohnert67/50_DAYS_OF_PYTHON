"""Your new company has a list of figures saved in a list. The issue
is that these numbers have no separator. The numbers are
saved in the following format:
[1000000, 2356989, 2354672, 9878098].
You have been asked to write a code that will convert each of the
numbers in the list into a string. Your code should then add a
comma on each number as a thousand separator for
readability. When you run your code on the above list, your
output should be:
[ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]
Write a function called convert_numbers that will take one
argument, a list of numbers above."""

def convert_numbers(numbers):
    if type(numbers) is not list:
        return "Invalid input."
    if len(numbers) == 0:
        return []
    return [format(number, ',') for number in numbers]

print(convert_numbers([1000000, 2356989, 2354672, 9878098]))  # ['1,000,000', '2,356,989', '2,354,672', '9,878,098']
print(convert_numbers([]))  # []
print(convert_numbers("Hello"))  # Invalid input.
print(convert_numbers([1, 2, 3, 4]))  # ['1', '2', '3', '4']
print(convert_numbers([1000000]))  # ['1,000,000']