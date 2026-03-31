class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        next_max = [0] * n
        next_max[-1] = prices[-1]
        for i in range(n-2, -1, -1):
            next_max[i] = max(next_max[i+1], prices[i])
        
        profit = 0

        for i in range(n):
            profit = max(profit, next_max[i] - prices[i])
        
        return profit
