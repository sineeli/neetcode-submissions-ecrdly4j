class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        memo = {}

        def dfs(i, target):
            if (i, target) in memo:
                return memo[(i, target)]
            if target == amount:
                return 1
            
            if target > amount or i >= n:
                return 0
            
            memo[(i, target)] = dfs(i, target + coins[i]) + dfs(i + 1, target)

            return memo[(i, target)]


            

        res = dfs(0, 0)
        return res if res != float("inf") else 0
