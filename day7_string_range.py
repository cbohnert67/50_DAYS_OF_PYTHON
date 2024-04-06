"""Write a function called string_range that takes a single
number and returns a string of its range. The string characters
should be separated by dots(.) For example, if you pass 6 as
an argument, your function should return ‘0.1.2.3.4.5’."""

def string_range(number):
    if type(number) is not int:
        return "Invalid input."
    if number < 0:
        return "Invalid input."
    if number == 0:
        return "0"
    return '.'.join(map(str, range(number)))

print(string_range(6))  # 0.1.2.3.4.5
print(string_range(0))  # 0
print(string_range(-1))  # Invalid input.
print(string_range("Hello"))  # Invalid input.
print(string_range(5.5))  # Invalid input.
print(string_range(5))  # 0.1.2.3.4