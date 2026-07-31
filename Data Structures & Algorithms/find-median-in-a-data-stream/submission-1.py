class MedianFinder:

    def __init__(self):
        self.first, self.second = [], []
        self.size = 0

    def addNum(self, num: int) -> None:
        # check if second minHeap
        # check if first maxHeap
        if self.size == 0:
            heapq.heappush(self.second, num)
        else:
            if self.first and num <= self.first[0]:
                heapq.heappush_max(self.first, num)
            else:
                 heapq.heappush(self.second, num)

            while len(self.first) > len(self.second):
                node =  heapq.heappop_max(self.first)
                heapq.heappush(self.second, node)
            while len(self.second) > len(self.first) + 1:
                node =  heapq.heappop(self.second)
                heapq.heappush_max(self.first, node)
        self.size += 1
        

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (self.first[0] + self.second[0])/2
        else:
            return self.second[0]
        