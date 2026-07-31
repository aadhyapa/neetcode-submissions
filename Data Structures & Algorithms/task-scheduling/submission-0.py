class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        frequencies = [0] * 26

        for task in tasks:
            frequencies[ord(task) - 65] += 1

        frequencies = [f for f in frequencies if f > 0]

        heapq.heapify_max(frequencies)

        cycle = 0
        cooldown = deque()

        while frequencies or cooldown:
            cycle += 1

            while cooldown and cycle - cooldown[0][1] > n:
                heapq.heappush_max(frequencies, cooldown.popleft()[0])
            
            if frequencies:
                task = heapq.heappop_max(frequencies)
                task -= 1
                if task:
                    cooldown.append((task, cycle))


        return cycle
            

