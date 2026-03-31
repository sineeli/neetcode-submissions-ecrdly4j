class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited = set()
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m,  n = len(grid), len(grid[0])

        def bfs(x, y):

            q = deque()
            q.append([x, y])
            # visited.add((x, y))
            while q:
                x, y = q.popleft()
                grid[x][y] = 1
                for dx, dy in directions:
                    curr_x, curr_y = x + dx, y + dy

                    if (0 <= curr_x < m and 
                        0 <= curr_y < n and
                        grid[curr_x][curr_y] == "1"
                    ):
                        q.append([curr_x, curr_y])
            
            return 1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += bfs(i, j)
        
        return count




