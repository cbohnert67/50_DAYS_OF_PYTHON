"""Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
Write a code that generates a list of the following numbers from
the nested list above 34, 67, 78. Your output should be another
list:
[34, 67, 78]. The list output should not have duplicates."""

def unpack_a_nest(nested_list):
    if type(nested_list) is not list:
        return "Invalid input."
    if len(nested_list) == 0:
        return []
    return list(set([number for sublist in nested_list for number in sublist]))

print(unpack_a_nest([[12, 34, 56, 67], [34, 68, 78]]))  # [34, 67, 68, 12, 78, 56]