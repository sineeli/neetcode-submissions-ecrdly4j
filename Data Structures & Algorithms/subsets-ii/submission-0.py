class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        res = []
        n = len(nums)
        def dfs(i):
            if i == n:
                res.append(subset.copy())
                return
        
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            
            
            dfs(i + 1)
        
        dfs(0)
        return res


        