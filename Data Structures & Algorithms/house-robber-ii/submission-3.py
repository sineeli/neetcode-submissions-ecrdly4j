class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(
            self.helper(nums[:-1]),
            self.helper(nums[1:])
        )
        
    
    def helper(self, nums):
        prev_prev = nums[0]
        if len(nums) == 1:
            return nums[0]

        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(prev_prev + nums[i], prev)

            prev_prev = prev
            prev = current
        
        return prev