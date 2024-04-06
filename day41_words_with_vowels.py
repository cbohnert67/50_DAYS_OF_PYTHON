"""Create a function called words_with_vowels, this function
takes a string of words and returns a list of only words that have
vowels in them. For example, ‘You have no rhythm’ should
return [‘You’,’have’, ‘no’]."""

def words_with_vowels(string):
    if type(string) != str:
        return "Invalid input"
    vowels = "aeiou"
    words = string.split()
    return [word for word in words if any(char.lower() in vowels for char in word)]

print(words_with_vowels('You have no rhythm'))  # ['You', 'have', 'no']
print(words_with_vowels('I Love Python'))  # ['I', 'Love', 'Python']
print(words_with_vowels(12345))  # Invalid input
print(words_with_vowels([1, 2, 3, 4, 5]))  # Invalid input
print(words_with_vowels(12345.0))  # Invalid input