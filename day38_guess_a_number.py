"""Write a function called guess_a_number. The function
should ask a user to guess a randomly generated number. If the
user guesses a higher number, the code should tell them that the
guess is too high, if the user guesses low, the code should tell
them that their guess is too low. The user should get a maximum
of three guesses. When the user guesses right, the code should
declare them a winner. After three wrong guesses, the code
should declare them a loser."""

import random

def guess_a_number():
    number = random.randint(1, 10)
    print("Guess a number between 1 and 10")
    for _ in range(3):
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("You are a winner")
            return
        if guess < number:
            print("Your guess is too low")
        if guess > number:
            print("Your guess is too high")
    print(f"You are a loser. The number was {number}")

guess_a_number()