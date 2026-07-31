class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(subs, i):
            nonlocal res
            if sum(subs) == target:
                res.append(subs.copy())
                return
            if i >= len(nums) or sum(subs) > target:
                return
            subs.append(nums[i])
            backtrack(subs, i)
            subs.pop()
            backtrack(subs, i + 1)
        backtrack([], 0)
        return res