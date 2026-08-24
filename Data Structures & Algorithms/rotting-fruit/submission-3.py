class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(grid), len(grid[0])
        
        fresh_fruit = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh_fruit += 1
        time = 0
        while q and fresh_fruit > 0:
            temp_len = len(q)
            for _ in range(temp_len):
                r, c = q.popleft()
                for dr, dc in directions:
                    curr_r, curr_c = r + dr, c + dc
                    if (
                        0 <= curr_r < R and
                        0 <= curr_c < C and
                        grid[curr_r][curr_c] == 1
                    ):
                        grid[curr_r][curr_c] = 2
                        fresh_fruit -= 1
                        q.append((curr_r, curr_c))
            time += 1
            
        
        if fresh_fruit:
            return -1
        return time