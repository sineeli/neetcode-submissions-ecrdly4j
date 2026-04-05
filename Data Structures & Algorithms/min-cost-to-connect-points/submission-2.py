class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        
        if len(points) == 2:
            return abs(points[0][0] - points[1][0]) + abs(points[0][1] - points[1][1])

        mst = []
        graph = {}
        minHeap = []
        visited = set()

        for (x, y) in points:
            graph[(x, y)] = []
        
        
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i+1:]):
                weight = abs(y2 - y1) + abs(x2 - x1)
                graph[(x1, y1)].append((weight, (x2, y2)))
                graph[(x2, y2)].append((weight, (x1, y1)))
        
        for weight, neigh in graph[tuple(points[0])]: # any random point
            heapq.heappush(minHeap, (weight, tuple(points[0]), neigh)) # push edges and there weights
        
        visited.add(tuple(points[0]))

        cost = 0
        mst_len = 1
        # print(minHeap)
        while len(visited) < len(points):
            w, src, dst = heapq.heappop(minHeap)
            # print(w)
            if dst in visited:
                continue
            cost += w # so here basically add the minimum weight edge across all edges instead in this case we just sum up those weighted edges
            visited.add(dst)
            mst_len += 1

            for weight, neigh in graph[dst]:
                if neigh not in visited:
                    heapq.heappush(minHeap, (weight, dst, neigh))
        
        return cost


                    

    
