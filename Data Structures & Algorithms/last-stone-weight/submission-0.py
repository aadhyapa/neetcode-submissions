class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            e1 = heapq.heappop_max(stones)
            e2 = heapq.heappop_max(stones)
            if e1 - e2 != 0:
                heapq.heappush_max(stones, e1 - e2)

        return 0 if not stones else stones[0]
