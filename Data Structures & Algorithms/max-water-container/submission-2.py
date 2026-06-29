class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        curr_area = 0
        max_area = 0
        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])

            max_area = max(curr_area, max_area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
