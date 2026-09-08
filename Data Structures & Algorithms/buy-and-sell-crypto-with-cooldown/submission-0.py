class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(i, buying):
            if i >= n:
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            cooldown = dfs(i + 1, buying) # cooldown

            if buying:
                memo[(i, buying)] = max(dfs(i + 1, not buying) - prices[i], cooldown)
            else:
                memo[(i, buying)] = max(prices[i] + dfs(i + 2, not buying), cooldown)
            return memo[(i, buying)]   
        return dfs(0,  True)
            