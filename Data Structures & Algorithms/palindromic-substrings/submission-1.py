class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1
                    count += 1

        return count
