class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        
        if n != m:
            return False

        s_arr = [0] * 26

        for char in s:
            s_arr[ord(char) - 97] += 1
        
        for char in t:
            s_arr[ord(char) - 97] -= 1
        
        for i in range(26):
            if s_arr[i] != 0:
                return False
        
        return True