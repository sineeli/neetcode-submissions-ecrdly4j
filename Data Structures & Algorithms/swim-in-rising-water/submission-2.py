class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = set()
        min_heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == R - 1 and c == C - 1:
                return t

            for dr, dc in directions:
                curr_r, curr_c = r + dr, c + dc
                if 0 <= curr_r < R and 0 <= curr_c < C and (curr_r, curr_c) not in visited:
                    heapq.heappush(min_heap, (max(t, grid[curr_r][curr_c]), curr_r, curr_c))
                    visited.add((curr_r, curr_c))
