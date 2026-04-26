class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()

        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                return num
        
        return 