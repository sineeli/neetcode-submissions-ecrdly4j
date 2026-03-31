class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m != n:
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

        