class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        hash_set = set(nums)
        max_len = 0
        
        while i < n:
            if nums[i] - 1 not in hash_set:
                count = 1
                curr_num = nums[i]
                while curr_num + 1 in hash_set:
                    count += 1
                    curr_num += 1
                max_len = max(max_len, count)
            i += 1
            print(max_len)
        
        return max_len

        