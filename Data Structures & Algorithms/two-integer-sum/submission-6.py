class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {num: i for i, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            if nums_dict.get(target - num) is not None and idx != nums_dict.get(target - num):
                return [idx, nums_dict[target - num]]