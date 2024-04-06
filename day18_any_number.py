"""Write a function called any_number that can receive any
number of arguments (integers and floats) and return the
average of those integers. If you pass 12, 90, 12, 34 as
arguments your function should return 37.0 as average. If you
pass 12, 90 your function should return 51.0 as average."""

def any_number(*args):
    if len(args) == 0:
        return "Invalid input."
    return sum(args) / len(args)

print(any_number(12, 90, 12, 34))  # 37.0
print(any_number(12, 90))  # 51.0
print(any_number())  # Invalid input.
print(any_number(12, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90))  # 53.5
