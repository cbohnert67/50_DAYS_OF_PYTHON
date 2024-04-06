"""Write a function called add_reverse. This function takes two
lists as argument and adds each corresponding number, and
reverses the outcome. For example, if you pass [10, 12, 34]
and [12, 56, 78]. Your code should return [112, 68, 22]. If the
two lists are not of equal lengths, the code should return a
message that "the lists are not of equal lengths"."""

def add_reverse(list1, list2):
    if type(list1) is not list or type(list2) is not list:
        return "Invalid input."
    if len(list1) != len(list2):
        return "The lists are not of equal lengths."
    return list(reversed([list1[index] + list2[index] for index in range(len(list1))]))

print(add_reverse([10, 12, 34], [12, 56, 78]))  # [112, 22, 68]
print(add_reverse([], []))  # []
print(add_reverse([1, 2, 3], [4, 5]))  # The lists are not of equal lengths.
print(add_reverse("Hello", "World"))  # Invalid input.
print(add_reverse([1, 2, 3], [4, 5, 6, 7]))  # The lists are not of equal lengths.
print(add_reverse([1, 2, 3], [4, 5, 6]))  # [9, 7, 7]