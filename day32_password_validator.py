"""Write a function called password_validator. The function
asks the user to enter a password. A valid password should have
at least one upper letter, one lower letter, and one
number. It should not be less than 8 characters long. When
the user enters a password, the function should check if the
password is valid. If the password is valid, the function should
return the valid password. If the password is not valid, the
function should tell the users the errors in the password and
prompt the user to enter another password. The code should
only stop once the user enters a valid password. (use while loop)."""

def password_validator():
    while True:
        password = input("Enter your password: ")
        if len(password) < 8:
            print("Password should not be less than 8 characters.")
        elif not any(char.isupper() for char in password):
            print("Password should have at least one upper letter.")
        elif not any(char.islower() for char in password):
            print("Password should have at least one lower letter.")
        elif not any(char.isdigit() for char in password):
            print("Password should have at least one number.")
        else:
            return password
        
print(password_validator())