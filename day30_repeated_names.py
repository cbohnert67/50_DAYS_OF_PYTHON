"""Write a function called repeated_name that finds the most
repeated name in the following list.
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]"""

def repeated_name(names):
    if type(names) is not list:
        return "Invalid input."
    if len(names) == 0:
        return "Invalid input."
    return max(set(names), key=names.count)

name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(name))  # Peter
print(repeated_name([]))  # Invalid input.
print(repeated_name(5))  # Invalid input.
print(repeated_name("John"))  # Invalid input.
print(repeated_name(["John", "John", "John", "John"]))  # John