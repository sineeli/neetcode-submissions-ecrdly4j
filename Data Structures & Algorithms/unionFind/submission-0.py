class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {i:i for i in range(n)}
        self.size = [1] * n
        self.num_components = n
        

    def find(self, x: int) -> int:
        p = self.parent[x]

        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        
        return p
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            self.num_components -= 1
            return True
        
        return False
        

    def getNumComponents(self) -> int:
        return self.num_components      

