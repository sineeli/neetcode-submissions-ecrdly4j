class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        MAX = 2**31 - 1        #  2147483647, last digit 7
        MIN = -2**31           # -2147483648, last digit 8 (abs)

        x = abs(x)
        output = 0
        while x:
            digit = x % 10
            x = x // 10
            # overflow check BEFORE multiplying
            if output > MAX // 10 or (output == MAX // 10 and digit > MAX % 10):
                return 0

            output = output * 10 + digit
        
        return output * sign