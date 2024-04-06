"""Write a function called check_duplicates that takes a list of
strings as an argument. The function should check if the list has
any duplicates. If there are duplicates, the function should return
the duplicates. If there are no duplicates, the function should
return "No duplicates". For example, the list of fruits below
should return apple as a duplicate and list of names should
return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']"""

def check_duplicates(strings):
    if type(strings) != list:
        return "Invalid input"
    duplicates = list({string for string in strings if strings.count(string) > 1})
    if duplicates:
        return duplicates
    return "No duplicates"

fruits = ['apple', 'orange', 'banana', 'apple'] # apple
names = ['Yoda', 'Moses', 'Joshua', 'Mark'] # No duplicates
print(check_duplicates(fruits))
print(check_duplicates(names))
print(check_duplicates(10)) # Invalid input
print(check_duplicates("fruits")) # Invalid input
print(check_duplicates(['apple', 'orange', 'banana', 'apple', 'orange'])) # ['apple', 'orange']
print(check_duplicates(['apple', 'orange', 'banana', 'apple', 'orange', 'banana'])) # ['apple', 'orange', 'banana'] 
