class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = Counter(nums)
        nums_l = [(-count, key) for key, count in nums_dict.items()]

        heapq.heapify(nums_l)
        output = []
        for i in range(k):
            output.append(heapq.heappop(nums_l)[1])
        
        return output
        
        