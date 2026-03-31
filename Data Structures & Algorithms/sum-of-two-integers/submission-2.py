class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # Mask to limit to 32-bit
        MAX_INT = 0x7FFFFFFF  # Maximum 32-bit signed integer (2147483647)

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        
        return a if a <= MAX_INT else ~(a ^ MASK)
