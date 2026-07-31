class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        COLS = len(matrix[0])
        ROWS = len(matrix)
        dp = [[0] * COLS for _ in range(ROWS)]

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            node = matrix[r][c]
            if dp[r][c]:
                return dp[r][c]
            dp[r][c] = 1
            for x, y in dirs:
                new_r, new_c = r + x, c + y
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS:
                    continue
                child = matrix[new_r][new_c]
                if node < child:
                    dp[r][c] = max(dp[r][c], dfs(new_r, new_c) + 1)

            return dp[r][c]

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r, c))
        return ans
