class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        i = 0
        string = ''
        while i < len(s):
            while i < len(s) and s[i] not in string:
                string += s[i]
                i += 1
            longest = max(longest, len(string))
            if i < len(s):
                string = string[string.index(s[i]) + 1:]
        return longest
            


                