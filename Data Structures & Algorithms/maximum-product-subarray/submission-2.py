class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cM, cm, gM =1, 1, nums[0] 

        for num in nums:
            tmp = cM * num
            cM = max(cM * num, num, cm * num)
            cm = min(tmp, num, cm * num)
            gM = max(gM, cM)

        return gM