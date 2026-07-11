class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i =  0
        s_dict = {}
        max_len = 0
        for j in range(n):
            if s[j] in s_dict:
                i = max(s_dict[s[j]] + 1, i)
            max_len = max(j - i + 1, max_len)
            s_dict[s[j]] = j
            
        return max_len
                
            