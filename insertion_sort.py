"""
    - This algorithm iterates through the array, inserting each number in the rightful location, 
    on its left, and repeats till the end of the array. As such, by the time it checks the last 
    number, the array is already sorted.
"""

def insertion_sort(array):
    """
        - for each item (if it is not the first item), store it in a variable current. 
            - loop through the items before it, pushing each of these items that are larger than
            current to the right to create space for that value current.
    """
    for i in range(len(array)):
        current = array[i] 
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j+1] = array[j] 
            j -= 1
        array[j+1] = current
    return array 


list_1 = [5,2,10,11]
print(insertion_sort(list_1))           # prints [2,5,10,11]

