class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dist = nums[0]
        for i in range(1, len(nums)):
            dist -= 1
            if dist < 0:
                return False
            if nums[i] > dist and i != len(nums) - 1:
                dist = nums[i]
        return True
