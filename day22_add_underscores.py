"""Create three functions. The first called add_hash takes a string and
adds a hash # between the words. The second function called
add_underscore removes the hash (#) and replaces it with an
underscore "_" The third function called remove_underscore,
removes the underscore and replaces it with nothing. if you pass
‘Python’ as an argument for the three functions, and you call them at
the same time like:
print(remove_underscore(add_underscore(add_hash('Python'))))
it should return ‘Python’."""

def add_hash(string):
    if type(string) is not str:
        return "Invalid input."
    return '#'.join(string.split())

def add_underscore(string):
    if type(string) is not str:
        return "Invalid input."
    return '_'.join(string.split('#'))

def remove_underscore(string):
    if type(string) is not str:
        return "Invalid input."
    return ''.join(string.split('_'))

print(remove_underscore(add_underscore(add_hash('Python'))))  # Python
