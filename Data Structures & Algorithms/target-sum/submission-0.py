class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums)
        n = len(nums)

        dp = [[-1] * (2 * offset + 1) for _ in range(n)]

        def dfs(i, added):
            if i == n:
                return 1 if added == target else 0

            if dp[i][added + offset] != -1:
                return dp[i][added + offset]

            dp[i][added + offset] = (
                dfs(i + 1, added + nums[i]) +
                dfs(i + 1, added - nums[i])
            )

            return dp[i][added + offset]

        return dfs(0, 0)