class listNode:
    def __init__(self,key = None,value= None):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
    
class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = listNode()
        self.tail = listNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNode(self,node):
        node.prev =self.head
        node.next = self.head
        self.head.next.prev = node
        self.head.next = node
    def remNode(self,node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev =prev

    def get(self,key):
        if key in self.cache:
            node = self.cache[key]
            self.remNode(node)
            self.addNode(node)
            return node.value
        return -1
    def set(self,key,value):
        if key in self.cache:
            self.remNode(self.cache[key])
            node = listNode(key,value)
            self.addNode(node)
            self.cache[key]=node
            if len(self.cache)>self.capacity:
                del self.cache[self.tail.prev.key]
                self.remNode(self.tail.prev)


        