"""Create a function called save_emails. This function takes no
arguments but asks the user to input email, and it saves the
emails in a CSV file. The user can input as many emails as they
want. Once they hit ‘done’ the function saves the emails and
closes the file. Create another function called open_emails.
This function opens and reads the content of the CSV file. Each
email must be in its line. Here is an example of how the emails
must be saved:
jj@gmail.com
kate@yahoo.com
and not like this:
jj@gmail.comkate@yahoo.com"""

import csv

def save_emails():
    with open("emails.csv", "w") as file:
        writer = csv.writer(file)
        while True:
            email = input("Enter email: ")
            if email == "done":
                break
            writer.writerow([email])


def open_emails():
    with open("emails.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                print(row[0])


save_emails()
open_emails()
