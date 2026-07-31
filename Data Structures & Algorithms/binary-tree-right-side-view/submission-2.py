# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return[]
        right_nodes = []
        
        def dfs(root, depth):
            nonlocal right_nodes
            if not root:
                return

            if depth == len(right_nodes):
                right_nodes.append(root.val)

            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)
        return right_nodes

