class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]
        
        def dfs(r, c, prevh, ocean):
            if (r < 0 or c < 0 or 
                r == m or c == n or
                heights[r][c] < prevh or ocean[r][c]
            ):
                return
            
            ocean[r][c] = True
            dfs(r + 1, c, heights[r][c], ocean)
            dfs(r, c + 1, heights[r][c], ocean)
            dfs(r - 1, c, heights[r][c], ocean)
            dfs(r, c - 1, heights[r][c], ocean)

            
        for j in range(n):
            dfs(0, j, heights[0][j], pac)
            dfs(m-1, j, heights[m-1][j], atl)
            

        for i in range(m):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, n-1, heights[i][n-1], atl)
        
        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append((i, j))
        
        return res

            

