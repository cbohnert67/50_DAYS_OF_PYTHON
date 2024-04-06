"""str1 = "the love is real"
Write a function called read_backwards that takes a string as
an argument and reverses it. For example, the string above
should return: "real is love the" """

def read_backwards(string):
    if type(string) is not str:
        return "Invalid input."
    return ' '.join(string.split()[::-1])

str1 = "the love is real"
print(read_backwards(str1))  # real is love the
str1 = "the love is real and true"
print(read_backwards(str1))  # true and real is love the