"""
    - This algorithm starts at the beginning of the input array, treating the first value
    as the current minimum, and iterates through the remaining part of the array checking if 
    a number smaller than this current minimum exists, consequently switching their positions.
"""


def selection_sort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

    return array


list_1 = [8, 62, 2, 100, 0, 24]
print(selection_sort(list_1))
