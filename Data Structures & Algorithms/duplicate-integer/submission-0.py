class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}

        for num in nums:
            if dup_dict.get(num) is not None:
                return True
            dup_dict[num] = 1
        
        return False
         