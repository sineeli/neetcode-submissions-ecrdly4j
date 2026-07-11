class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = j = 0
        s_dict = {}
        max_len = 0
        while j < n:
            if s[j] not in s_dict:
                max_len = max(j - i + 1, max_len)
                s_dict[s[j]] = j
                j += 1
                print(max_len)
            else:
                i = max(s_dict[s[j]] + 1, i)
                max_len = max(j - i + 1, max_len)
                s_dict[s[j]] = j
                j += 1
            
        
        return max_len
                
            