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
        queue = deque()
        queue.append(root)

        while queue:
            breadth = len(queue)
            right_nodes.append(queue[-1].val)
            for i in range(breadth):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_nodes
