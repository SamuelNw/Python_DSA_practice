class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        # Pre-Order Depth First Search.
        """
        - Return True if the value is in the tree, return False otherwise.
            - use a stack (implement it with a list) and initiate it with the root as first object. 
            - as long as the stack has an item, continue iterating.
            - for each iteration:
                - begin by assigning "current" to the value you pop from the stack.
                - check if the value for current is the target value and return true if so.
                - if it is not the value (meaning iteration continues);
                    - conditionally append the right and left children to the stack.
                    (the right children are appended first, so that the left nodes can be visited(popped) first)
        """
        stack = [self.root]
        while len(stack) != 0:
            current = stack.pop()
            if current.value == find_val:
                return True
            else:
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)

        return False

    def print_tree(self):
        """
            - Print out all tree nodes as they are visited in a pre-order traversal.
            - Logic similar to the search function above, only, there is no checking for
            target values, just printing the value for each node you visit
        """
        stack = [self.root]
        values = []
        while len(stack) != 0:
            current = stack.pop()
            values.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        print("-".join(map(str, values)))


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.right = Node(25)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
tree.print_tree()
