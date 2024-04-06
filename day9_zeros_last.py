"""Write a function called zeros_last. This function takes a list as
argument. If a list has zeros (0), it will move them to the front of
the list and maintain the order of the other numbers in the list.
If there are no Zeros in the list, the function should return the
original list sorted in ascending order. For example, if you pass
[1, 4, 6, 0, 7,0,9] as an argument, your code should return [1,
4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
your code should return [1, 2, 4, 6, 7]."""

def zeros_last(numbers):
    if type(numbers) is not list:
        return "Invalid input."
    if len(numbers) == 0:
        return []
    zeros = [number for number in numbers if number == 0]
    if len(zeros) == 0:
        return sorted(numbers)
    return [number for number in numbers if number != 0] + zeros

print(zeros_last([1, 4, 6, 0, 7, 0, 9]))  # [1, 4, 6, 7, 9, 0, 0]
print(zeros_last([]))  # []
print(zeros_last("Hello"))  # Invalid input.
print(zeros_last([2, 1, 4, 7, 6]))  # [1, 2, 4, 6, 7]
print(zeros_last([0, 0, 0, 0, 0]))  # [0, 0, 0, 0, 0]
print(zeros_last([0, 0, 0, 0, 0, 1]))  # [1, 0, 0, 0, 0, 0]
print(zeros_last([1, 0, 0, 0, 0, 0]))  # [1, 0, 0, 0, 0, 0]
print(zeros_last([0, 1, 0, 0, 0, 0]))  # [1, 0, 0, 0, 0, 0]

