class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = { i: set() for i in range(n)}

        for edge1, edge2 in edges:
            graph[edge1].add(edge2)
            graph[edge2].add(edge1)
        
        discovered = [0 for i in range(n)]
        visited = set()

        def dfs(parent, edge):

            if discovered[edge]:
                return False

            if edge in visited:
                return True
            
            discovered[edge] = 1

            for e in graph[edge]:
                if e == parent:
                    continue

                if not dfs(edge, e):
                    return False
            
            discovered[edge] = 0
            visited.add(edge)

            return True

        res = dfs(-1, 0)

        if len(visited) != n:
            return False

        return res                    
            
