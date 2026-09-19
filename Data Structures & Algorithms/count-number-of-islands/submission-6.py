class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        COLS, ROWS = len(grid[0]), len(grid)

        def isValid(r, c):
                return not (c >= COLS or c < 0 or r >= ROWS or r < 0)

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while q:
                size = len(q)
                for _ in range(size):
                    cr, cc = q.popleft()
                    if isValid(cr + 1, cc) and grid[cr + 1][cc] == "1":
                        q.append((cr + 1, cc))
                        grid[cr + 1][cc] = "0"
                    if isValid(cr - 1, cc) and grid[cr - 1][cc] == "1":
                        q.append((cr - 1, cc))
                        grid[cr - 1][cc] = "0"
                    if isValid(cr, cc + 1) and grid[cr][cc + 1] == "1":
                        q.append((cr, cc + 1))
                        grid[cr][cc + 1] = "0"
                    if isValid(cr, cc - 1) and grid[cr][cc - 1] == "1":
                        q.append((cr, cc - 1))
                        grid[cr][cc - 1] = "0"


        def dfs(c, r):
            if c >= COLS or c < 0 or r >= ROWS or r < 0 :
                return
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(c + 1, r)
            dfs(c - 1, r)
            dfs(c, r + 1)
            dfs(c, r - 1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)
        return res