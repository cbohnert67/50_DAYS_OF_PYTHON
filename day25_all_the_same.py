"""Create a function called all_the_same that takes one
argument, a string, a list, or a tuple and checks if all the
elements are the same. If the elements are the same, the function
should return True. If not, it should return False. For example,
[‘Mary’, ‘Mary’, ‘Mary’] should return True."""

def all_the_same(elements):
    if type(elements) is not list and type(elements) is not tuple:
        return "Invalid input."
    if len(elements) == 0:
        return "Invalid input."
    return len(set(elements)) == 1

print(all_the_same([1, 1, 1]))  # True
print(all_the_same([1, 1, 2]))  # False
print(all_the_same([]))  # Invalid input.
print(all_the_same("Hello"))  # Invalid input.
print(all_the_same((1, 1, 1)))  # True
print(all_the_same((1, 1, 2)))  # False
print(all_the_same(()))  # Invalid input.
