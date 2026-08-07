class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [
            (((point[0])**2 + (point[1])**2)**0.5, point) for point in points
        ]

        heapq.heapify(distances)

        ans = []
        for _ in range(k):
            curr = heapq.heappop(distances)
            ans.append(curr[1])
        
        return ans