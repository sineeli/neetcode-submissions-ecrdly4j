class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            count = dfs(i + 1, j) + dfs(i, j + 1)
            memo[(i, j)] = count
            return count

        return dfs(0, 0)