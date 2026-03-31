class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        def dfs(i, j, dist):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                grid[i][j] < dist   # already has a shorter distance
            ):
                return

            grid[i][j] = dist

            dfs(i + 1, j, dist + 1)
            dfs(i - 1, j, dist + 1)
            dfs(i, j + 1, dist + 1)
            dfs(i, j - 1, dist + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:  # gate
                    dfs(i, j, 0)