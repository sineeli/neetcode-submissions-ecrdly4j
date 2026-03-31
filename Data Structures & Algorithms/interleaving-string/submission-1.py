class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        def dfs(i: int, j: int, k: int):
            if memo.get((i,j)) is not None:
                return memo[(i, j)]

            if k == len(s3):
                return (i == len(s1) and (j == len(s2)))
            
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1): return True

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1): return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0, 0)
