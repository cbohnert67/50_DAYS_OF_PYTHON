"""Write a function called find_index that takes two arguments;
a list of integers, and an integer. The function should return the
indexes of the integer in the list. If the integer is not in the list,
the function should convert all the numbers in the list into the
given integer.
For example, if the list is: [1, 2, 4, 6, 7, 7] and the integer is 7,
your code should return [4, 5] as the indexes of 7 in the list. If
the list is [1, 2, 4, 6, 7, 7] and the integer is 8, your code should
return [8, 8, 8, 8, 8, 8] because 8 is not in the list."""

def find_index(lst, num):
    if type(lst) != list or type(num) != int:
        return "Invalid input"
    if num not in lst:
        return [num for _ in lst]
    return [i for i in range(len(lst)) if lst[i] == num]

print(find_index([1, 2, 4, 6, 7, 7], 7))  # [4, 5]
print(find_index([1, 2, 4, 6, 7, 7], 8))  # [8, 8, 8, 8, 8, 8]
print(find_index([1, 2, 4, 6, 7, 7], "7"))  # Invalid input
print(find_index("1, 2, 4, 6, 7, 7", 7))  # Invalid input
print(find_index([1, 2, 4, 6, 7, 7], 7.0))  # Invalid input