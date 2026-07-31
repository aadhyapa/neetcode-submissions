class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def binarySearch(l, r):
            mid = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)

            if totalTime < h:
                return binarySearch(l, mid - 1)
            elif totalTime > h:
                return binarySearch(mid + 1, r)
            else:
                return mid

        n = len(piles)
        m = max(piles)
        l, r = 1, m

        k = 0

        while l <= r:
            mid = (l + r) // 2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p) / mid)

            if totalTime > h:
                l = mid + 1
            elif totalTime <= h:
                k = mid
                r = mid - 1
        return k