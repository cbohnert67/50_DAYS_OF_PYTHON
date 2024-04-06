"""Write a function called count that takes one argument a string,
and returns a dictionary of how many times each element
appears in the string. For example, ‘hello’ should return:
{‘h’:1,’e’: 1,’l’:2, ‘o’:1}."""

def count(string):
    if type(string) != str:
        return "Invalid input"
    return {char: string.count(char) for char in string}

print(count('hello'))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(count('hello world'))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print(count(12345))  # Invalid input
print(count([1, 2, 3, 4, 5]))  # Invalid input
print(count(12345.0))  # Invalid input
print(count('hello world!'))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}