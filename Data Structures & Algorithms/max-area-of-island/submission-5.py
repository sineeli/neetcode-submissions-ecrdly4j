class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m,  n = len(grid), len(grid[0])

        def bfs(x, y):

            q = deque()
            q.append([x, y])
            grid[x][y] = 0
            area = 1
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    curr_x, curr_y = x + dx, y + dy

                    if (0 <= curr_x < m and 
                        0 <= curr_y < n and
                        grid[curr_x][curr_y] == 1
                    ):
                        area += 1
                        q.append([curr_x, curr_y])
                        grid[curr_x][curr_y] = 0
            
            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(bfs(i, j), max_area)
        
        return max_area