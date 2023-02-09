# Implementation of Quicksort to arrange items in ascending order.
def quick_sort(array):
    """
        - Choose a pivot (number at the end of the array), compare it to the array's items one by one by
        while putting all items smaller than the pivot to the left, and all larger ones to the right, 
        and when this is done, pin down that pivot to that position.
        - since the array is now halved, repeat the above process on each half of the initial array.
    """
    array_length = len(array)

    if array_length <= 1:
        return array
    else:
        pivot = array.pop()
        items_smaller = []
        items_larger = []

        for item in array:
            if item < pivot:
                items_smaller.append(item)
            else:
                items_larger.append(item)

    return quick_sort(items_smaller) + [pivot] + quick_sort(items_larger)


array_1 = [15, 2, 30, 7]
print(quick_sort(array_1))              # prints [2,7,15,30]
