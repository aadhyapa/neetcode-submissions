class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        count = 0
        visited = [0 for i in range(n)]
        visiting = [0 for i in range(n)]
        def dfs(node, parent):

            if visited[node] == 1:
                return

            if visiting[node] == 1:
                return

            visiting[node] = 1

            for e in graph[node]:
                if e == parent:
                    continue
                dfs(e, node)

            visiting[node] = 0
            visited[node] = 1

        for i in range(n):
            if visited[i] == 0:
                count += 1
                dfs(i, -1)

        return count