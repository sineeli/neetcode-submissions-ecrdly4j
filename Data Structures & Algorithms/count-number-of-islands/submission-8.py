class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y):
            if (x, y) not in visited:
                visited.add((x, y))
            
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                curr_x, curr_y = x + dx, y + dy
                if 0 <= curr_x < R and 0 <= curr_y < C and (curr_x, curr_y) not in visited and grid[curr_x][curr_y] == "1": 
                    dfs(curr_x, curr_y)

        num_islands = 0
        for x in range(R):
            for y in range(C):
                if grid[x][y] == "1" and (x, y) not in visited:
                    dfs(x, y)
                    num_islands += 1

        return num_islands