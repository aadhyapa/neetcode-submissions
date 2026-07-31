"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        hm = {}
        visited = []
        def dfs(node):
            if node not in visited:
                visited.append(node)
                if node not in hm:
                    new_node = Node(node.val)
                    hm[node] = new_node
                for neighbor in node.neighbors:
                    if neighbor not in hm:
                        new_neighbor = Node(neighbor.val)
                        hm[neighbor] = new_neighbor
                    hm[node].neighbors.append(hm[neighbor])
                    dfs(neighbor)      
            else:
                return 
        temp = Node(node.val)
        hm[node] = temp
        dfs(node)
        
            
        return hm[node]

