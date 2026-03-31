class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_dict = {}

        for i in range(n):
            if (target - nums[i]) in nums_dict:
                return [nums_dict[target - nums[i]], i]
            nums_dict[nums[i]] = i
        

        

        