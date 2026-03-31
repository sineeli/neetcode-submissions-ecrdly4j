class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i, amount):
            # Base cases
            if amount == 0:
                return 0
            if (i, amount) in memo:
                return memo[(i, amount)]
            
            if amount < 0 or i >= len(coins):
                return float('inf')  # impossible to make this amount
            
            # Option 1: Skip this coin, move to next
            res = dfs(i + 1, amount)
            
            # Option 2: Use this coin (if possible)
            if amount - coins[i] >= 0:
                res = min(res, 1 + dfs(i, amount - coins[i]))
            
            memo[(i, amount)] = res
            return memo[(i, amount)]

        minCoins = dfs(0, amount)
        return -1 if minCoins == float('inf') else minCoins
