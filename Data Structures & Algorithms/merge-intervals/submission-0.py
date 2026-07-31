class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        ind = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[ind][1]:
                res[ind][1] = max(res[ind][1], intervals[i][1])
                res[ind][0] = min(res[ind][0], intervals[i][0])
            else:
                res.append(intervals[i])
                ind += 1
        return res