class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # backtracking. + dp
        coins.sort()
        dp = dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        def dfs(i, amt):
            if amt > amount or i >= len(coins):
                return 0

            if amt == amount:
                return 1

            if dp[i][amt] != -1:
                return dp[i][amt]

            res = 0
            if amt + coins[i] <= amount:
                res = dfs(i + 1, amt)
                res += dfs(i, amt + coins[i])

            dp[i][amt] = res
            return res

        return dfs(0, 0) 