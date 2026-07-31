class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eucledian(x, y):
            return math.sqrt(x**2 + y**2)

        maxHeap = []
        for x, y in points:
            heapq.heappush(maxHeap, [-eucledian(x, y), x, y])

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        

        return res