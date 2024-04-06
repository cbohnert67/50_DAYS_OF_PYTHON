"""Write a function called largest_number that takes a list of
integers and re-arrange the individual digits to create the largest
number possible. For example, if you pass the following as an
argument: list1 = [3, 67, 87, 9, 2]. Your code should return the
number in this exact format: 9,877,632 as the largest number."""

def largest_number(numbers):
    if type(numbers) is not list:
        return "Invalid input."
    return int(''.join(sorted([str(i) for i in numbers], reverse=True)))

list1 = [3, 67, 87, 9, 2]
print(largest_number(list1))  # 987632
list2 = [3, 67, 87, 9, 2, 0]
print(largest_number(list2))  # 9876320
list3 = [3, 67, 87, 9, 2, 0, 0]
print(largest_number(list3))  # 98763200
list4 = [3, 67, 87, 9, 2, 0, 0, 0]
print(largest_number(list4))  # 987632000