
class Solution:
    def jump(self, nums) -> int:
        if len(nums) <= 1:
            return 0
        jumps = 1
        farthest = nums[0]
        dist = nums[0]
        for i in range(1, len(nums)):
            farthest = max(farthest, i + nums[i])
            if i != len(nums) - 1 and dist == i:
                dist = farthest
                jumps += 1
        
        return jumps
            
            