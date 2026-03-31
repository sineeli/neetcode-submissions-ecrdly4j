# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root, subRoot):
            if not subRoot:
                return True
            
            if not root:
                return False
            
            if validate_tree(root, subRoot):
                return True
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        def validate_tree(p, q):
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if p is not None and q is None:
                return False
            if p.val != q.val:
                return False
            
            return validate_tree(p.left, q.left) and validate_tree(p.right, q.right)

        return dfs(root, subRoot)


        