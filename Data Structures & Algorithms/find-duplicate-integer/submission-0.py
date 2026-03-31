class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bins = [0] * len(nums)

        for num in nums:
            bins[num] += 1
        
        for i in range(1, len(nums)):
            if bins[i] > 1:
                return i
        
        