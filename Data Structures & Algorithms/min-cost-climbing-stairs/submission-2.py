class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        memo = {}
        def dfs(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            single_step = cost[i] + dfs(i + 1)
            two_step = cost[i] + dfs(i + 2)

            memo[i] = min(single_step, two_step)
            return memo[i]
        
        return min(dfs(0), dfs(1))