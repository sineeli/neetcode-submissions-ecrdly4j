class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        q = deque()
        fresh = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    q.append((x, y))
                if grid[x][y] == 1:
                    fresh += 1
        time = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c  = r + dr, c + dc
                    
                    if (0 <= new_r < m and
                        0 <= new_c < n and
                        grid[new_r][new_c] == 1):
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 2
                
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

