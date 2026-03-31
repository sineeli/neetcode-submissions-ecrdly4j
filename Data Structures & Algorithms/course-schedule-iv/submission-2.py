class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        isPrereq = [[-1] * numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            graph[i] = []
        
        for preq, subj in prerequisites:
            graph[subj].append(preq)
        

        def dfs(crs):
            if crs not in premap:
                premap[crs] = set()
                for preq in graph[crs]:
                    premap[crs] |= dfs(preq)
                premap[crs].add(crs)
            
            return premap[crs]
        
        premap = {}
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            res.append(u in premap[v])
        
        return res
