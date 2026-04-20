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
        
        good_nodes = [0]

        def dfs(node, prev):
            if node is None:
                return
            print(node.val, prev)
            if node.val >= prev:
                good_nodes[0] += 1
            dfs(node.left, max(node.val, prev))
            dfs(node.right, max(node.val, prev))
        
        dfs(root, root.val)
        return good_nodes[0]
        