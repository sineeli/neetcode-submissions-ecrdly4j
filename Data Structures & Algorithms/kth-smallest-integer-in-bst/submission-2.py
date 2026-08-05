# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current_count = 0
        ans = None
        def inorder(node):
            nonlocal current_count
            nonlocal ans
            if node is None or ans is not None:
                return
            inorder(node.left)
            current_count += 1
            if current_count == k:
                ans = node.val
            inorder(node.right)
        
        inorder(root)
        return ans