class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and (i, j) not in visited and grid[i][j] == "1"):
                return

            visited.add((i, j))
            for dx, dy in directions:
                x, y = i + dx, j + dy
                dfs(x, y)

        islands = 0

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands
