class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calcDist(p1, p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

        visited = [False] * len(points)
        edges = 0
        dists = [float('inf')] * len(points)
        res = 0
        i = 0
        while edges < len(points) - 1:
            visited[i] = True
            ni = -1
            for j in range(len(points)):
                if visited[j]:
                    continue
                dists[j] = min(dists[j], calcDist(points[i], points[j]))
                if ni == -1 or dists[j] < dists[ni]:
                    ni = j
            if ni != -1:
                res += dists[ni]
                i = ni
                edges += 1
        return res
        

        

