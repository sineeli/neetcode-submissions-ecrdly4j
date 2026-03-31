# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque()
        res = []
        rightside = None
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                rightside = queue.popleft()
                if rightside.left:
                    queue.append(rightside.left)
                if rightside.right:
                    queue.append(rightside.right)
            
            if rightside:
                res.append(rightside.val)
        
        return res


        