class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        left = 0
        right = 0

        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        for i in range(0, n-m+1):
            count2 = {}
            for char in (s2[i:i+m]):
                count2[char] = count2.get(char, 0) + 1
            
            flag = True
            if need == len(count2):
                for char in count1:
                    if count2.get(char) is None:
                        flag = False
                    elif count2.get(char) < count1.get(char) or count2.get(char) > count1.get(char):
                        flag = False
            else:
                flag = False

            if flag:
                return True
        
        return False
                    
        

            
                