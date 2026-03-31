class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        queries = sorted(enumerate(queries), key=lambda x: x[1])
        intervals.sort()

        i = 0
        res = [-1] * len(queries)
        n = len(intervals)
        for orig_idx, q in queries:
            while i < n and q >= intervals[i][0]:
                intv = intervals[i]
                heapq.heappush(minHeap, ((intv[1] - intv[0] + 1), intv[0], intv[1]))
                i += 1
            
            while minHeap and q > minHeap[0][2]:
                heapq.heappop(minHeap)
            
            if minHeap:
                res[orig_idx] = minHeap[0][0]
                print(minHeap[0][0])
            print(minHeap, q)
        
        return res

