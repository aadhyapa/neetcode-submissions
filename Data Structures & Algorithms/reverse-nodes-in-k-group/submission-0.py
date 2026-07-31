# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        groups = size // k

        count, group_count = 0, 0
        prev_tail, root  = None, None

        # if we reach groups, stop
            # attach current prev tail to the current node and return
        
        curr = head
        prev = None
        while curr:
            if count == 0:
                curr_root = curr
            
            # reversing logic
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

            count += 1

            if count == k:
                group_count += 1

                if prev_tail:
                    prev_tail.next = prev
                else:
                    root = prev

                prev_tail = curr_root
                prev = None
                count = 0

                if group_count == groups:
                    prev_tail.next = curr
                    break

        return root

            
            
            
