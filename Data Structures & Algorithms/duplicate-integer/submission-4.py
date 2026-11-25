class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        
        nums_dict = {}
        for i in range(n):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1
        
        for key, value in nums_dict.items():
            if value > 1:
                return True
        
        return False


