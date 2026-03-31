class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                
        
        while q:
            x, y = q.popleft()
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                curr_x, curr_y = x + dx, y + dy
                if 0 <= curr_x < m and 0 <= curr_y < n and grid[curr_x][curr_y] == 2147483647:
                    grid[curr_x][curr_y] = grid[x][y] + 1
                    q.append((curr_x, curr_y))


