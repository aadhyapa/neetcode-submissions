class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right, star = [], [], []

        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            if s[i] == '*':
                star.append(i)
            if s[i] == ')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False

        
        while len(right) < len(left):
            if not star:
                return False
            l = left.pop()
            st = star.pop()
            if st < l:
                return False
        return True
