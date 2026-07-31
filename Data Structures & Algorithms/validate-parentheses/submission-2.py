class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')' : '(', ']' : '[', '}' : '{'}
        for ch in s:
            if ch in map:
                if stack and stack[-1] == map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack