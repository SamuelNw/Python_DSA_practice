"""
    **NOTES**
    - A Linked list is a linear collection of data elements whose order is not determined by the physical placements 
    of the elements in memory, rather each element has an attribute that points to the next element.
    - In comparison to lists, while lists have an advantage of lesser complexity in accessing elements, linked lists
    have a better efficiency in insertion and deletion of elements. Moreso, linked lists have better memory 
    utilization as memory is allocated and deallocated in run-time as opposed to that of arrays that happen in 
    compile-time.

    -The following is an implementation of a linked list, along with various functionalities.
"""


# node class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# linked_list implementation.
class Linked_list(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
            - If the linked list is empty, make the new_element the head.
            - If not:
                - Assign the pointer to a variable current, which is initially the head.
                - Continuously check for the element after 'current' being None, so you can assign the new_element
                to it.
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def show(self):
        """
            - In order to show the values of the linked list (as an array of values), initiate an empty array.
            - As long as the linked_list is not empty, append to values, the value of each node, while moving
            the pointer to the next node after each iteration.
        """
        values = []
        node = self.head
        if self.head:
            while node is not None:
                # print(node.value)
                values.append(node.value)
                node = node.next
            print(values)
        return

    def get_position(self, position):
        # gets an element at a certain position assuming the first position is 1
        """
            - Use two variables, one for the current node, and another for the count,
            which will be incremented in each iteration, and count will be compared to position such that 
            when count is equal to position, the value for the current node will be the target value.
        """
        if self.head:
            current_node = self.head
            current_position = 1
            if current_position == position:
                print(current_node.value)
                return
            while position > current_position:
                current_node = current_node.next
                current_position += 1
            print(current_node.value)
        return None

    def insert(self, new_element, position):
        # if we are inserting the new element at position 1:
        head_pos = self.head
        if position == 1:
            self.head = new_element
            new_element.next = head_pos
            return
        """
            - There is need for three variables:
                prev, which will be originally None
                current, will originally be the head
                count, will be compared to position, such that when position is equal to count, 
                make the prev.next point to new element, and the new element's next be equal to the original prev.next
        """
        # inserting at any other position
        count = 1
        current = head_pos
        prev = None
        while position > count:
            prev = current
            if current:
                current = current.next
                count += 1
            else:
                print("position out of range!")
                return

        address_to_current = prev.next
        prev.next = new_element
        new_element.next = address_to_current

    def sum_list(self):
        """
            - have a variable to hold the initial sum which is zero.
            - traverse through the linked_list adding the value for each node onto sum.
        """
        summation = 0
        if self.head == None:
            return summation
        current = self.head

        while current != None:
            summation += current.value
            current = current.next
        print(summation)

    def delete(self, value):
        """
            - Return head.next as the new head if value for head is the same as value given.
            - Traverse the list such that, as long as current and current.next are not none:
                - if current.next value is equal to the value, set the current.next to 
                current.next.next
        """
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current != None and current.next != None:
            if current.next.value == value:
                current.next = current.next.next
                return  # since we are to delete the first element only.
            else:
                current = current.next

    def reverse_list(self):
        # should return the new head of the linked list
        """
            - Variables needed include - prev (originally null), current (originally head), and 
            in each iteration initiate a next_node value to hold the current.next for that instant. Traverse the
            list while moving each one step forward. Last step will have prev on the new head, so return it.
        """

        # variables
        prev = None
        current = self.head

        if self.head == None:
            return None

        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        print(f"New head is {prev.value}")


# Instantiating nodes.
node_1 = Node("a")
node_2 = Node("b")
node_3 = Node("c")
node_4 = Node("d")
node_5 = Node("e")
node_6 = Node("f")
node_7 = Node("z")
node_8 = Node("r")
node_9 = Node("q")
node_10 = Node("s")
node_11 = Node("t")
node_12 = Node("w")
node_13 = Node("python")
node_14 = Node("stuff")
node_15 = Node("javascript")
node_16 = Node("echo")

# Instantiating the linked_list with a node_1 as the head
l_list = Linked_list(node_1)

# Using the append method to add a few nodes to the linked list
l_list.append(node_2)
l_list.append(node_3)
l_list.append(node_4)
l_list.append(node_5)
l_list.append(node_6)
l_list.append(node_7)
l_list.append(node_8)


l_list.insert(node_13, 3)
l_list.insert(node_14, 10)
l_list.insert(node_15, 10)
