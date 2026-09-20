class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.__rearrange(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.__rearrange(key)
        else:
            if len(self.order) == self.capacity:
                least_used_key = self.order.popleft()
                del self.cache[least_used_key]
            self.order.append(key)
            self.cache[key] = value


    def  __rearrange(self, key):
        self.order.append(key)
        self.order.remove(key)
