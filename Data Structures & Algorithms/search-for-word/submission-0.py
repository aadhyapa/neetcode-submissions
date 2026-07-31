class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(validateAlphaInd, row, col):
            if (0 > row) or(row >= len(board)) or (0 > col) or (col >= len(board[0])):
                return False

            if board[row][col] == "#":
                return False

            if word[validateAlphaInd] != board[row][col]:
                return False

            if validateAlphaInd == len(word) - 1:
                return True

            validateAlphaInd += 1
            currAlpha = board[row][col]
            board[row][col] = '#'
            
            found = (
                backtrack(validateAlphaInd, row + 1, col) or
                backtrack(validateAlphaInd, row - 1, col) or
                backtrack(validateAlphaInd, row, col + 1) or
                backtrack(validateAlphaInd, row, col - 1)
            )
            
            board[row][col] = currAlpha
            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(0, row, col):
                    return True

        return False