class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # Find which row by checking with first element of every row
        t, b = 0, ROWS - 1
        col = 0
        targetRow = -1
        while t <= b:
            mid = (t + b) // 2
            if matrix[mid][0] <= target:
                targetRow = mid
                t = mid + 1
            else:
                b = mid - 1

        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[targetRow][mid] == target:
                return True
            if matrix[targetRow][mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return False


        