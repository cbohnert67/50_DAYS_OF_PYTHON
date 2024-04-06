"""You want to implement a code that will search for a number in
a range. You have a decision to make as to whether to store the
number in a set or a list. Your decision will be based on time.
You have to pick a data type that executes faster.
You have a range and you can either store it in a set or a list
depending on which one executes faster when you are searching
for a number in the range. See below:
a = range(10000000)
x = set(a)
y = list(a)
Let’s say you are looking for a number 9999999 in the range
above. Search for this number in the list and the set. Your
challenge is to find which code executes faster. You will pick the
one that executes quicker, lists, or sets. Run the two searches
and time them. You can use the time module to time them"""

import time

a = range(10000000)
x = set(a)
y = list(a)

start = time.time()
if 9999999 in x:
    print("Found in set.")
else:
    print("Not found in set.")
print("Time taken to search in set:", time.time() - start)

start = time.time()
if 9999999 in y:
    print("Found in list.")
else:
    print("Not found in list.")
print("Time taken to search in list:", time.time() - start)

