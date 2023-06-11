# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # O(n) Space complexity
        """
        arr = []
        current = head

        while current:
            arr.append(current.val)
            current = current.next

        ans = 0
        left = 0
        right = len(arr) - 1

        while left < right:
            ans = max(ans, arr[left] + arr[right])
            left += 1
            right -= 1

        return ans
        """

        # O(1) Time complexity
        slow = head
        fast = head

        # get the center of the linkedlist
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linkedlist
        current = slow
        prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        # check twin sums
        # prev is the head of reversed linkedlist
        ans = 0
        while head != slow:
            ans = max(ans, head.val + prev.val)
            head = head.next
            prev = prev.next

        return ans
