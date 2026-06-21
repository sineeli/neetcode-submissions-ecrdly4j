class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        
        if n != m:
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)

        for key in s_dict:
            if t_dict.get(key) is None:
                return False
            if t_dict.get(key) != s_dict.get(key):
                return False
        
        return True
            