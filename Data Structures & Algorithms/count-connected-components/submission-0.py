class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # print(graph)
        def dfs(node):
            if node in visited:
                return
            if node == []:
                return
            # print(node)
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                components += 1
            dfs(i)
            # print(visited)
    
        return components
            
            

