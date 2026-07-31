# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        
        def checkSame(currRoot, currSubRoot):
            if currRoot is None and currSubRoot is None:
                return True

            if currRoot is None or currSubRoot is None or currRoot.val != currSubRoot.val:
                return False

            return checkSame(currRoot.left, currSubRoot.left) and checkSame(currRoot.right, currSubRoot.right)

        def search(node):
            if node is None:
                return False
            if checkSame(node, subRoot):
                return True
            return search(node.left) or search(node.right)
        return search(root)