class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1  # base case: empty string
        dp[1] = 1  # first char is non-zero

        for i in range(2, len(s) + 1):
            numOfWays = 0
            one_digit = int(s[i-1])
            two_digit = int(s[i-2:i])

            if one_digit >= 1:
                dp[i] += dp[i-1]

            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]

        return dp[-1]
