"""
Implementation of a minHeap.
"""


class MinHeap:
    """MinHeap Implementation."""

    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity        # max number of elements to store.
        self.size = 0       # number of elements to currently within the heap.

    def get_parent_index(self, index: int) -> int:
        """
        Get the index of the parent of a given node.
        index -> index of the node.
        """
        return (index - 1) // 2

    def get_left_child_index(self, index: int) -> int:
        """
        Get the index of the left child of a given node.
        index -> index of the node.
        """
        return (index * 2) + 1

    def get_right_child_index(self, index: int) -> int:
        """
        Get the index of the right child of a node.
        index -> index of the node.
        """
        return (index * 2) + 2

    def has_parent(self, index: int) -> bool:
        """
        Return True if the node at index has a parent, False otherwise.
        """
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index: int) -> bool:
        """
        Return True if the left child index is lesser than the
        size (current num of elements).
        """
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index: int) -> bool:
        """
        Return True if the right child index is lesser than the size.
        """
        return self.get_right_child_index(index) < self.size

    # Get the actual node data
    def parent(self, index: int) -> int:
        return self.storage[self.get_parent_index(index)]

    def left_child(self, index: int) -> int:
        return self.storage[self.get_left_child_index(index)]

    def right_child(self, index: int) -> int:
        return self.storage[self.get_right_child_index(index)]
