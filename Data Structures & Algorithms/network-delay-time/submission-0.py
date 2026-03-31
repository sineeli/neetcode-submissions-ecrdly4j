class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for i in range(1, n+1):
            graph[i] = []
        
        for u, v, t in times:
            graph[u].append((v, t))
        
        pq = [(0, k)]
        shortest = {
            node: float("inf") for node in graph
        }
        visited = set()
        t = 0
        while pq:
            t1, n1 = heapq.heappop(pq)

            if n1 in visited:
                continue
            visited.add(n1)
            t = t1
            for n2, t2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(pq, (t1 + t2, n2))
        return t if len(visited) == n else -1

                




        
        