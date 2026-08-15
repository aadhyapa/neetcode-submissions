class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total//2

        if max(nums) > target:
            return False
        
        dp = [False] * (target + 1)
        dp[0] = True 
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]