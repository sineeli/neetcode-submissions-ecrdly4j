class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_pos = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_pos.append((i, j))
        
        for z_i, z_j in zero_pos:
            for j in range(0, n):
                matrix[z_i][j] = 0
            for i in range(0, m):
                matrix[i][z_j] = 0
        
        