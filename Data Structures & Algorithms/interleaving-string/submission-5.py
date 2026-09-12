class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N, O = len(s1), len(s2), len(s3)
        memo = {}

        def dfs(i, j, k):
            if (i, j) in memo:
                return memo[(i, j)]
            if k == O:
                return i == M and j == N

            if i < M and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    return True

            if j < N and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0, 0)