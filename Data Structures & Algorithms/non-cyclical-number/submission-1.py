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
        fast = n
        while fast != 1:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
            if fast == 1:
                return True

            if slow == fast:
                return False
            
        
        return True
        