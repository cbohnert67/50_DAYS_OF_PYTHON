"""Write a function called hide_password that takes no
parameters. The function takes an input (a password) from a
user and returns a hidden password. For example, if the user
enters ‘hello’ as a password the function should return ‘****’ as
a password and tell the user that the password is 4 characters
long."""

def hide_password():
    password = input("Enter your password: ")
    return '*' * len(password)

print(hide_password())