class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_graph = {}

        for i in range(n):
            adj_graph[i] = []
        
        for u, v, cost in flights:
            adj_graph[u].append((v, cost))
        
        min_heap = [(0, src, 0)]
        visited_stops = {}
        
        while min_heap:
            cost1, u, stops = heapq.heappop(min_heap)

            if u == dst:
                return cost1

            if stops > k:
                continue
            
            if u in visited_stops and visited_stops[u] <= stops:
                continue
            visited_stops[u] = stops

            for v, cost2 in adj_graph[u]:
                heapq.heappush(min_heap, (cost1 + cost2, v, stops + 1))
        
        return -1