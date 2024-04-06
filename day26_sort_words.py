"""Write a function called sort_words that takes a string of words
as an argument, removes the whitespaces, and returns a list of
letters sorted in alphabetical order. Letters will be separated by
commas. All letters should appear once in the list. This means
that you sort and remove duplicates. For example ‘love life’
should return as ['e,f,i,l,o,v']."""

def sort_words(words):
    if type(words) is not str:
        return "Invalid input."
    if len(words) == 0:
        return "Invalid input."
    return ','.join(sorted(set(words.replace(' ', ''))))

print(sort_words('love life'))  # e,f,i,l,o,v
print(sort_words(''))  #
print(sort_words(5))  # Invalid input.
print(sort_words('love life and laugh'))  # a,d,e,f,g,h,i,l,o,v