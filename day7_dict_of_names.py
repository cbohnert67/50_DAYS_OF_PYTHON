"""You are given a list of names, and you are asked to write a code
that returns all the names that start with ‘S’. Your code should
return a dictionary of all the names that start with S and how
many times they appear in the dictionary. Here is a list below:
names = ["Joseph","Nathan", "Sasha", "Kelly",
"Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
Your code should return: {“Sasha”: 1, “Sera”: 2}"""

names = ["Joseph","Nathan", "Sasha", "Kelly",
"Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

def names_starting_with_s(names):
    if type(names) is not list:
        return "Invalid input."
    names_dict = {}
    for name in names:
        if name[0].lower() == 's':
            if name in names_dict:
                names_dict[name] += 1
            else:
                names_dict[name] = 1
    return names_dict

print(names_starting_with_s(names)) # {'Sasha': 1, 'Sera': 2}
print(names_starting_with_s([]))  # {}
print(names_starting_with_s("Hello"))  # Invalid input.
