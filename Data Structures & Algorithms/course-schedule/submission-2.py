class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for i in range(numCourses):
            graph[i] = []
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            
            if not graph[node]:
                return True
            
            visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            visited.remove(node)
            graph[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True