class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_map = {}
        for i in nums:
            if i not in count_map:
                count_map[i] = 1
            else:
                count_map[i] += 1
        count_map = [x for x,y in sorted(count_map.items(), key=lambda x: x[1], reverse = True)][:k]
        return count_map