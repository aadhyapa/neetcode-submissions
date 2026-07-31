# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        visited = Queue()
        visited.put(root)
        result = []
        while not visited.empty():
            temp = []
            size = visited.qsize()
            for i in range(size):
                node = visited.get()
                if node:
                    temp.append(node.val)
                    visited.put(node.left)
                    visited.put(node.right)
            if temp:
                result.append(temp)
        return result

        