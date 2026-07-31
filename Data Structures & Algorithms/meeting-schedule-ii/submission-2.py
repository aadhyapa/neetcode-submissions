"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        minheap = []
        intervals.sort(key=lambda i: i.start)
        for i in intervals:
            if minheap and minheap[0] <= i.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, i.end)
        return len(minheap)