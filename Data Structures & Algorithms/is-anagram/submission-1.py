class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        s_list.sort()
        t_list = list(t)
        t_list.sort()
        return t_list == s_list