class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(board), len(board[0])
        final_ans = False

        def dfs(x, y, i):

            if i == len(word):
                return True
            if not (0 <= x < m and 0 <= y < n) or board[x][y] != word[i] or (x, y) in visited:
                return False

            visited.add((x, y))
            for dx, dy in directions:
                if dfs(x + dx, y + dy, i + 1):
                    return True
            visited.remove((x, y))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
