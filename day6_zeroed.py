"""Write a function called zeroed that takes a list of numbers
as an argument. The code should zero (0) the first and the last
number in the list. For example, if the input is [2, 5, 7, 8, 9],
your code should return [0, 5, 7, 8, 0]."""

def zeroed(numbers):
    if type(numbers) is not list:
        return "Invalid input."
    if len(numbers) == 0:
        return []
    numbers[0] = 0
    numbers[-1] = 0
    return numbers

print(zeroed([2, 5, 7, 8, 9]))  # [0, 5, 7, 8, 0]
print(zeroed([]))  # []
print(zeroed("Hello"))  # Invalid input.
print(zeroed([2, 5, 7, 8]))  # [0, 5, 7, 0]