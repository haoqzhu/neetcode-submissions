class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

        self.capacity = capacity
        self.size = 0
        self.cache = {}
        
    def insert(self, node: Node):
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev = node

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.size += 1
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            if self.size > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
                self.size -= 1
        
