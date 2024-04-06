"""Write a function called count_dots. This function takes a
string separated by dots as a parameter and counts how many
dots are in the string. For example, ‘h.e.l.p.’ should return 4
dots, and ‘he.lp.’ should return 2 dots."""

def count_dots(string):
    if type(string) is not str:
        return "Invalid input."
    return string.count(".") if "." in string else 0

print(count_dots("h.e.l.p."))  # 4
print(count_dots("he.lp."))  # 2
print(count_dots("help"))  # 0
print(count_dots("h.e.l.p"))  # 3