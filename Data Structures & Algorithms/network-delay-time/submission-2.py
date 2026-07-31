class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, t in times:
            graph[u].append((v, t))

        minHeap = [(0, k)]
        visit = set()
        tt = 0
        while minHeap:
            t, u = heapq.heappop(minHeap)
            if u in visit:
                continue
            visit.add(u)
            tt = t
            for v1, t1 in graph[u]:
                if v1 not in visit:
                    heapq.heappush(minHeap, (t1 + t, v1))

        return tt if len(visit) == n else -1

        