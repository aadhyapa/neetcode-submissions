class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def solve(a, b, oper):
            if oper == "+":
                return a + b
            if oper == "-":
                return a - b
            if oper == "*":
                return a * b
            if oper == "/":
                return int(a / b)
        
        stack = []
        opers = "+-*/"
        for tok in tokens:
            if tok not in opers:
                stack.append(int(tok))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(solve(a, b, tok))

        return stack[0]
            