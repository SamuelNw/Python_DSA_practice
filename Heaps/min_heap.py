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
