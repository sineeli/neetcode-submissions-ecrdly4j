class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        n = len(nums)
        memo = {}

        def dfs(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            if curr_sum == nums_sum // 2:
                return True

            if i >= n or curr_sum > nums_sum // 2:
                return False

            memo[(i, curr_sum)] = dfs(i + 1, curr_sum) or dfs(i + 1, curr_sum + nums[i])
            return memo[(i, curr_sum)]
        
        return dfs(0, 0)