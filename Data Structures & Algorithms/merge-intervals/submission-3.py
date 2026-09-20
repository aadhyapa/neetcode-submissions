class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        temp_res = []
        overlapping = True

        for i in range(len(intervals)):
            if not temp_res:
                temp_res.append(intervals[i])
                continue
            if temp_res[-1][1] >= intervals[i][0]:
                temp_res[-1][1] = max(temp_res[-1][1], intervals[i][1])
            else:
                temp_res.append(intervals[i])

        return temp_res
        


