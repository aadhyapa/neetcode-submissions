
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        hm = {}
        root = Node(node.val)
        hm[node.val] = root


        # q = deque()
        # q.append(node)
        # while q:
        #     size = len(q)
        #     for _ in range(size):
        #         curr = q.popleft()
        #         new_node = Node(node.val)
        #         hm[curr.val] = new_node
        #         for adj in curr.neighbors:
        #             q.append(adj)
        #             if adj.val in hm:
        #                 nei_node = hm[adj.val]
        #             else:
        #                 nei_node = Node(adj.val)
        #             hm[adj.val] = nei_node
        #             curr.neighbors.append(nei_node)
        visited = set()
        def dfs(new_parent, new_curr, curr):
            nonlocal hm
            for adj in curr.neighbors:
                if adj.val in hm:
                    new_nei = hm[adj.val]
                else:
                    new_nei = Node(adj.val)
                    hm[adj.val] = new_nei
                    dfs(new_curr, new_nei, adj)
                new_curr.neighbors.append(new_nei)
                if new_parent and adj.val == new_parent.val:
                    continue
        
        dfs(None, root, node)

        return root

        