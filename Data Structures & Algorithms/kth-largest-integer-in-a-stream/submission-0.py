class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.tree = nums
        heapq.heapify(self.tree)
        while len(self.tree) > self.k:
            heapq.heappop(self.tree)

    def add(self, val: int) -> int:
        heapq.heappush(self.tree, val)
        if len(self.tree) > self.k:
            heapq.heappop(self.tree)
        return self.tree[0]
