class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ok(rate):
            time = 0
            for pile in piles:
                time += (pile + rate - 1) // rate
            
            return time <= h
        
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2

            if ok(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
