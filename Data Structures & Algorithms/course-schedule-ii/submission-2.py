from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b) 
        
        visited = set()
        visiting = set()
        order = []
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visiting.remove(node)
            visited.add(node)
            order.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order