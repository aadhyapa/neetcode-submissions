class Solution:
    def countSubstrings(self, s: str) -> int:
        if s == '':
            return 0

        totalSubs = 0
        def expand(i):

            count = 0

            # Odd
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            # Odd
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        for i in range(len(s)):
            totalSubs += expand(i)

        return totalSubs
