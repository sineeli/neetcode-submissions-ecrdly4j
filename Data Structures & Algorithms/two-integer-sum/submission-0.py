class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        n = len(nums)

        for i in range(n):
            if nums_dict.get(target - nums[i]) is not None:
                return [nums_dict[target - nums[i]], i]
            
            nums_dict[nums[i]] = i
        
        

            
        