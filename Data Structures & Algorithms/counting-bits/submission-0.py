class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            res = 0
            while i:
                res += i % 2
                i >>= 1
            
            output.append(res)
        
        return output