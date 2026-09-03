class Solution:
    def longestPalindrome(self, s: str) -> str:
        # treat each characters as a center

        n = len(s)
        start_idx = 0
        max_len = 0
        for i in range(n):
            l, r = i, i  # odd condition where it has same center

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start_idx = l
                    max_len = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1  # even case

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start_idx = l
                    max_len = r - l + 1

                l -= 1
                r += 1

        return s[start_idx : start_idx + max_len]
