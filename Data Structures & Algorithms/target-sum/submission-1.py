class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            if i == n:
                return 1 if curr_sum == target else 0

            memo[(i, curr_sum)] = dfs(i + 1, nums[i] + curr_sum) + dfs(i + 1, -nums[i] + curr_sum)
            return memo[(i, curr_sum)]

        return dfs(0, 0)