"""Write a function called flat_list that takes one argument, a
nested list. The function converts the nested list into a one-
dimension list. For example [[2,4,5,6]] should return
[2,4,5,6]."""

def flat_list(nested_list):
    if type(nested_list) is not list:
        return "Invalid input."
    if len(nested_list) == 0:
        return []
    return [number for sublist in nested_list for number in sublist]

print(flat_list([[2,4,5,6]]))  # [2, 4, 5, 6]
print(flat_list([]))  # []
print(flat_list("Hello"))  # Invalid input.
print(flat_list([[2,4,5,6], [1, 2, 3]]))  # [2, 4, 5, 6, 1, 2, 3]
print(flat_list([[2,4,5,6], [1, 2, 3], [4, 5, 6]]))  # [2, 4, 5, 6, 1, 2, 3, 4, 5, 6]