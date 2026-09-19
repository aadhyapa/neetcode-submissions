class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        COLS, ROWS = len(grid[0]), len(grid)
        def dfs(c, r):
            if c >= COLS or c < 0 or r >= ROWS or r < 0 :
                return
            if grid[r][c] == "0" or grid[r][c] == "X":
                return
            if grid[r][c] == "1":
                grid[r][c] = "X"
            dfs(c + 1, r)
            dfs(c - 1, r)
            dfs(c, r + 1)
            dfs(c, r - 1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(c, r)
        return res