class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            indN = nums[abs(num) - 1]
            if indN < 0:
                return abs(num)
            nums[abs(num) - 1] *= -1