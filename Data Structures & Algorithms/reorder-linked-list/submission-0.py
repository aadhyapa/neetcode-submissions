# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        before = slow.next = None
        while right:
            after = right.next
            right.next = before
            before = right
            right = after
        left, right = head, before
        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1
            left, right = tmp1, tmp2
            