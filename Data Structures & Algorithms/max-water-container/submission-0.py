class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l, r = 0, len(height) - 1
        previus_max = max(height)
        while l < r:
            max_area = max(max_area, min(height[l],height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
            if max_area >= previus_max * (r - l):
               break 
        return max_area