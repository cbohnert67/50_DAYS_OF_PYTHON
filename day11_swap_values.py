"""Write a function called swap_values. This function takes a list
of numbers and swaps the first element with the last element.
For example, if you pass [2, 4,67, 7] as a parameter, your
function should return
[7, 4, 67, 2]."""

def swap_values(numbers):
    if type(numbers) is not list:
        return "Invalid input."
    if len(numbers) == 0:
        return []
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers

print(swap_values([2, 4, 67, 7]))  # [7, 4, 67, 2]
print(swap_values([]))  # []
print(swap_values("Hello"))  # Invalid input.
print(swap_values([2, 4, 67]))  # [67, 4, 2]
