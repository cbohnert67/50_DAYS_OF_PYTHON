"""Write a function called word_index that takes one argument,
a list of strings and returns the index of the longest word in the
list. If there is no longest word (if all the strings are of the same
length), the function should return zero (0). For example, the list
below should return 2.
words1 = ["Hate", "remorse", "vengeance"]
And this list below, shoul return zero (0)
words2 = ["Love", "Hate"]"""

def word_index(words):
    if type(words) != list:
        return "Invalid input"
    longest = max(words, key=len)
    if len(set(map(len, words))) == 1:
        return 0
    return words.index(longest)

words1 = ["Hate", "remorse", "vengeance"] # 2
words2 = ["Love", "Hate"] # 0
print(word_index(words1))
print(word_index(words2))
print(word_index(10)) # Invalid input
print(word_index("words")) # Invalid input
print(word_index(["Love", "Hate", "Peace"])) # 2
print(word_index(["Love", "Hate", "Peace", "War"])) # 2
print(word_index(["Love", "Hate", "Peace", "War", "Joy"])) # 2  
print(word_index(["Love", "Hate", "Peace", "War", "Joy", "Sorrow"])) # 5