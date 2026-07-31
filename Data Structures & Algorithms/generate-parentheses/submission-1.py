class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking
        res = []
        def backtrack(ope, clo, pars):
            if len(pars) == 2 * n:
                if ope == clo:
                    res.append(pars)
                return
            if clo > ope:
                return
            backtrack(ope + 1, clo, pars + "(")
            if ope > clo:
                backtrack(ope, clo + 1, pars + ")")
        backtrack(0, 0, "")
        return res
            
                

        