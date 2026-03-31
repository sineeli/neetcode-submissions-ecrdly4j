class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]
        
        def bfs(source, ocean):
            q = deque(source)

            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))
            

        
        pacific = []
        atlantic = []

        for i in range(n):
            pacific.append((0, i))
            atlantic.append((m-1, i))
        
        for j in range(m):
            pacific.append((j, 0))
            atlantic.append((j, n-1))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)
        
        res = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        
        return res
        

            

