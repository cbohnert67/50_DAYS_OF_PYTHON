""" Write a function called divide_or_square that takes one
argument (a number), and returns the square root of the number
if it is divisible by 5, returns its remainder if it is not divisible by
5. For example, if you pass 10 as an argument, then your function
should return 3.16 as the square root. """

import math

def divide_or_square(number):
    if type(number) != int:
        return "Invalid input"
    if number % 5 == 0:
        if number < 0:
            return "Invalid input"
        else:
            return math.sqrt(number)
    else:
        return number % 5
    
print(divide_or_square(10)) # 3.1622776601683795
print(divide_or_square(11)) # 1
print(divide_or_square(0)) # 0.0
print(divide_or_square(-10)) # Invalid input
print(divide_or_square("10")) # Invalid input