class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sum_of_squares(k):
            total = 0
            while k > 0:
                total += (k % 10) ** 2
                k = k // 10
            
            return total
        
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = sum_of_squares(n)
        
        return True
        