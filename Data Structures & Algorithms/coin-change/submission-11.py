class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}

        def dfs(i, target):
            if target == amount:
                return 0
            if i >= n or target > amount:
                return float('inf')
            
            if (i, target) in memo:
                return memo[(i, target)]

            take = 1 + dfs(i, target + coins[i])
            skip = dfs(i + 1, target)
            
            memo[(i, target)] = min(take, skip)
            return memo[(i, target)]
        
        res = dfs(0, 0)
        return res if res != float('inf') else -1