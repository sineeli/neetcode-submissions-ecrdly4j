class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_graph = {}

        for a, b in edges:
            if a not in adj_graph:
                adj_graph[a] = []
            if b not in adj_graph:
                adj_graph[b] = []

            adj_graph[a].append(b)
            adj_graph[b].append(a)

        visited = set()
        cycle_start = -1
        cycle = set()

        def dfs(node, prev):
            nonlocal cycle_start
            if node in visited:
                cycle_start = node
                return True

            visited.add(node)
            for neigh in adj_graph[node]:
                if neigh == prev:
                    continue
                if dfs(neigh, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if node == cycle_start:
                        cycle_start = -1
                    return True

            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []
