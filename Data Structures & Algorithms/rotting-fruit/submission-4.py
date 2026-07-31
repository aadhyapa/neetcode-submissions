class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        mins = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])

        while q:
            lev = len(q)
            spread = False
            for i in range(lev):
                r, c = q.popleft()    

                if r < ROWS - 1:
                    if grid[r + 1][c] == 1:
                        q.append([r + 1, c])
                        grid[r + 1][c] = 2
                        spread = True
                if c < COLS - 1:
                    if grid[r][c + 1] == 1:
                        q.append([r, c + 1])
                        grid[r][c + 1] = 2
                        spread = True
                if r > 0:
                    if grid[r - 1][c] == 1:
                        q.append([r - 1, c])
                        grid[r - 1][c] = 2
                        spread = True
                if c > 0:
                    if grid[r][c - 1] == 1:
                        q.append([r, c - 1])
                        grid[r][c - 1] = 2
                        spread = True
            if spread:
                mins += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return mins
