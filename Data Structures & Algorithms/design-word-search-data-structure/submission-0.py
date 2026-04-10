class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.isEndOfWord
            char = word[index]
            if char == '.':
                return any(dfs(index + 1, child) for child in node.children.values())
            else:
                if char in node.children:
                    return dfs(index + 1, node.children[char])
                return False
        
        return dfs(0, self.root)
        