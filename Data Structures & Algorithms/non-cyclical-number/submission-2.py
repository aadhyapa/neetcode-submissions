class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(num):
            numStr = str(num)
            return sum([int(i)**2 for i in numStr])

        slow, fast = n, sumOfSquares(n)
        while slow != fast:
            fast = sumOfSquares(fast)
            fast = sumOfSquares(fast)
            slow = sumOfSquares(slow)

        return True if slow == True else False