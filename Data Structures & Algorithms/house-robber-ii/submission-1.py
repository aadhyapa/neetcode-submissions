class Solution:
    def rob(self, nums: List[int]) -> int:
      
        if len(nums) == 1:
            return nums[0]
            
        house11, house12, house21, house22, curr1, curr2 = 0, 0, 0, 0, 0, 0
        for num in nums[1:]:
            curr1 = max(house11 + num, house21)
            house11 = house21
            house21 = curr1

        for num in nums[:-1]:
            curr2 = max(house12 + num, house22)
            house12 = house22
            house22 = curr2

        return max(house21, house22)