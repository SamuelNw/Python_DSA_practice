# Bubble sort repeatedly checks adjacent items from the beginning of an unsorted list swapping them if need be.
"""
    - Loop through elements from the first to the second_last checking if one on the left, 
    is larger than one on the right so you can swap them. 
    - Base case is if the array is sorted, then stop looping, so create a variable that will be altered 
    accordingly in each iteration, to hold the state of that list.
"""
def bubble_sort(array):
    new_length = len(array) - 1     #since we shall be comparing values array[i] and array[i+1]
    sorted = False 

    while sorted == False:
        sorted = True               # If no swap will happen in the for loop, it remains true.
        for i in range(new_length):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False

    return array


# The recursive way
def bubble_sort_recursive(array):
    for i in range(len(array)):
        try:
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                bubble_sort_recursive(array)
        except IndexError:
            pass

    return array


list_a = [30,2,58,96,3]
print(bubble_sort(list_a))                          # prints [2, 3, 30, 58, 96]
print(bubble_sort_recursive(list_a))                # prints [2, 3, 30, 58, 96]
