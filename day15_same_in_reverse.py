"""Write a function called same_in_reverse that takes a string
and checks if the string reads the same in reverse. If it is the
same, the code should return True if not, it should return False.
For example, ‘dad’ should return True, because it reads the
same in reverse."""

def same_in_reverse(string):
    if type(string) is not str:
        return "Invalid input."
    return string == string[::-1]

print(same_in_reverse("dad"))  # True
print(same_in_reverse("Hello"))  # False
print(same_in_reverse(5))  # Invalid input.
print(same_in_reverse("madam"))  # True
print(same_in_reverse("madame"))  # False
print(same_in_reverse(""))  # True
print(same_in_reverse("a"))  # True