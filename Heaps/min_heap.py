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

    def is_full(self) -> bool:
        """
        Invoked just before insertion to check whether there is room.
        """
        return self.size == self.capacity

    def swap(self, index1: int, index2: int) -> None:
        """Swap the data between the two given indexes."""
        tmp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = tmp

    def insert(self, data: int) -> None:
        """Insert data into the heap."""
        if self.is_full():
            raise Exception("Heap at full capacity. No insertion allowed.")
        self.storage[self.size] = data
        self.size += 1
        # self.iterative_heapify_up()
        self.recursive_heapify_up(self.size - 1)

    def iterative_heapify_up(self) -> None:
        """Enforce the heap principle. (from current index upwareds)"""
        idx = self.size - 1
        while (
            self.has_parent(idx) and
            self.parent(idx) > self.storage[idx]
        ):
            self.swap(self.get_parent_index(idx), idx)
            idx = self.get_parent_index(idx)

    def recursive_heapify_up(self, index: int) -> None:
        """Heapify recursively."""
        if (
            self.has_parent(index) and
            self.parent(index) > self.storage[index]
        ):
            self.swap(self.get_parent_index(index), index)
            self.recursive_heapify_up(self.get_parent_index(index))

    def remove_min(self) -> int:
        """Remove and return minimum value from heap."""
        if self.size == 0:
            raise Exception("Heap is already empty!")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.storage.pop()
        # self.iterative_heapify_down()
        self.recursive_heapify_down(0)
        return data

    def iterative_heapify_down(self) -> None:
        """Enforce the heap principle. (from root downwards)"""
        index = 0
        while (self.has_left_child(index)):
            smaller_child_idx = self.get_left_child_index(index)
            if (
                self.has_right_child(index) and
                self.right_child(index) < self.left_child(index)
            ):
                smaller_child_idx = self.get_right_child_index(index)
            if self.storage[index] < self.storage[smaller_child_idx]:
                break
            else:
                self.swap(index, smaller_child_idx)
            index = smaller_child_idx

    def recursive_heapify_down(self, index: int) -> None:
        """Heapify down recursively."""
        smallest = index
        if (
            self.has_left_child(index) and
            self.storage[smallest] > self.left_child(index)
        ):
            smallest = self.get_left_child_index(index)
        if (
            self.has_right_child(index) and
            self.storage[smallest] > self.right_child(index)
        ):
            smallest = self.get_right_child_index(index)
        if smallest != index:
            self.swap(index, smallest)
            self.recursive_heapify_down(smallest)
