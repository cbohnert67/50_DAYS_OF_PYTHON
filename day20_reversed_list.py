"""str1 = 'leArning is hard, bUt if You appLy youRself ' \
'you can achieVe success'
You are given a string of words. Some of the words in the string
contain uppercase letters. Write a code that will return all the
words that have an uppercase letter. Your code should return a
list of the words. Each word in the list should be reversed. Here
is how your output should look:
['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']"""

str1 = 'leArning is hard, bUt if You appLy youRself ' \
'you can achieVe success'

def reversed_list(string):
    if type(string) is not str:
        return "Invalid input."
    if len(string) == 0:
        return []
    return [word[::-1] for word in string.split() if any(letter.isupper() for letter in word)]

print(reversed_list(str1))  # ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
print(reversed_list(""))  # []
print(reversed_list(123))  # Invalid input.
print(reversed_list("Hello"))  # ['olleH']