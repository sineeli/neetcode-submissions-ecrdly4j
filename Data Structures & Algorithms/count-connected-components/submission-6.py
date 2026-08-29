class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        adj_graph = {}

        for i in range(n):
            adj_graph[i] = []

        for a, b in edges:
            adj_graph[a].append(b)
            adj_graph[b].append(a)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neigh in adj_graph[node]:
                dfs(neigh)

            return

        c = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                c += 1
            # print(visited)

        return c
