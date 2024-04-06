"""Write a function called spelling_checker. This code asks the
user to input a word and if a user inputs a wrong spelling it
should suggest the correct spelling by asking the user if they
meant to type that word. If the user says no, it should ask the
user to enter the word again. If the user says yes, it should
return the correct word. If the word entered by the user is
correctly spelled the function should return the correct word.
Use the module textblob."""

from textblob import Word

def spelling_checker():
    while True:
        word = input("Enter a word: ")
        if Word(word).spellcheck()[0][1] >= 0.95:
            return word
        else:
            suggestion = Word(word).spellcheck()[0][0]
            response = input(f"Did you mean {suggestion}? (yes/no): ")
            if response.lower() == "yes":
                return suggestion

print(spelling_checker())