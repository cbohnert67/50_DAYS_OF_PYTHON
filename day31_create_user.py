"""Write a function called create_user. This function asks the
user to enter their name, age, and password. The function
saves this information in a dictionary. For example, if the use
enters name as Peter, age - 18 and password - love. The
function should save the information as: {'name': 'Peter',
'age': 18, 'password': 'love'}
Once the information is saved. The function should print to the
user that - "User saved. Please login"
The function should then ask the user to re-enter their name
and password. If the name and password match with what is
saved in the dictionary, the function should return "Logged in
successfully". If the name and password do not match with
what is saved in the dictionary, the function should print
('Wrong password or user name. Please try again'. The
function should keep running until the user enters correct
logging details."""

def create_user():
    user = {}
    user['name'] = input("Enter your name: ")
    user['age'] = int(input("Enter your age: "))
    user['password'] = input("Enter your password: ")
    print("User saved. Please login.")
    while True:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if name == user['name'] and password == user['password']:
            return "Logged in successfully."
        print("Wrong password or user name. Please try again.")

print(create_user())