class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = nums_dict.get(nums[i], 0) + 1
        
        num_sorted = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(num_sorted[i][0])
        
        return ans
        
        