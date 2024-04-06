"""Write a function called odd_even that has one parameter and
takes a list of numbers as an argument. The function returns the
difference between the largest even number in the list and the
smallest odd number in the list. For example, if you pass
[1,2,4,6] as an argument the function should return 6 -1= 5"""

def odd_even(numbers):
    if type(numbers) is not list:
        return "Invalid input."
    if len(numbers) == 0:
        return "Invalid input."
    even_numbers = [number for number in numbers if number % 2 == 0]
    odd_numbers = [number for number in numbers if number % 2 != 0]
    if len(even_numbers) == 0 or len(odd_numbers) == 0:
        return "Invalid input."
    return max(even_numbers) - min(odd_numbers)

print(odd_even([1,2,4,6]))  # 5
print(odd_even([]))  # Invalid input.
print(odd_even("Hello"))  # Invalid input.
print(odd_even([1,2,4,6,7]))  # 5
print(odd_even([1,2,4,6,7,8]))  # 7