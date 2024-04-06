"""Write a function called equal_strings. The function takes two
strings as arguments and compares them. If the strings are equal
(if they have the same characters and have equal length), it
should return True, if they are not, it should return False. For
example, ‘love’ and ‘evol’ should return True."""

def equal_strings(string1, string2):
    return string1 == string2

print(equal_strings("love", "evol"))  # False
print(equal_strings("love", "love"))  # True
print(equal_strings("love", "live"))  # False
print(equal_strings("love", "livee"))  # False