
class Solution:
    def jump(self, nums) -> int:
        i, j = 0, 0
        jumps = 0
        while i < len(nums) - 1 and j < len(nums) - 1:
            max_ind = i
            while i <= j:
                if i + nums[i] > max_ind + nums[max_ind]:
                    max_ind = i
                i += 1
            i = j + 1
            j = nums[max_ind] + max_ind
            jumps += 1
        return jumps