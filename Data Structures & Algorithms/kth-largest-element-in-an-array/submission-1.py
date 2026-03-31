class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quick_select(start, end):
            pivot = nums[end]
            p = start

            for i in range(start, end):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[end] = nums[end], nums[p]

            if k < p: return quick_select(start, p - 1)
            elif k > p: return quick_select(p + 1, end)
            else: return nums[p]
        
        return quick_select(0, len(nums)-1)