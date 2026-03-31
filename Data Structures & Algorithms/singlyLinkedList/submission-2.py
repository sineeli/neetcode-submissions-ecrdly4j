class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(val=-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        temp = self.head.next
        while temp:
            if index == i:
                return temp.val
            temp = temp.next
            i += 1
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0 
        curr = self.head
        
        while i < index and curr:
            curr = curr.next
            i += 1

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        output = []
        curr = self.head.next

        while curr:
            output.append(curr.val)
            curr = curr.next
        
        return output
        
