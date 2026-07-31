class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, rem, sub):

            if rem == 0:
                res.append(sub.copy())
                return
                
            if i >= len(candidates) or rem < 0:
                return

            sub.append(candidates[i])
            backtrack(i + 1, rem - candidates[i], sub)
            sub.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1, rem, sub)

        backtrack(0, target, [])

        return res