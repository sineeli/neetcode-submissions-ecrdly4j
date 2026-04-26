class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        for i in range(n):
            adj[i] = []
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            if node == []:
                return
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh)
        
        components = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components

