"""Write a function called translate that takes the following
words and translates them into pig Latin.
a = 'i love python'
Here are the rules:
1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the
end. For example, ‘eat’ will become ‘eatyay’
2. If a word starts with anything other than a vowel, move
the first letter to the end and add ‘ay’ to the end. For
example, ‘day’ will become ‘ayday’.
Your code should return:
iyay ovelay ythonpay"""

def translate(string):
    if type(string) != str:
        return "Invalid input"
    vowels = "aeiou"
    words = string.split()
    pig_latin = []
    for word in words:
        if word[0].lower() in vowels:
            pig_latin.append(word + "yay")
        else:
            pig_latin.append(word[1:] + word[0] + "ay")
    return " ".join(pig_latin)

print(translate('i love python'))  # iyay ovelay ythonpay
print(translate('I Love Python'))  # iyay ovelay ythonpay
print(translate(12345))  # Invalid input
print(translate([1, 2, 3, 4, 5]))  # Invalid input
print(translate(12345.0))  # Invalid input