class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sum_of_squares(k):
            total = 0
            while k > 0:
                total += (k % 10) ** 2
                k = k // 10
            
            return total
        slow = n
        fast = sum_of_squares(n)
        while slow != fast:
            fast = sum_of_squares(sum_of_squares(fast))
            slow = sum_of_squares(slow)
        
        return True if fast == 1 else False
        