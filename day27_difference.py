"""Write a function called difference that takes two lists as
arguments. This function should return all the elements that are
in list a but not in list b and all the elements in list b not in list
a. For example:
list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
should return:
[4, 6, 7, 9]
Use list comprehension in your function."""

def difference(a, b):
    if type(a) is not list or type(b) is not list:
        return "Invalid input."
    return [i for i in a if i not in b] + [i for i in b if i not in a]

list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
print(difference(list1, list2))  # [4, 6, 7, 9]