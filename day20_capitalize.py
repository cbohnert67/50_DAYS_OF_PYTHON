"""Write a function called capitalize. This function takes a string
as an argument and capitalizes the first letter of each word. For
example, ‘i like learning’ becomes ‘I Like Learning’."""

def capitalize(string):
    if type(string) is not str:
        return "Invalid input."
    return ' '.join([word.capitalize() for word in string.split()])

print(capitalize("i like learning"))  # I Like Learning
print(capitalize("hello world"))  # Hello World
print(capitalize(5))  # Invalid input.