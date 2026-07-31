class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        fuel = 0
        ind = 0
        for i in range(len(cost)):
            fuel += gas[i]
            fuel -= cost[i]
            if fuel <= 0 and i != len(cost) - 1:
                fuel = 0
                ind = i + 1

        return ind