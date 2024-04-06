"""s = 'Hi my name is Richard'
Write a function called string_length that takes a string of
words (words and spaces) as argument. This function should
return the length of all the words in the string. Return the results
in a form of a dictionary. The string above should return:
{'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}"""

def string_length(words):
    if type(words) is not str:
        return "Invalid input."
    return {word: len(word) for word in words.split()}

s = 'Hi my name is Richard'
print(string_length(s))  # {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}
s = 'Hello World'
print(string_length(s))  # {'Hello': 5, 'World': 5}
print(string_length([]))  # Invalid input.
print(string_length(5))  # Invalid input.
print(string_length("Hello"))  # {'Hello': 5}