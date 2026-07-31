class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        left, right = 0, len(self.map[key]) - 1
        bestCand = ""
        bestTime = -1
        arr = self.map[key]

        while left <= right:

            mid = (left + right) // 2

            if arr[mid][1] <= timestamp:
                bestCand = arr[mid][0]
                left = mid + 1
            if arr[mid][1] > timestamp:
                right = mid - 1
    
        return bestCand