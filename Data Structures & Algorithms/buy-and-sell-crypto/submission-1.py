class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = float('inf')

        for i, num in enumerate(prices):
            if num <= min_val:
                min_val = num
            
            if num - min_val > max_profit:
                max_profit = num - min_val
        
        return max_profit
