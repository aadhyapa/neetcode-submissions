class Solution:
    def climbStairs(self, n: int) -> int:
        dpArr = [-1] * (n + 1)

        dpArr[0] = 0

        def recurse(stair, dpArr):
            if stair <= 1:
                dpArr[stair] = 1

            if dpArr[stair] != -1:
                return dpArr[stair]

            dpArr[stair] = recurse(stair - 1, dpArr) + recurse(stair - 2, dpArr)
            return dpArr[stair]

        recurse(n, dpArr)
        return dpArr[n]