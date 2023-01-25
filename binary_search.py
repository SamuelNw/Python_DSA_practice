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


def binary_search_iterative(input_array, value):
    """
        - Handle edge cases of array being empty or being with just one value.
        - Have 2 variables for the start and end indexes, that will change per iteration. 
        - As long as the start index is lesser than or equal to the end index:
            - get the middle index of the [start, end]. 
            - get the value in that middle index.
            - check if that middle value is equal to the value being searched for, and if so, return that index.
            - if it is lesser, make the start index one more the current middle index and repeat. 
            - if greater, make the end index one lesser than the current middle index and repeat. 
        - If the start index is no longer lower than or equal to the end index, the value is not in the array.
    """
    if len(input_array) == 0 or (len(input_array) == 1 and not input_array[0] == value):
        return -1

    start_index = 0
    end_index = len(input_array) - 1

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2
        mid_value = input_array[middle_index]
        if mid_value == value:
            return middle_index
        elif mid_value < value:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))

