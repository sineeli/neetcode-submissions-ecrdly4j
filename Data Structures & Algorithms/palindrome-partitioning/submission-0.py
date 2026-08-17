class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def dfs(i):
            if i >= len(s):
                ans.append(list(path))
                return

            for j in range(i, len(s)):
                part = s[i : j + 1]
                if part == part[::-1]:
                    path.append(part)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans
