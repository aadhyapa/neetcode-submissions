class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        longest = 0
        nums_set = set(nums)
        for i in nums_set:
            if i-1 not in nums_set:
                length = 0
                while i + length in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest