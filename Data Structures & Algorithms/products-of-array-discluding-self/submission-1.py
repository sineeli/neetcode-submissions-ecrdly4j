class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        output = [0 for _ in range(n)]

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        print(prefix)
        print(suffix)
        
        output[0] = suffix[1]
        output[-1] = prefix[n-2]
        for i in range(1, n-1):
            output[i] = suffix[i+1] * prefix[i-1]
        
        return output
        