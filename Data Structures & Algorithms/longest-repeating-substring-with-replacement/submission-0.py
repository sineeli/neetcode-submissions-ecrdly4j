class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        n = len(s)
        char_count = {
            chr(i): 0 for i in range(65, 91)
        }

        max_len = 0
        for r in range(n):
            char_count[s[r]] += 1

            while (r - l + 1) - max(char_count.values()) > k:
                char_count[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
        
        return max_len

        