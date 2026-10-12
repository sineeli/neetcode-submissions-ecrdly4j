class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        
        # Insert newInterval at the correct position by start time
        inserted = False
        for idx, interval in enumerate(intervals):
            if newInterval[0] < interval[0]:
                intervals.insert(idx, newInterval)
                inserted = True
                break
        if not inserted:
            intervals.append(newInterval)

        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        
        return output