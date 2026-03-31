class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []

        res = [0] * len(temperatures)
        stck = []

        for i in range(n-1, -1, -1):
            while stck and stck[-1][0] <= temperatures[i]:
                stck.pop()
            
            if stck:
                res[i] = stck[-1][1] - i
            
            stck.append((temperatures[i], i))

        return res


        


        