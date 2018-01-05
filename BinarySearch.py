"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    count = 0
    upper = len(input_array)-1
    lower = 0
    while upper >= lower:
        count += 1
        middle = int((upper+lower)/2)
        if input_array[middle] == value:
            return middle,count
        elif input_array[middle] < value:
            lower = middle+1
        else:
            upper = middle-1
    return -1,count

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)