"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque([node])
        clone_map = {node: Node(node.val)}

        while q:
            curr_node = q.popleft()
            new_node = clone_map[curr_node]
            for neigh in curr_node.neighbors:
                if neigh not in clone_map:
                    clone_map[neigh] = Node(neigh.val)
                    q.append(neigh)
                new_node.neighbors.append(clone_map[neigh])
        
        return clone_map[node]