class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1:
                return
            if board[r][c] == 'X' or board[r][c] == '#':
                return
            # capturing:
            if board[r][c] == 'O':
                board[r][c] = 'X'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        def dfsBorder(r, c):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1:
                return
            if board[r][c] == 'X' or board[r][c] == '#':
                return
            if board[r][c] == 'O':
                board[r][c] = '#'
                dfsBorder(r + 1, c)
                dfsBorder(r - 1, c)
                dfsBorder(r, c + 1)
                dfsBorder(r, c - 1)

        def dfsBorderFill(r, c):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1:
                return
            if board[r][c] == 'X':
                return
            if board[r][c] == '#':
                board[r][c] = 'O'
                dfsBorderFill(r + 1, c)
                dfsBorderFill(r - 1, c)
                dfsBorderFill(r, c + 1)
                dfsBorderFill(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (c == 0 or c == COLS - 1 or r == 0 or r == ROWS - 1):
                    dfsBorder(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '#':
                    dfsBorderFill(r, c)

            