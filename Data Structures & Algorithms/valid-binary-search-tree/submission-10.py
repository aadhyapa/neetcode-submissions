# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini, maxi = -float('inf'), float('inf')
        def dfs(mini, maxi, curr):
            if curr is None:
                return True
            if curr.val >= maxi or curr. val <= mini:
                return False
            return (dfs(mini, curr.val, curr.left) and dfs(curr.val, maxi, curr.right))
            
        return dfs(mini, maxi, root)