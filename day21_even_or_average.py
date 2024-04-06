"""Write a function called even_or_average that ask a user to
input five numbers. Once the user is done, the code should
return the largest even number in the inputted numbers. If
there is no even number in the list, the code should return the
average of all the five numbers."""

def even_or_average():
    numbers = []
    for i in range(5):
        number = int(input("Enter a number: "))
        numbers.append(number)
    even_numbers = [number for number in numbers if number % 2 == 0]
    if len(even_numbers) == 0:
        return sum(numbers) / 5
    return max(even_numbers)

print(even_or_average())