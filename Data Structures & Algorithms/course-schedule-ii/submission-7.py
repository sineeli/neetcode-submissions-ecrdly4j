class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        preq_adj = {}

        for i in range(numCourses):
            preq_adj[i] = []
        
        for a, b in prerequisites:
            preq_adj[a].append(b)

        visited = set()
        completed = set()

        def dfs(node):
            if node in visited:
                return False
            if node in completed:
                return True
            
            visited.add(node)

            for neigh in preq_adj[node]:
                if not dfs(neigh):
                    return False
            
            visited.remove(node)
            completed.add(node)
            order.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order