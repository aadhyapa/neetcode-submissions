class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int: 
        visited = [] 
        count = 0 
        def dfs(x, y): 
            if (x, y) is not visited: 
                if grid[x][y] == "0": 
                    return 
                if grid[x][y] == "1": 
                    visited.append((x, y)) 
                    grid[x][y] = "0" 
                    up = x - 1 
                    down = x + 1 
                    left = y - 1 
                    right = y + 1 
                    if up >= 0: 
                        dfs(up, y) 
                    if down < len(grid): 
                        dfs(down, y) 
                    if left >= 0: 
                        dfs(x, left) 
                    if right < len(grid[0]): 
                        dfs(x, right) 

        for x in range(len(grid)): 
            for y in range(len(grid[0])): 
                if grid[x][y] == "1": 
                    dfs(x, y) 
                    count += 1 
        return count