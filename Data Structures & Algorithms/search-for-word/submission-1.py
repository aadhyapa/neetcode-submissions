class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def checkWord(r, c, i):
            if r >= ROWS or r < 0 or c >= COLS or c < 0:
                return 
            if board[r][c] != word[i] or board[r][c] == "#":
                return
            temp = board[r][c]
            board[r][c] = "#"
            if i == len(word) - 1:
                return True
            result = (
                checkWord(r + 1, c, i + 1) or
                checkWord(r - 1, c, i + 1) or
                checkWord(r, c + 1, i + 1) or
                checkWord(r, c - 1, i + 1)
            )
            board[r][c] = temp
            return result
        result = False
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if checkWord(r, c, 0):
                        return True
        return False

