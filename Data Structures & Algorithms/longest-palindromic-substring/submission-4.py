class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        def expand(i):
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            odd = s[l + 1: r]
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            even = s[l + 1: r]
            return odd if len(odd) > len(even) else even

        for i in range(len(s)):
            pal = expand(i)
            if len(pal) > len(res):
                res = pal

        return res
