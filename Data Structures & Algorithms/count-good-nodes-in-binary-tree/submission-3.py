# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def dfs(node, prev):
            if node is None:
                return 0 
            
            res = 1 if node.val >= prev else 0
            prev = max(prev, node.val)
            res += dfs(node.left, prev)
            res += dfs(node.right, prev)
            return res
        
        return dfs(root, root.val)
        