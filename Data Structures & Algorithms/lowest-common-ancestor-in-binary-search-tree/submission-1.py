# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #bfs
        lower, higher = min(p.val, q.val), max(p.val, q.val)
    
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.val == lower or node.val == higher:
                    return node
                if node.val > lower and node.val < higher:
                    return node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

