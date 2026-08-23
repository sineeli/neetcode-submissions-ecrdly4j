class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        R, C = len(grid), len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                curr_r, curr_c = r + dr, c + dc
                if (
                    0 <= curr_r < R
                    and 0 <= curr_c < C
                    and grid[curr_r][curr_c] == 2147483647
                ):
                    grid[curr_r][curr_c] = grid[r][c] + 1
                    q.append((curr_r, curr_c))