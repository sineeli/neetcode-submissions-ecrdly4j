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
        copy_dict = {}

        temp1 = head
        dummy = Node(-1)
        temp2 = dummy

        while temp1:
            node = Node(temp1.val)
            copy_dict[temp1] = node
            temp2.next = node
            temp2 = temp2.next
            temp1 = temp1.next
        
        temp1 = dummy.next
        temp2 = head
        while temp1 and temp2:
            temp1.random = None if temp2.random is None else copy_dict[temp2.random]
            temp1 = temp1.next
            temp2 = temp2.next

        return dummy.next
            