"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}

        temp1 = head
        dummy = Node(x=-1)
        temp2 = dummy

        while temp1:
            node_map[temp1] = Node(temp1.val)
            temp2.next = node_map[temp1]
            temp1 = temp1.next
            temp2 = temp2.next
        
        temp1 = head
        temp2 = dummy.next
        while temp1:
            if temp1.random in node_map:
                temp2.random = node_map[temp1.random]
            temp1 = temp1.next
            temp2 = temp2.next

        return dummy.next
        
        

            
