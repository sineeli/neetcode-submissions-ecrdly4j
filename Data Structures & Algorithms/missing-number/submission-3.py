class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        for i in range(1, len(nums) + 1):
            xor_sum ^= i
        
        xor_arr = 0
        for num in nums:
            xor_arr ^= num
        
        return xor_sum ^ xor_arr