class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            nex = i + 1
            found = True
            while nex < len(temperatures) and temperatures[nex] <= temperatures[i]:
                if res[nex] == 0:
                    found = False
                    break
                nex += res[nex]

            if found:
                res[i] = nex - i
        return res