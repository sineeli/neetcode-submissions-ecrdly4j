class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = (hi - lo) // 2 + lo
            if self.calc_completion(mid, piles) <= h:
                hi = mid
            else:
                lo = mid + 1
            
        return lo
    

    def calc_completion(self, k, piles):
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        
        return total