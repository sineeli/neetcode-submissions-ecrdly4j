class TrieNode:
    def __init__(self):
        self.node = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.node:
                curr.node[char] = TrieNode()
            curr = curr.node[char]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char in curr.node:
                curr = curr.node[char]
            else:
                return False
        if curr.word:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char in curr.node:
                curr = curr.node[char]
            else:
                return False
        
        return True
        
        