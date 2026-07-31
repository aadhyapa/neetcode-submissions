class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = float('inf')
        ma = 0

        for price in prices:
            if price < mi:
                mi = price
            elif price - mi > ma:
                ma = price - mi
        return ma 
