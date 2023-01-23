"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
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
                #print(node.value)
                values.append(node.value)
                node = node.next
            print(values)
        return

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        """
            - If the linked_list is empty, the new element is made the head.
            - store the reference to the original head, then append the new element
            and make its next value to be the that original head.
        """
        if self.head == None:
            self.head = new_element
            return
        current = self.head
        self.head = new_element
        new_element.next = current

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        """
            - If the linked list is empty, return None
            - if only one node is present, make None the head and return the original head.
            - else, save the address for head and head.next, then make head.next the current head, whilst
            storing head.value just before deleting it.
        """
        if self.head == None: 
            return None
        elif self.head.next == None:
            popped = self.head.value
            self.head = None
            return popped
        else: 
            original_head = self.head
            popped = original_head.value            
            new_head = self.head.next 
            del self.head 
            self.head = new_head 
            return popped
            

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        return 

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        node_deleted = self.ll.delete_first()
        if node_deleted:
            return Element(node_deleted)                #return it as a node
        else:
            return None

    
    def show_stack(self):
        self.ll.show()

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)          #adds e2 to the top of the stack
stack.push(e3)          #adds e2 to the top of the stack

print(stack.pop().value)                #prints 3
print(stack.pop().value)                #prints 2
print(stack.pop().value)                #prints 1
print(stack.pop())                      #returns None since the list is empty
stack.push(e4)                          #adds 4 to the empty stack

print(stack.pop().value)                #prints 4