class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.par = {}
        self.rank = {}

        for edge in edges:
            if edge[0] not in self.par:
                self.par[edge[0]] = edge[0]
                self.rank[edge[0]] = 0
            if edge[1] not in self.par:
                self.par[edge[1]] = edge[1]
                self.rank[edge[1]] = 0
        
        for edge in edges:
            if not self.union(edge[0], edge[1]):
                return edge


    
    def find(self, node):
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p
        
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        
        return True

        
