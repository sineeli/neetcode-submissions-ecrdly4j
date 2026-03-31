class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        
        for s, d in trust:
            graph[s].append(d)
        
        judge = 0

        for i in range(1, n+1):
            if len(graph[i]) == 0:
                judge = i
        
        if judge == 0:
            return -1
        
        output = judge
        for i in range(1, n+1):
            if i != judge:
                if judge not in graph[i]:
                    output = -1
        
        return output


        