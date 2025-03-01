class Node:
    def __init__(self,key,value):
        self.key , self.value = key, value
        self.prev , self.next = None , None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left , self.right = Node(0,0) , Node(0,0)
        self.left.next , self.right.prev =  self.right , self.left

    def remove(self,node):
        prev , next = node.prev , node.next
        prev.next , next.prev = next, prev

    def insert(self,node):
        prev , next =  self.right.prev , self.right
        prev.next = next.prev = node
        node.prev , node.next = prev , next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
