class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}

        for i in range(n):
            graph[i] = []

        for src, dst in edges:
            graph[src].append(dst)
        
        visited = set()
        recstack = set()
        res = []

        def dfs(src):
            if src in visited:
                return True
            if src in recstack:
                return False
            
            recstack.add(src)
            
            for neighbor in graph[src]:
                if not dfs(neighbor):
                    return False
            recstack.remove(src)
            visited.add(src)
            res.append(src)

            return True
            
        
        for i in range(n):
            if not dfs(i):
                return []
        
        res.reverse()
        return res
        
            

        