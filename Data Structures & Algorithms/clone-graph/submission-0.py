"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        clone = {node: Node(node.val)}

        q = deque([node])
        while q:
            n1 = q.popleft()
            for n2 in n1.neighbors:
                if clone.get(n2) is None:
                    clone[n2] = Node(n2.val)
                    q.append(n2)
                clone[n1].neighbors.append(clone[n2])

        return clone[node]
                


        


        