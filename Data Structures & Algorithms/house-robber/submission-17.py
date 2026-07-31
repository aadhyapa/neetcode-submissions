class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # house1, house2 = nums[0], nums[1]
        # curr = max(house1, house2)
        # for i in range(2, len(nums)):
        #     curr = max(house1 + nums[i], house2)
        #     house1 = house2
        #     house2 = curr
        # return curr

        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])

        return dp[-1]
