class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            nex = i
            found = False
            while nex < len(temperatures):
                if temperatures[nex] > temperatures[i]:
                    found = True
                    break
                nex += 1
            if found:
               res[i] = nex - i 
        return res