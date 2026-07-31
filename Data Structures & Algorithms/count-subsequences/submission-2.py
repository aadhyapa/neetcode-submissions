class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1] * len(t) for _ in s]
        
        def dfs(parent, target):
            if target == len(t):
                return 1

            if parent == len(s):
                return 0
                
            if dp[parent][target] != -1:
                return dp[parent][target]

            if s[parent] == t[target]:
                dp[parent][target] = dfs(parent + 1, target + 1) + dfs(parent + 1, target)
            else:
                dp[parent][target] = dfs(parent + 1, target)

            return dp[parent][target]
    
        return dfs(0, 0)