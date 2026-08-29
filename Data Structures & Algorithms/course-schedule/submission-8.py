class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_adj = {}

        for i in range(numCourses):
            preq_adj[i] = []

        for a, b in prerequisites:
            preq_adj[a].append(b)

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            if not preq_adj[node]:
                return True

            visited.add(node)
            for neigh in preq_adj[node]:
                if not dfs(neigh):
                    return False

            visited.remove(node)
            preq_adj[node] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
