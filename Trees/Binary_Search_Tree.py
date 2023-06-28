"""
INFO: Implementation of a Binary Search Tree.
    - Creation.
    - Inserting Nodes (without duplicates).
    - Searching for nodes (returning True/False if target nodes are present).
    - Printing the nodes of the tree (BFS and DFS)
    - Deletion of nodes.
"""
import collections

# TreeNode class:


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BST Class:


class BST(object):
    def __init__(self):
        self.root = None

# INSERT:
    # Iterative insertion solution.
    def insert_node_iterative(self, value):
        """
        Info: If the tree is empty, make the value the root.
            - If it is not empty, check whether it is larger than the root
            meaning that insertion happens on the right, and if it is smaller,
            insertion happens on the left.
        """
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value > current.value:
                    if current.right != None:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break
                elif value < current.value:
                    if current.left != None:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break
                else:
                    # duplicates
                    print(f"{value} is already in the tree. No duplicates allowed.")
                    break

    # Recursive insertion solution.
    def insert_node_recursive(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_node(self.root, value)

    def _add_node(self, current, value):
        if value > current.value:
            if not current.right:
                current.right = Node(value)
            else:
                self._add_node(current.right, value)
        elif value < current.value:
            if not current.left:
                current.left = Node(value)
            else:
                self._add_node(current.left, value)
        else:
            print(f"{value} already in tree. No duplicates allowed.")
            return

# SEARCH:
    # Iterative search solution.
    def search_node_iterative(self, value):
        """
        Info: If the value is greater than the root.value, repeatedly search the
        right side of the tree. If the value is smaller, repeatedly search the
        left side of the tree.
        """
        if not self.root:
            return False
        current = self.root
        while True:
            if current.value == value:
                return True
            elif current.value > value:
                if current.left:
                    current = current.left
                    continue
                break
            else:
                if current.right:
                    current = current.right
                    continue
                break
        return False

    # Recursive searching solution.
    def search_node_recursive(self, value):
        if not self.root:
            return False
        is_found = self._find(self.root, value)
        if is_found:
            return True
        return False

    def _find(self, root, value):
        if root:
            if root.value == value:
                return True
            elif root.value > value:
                return self._find(root.left, value)
            else:
                return self._find(root.right, value)
        return False

# TRAVERSAL AND PRINTING TREE NODES PRESENT
    # Breadth First Search
    # (1) Prints the result in the form "a-b-c-d-e"...
    def breadth_first_search_1(self):
        if not self.root:
            return None
        else:
            self._bfs_1(self.root)

    def _bfs_1(self, root):
        q = collections.deque()                 # Because deques use FIFO technique
        result = []
        q.append(root)
        while len(q) != 0:
            current = q.popleft()
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            result.append(current.value)

        print("-".join(map(str, result)))

    # (2) Prints the result in the form of an array of arrays of the different tree levels
    def breadth_first_search_2(self):
        if not self.root:
            return None
        else:
            self._bfs_2(self.root)

    def _bfs_2(self, root):
        q = collections.deque()
        result = []
        q.append(root)
        while q:
            q_length = len(q)
            level = []

            for _ in range(q_length):
                # Storing q_lenth ensures this loop only runs for enough times
                # (same as the number of nodes in a certain level)
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                level.append(current.value)
            result.append(level)

        print(result)

    # Depth First Iteration
    # (1a.) Pre-Order Iterative
    def pre_order_iterative(self):
        if not self.root:
            return None
        else:
            self._pre_order(self.root)

    def _pre_order(self, root):
        result = []
        stack = [root]

        while len(stack) > 0:
            current = stack.pop()
            result.append(current.value)
            # Append the right child first since stack uses LIFO concept.
            # meaning the left nodes will be added to the results first
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        print("-".join(map(str, result)))

    # (1b.) Pre-order Recursive   (prints node values one by one)
    def pre_order_recursive(self):
        if not self.root:
            return None
        else:
            self._pre_order_2(self.root)

    def _pre_order_2(self, root):
        if not root:
            return None

        # visit the parent before the children
        print(root.value)
        self._pre_order_2(root.left)
        self._pre_order_2(root.right)

    # (2a.) In-order Recursive              (prints nodes one by one)
    def in_order(self):
        if not self.root:
            return None
        else:
            self._in_order(self.root)

    def _in_order(self, root):
        if not root:
            return None

        # Visit the parent after visiting the left child only
        self._in_order(root.left)
        print(root.value)
        self._in_order(root.right)

    # (2b.) In-order Iterative

    def in_order_iterative(self):
        if not self.root:
            return None
        else:
            self._in_order_iter(self.root)

    def _in_order_iter(self, root: Node) -> list:
        if not root:
            return None

        stack = []
        current = root
        res = []

        while stack or current:
            while current:
                stack.append(current)
                current = current.next

            current = stack.pop()
            res.append(current.val)
            current = current.right

        return res

    # (2c.) Post-order Recursive

    def post_order(self):
        if not self.root:
            return None
        else:
            self._post_order(self.root)

    def _post_order(self, root):
        if not root:
            return None

        # visit the parent after visiting both the left and right child
        self._post_order(root.left)
        self._post_order(root.right)
        print(root.value)

# DELETING NODES ON A TREE
    def delete_node(self, node):
        if not self.root:
            return None
        else:
            self._delete(self.root, node)

    def _delete(self, root, target):
        if not root:
            return None
        if target == root.value:
            if not root.left and not root.right:
                return None
            if not root.left and root.right:
                return root.right
            if root.left and not root.right:
                return root.left
            """
            Info: The root here, has both right and left children.
            Trick is to replace the root at this point (current) with NEXT MINIMUM
            value from current.right. If current.right has no children, that is our
            node, if it does, the left-most node from here, is the node we are looking for.
            """
            pointer = root.right
            while pointer.left:
                pointer = pointer.left
            root.value = pointer.value
            root.right = self._delete(root.right, root.value)
        elif target > root.value:
            root.right = self._delete(root.right, target)
        else:
            root.left = self._delete(root.left, target)
        return root
