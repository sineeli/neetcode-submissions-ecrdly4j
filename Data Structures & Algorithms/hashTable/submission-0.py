class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.hash_table = [None] * capacity
        self.size = 0
        self.capacity = capacity
    
    def hash_function(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        
        if self.hash_table[index] is None:
            self.hash_table[index] = Node(key, value)
            self.size += 1
        else:
            node = self.hash_table[index]
            prev = None
            while node:
                if node.key == key:
                    node.val = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        print(key)
        index = self.hash_function(key)
        print(index, self.hash_table)
        node = self.hash_table[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1


    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.hash_table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.hash_table[index] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next
        
        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.hash_table:
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.val)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next

        self.capacity = new_capacity
        self.hash_table = new_table

