class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, subset, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if curr_sum + candidates[j] > target:
                    break

                dfs(j + 1, subset + [candidates[j]], curr_sum + candidates[j])
        
        dfs(0, [], 0)
        return res