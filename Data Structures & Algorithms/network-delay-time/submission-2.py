class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_graph = {}

        for i in range(1, n + 1):
            adj_graph[i] = []

        for ui, vi, ti in times:
            adj_graph[ui].append((vi, ti))

        min_heap = [(0, k)]
        shortest = {}
        while min_heap:
            t1, node = heapq.heappop(min_heap)
            if node in shortest:
                continue

            shortest[node] = t1
            for neigh, t2 in adj_graph[node]:
                if neigh not in shortest:
                    heapq.heappush(min_heap, (t1 + t2, neigh))

        return max(shortest.values()) if len(shortest) == n else -1
