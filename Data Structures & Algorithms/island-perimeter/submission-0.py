

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()


        def bfs(x, y):
            length = 0
            q = deque()
            visited.add((x, y))
            q.append((x, y))
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    curr_x, curr_y = x + dx, y + dy
                    if (
                       curr_x < 0 or curr_y < 0 or
                       curr_x >= m or curr_y >= n or 
                       grid[curr_x][curr_y] == 0
                    ):
                        length += 1
                    elif (curr_x, curr_y) not in visited:
                        q.append((curr_x, curr_y))
                        visited.add((curr_x, curr_y))
            
            return length
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return bfs(i, j)
        
        return 0
        


                





        