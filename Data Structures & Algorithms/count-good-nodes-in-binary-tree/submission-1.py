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

        def dfs(root, prev_val):
            if root is None:
                return 0
            
            res = 1 if root.val >= prev_val else 0
            prev_val = max(prev_val, root.val)
            res += dfs(root.left, prev_val)
            res += dfs(root.right, prev_val)
            return res

        return dfs(root, root.val)
        