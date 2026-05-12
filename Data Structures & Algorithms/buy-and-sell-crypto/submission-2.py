class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_arr = [0] * n
        min_arr = [0] * n

        max_arr[-1] = prices[-1]
        
        for i in range(n-2, -1, -1):
            max_arr[i] = max(max_arr[i+1], prices[i])
        
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_arr[i]- prices[i])
        
        return max_profit
        