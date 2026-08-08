class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        nums_bin = [0] * (max_val - min_val + 1)

        for num in nums:
            nums_bin[num - min_val] += 1
        
        for i in range(len(nums_bin) - 1, -1, -1):
            k -= nums_bin[i]
            if k <= 0:
                return i + min_val