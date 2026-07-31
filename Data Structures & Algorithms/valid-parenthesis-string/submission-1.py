class Solution:
    def checkValidString(self, s: str) -> bool:
        remin, remax = 0, 0

        for c in s:
            if c == '(':
                remin += 1
                remax += 1

            if c == ')':
                remin -= 1
                remax -= 1

            if c == '*':
                remin -= 1
                remax += 1

            if remax < 0:
                return False
            
            if remin < 0:
                remin = 0

        return remin == 0