"""names = [ "Peter", "Jon", "Andrew"]
Write a function called sort_length that takes a list of strings
as an argument, and sorts the strings in ascending order
according to their length. For example, the list above should
return:
['Jon', 'Peter', 'Andrew']
Do not use the built-in sort functions"""

def sort_length(names):
    if type(names) is not list:
        return "Invalid input."
    for i in range(len(names)):
        for j in range(len(names) - 1):
            if len(names[j]) > len(names[j + 1]):
                names[j], names[j + 1] = names[j + 1], names[j]
    return names

print(sort_length(["Peter", "Jon", "Andrew"]))  # ['Jon', 'Peter', 'Andrew']
print(sort_length([]))  # []
print(sort_length("Hello"))  # Invalid input.
print(sort_length(["Peter", "Jon", "Andrew", "John"]))  # ['Jon', 'John', 'Peter', 'Andrew']
print(sort_length(["Peter", "Jon", "Andrew", "John", "James"]))  # ['Jon', 'John', 'Peter', 'James', 'Andrew']