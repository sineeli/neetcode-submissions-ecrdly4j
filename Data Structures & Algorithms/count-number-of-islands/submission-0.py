class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: # basically connected components
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y):
            stack = [(x, y)]

            while stack:
                curr_x, curr_y = stack.pop()
                visited.add((curr_x, curr_y))
                for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    new_x, new_y = curr_x + dx, curr_y + dy
                    if (0 <= new_x < m) and (0 <= new_y < n) and (grid[new_x][new_y] == "1") and (new_x, new_y) not in visited:
                        stack.append((new_x, new_y))
 
            return 1

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    num_islands += dfs(i, j)
        
        return num_islands
        