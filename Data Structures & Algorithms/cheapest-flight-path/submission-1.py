class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = {i: [] for i in range(n)}
        res = float('inf')
        for from_i, to_i, price_i in flights:
            graph[from_i].append([to_i, price_i])

        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                temp[d] = min(prices[s] + p, temp[d])
            prices = temp
        return -1 if prices[dst] == float('inf') else prices[dst]