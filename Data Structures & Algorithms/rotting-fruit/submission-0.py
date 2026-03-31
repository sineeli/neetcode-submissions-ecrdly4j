class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        time = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c  = r + dr, c + dc
                    
                    if (0 <= new_r < ROWS and
                        0 <= new_c < COLS and
                        grid[new_r][new_c] == 1):
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 2
                
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1




