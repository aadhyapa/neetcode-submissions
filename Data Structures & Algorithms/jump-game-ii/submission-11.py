
class Solution:
    def jump(self, nums) -> int:
        if len(nums) <= 1:
            return 0
        jumps = 1
        farthest = nums[0]
        dist = nums[0]
        for i in range(1, len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if dist == i:
                dist = farthest
                jumps += 1
        
        return jumps
            
            