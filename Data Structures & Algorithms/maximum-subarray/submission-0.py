class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = 0
        max_sum_sub = nums[0]

        l = 0
        for r in range(len(nums)):
            sub_sum = max(sub_sum, 0) + nums[r]
            max_sum_sub = max(max_sum_sub, sub_sum)
        
        return max_sum_sub
        