
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Use a hashmap to keep track of the new node create
# Don't turn the hashmap into the graph. The graph is still the graph
# The purpose of the hashmap is to simply make sure we have the node we created

# Time complexity of this is O(V^2 + E) because of the list look-ups
class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        hm = {}

        def dfs(node):
            if node not in hm:
                new_node = Node(node.val)
                hm[node] = new_node
                for neighbor in node.neighbors:
                    hm[node].neighbors.append(dfs(neighbor))
                return new_node
            else:
                return hm[node]
        

        return dfs(node)

# Optimal