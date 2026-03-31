class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}

        for i in range(n):
            graph[i] = []
        
        for s, d, w in edges:
            graph[s].append((d, w))

        pq = [(0, src)]

        shortest = {}

        while pq:
            w1, n1 = heapq.heappop(pq)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in graph[n1]:
                if n2 not in shortest:
                    heapq.heappush(pq, (w1 + w2, n2))
        
        for node in graph:
            if node not in shortest:
                shortest[node] = -1
        return shortest
                    
                


        
