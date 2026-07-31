class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s, e = 0, 0
        res = []
        def backtrack(paran, s, e):
            if s == e and len(paran) == 2 * n:
                res.append(paran)
                return

            if s < n:
                backtrack(paran + "(", s + 1, e)
            if s > e:
                backtrack(paran + ")", s, e + 1)

        backtrack("", 0, 0)
        return res

        