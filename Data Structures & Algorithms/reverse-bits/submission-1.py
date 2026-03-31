class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        output = 0
        for i in range(32):
            output += 2**(31-i) * (n & 1)
            n //= 2
        
        return output
        

        