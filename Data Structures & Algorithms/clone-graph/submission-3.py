"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = {}
        if not node:
            return
        
        visited = set()
        q = deque()
        q.append(node)
        while q:
            n = deque.popleft(q)
            visited.add(n)
            clone_map[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in visited:
                    q.append(neigh)
        
        for orig, clone in clone_map.items():
            for neigh in orig.neighbors:
                clone.neighbors.append(clone_map[neigh])
        
        return clone_map[node]

            
            