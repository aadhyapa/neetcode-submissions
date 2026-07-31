"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        hm = {}
        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                hm[curr].next = hm[curr.next]
            if curr.random:
                hm[curr].random = hm[curr.random]
            else:
                hm[curr].random = None
            curr = curr.next

        return hm[head]
        