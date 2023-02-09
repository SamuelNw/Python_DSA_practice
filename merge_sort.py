"""
    - This algorithm uses divide and conquer concept - divides the array into half repeatedly
    then builds up one sorted array from these halves.
"""


def merge_sort(array):
    # base case for stopping the recursion is if the subarrays get to a length of 1
    if len(array) <= 1:
        return array

    mid_point = len(array)//2
    left_array = merge_sort(array[:mid_point])
    right_array = merge_sort(array[mid_point:])

    return merge_subarrays(left_array, right_array)


def merge_subarrays(list_1, list_2):
    result = []  # appending the sorted numbers
    i = 0                           # starting index for the list_1
    j = 0                           # starting index for the list_2

    while i < len(list_1) and j < len(list_2):  # means the lists have values
        if list_1[i] < list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    # when either of the lists are empty, just append the contents of the remaining one to the result list.
    result += list_1[i:]
    result += list_2[j:]

    return result


some_list = [10, 2, 45, 12, 3]
print(merge_sort(some_list))
