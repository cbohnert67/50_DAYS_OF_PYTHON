"""Write a function called python_snakes that takes a number
as an argument and creates the following shape, using the
number’s range: (hint: Use the loops and emoji library.
        🐍🐍
      🐍🐍🐍🐍
    🐍🐍🐍🐍🐍🐍
  🐍🐍🐍🐍🐍🐍🐍🐍
🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍"""

def python_snakes(number):
    if type(number) is not int:
        return "Invalid input."
    if number < 1:
        return "Invalid input."
    s = ""
    for i in range(1, number + 1):
        s += " " * 2 * (number - i) + "🐍" * 2 * i + "\n"
    print(s)


print(python_snakes(5))
print(python_snakes(10))
print(python_snakes(0))
print(python_snakes("Hello"))
print(python_snakes(5.5))
print(python_snakes(-5))
print(python_snakes(1))
