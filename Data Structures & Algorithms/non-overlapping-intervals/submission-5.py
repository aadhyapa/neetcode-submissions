class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
                continue
            prevEnd = min (prevEnd, intervals[i][1])
            res += 1    
        return res