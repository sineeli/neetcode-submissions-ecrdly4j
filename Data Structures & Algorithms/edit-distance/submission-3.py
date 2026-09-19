class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m:
                return n - j

            if j == n:
                return m - i

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                res = min(
                    dfs(i + 1, j), dfs(i, j + 1)
                )  # (delete a character in word1 so we cannot move j still we didnt match with j, insert a character in word1, basically we are matching and moving ahead but i currently we are is not the character)
                res = min(
                    res, dfs(i + 1, j + 1)
                )  # just replace current character with j so that they match anyway and then we move on
                memo[(i, j)] = res + 1

            return memo[(i, j)]

        return dfs(0, 0)
