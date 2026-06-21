class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = Counter(nums)

        for cnt in nums_dict.values():
            if cnt > 1:
                return True
        return False