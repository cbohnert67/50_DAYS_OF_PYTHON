"""list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
Write a function called missing_numbers that takes a list of
sequence of numbers and finds the missing numbers in the
sequence. The list above should return:
[4, 8, 10, 13, 16, 29, 30]"""

def missing_numbers(lst):
    if type(lst) != list:
        return "Invalid input"
    lst.sort()
    missing = []
    for i in range(lst[0], lst[-1]):
        if i not in lst:
            missing.append(i)
    return missing

print(missing_numbers([1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17]))   # [4, 8, 10, 13, 16, 18, 19, 20, 21, 22]
print(missing_numbers([1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]))   # [4, 8, 10, 13, 16, 29, 30]
print(missing_numbers([1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]))   # [4, 8, 10, 13, 16, 29, 30]