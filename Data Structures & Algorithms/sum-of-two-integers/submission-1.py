class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # Mask to limit to 32-bit
        MAX_INT = 0x7FFFFFFF  # Maximum 32-bit signed integer (2147483647)

        while b != 0:
            carry = (a & b) << 1  # Compute carry
            a = (a ^ b) & MASK # Sum without carry
            b = carry & MASK  # Assign carry to b
        
        return a if a <= MAX_INT else ~(a ^ MASK)