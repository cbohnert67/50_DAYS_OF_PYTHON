"""Write a function called analyse_string that returns the number of
special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words,
and, total characters (all letters and special characters minus
whitespaces) in a string. Return everything in a dictionary format:
{“special character”: “number”, “words”: “number”, “total
characters”: “number”}
Use the string below as an argument:
“Python has a string format operator %. This functions
analogously to printf format strings in C, e.g. "spam=%s
eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2"."""

def analyse_string(string):
    if not string:
        return {"special character": 0, "words": 0, "total characters": 0}
    special_characters = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    special_count = 0
    words = string.split()
    word_count = len(words)
    total_characters = len(string.replace(" ", ""))
    for char in string:
        if char in special_characters:
            special_count += 1
    return {"special character": special_count, "words": word_count, "total characters": total_characters}

string = "Python has a string format operator %. This functions analogously to printf format strings in C, e.g. 'spam=%s eggs=%d' % ('blah', 2) evaluates to 'spam=blah eggs=2'"
print(analyse_string(string))