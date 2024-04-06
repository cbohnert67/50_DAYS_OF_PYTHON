"""Write a function called register_check that checks how many
students are in school. The function takes a dictionary as a
parameter. If the student is in school, the dictionary says ‘yes’. If
the student is not in school, the dictionary says ‘no’. Your
function should return the number of students in school. Use the
dictionary below. Your function should return 3.
register = {'Michael':'yes','John': 'no',
'Peter':'yes', 'Mary': 'yes'}"""

def register_check(dictionary):
    if type(dictionary) != dict:
        return "Invalid input"
    students = list(dictionary.values())
    return students.count('yes')

register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}
print(register_check(register)) # 3
print(register_check(10)) # Invalid input
print(register_check("register")) # Invalid input
print(register_check({'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes', 'Jane': 'no'})) # 3
print(register_check({'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes', 'Jane': 'yes'})) # 4