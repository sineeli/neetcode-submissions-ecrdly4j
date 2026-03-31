class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for dst, src in prerequisites:
            graph[src].append(dst)
        
        visited = set()
        
        def isCyclic(crs):
            if crs in visited:
                return False
            
            if graph[crs] == []:
                return True
            
            visited.add(crs)
            for pre in graph[crs]:
                if not isCyclic(pre):
                    return False
            
            visited.remove(crs)
            graph[crs] = []
            return True
        

        for c in range(numCourses):
            if c not in visited and not isCyclic(c):
                return False
            
        return True


        
        