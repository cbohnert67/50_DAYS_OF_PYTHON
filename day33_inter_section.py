"""Write a function called inter_section that takes two lists and
finds the intersection (the elements that are present in both
lists). The function should return a tuple of intersections. Use
list comprehension in your solution. Use the lists below. Your
function should return (30, 65, 80).
list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]"""

def inter_section(list1, list2):
    if type(list1) is not list or type(list2) is not list:
        return "Invalid input."
    return tuple([i for i in list1 if i in list2])

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]
print(inter_section(list1, list2))  # (30, 65, 80)
print(inter_section([], list2))  # ()
print(inter_section(list1, []))  # ()
print(inter_section(5, list2))  # Invalid input.
print(inter_section(list1, 5))  # Invalid input.
print(inter_section(5, 5))  # Invalid input.
print(inter_section("Java", list2))  # Invalid input.
print(inter_section(list1, "Java"))  # Invalid input.
print(inter_section("Java", "Java"))  # Invalid input.
