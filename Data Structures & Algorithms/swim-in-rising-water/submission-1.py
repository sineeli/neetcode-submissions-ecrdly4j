class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = set()
        minH = [(grid[0][0], 0, 0)]
        visited.add((0, 0))

        while minH:
            t, x, y = heapq.heappop(minH)

            if x == n - 1 and y == n - 1:
                return t
            
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                curr_x, curr_y = x + dx, y + dy

                if 0 <= curr_x < n and 0 <= curr_y < n and (curr_x, curr_y) not in visited:
                    heapq.heappush(minH, [max(t, grid[curr_x][curr_y]), curr_x, curr_y])
                    visited.add((curr_x, curr_y))
            
        


        


                