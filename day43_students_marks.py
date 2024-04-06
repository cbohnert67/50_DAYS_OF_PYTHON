"""Write a function called student_marks that records marks
achieved by students in a test. The function should ask the user
to input the name of the student and then ask the user to input
the marks achieved by the student. The information should be
stored in a dictionary. The name is the key and the marks is the
value. When the user enters done, the function should return a
dictionary of names and values entered."""

def student_marks():
    marks = {}
    while True:
        name = input("Enter the name of the student: ")
        if name == "done":
            return marks
        mark = int(input("Enter the marks: "))
        marks[name] = mark

print(student_marks())