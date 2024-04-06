"""Create a simple calculator. The calculator should be able to perform
basic math operations, add, subtract, divide and multiply. The
calculator should take input from users. The calculator should be
able to handle ZeroDivisionError, NameError, and
ValueError."""

def simple_calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            return "Invalid operator."
    except ZeroDivisionError:
        return "You cannot divide by zero."
    except NameError:
        return "Invalid input."
    except ValueError:
        return "Invalid input."
    
print(simple_calculator())