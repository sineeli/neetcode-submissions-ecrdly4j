class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            bit = n & 1
            ans += bit * 2 ** (32 - i - 1)
            n >>= 1
        
        return ans
