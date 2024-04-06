"""Create a function called biggest_odd that takes a string of
numbers and returns the biggest odd number in the list. For
example, if you pass ‘23569’ as an argument, your function
should return 9. Use list comprehension."""

def biggest_odd(numbers):
    if type(numbers) is not str:
        return "Invalid input."
    if len(numbers) == 0:
        return "Invalid input."
    if not numbers.isdigit():
        return "Invalid input."
    numbers = [int(number) for number in numbers if int(number) % 2 != 0]
    if len(numbers) == 0:
        return "Invalid input."
    return max(numbers)

print(biggest_odd("23569"))  # 9
print(biggest_odd(""))  # Invalid input.
print(biggest_odd("Hello"))  # Invalid input.
print(biggest_odd("2468"))  # Invalid input.
print(biggest_odd("13579"))  # 9