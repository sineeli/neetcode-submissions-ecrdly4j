class Solution:
    def numDecodings(self, s: str) -> int:
        alpha_to_num = {f"{i + 1}": chr(65 + i) for i in range(26)}
        count = 0
        n = len(s)
        memo = {}

        def dfs(i):
            nonlocal count
            if i in memo:
                return memo[i]
            if i == n:
                return 1

            if s[i] == "0":
                return 0

            res = dfs(i + 1)

            if i < n - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)

            memo[i] = res
            return memo[i]

        return dfs(0)
