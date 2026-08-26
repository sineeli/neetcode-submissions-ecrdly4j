class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac = [[False] * C for _ in range(R)]
        atl = [[False] * C for _ in range(R)]
        res = []

        def dfs(r, c, prevh, ocean):
            if (
                r < 0 or c < 0 or
                r == R or c == C or 
                heights[r][c] < prevh or ocean[r][c]
            ):
                return
            
            ocean[r][c] = True
            
            dfs(r + 1, c, heights[r][c], ocean)
            dfs(r - 1, c, heights[r][c], ocean)
            dfs(r, c + 1, heights[r][c], ocean)
            dfs(r, c - 1, heights[r][c], ocean)

        
        for j in range(C):
            dfs(0, j, heights[0][j], pac)
            dfs(R-1, j, heights[R-1][j], atl)
        
        for i in range(R):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, C-1, heights[i][C-1], atl)
        
        for i in range(R):
            for j in range(C):
                if pac[i][j] and atl[i][j]:
                    res.append((i, j))
        
        return res





        