class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        expected_sum = (N * (N + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum