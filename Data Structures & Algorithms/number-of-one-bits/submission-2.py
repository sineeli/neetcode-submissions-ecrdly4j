class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            count += 1 if n & 1 else 0
            n = n >> 1
        
        return count