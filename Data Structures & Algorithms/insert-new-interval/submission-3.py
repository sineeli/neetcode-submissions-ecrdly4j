class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]

        for idx, interval in enumerate(intervals):
            if newInterval[0] < interval[0]:
                intervals.insert(idx, newInterval)
                break
        if newInterval[0] >= intervals[-1][0]:
            intervals.append(newInterval)
        
        print(intervals)
        new_intervals = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= new_intervals[-1][1]:
                new_intervals[-1][1] = max(interval[1], new_intervals[-1][1])
            else:
                new_intervals.append(interval)
        
        return new_intervals


        
