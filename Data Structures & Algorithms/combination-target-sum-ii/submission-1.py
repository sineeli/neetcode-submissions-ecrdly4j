class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        output = []
        candidates.sort()
        def dfs(i, temp, temp_sum):
            if temp_sum == target:
                output.append(temp.copy())
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if temp_sum + candidates[j] > target:
                    break
                dfs(j + 1, temp + [candidates[j]], temp_sum + candidates[j])
            

        dfs(0, [], 0)
        return output