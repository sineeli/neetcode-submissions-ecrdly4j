class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = ans = nums[0]

        for x in nums[1:]:
            if x < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(x, x * curr_max)
            curr_min = min(x, x * curr_min)

            ans = max(ans, curr_max)

        return ans
