class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for ch in s:
            s_dict[ch] = s_dict.get(ch, 0) + 1
        
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1

        if len(s_dict) != len(t_dict):
            return False
        
        for ch in t:
            if s_dict.get(ch) is None:
                return False
            
            if s_dict.get(ch) != t_dict.get(ch):
                return False
        
        return True
        