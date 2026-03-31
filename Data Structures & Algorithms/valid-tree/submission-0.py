class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()

        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)

            for neighbor in graph[node]:
                if neighbor == par:
                    continue
                
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        