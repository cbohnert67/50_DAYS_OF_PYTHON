"""Write a function called convert_add that takes a list of strings
as an argument and converts it to integers and sums the list. For
example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
summed to 9."""

def convert_add(strings):
    if type(strings) != list:
        return "Invalid input"
    integers = list(map(int, strings))
    return sum(integers)

print(convert_add(['1', '3', '5'])) # 9
print(convert_add([1, 3, 5])) # 9
print(convert_add(10)) # Invalid input
print(convert_add("10")) # Invalid input
print(convert_add(['1', '3', '5', '7'])) # 16
print(convert_add(['1', '3', '5', '7', '9'])) # 25