"""Write a function called search_binary that searches for the
number 22 in the following list and returns its index. The
function should take two parameters, the list and the item that
is being searched for. Use binary search (iterative Method)."""

def search_binary(lst, item):
    low = 0
    high = len(lst) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < item:
            low = mid + 1
        elif lst[mid] > item:
            high = mid - 1
        else:
            return mid
    return None

list1 = [12, 34, 56, 78, 98, 22, 45, 13]
list1.sort()
print(search_binary(list1, 22))