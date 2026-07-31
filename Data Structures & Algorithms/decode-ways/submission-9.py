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
            if i >= 1 and ((num < 7 and int(s[i-1]) == 2) or int(s[i-1]) == 1):
                dp[i + 1] += dp[i-1]
            
        return dp[-1]
        

