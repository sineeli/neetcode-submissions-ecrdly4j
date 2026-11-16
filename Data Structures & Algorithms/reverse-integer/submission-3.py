class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 0x7FFFFFFF

        sign = -1 if x < 0 else 1

        x = abs(x)
        output = 0
        while x:
            digit = x % 10
            x = x // 10
            output = output * 10 + digit
        
        output = output * sign
        if not (-2**31 <= output <= 2**31 - 1):
            return 0
        return output