class Node:
    def __init__(self, key, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache_head = None
        self.capacity = capacity
        self.cache_size = 0
        self.cache = {}
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.use(key)
        return self.cache[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.use(key)
        else:
            new = Node(key, value)
            self.cache_size += 1
            self.cache[key] = new
            if self.cache_head is None:
                self.cache_head = new
                self.tail = new
            else:
                new.prev = self.tail
                self.tail.next = new
                self.tail = self.tail.next

        while self.cache_size > self.capacity:

            old = self.cache_head
            del self.cache[old.key]

            # reset head
            self.cache_head = old.next
            old.next = None
            self.cache_head.prev = None
            self.cache_size -= 1

    def use(self, key):
        node = self.cache[key]
        prev = node.prev
        nex = node.next
        if self.tail == node:
            return
        # head
        if self.cache_head == node:
            # resetting head
            self.cache_head = nex
            nex.prev = None
        else:
            # bridging the gap
            prev.next = nex
            nex.prev = prev
            node.next, node.prev = None, None

        # setting node at tail
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = self.tail.next

