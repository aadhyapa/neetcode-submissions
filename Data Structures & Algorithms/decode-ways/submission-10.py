class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        if s[0] == "0":
            return 0
        dp[0] = 1
        dp[1] = 1
        
        for i in range(1, len(s)):
            num = int(s[i])
            if num > 0 and num < 10:
                dp[i + 1] += dp[i]
            two = int(s[i-1:i+1])
            if two >= 10 and two <= 26:
                dp[i + 1] += dp[i-1]
            
        return dp[-1]

