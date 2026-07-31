# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        # store the max parent for the node
        # compare current node to that parent

        def dfs(root, max_height):
            nonlocal good_nodes

            if root is None:
                return

            if root.val >= max_height:
                good_nodes += 1

            dfs(root.left, max(max_height, root.val))
            dfs(root.right, max(max_height, root.val))

        dfs(root, -float('inf'))
        return good_nodes