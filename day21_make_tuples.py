"""Write a function called make_tuples that takes two lists,
equal lists, and combines them into a list of tuples. For
example, if list a is [1,2,3,4] and list b is [5,6,7,8], your
function should return [(1,5), (2,6), (3,7), (4,8)]."""

def make_tuples(list1, list2):
    if type(list1) is not list or type(list2) is not list:
        return "Invalid input."
    if len(list1) != len(list2):
        return "The lists are not of equal lengths."
    return list(zip(list1, list2))

print(make_tuples([1,2,3,4], [5,6,7,8]))  # [(1, 5), (2, 6), (3, 7), (4, 8)]
print(make_tuples([], []))  # []
print(make_tuples([1,2,3,4], [5,6,7]))  # The lists are not of equal lengths.
print(make_tuples("Hello", "World"))  # Invalid input.