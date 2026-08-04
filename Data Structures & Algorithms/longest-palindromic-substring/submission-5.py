class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        def isPal(l, r):
            if s[l] == s[r]:
                return True
            return False

        resL, resR, currMaxLen = 0, 0, 0

        def dfs(l, r):
            nonlocal resL, resR, currMaxLen
            if l < 0 or r >= len(s):
                return False

            if l >= r:
                return True

            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = dfs(l + 1, r - 1) and s[l] == s[r]

            if r - l + 1 > currMaxLen and dp[(l, r)]: 
                currMaxLen = r - l + 1
                resL, resR = l, r

            return dp[(l, r)]
            
        for l in range(len(s)):
            for r in range(l, len(s)):
                dfs(l, r)

        return s[resL : resR + 1]
