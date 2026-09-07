class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(i, j):
            if i >= n:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = dfs(i+1, j)

            if j == -1 or  nums[i] > nums[j]:
                memo[(i, j)] = max(memo[(i, j)], 1 + dfs(i + 1, i))
            
            return memo[(i, j)]
        
        return dfs(0, -1)
            
            
            
