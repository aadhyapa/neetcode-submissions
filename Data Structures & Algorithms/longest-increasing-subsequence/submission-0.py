class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1] * (len(nums) + 1) for _ in range(len(nums))]

        def dfs(i, j):
            if i >= len(nums):
                return 0

            if memo[i][j + 1] != -1:
                return memo[i][j + 1]
            
            res = dfs(i + 1, j)

            if j == -1 or nums[i] > nums[j]:
                res = max(res, dfs(i + 1, i) + 1)

            memo[i][j + 1] = res
            return res

        return dfs(0, -1)
        


        
            