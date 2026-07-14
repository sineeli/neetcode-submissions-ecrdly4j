class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxfreq = 0
        s_dict = {}
        l = 0
        max_len = 0

        for r in range(n):
            s_dict[s[r]] = s_dict.get(s[r], 0) + 1
            # maxfreq = max(maxfreq, s_dict[s[r]])
                
            while (r - l + 1) - max(s_dict.values()) > k:
                s_dict[s[l]] -= 1
                l += 1
    
            max_len = max(max_len, r - l + 1)

        return max_len
