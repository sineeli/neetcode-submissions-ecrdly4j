# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "N"
        output = []

        def dfs(node):
            if node is None:
                output.append("N")
                return
            
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(output)
        return ",".join(output)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N":
            return None
        
        n = len(data)
        data = data.split(",")
        self.i = 0
        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(val=int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node


        return dfs()

