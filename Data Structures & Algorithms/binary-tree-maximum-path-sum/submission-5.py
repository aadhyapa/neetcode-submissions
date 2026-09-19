# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(curr):
            nonlocal res
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            right = max(0, right)
            left = max(0, left)
            res = max(res, curr.val + right + left)
            return curr.val + max(right, left)
        dfs(root)
        return res
            