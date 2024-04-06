"""Create a function called count_the_vowels. The function
takes one argument, a string, and returns the number of vowels
in the string. For example, ‘hello’ should return 2 vowels. If a
vowel appears in a string more than once it should be counted
as one. For example, ‘saas’ should return 1 vowel. Your code
should count lowercase and uppercase vowels."""

def count_the_vowels(string):
    if type(string) != str:
        return "Invalid input"
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

print(count_the_vowels('hello'))  # 2
print(count_the_vowels('saas'))  # 2
print(count_the_vowels('SAAS'))  # 2
print(count_the_vowels('hello world'))  # 3
print(count_the_vowels(12345))  # Invalid input
print(count_the_vowels([1, 2, 3, 4, 5]))  # Invalid input
print(count_the_vowels(12345.0))  # Invalid input