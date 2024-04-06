"""Write a function called middle_figure that takes two
parameters a, and b. The two parameters are strings. The
function joins the two strings and finds the middle element.
If the combined string has a middle element, the function should
return the element, otherwise, return ‘no middle figure’. Use
‘make love’ as an argument for a and ‘not wars’ as an
argument for b. Your function should return ‘e’ as the middle
element. Whitespaces should be removed."""

def middle_figure(a, b):
    if type(a) is not str or type(b) is not str:
        return "Invalid input."
    combined = a + b
    middle = len(combined) // 2
    if len(combined) % 2 == 0:
        return "no middle figure"
    return combined[middle]

print(middle_figure('make love', 'not wars'))  # e
print(middle_figure('make love', 'not war'))  # no middle figure
print(middle_figure('make love', 5))  # Invalid input.
print(middle_figure('make love', []))  # Invalid input.
