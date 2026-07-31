class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1, 0, -1):
            y = target - nums[i]
            if y in nums[:i]:
                j = nums[:i].index(y)
                return j, i