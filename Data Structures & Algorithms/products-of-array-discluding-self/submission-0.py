class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        prefix[0] = nums[0]
        postfix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i-1]
        
        for i in range(n-2, -1, -1):
            postfix[i] = nums[i] * postfix[i+1]
        
        res = []
        # print(prefix, postfix)
        for i in range(n):
            if i == 0:
                res.append(postfix[i+1])
                continue
            if i == n-1:
                res.append(prefix[i-1])
                continue

            res.append(postfix[i+1] * prefix[i-1])
        
        return res

        