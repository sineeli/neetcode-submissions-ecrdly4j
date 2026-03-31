class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        
        for key, v in nums_count.items():
            buckets[v].append(key)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res