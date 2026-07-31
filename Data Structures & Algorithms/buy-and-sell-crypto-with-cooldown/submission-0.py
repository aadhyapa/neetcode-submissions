class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        memo = [[0] * 2 for _ in range(len(prices) + 2)]
        # 0 -> buy
        # 1 -> sell
        for i in range(len(prices) - 1, -1, -1):
            #buy:
            #buy = memo[i + 1][1] - prices[i] if i + 1 < len(prices) else  - prices[i]
            memo[i][0] = max( memo[i + 1][1] - prices[i], memo[i + 1][0])
            #sell:
            #sell = memo[i + 2][0] + prices[i] if i + 2 < len(prices) else prices[i]
            memo[i][1] = max( memo[i + 2][0] + prices[i], memo[i + 1][1])

        return memo[0][0]
        
