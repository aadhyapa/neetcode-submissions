class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r,c))
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            leaf_count = len(q)
            for i in range(leaf_count):
                r, c = q.popleft()
                for x, y in dirs:
                    newR, newC = r + x, c + y
                    if newR > -1 and newR < ROWS and newC > -1 and newC < COLS and (newR, newC) not in visited and grid[newR][newC] != -1:
                        grid[newR][newC] = min(grid[newR][newC], grid[r][c] + 1)
                        q.append([newR, newC])
                        visited.add((newR, newC))