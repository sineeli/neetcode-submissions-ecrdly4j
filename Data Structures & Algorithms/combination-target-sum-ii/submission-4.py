class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            if curr_sum > target or i >= n:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i])
            subset.pop()

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr_sum)
        
        dfs(0, 0)
        return res