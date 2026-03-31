class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        curr.word = True
        return
    
    def search(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.word



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        m, n = len(board), len(board[0])

        for word in words:
            self.trie.insert(word)

        output = set()
        visited = set()
        def dfs(x, y, word, trie_root):
            if (
                x < 0 or x > m - 1 or
                y < 0 or y > n - 1 or
                (x, y) in visited or
                board[x][y] not in trie_root.children
            ):
                return
            
            visited.add((x, y))
            trie_root = trie_root.children[board[x][y]]
            word += board[x][y]
            if trie_root.word:
                output.add(word)

            dfs(x + 1, y, word, trie_root)
            dfs(x, y + 1, word, trie_root)
            dfs(x - 1, y, word, trie_root)
            dfs(x, y - 1, word, trie_root)
            visited.remove((x, y))
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in self.trie.root.children:
                    dfs(i, j, "", self.trie.root)
        # print(output)
        return list(output)