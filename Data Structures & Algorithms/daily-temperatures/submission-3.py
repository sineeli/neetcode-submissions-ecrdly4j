class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stck = []
        res = [0] * len(temperatures)
        n = len(temperatures)
        for i in range(n-1, -1, -1):
            while stck and temperatures[i] >= stck[-1][0]:
                stck.pop()
            
            if stck:
                res[i] = stck[-1][1] - i

            stck.append([temperatures[i], i])
            # print(stck)
        
        return res
            