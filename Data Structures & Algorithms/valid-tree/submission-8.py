class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]

        #creating an undirected graph
        for e1, e2, in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        visited, visiting = set(), [False] * n
        
        def dfs(parent, edge):
            if edge in visited:
                return True
            if visiting[edge]:
                return False

            visiting[edge] = True
            res = True
            for e in graph[edge]:
                if e == parent:
                    continue
                res = res and dfs(edge, e)
            visited.add(edge)
            visiting[edge] = False
            return res

        return dfs(-1, 0) and len(visited) == n