class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(target):
            if target == n:
                return 1
            if target > n:
                return 0
            
            return climb(target + 1) + climb(target + 2)
        
        return climb(0)
        