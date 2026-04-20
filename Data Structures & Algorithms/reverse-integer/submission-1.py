class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        ans = 0
        while x:
            val = x % 10
            ans = ans * 10 + val
            x = x // 10
        
        ans = sign * ans

        if ans < 0:
            if ans < -2**31:
                return 0
            else:
                return ans
        else:
            if ans > 2**31 - 1:
                return 0
            else:
                return ans

        