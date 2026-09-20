class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        found = set()
        l, r = 0, 0

        res = 0

        while l <= r and r < len(s):
            if s[r] in found:
                res = max(res, r - l)
                found_letter = s[r]
                while s[l] != found_letter:
                    found.remove(s[l])
                    l += 1
                l += 1

            found.add(s[r])
            r += 1
        res = max(res, r - l)
        return res







                