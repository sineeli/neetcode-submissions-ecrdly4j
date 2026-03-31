class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n > 0:
            prev = x
            while n > 1:
                x = x * prev
                n -= 1
            return x
        else:
            prev = 1 / x
            n = abs(n)
            x = 1 / x
            while n > 1:
                x = x * prev
                n -= 1
            return x
