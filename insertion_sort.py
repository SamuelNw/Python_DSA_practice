"""
    - The way this algorithm works, is that, it traverses an array from the beginning, for each element,
    it compares it with the previous elements (if any), and places that element in the rightful location 
    as required. Say arranging in an ascending order, of list [5,2,3,11], since no element before 5, it 
    swiftly moves to 2, checks if 5 is greater than it, and places the 2 before the 5, and moves on to 3. This
    it checks both 5 and 2, placing 3 between the two numbers, and moves on, till the end of the array.
"""


def insertion_sort(array):
    """
        - for each item (if it is not the first item), store it in a variable current. 
            - loop through the items before it, pushing each of these items that are larger than
            current to the right to create space for that value current.
    """
    for i in range(1, len(array)):                  # start from the second element
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current
    return array


list_1 = [5, 2, 3, 15, 9, 30, 1, 11]
print(insertion_sort(list_1))           # prints [1, 2, 3, 5, 9, 11, 15, 30]
