class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}

        for i in range(n):
            adj[i] = []
        
        for s, d, w in flights:
            adj[s].append((d, w))
        INF = float("inf")
        minHeap = [(0, src, -1)]
        dist = [[INF] * (k + 2) for _ in range(n)]

        while minHeap:
            print(minHeap)
            cst, node, stops = heapq.heappop(minHeap)
            if node == dst: return cst
            if stops == k or dist[node][stops] < cst:
                continue
            
            for nei, w in adj[node]:
                nextCst = cst + w
                nextStops = 1 + stops
                if dist[nei][nextStops + 1] > nextCst:
                    dist[nei][nextStops + 1] = nextCst
                    heapq.heappush(minHeap, (nextCst, nei, nextStops))
            
        
        return -1

