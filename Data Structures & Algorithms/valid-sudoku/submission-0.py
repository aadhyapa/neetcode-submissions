class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for row in board:
            pres = set()
            for c in row:
                if c != '.' and c in pres:
                    return False
                pres.add(c)

        # check cols
        for col in range(9):
            pres = set()
            for row in range(9):
                c = board[row][col]
                if c != '.' and c in pres:
                    return False
                pres.add(c)

        sub_grid = {}
        for i in range(9):
            sub_grid[i] = set()
        # check grid
        for r in range(9):
            for c in range(9):
                char = board[r][c]
                grid_key = -1
                if r < 3:
                    if c < 3:
                        grid_key = 0
                    elif c < 6:
                        grid_key = 3
                    elif c < 9:
                        grid_key = 6
                elif r < 6:
                    if c < 3:
                        grid_key = 1
                    elif c < 6:
                        grid_key = 4
                    elif c < 9:
                        grid_key = 7
                elif r < 9:
                    if c < 3:
                        grid_key = 2
                        pass
                    elif c < 6:
                        grid_key = 5
                    elif c < 9:
                        grid_key = 8
                if char != '.' and char in sub_grid[grid_key]:
                    return False
                sub_grid[grid_key].add(char)
        return True
                

