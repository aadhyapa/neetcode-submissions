class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        arr = [0] * (len(nums) + 1)

        arr[0] = 0
        arr[1] = nums[0]
        arr[2] = nums[1]

        for i in range(2, len(nums)):
            if arr[i-2] > arr[i-1]:
                arr[i + 1] = arr[i - 2] + nums[i]
            else:
                arr[i + 1] = arr[i - 1] + nums[i]

        return max(arr)
