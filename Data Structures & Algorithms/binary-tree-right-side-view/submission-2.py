# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Simple BFS with last element of each level will be the answer
        if not root:
            return []

        output = []
        q = deque()
        q.append(root)
        while q:
            temp_len = len(q)
            for idx in range(temp_len):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if idx == temp_len - 1:
                    output.append(node.val)

        return output      


