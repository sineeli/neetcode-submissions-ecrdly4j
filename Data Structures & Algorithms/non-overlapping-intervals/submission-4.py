class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        output = [intervals[0]]
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < output[-1][1]:
                ans += 1
                output[-1][1] = min(intervals[i][1], output[-1][1])
            else:
                output.append(intervals[i])
        
        return ans
