""" Write a function called longest_value that takes a dictionary
as an argument and returns the first longest value of the
dictionary. For example, the following dictionary should return
– apple as the longest value.
fruits = {'fruit': 'apple', 'color': 'green'} """

def longest_value(dictionary):
    if type(dictionary) != dict:
        return "Invalid input"
    values = dictionary.values()
    longest = max(values, key=len)
    return longest

fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits)) # apple
print(longest_value(10)) # Invalid input
print(longest_value("fruits")) # Invalid input
print(longest_value({'fruit': 'apple', 'color': 'green', 'taste': 'sweety'})) # sweety