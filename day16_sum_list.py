"""Write a function called sum_list with one parameter that takes
a nested list of integers as an argument and returns the sum of
the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
as an argument your function should return a sum of 33."""

def sum_list(nested_list):
    if type(nested_list) is not list:
        return "Invalid input."
    if len(nested_list) == 0:
        return 0
    return sum([number for sublist in nested_list for number in sublist])

print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))  # 33
print(sum_list([]))  # 0
print(sum_list("Hello"))  # Invalid input.
print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6], [1, 2, 3]]))  # 39
print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6], [1, 2, 3], [4, 5, 6]]))  # 54