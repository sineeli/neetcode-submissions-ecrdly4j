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
        res = 0
        
        def dfs(node, prev_max):
            nonlocal res
            if node is None:
                return

            if node.val >= prev_max:
                res += 1
            dfs(node.left, max(node.val, prev_max))
            dfs(node.right, max(node.val, prev_max))

            return
        
        dfs(root, -99999)
        return res


