class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        n = len(nums)
        
        def dfs(idx, total, curr_l):
            if total > target:
                return
            if total == target:
                output.append(curr_l)
            print(idx)
            for i in range(idx, n):
                dfs(i, total + nums[i], curr_l + [nums[i]])
        
        dfs(0, 0, [])
        return output