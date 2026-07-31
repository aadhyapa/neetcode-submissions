class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        half = sum(nums) // 2


        memo = {}

        def dfs(currSum, i):
            if i >= len(nums):
                return False
    
            if currSum == half:
                return True

            if nums[i] > half or currSum > half:
                return False

            if (i, currSum) in memo:
                return memo[(i, currSum)]

            memo[(i, currSum)] = (
                dfs(currSum + nums[i], i + 1) or
                dfs(currSum, i + 1)
            )

            return memo[(i, currSum)]

        return True if dfs(0, 0) else False