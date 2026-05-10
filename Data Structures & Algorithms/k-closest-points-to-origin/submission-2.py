class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        topK = []

        for point in points:
            heapq.heappush(topK, ((point[1] ** 2 + point[0] ** 2) ** (1 / 2), point))

        res = []
        while k > 0:
            dist, point = heapq.heappop(topK)
            res.append(point)
            k -= 1
        
        return res
