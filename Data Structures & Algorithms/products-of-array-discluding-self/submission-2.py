class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_mul = [1] * n
        suffix_mul = [1] * n
        prefix_mul[0] = nums[0]
        suffix_mul[-1] = nums[-1]

        for i in range(1, n):
            prefix_mul[i] = prefix_mul[i-1] * nums[i]
        
        for i in range(n-2, -1, -1):
            suffix_mul[i] = suffix_mul[i+1] * nums[i]
        print(prefix_mul, suffix_mul)
        output = [0] * n
        output[0] = suffix_mul[1]
        output[-1] = prefix_mul[n-2]
        
        for i in range(1, n-1):
            output[i] = prefix_mul[i-1] * suffix_mul[i+1]
        
        return output
        