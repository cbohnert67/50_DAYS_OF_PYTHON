"""Write a function called prime_numbers. This function asks a
user to enter a number (integer) as an argument and returns a
list of all the prime numbers within its range. For example, if user
enters 10, your code should return [2, 3, 5, 7] as prime numbers."""

def prime_numbers(number):
    if type(number) is not int:
        return "Invalid input."
    if number < 2:
        return "Invalid input."
    prime_numbers = []
    for num in range(2, number):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)
    return prime_numbers

print(prime_numbers(10))  # [2, 3, 5, 7]

