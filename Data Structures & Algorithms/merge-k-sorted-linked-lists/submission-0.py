# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        root = None
        while heap:
            val, i, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            if not root:
                root = node
                curr = node
            else:
                node.next = None
                curr.next = node
                curr = curr.next
        return root
            
