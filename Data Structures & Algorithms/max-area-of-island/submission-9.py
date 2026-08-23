class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        R, C = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # visited = set()

        def dfs(r, c):
            if not (
                0 <= r < R and 0 <= c < C and
                # (r, c) not in visited and
                grid[r][c] == 1
            ):
                return 0
            
            # visited.add((r, c))
            grid[r][c] = 0
            island_area = 1 + (
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )
            return island_area
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)

        return max_area