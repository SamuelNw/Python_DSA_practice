class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        """
        Info: The rule is to check repeatedly to ensure that new_val goes 
        to the right of a parent node, if it is larger than this parent and that spot 
        is empty, or to the left, if it is lesser, and that spot is empty.

        - Note that the tree's root must always be checked so as to know what 
        side of the root that the insertion process happens
        """
        # make the new value the root if the tree is empty
        if self.root == None:
            self.root = Node(new_val)

        # use the root as the initial pointer
        current = self.root
        while True:
            if new_val >= current.value:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = Node(new_val)
                    break
            else:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = Node(new_val)
                    break

    def search(self, find_val):
        """
        Info: Following the same rules as those in insertion, only this time
        we are looking for each node that we arrive at, and comparing it to the 
        target value.
        """
        # the tree is empty return False
        if self.root == None:
            return False

        current = self.root
        while current != None:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                current = current.right
            else:
                current = current.left
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
