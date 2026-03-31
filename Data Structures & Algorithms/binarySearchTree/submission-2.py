class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if self.root is None:
            self.root = TreeNode(key, val)

        curr = self.root

        while curr:
            if key < curr.key:
                if curr.left is None:
                    curr.left = TreeNode(key, val)
                    return
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = TreeNode(key, val)
                    return
                curr = curr.right
            else:
                curr.val = val
                return
        
    def get(self, key: int) -> int:
        curr = self.root
        if curr is None:
            return -1
        
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        
        return -1

    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1

    # Returns the node with the minimum key in the subtree
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return -1 if curr is None else curr.val

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    def removeHelper(self, curr, key):
        if curr is None:
            return None

        if key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        elif key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        else:
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                # swap with min of right subtreee (inorder scuessor)
                min_node = self.findMin(curr.right)
                curr.key = min_node.key
                curr.val = min_node.val

                # right subtree wil be modified because of this so we asign the modified
                # right to right of the root

                # we will remove the swapped right minimum from the current node to the right
                curr.right = self.removeHelper(curr.right, min_node.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
    
    def inorderTraversal(self, root, result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
        


