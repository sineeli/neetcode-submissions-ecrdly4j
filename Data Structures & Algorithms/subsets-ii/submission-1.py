class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        def dfs(i, subset):
            ans.append(subset.copy())
            
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                dfs(j + 1, subset + [nums[j]])
        
        dfs(0, [])


        return ans