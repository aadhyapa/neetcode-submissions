class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            curr_n = int(s[i])
            lastTwo = int(s[i - 1 : i + 1])
            if curr_n > 0:
                dp[i + 1] += dp[i]
            if lastTwo > 9 and lastTwo < 27:
                dp[i + 1] += dp[i - 1]

        return dp[-1]