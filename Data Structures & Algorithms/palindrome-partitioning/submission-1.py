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
                if self.isPali(part):
                    path.append(part)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans
    
    def isPali(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
