class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        res = 0
        x = abs(x)
        MIN = -2147483648
        MAX = 2147483647  #  2^31 - 1
        while x:
            digit = x % 10
            x = x // 10
            if sign == -1 and sign * res < MIN:
                return 0
            elif sign == 1 and res > MAX:
                return 0
            res = (res * 10) + digit

        if sign == -1 and sign * res < MIN:
                return 0
        elif sign == 1 and res > MAX:
                return 0
        return sign * res

        