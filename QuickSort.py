"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    if len(array) > 1:
        # set the last element to be pivot 
        pivot = array[-1]
        compareIndex = 0
        pivotIndex = len(array)-1
        for i in range(len(array)-1):
            # if the comparison element is greater than pivot,
            # put comparison element in pivot position, the element before
            # pivot to comparison position and move pivot forward one position
            if array[compareIndex] > pivot:
                array[pivotIndex] = array[compareIndex]
                array[compareIndex] = array[pivotIndex-1]
                array[pivotIndex-1] = pivot
                pivotIndex -= 1
            else:
                compareIndex += 1
        # after swapping, the pivot now is in the right position,
        # do quicksort recursively to the part before and after pivot
        return quicksort(array[:pivotIndex])+[pivot]+quicksort(array[pivotIndex+1:])
    else:
        return array
                

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)