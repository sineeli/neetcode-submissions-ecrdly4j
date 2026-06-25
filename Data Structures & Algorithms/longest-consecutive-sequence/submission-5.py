class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        hash_set = set(nums)
        res_len = 0

        i = 0
        while i < n:
            temp_len = 1
            temp_num = nums[i]
            while i < n and nums[i] - 1 not in hash_set and temp_num + 1 in hash_set:
                temp_num += 1
                temp_len += 1
            res_len = max(temp_len, res_len)
            i += 1
        
        return res_len
        