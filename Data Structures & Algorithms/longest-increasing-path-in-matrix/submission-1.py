class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])

        memo = {}
        
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if matrix[i][j] <= prev:
                return 0
            if memo.get((i, j)) is not None:
                return memo[(i, j)]
            
            curr = matrix[i][j]
            best = 0
            for dx, dy in directions:
                best = max(best, dfs(i + dx, j + dy, curr))
            memo[(i, j)] = 1 + best
            return memo[(i, j)]

        max_path = 0
        for i in range(m):
            for j in range(n):
                path_count = dfs(i, j, float("-inf"))
                max_path = max(path_count, max_path)
            
        return max_path

        