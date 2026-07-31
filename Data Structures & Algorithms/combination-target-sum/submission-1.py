class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(resNums, add, i):
            if i >= len(nums) or add > target:
                return

            if add == target:
                res.append(resNums[:])
                return

            resNums.append(nums[i])
            backtrack(resNums, add + nums[i], i)
            
            resNums.pop()
            backtrack(resNums, add, i + 1)

        backtrack([], 0, 0)
        return res


            


        

            
        