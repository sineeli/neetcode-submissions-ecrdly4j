class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}

        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
        
        for num in hash_table:
            if hash_table.get(num) > 1:
                return True
        
        return False