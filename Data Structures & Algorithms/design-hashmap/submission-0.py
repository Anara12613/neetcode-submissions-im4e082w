class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, key):
        curr = self.head

        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1
    
    def put(self,key,value):
        curr = self.head

        while curr is not None:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        new_node = Node(key,value)
        new_node.next = self.head
        self.head = new_node

    def remove(self,key):
        if self.head is None:
            return 
        if self.head.key == key:
            self.head = self.head.next
            return

        curr = self.head

        while curr.next is not None:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

class MyHashMap:

    def __init__(self):
        self.n = 991
        self.bucket = [None] * self.n 
        for i in range(self.n):
            self.bucket[i] = LinkedList()

    def hash(self,key):
        return key % self.n


    def put(self, key: int, value: int) -> None:
        n = self.hash(key)
        self.bucket[n].put(key,value)        

    def get(self, key: int) -> int:
        n = self.hash(key)
        return self.bucket[n].get(key)    
        

    def remove(self, key: int) -> None:
        n = self.hash(key)
        self.bucket[n].remove(key) 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)