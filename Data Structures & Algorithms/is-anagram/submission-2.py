class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length_tracker = {}
        for char in s:
            if char not in length_tracker:
                length_tracker[char] = 0
            length_tracker[char] += 1

        for char in t:
            if char not in length_tracker:
                return False
            length_tracker[char] -= 1
            if length_tracker[char] < 0:
                return False

        if sum(length_tracker.values()) != 0:
            return False
        return True


