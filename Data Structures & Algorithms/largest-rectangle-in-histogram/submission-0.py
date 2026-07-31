class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        start = 0
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[i] <= heights[stack[-1]]):
                prev_h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                res = max(res, prev_h * w)
            stack.append(i)

        return res