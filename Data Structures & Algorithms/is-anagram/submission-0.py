class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        s_list.sort()
        t_list = list(t)
        t_list.sort()
        for i in range(len(s)):
            if s_list[i] != t_list[i]:
                return False
        return True