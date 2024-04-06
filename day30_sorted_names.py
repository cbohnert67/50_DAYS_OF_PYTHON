"""You work for a local school in your area. The school has a list of
names of students saved in a list. The school has asked you to
write a program that takes a list of names and sorts them
alphabetically. The names should be sorted by last names. Here
is a list of names:
[‘Beyonce Knowles, ‘Alicia Keys’, ‘Katie Perry’, ‘Chris
Brown’,’ Tom Cruise’]
Your code should not just sort them alphabetically, but it should
also switch the names (the last name must be the first). Here is
how your code output should look:
['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie',
'Knowles Beyonce']
Write a function called sorted_names."""

def sorted_names(names):
    if type(names) is not list:
        return "Invalid input."
    return sorted([f"{i.split()[1]} {i.split()[0]}" for i in names])

names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
print(sorted_names(names))  # ['Brown Chris', 'Cruise Tom   ', 'Keys Alicia  ', 'Perry Katie   ', 'Knowles Beyonce']
print(sorted_names([]))  # []
print(sorted_names(5))  # Invalid input.
print(sorted_names("John"))  # Invalid input.

