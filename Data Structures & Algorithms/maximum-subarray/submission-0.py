class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currM = nums[0]
        gloM = nums[0]
        
        for n in nums[1:]:
            currM = max(n, currM + n)
            gloM = max(gloM, currM)
        
        return gloM


