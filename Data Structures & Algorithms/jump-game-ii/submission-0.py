class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(nums) - 1:
                return 0
            
            if nums[i] == 0:
                return 100000
            res = 1000000
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                res = min(res, 1 + dfs(j))

            memo[i] = res
            return res

        return dfs(0)
