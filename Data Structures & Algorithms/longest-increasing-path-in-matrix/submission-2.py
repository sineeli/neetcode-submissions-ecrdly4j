class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            count = 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] > matrix[i][j]:
                    count = max(count, 1 + dfs(ni, nj))
            
            memo[(i, j)] = count
            return count
        
        max_len = 0

        for i in range(R):
            for j in range(C):
                max_len = max(max_len, dfs(i, j))
        
        return max_len
