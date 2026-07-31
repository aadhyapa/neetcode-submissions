class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count =  0
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return
            if grid[x][y] == "0":
                return
            
            grid[x][y] = "0"
            up = x - 1
            down = x + 1
            left = y - 1
            right = y + 1
            dfs(up, y)
            dfs(down, y)
            dfs(x, left)
            dfs(x, right)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    dfs(x, y)
                    count += 1
        return count