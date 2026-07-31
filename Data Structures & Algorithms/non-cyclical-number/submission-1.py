class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        def sumOfSquares(num):
            numStr = str(num)
            return sum([int(i)**2 for i in numStr])

        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = sumOfSquares(n)
        return True