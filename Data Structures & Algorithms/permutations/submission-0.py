class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [0] * len(nums)

        def dfs(subArr, visited):
            if len(subArr) == len(nums):
                res.append(subArr.copy())
                return
            for i in range(len(visited)):
                if not visited[i]:
                    visited[i] = 1
                    subArr.append(nums[i])
                    dfs(subArr, visited.copy())
                    subArr.pop()
                    visited[i] = 0
        dfs([], visited)
        return res
            

            