class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: {} for i in range(n + 1)}
        for u, v, t in times:
            if u not in graph:
                graph[u] = {}
            graph[u][v] = t

        track = [(0, k)]
        visited = set()
        res = 0
        while track:
            ut, u = heapq.heappop(track)
            if u in visited:
                continue
            res = ut
            visited.add(u)
            
            for v, t in graph[u].items():
                if v not in visited:
                    heapq.heappush(track, (ut + t, v))
        return res if len(visited) == n else -1