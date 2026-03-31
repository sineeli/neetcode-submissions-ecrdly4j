# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_nodes = [0]
        if root is None:
            return 0

        def dfs(root, prev_val):
            if root is None:
                return 
            
            if root.val >= prev_val:
                max_nodes[0] += 1
                prev_val = root.val
            
            dfs(root.left, prev_val)
            dfs(root.right, prev_val)
        
        dfs(root, root.val)
        return max_nodes[0]
        