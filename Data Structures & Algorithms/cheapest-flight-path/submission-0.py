class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
       # When nodes > k: amputate
       # When we reach dist, take min of curr and new

        graph = {i: [] for i in range(n)}
        res = float('inf')
        for from_i, to_i, price_i in flights:
            graph[from_i].append([to_i, price_i])

        prices = [float('inf')] * n
        prices[src] = 0

        # Relaxation of all the edges V times, not (V - 1) as we
        # need one additional relaxation to detect negative cycle
        for i in range(k + 1):
            temp = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            prices = temp
        return -1 if prices[dst] == float('inf') else prices[dst]